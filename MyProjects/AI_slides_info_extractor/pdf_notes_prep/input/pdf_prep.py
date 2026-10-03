#!/usr/bin/env python3
"""pdf_prep.py — prepare a lecture-slide PDF for manual LLM summarization.

Two-stage CLI:

  1. extract  — pull text from every page (OCR fallback for scanned pages),
                detect which pages contain diagrams, and render those pages
                as images.
  2. package  — group pages into upload-ready chunks: one folder per chunk,
                containing a combined text file and only the page images
                that chunk actually needs.

Nothing here calls an LLM. The output of `package` is what you manually
paste/attach into a chat, chunk by chunk.

Usage:
    python pdf_prep.py extract slides.pdf -o work/
    # -> creates work/slides/ automatically (named after the PDF)
    python pdf_prep.py package work/slides --pages-per-chunk 10
"""

from __future__ import annotations

import argparse
import io
import json
import shutil
from pathlib import Path

import pymupdf
import pytesseract
from PIL import Image

IMAGE_DPI = 220
DIAGRAM_DRAWING_THRESHOLD = 15  # vector shapes above this = "has a diagram"


# ---------------------------------------------------------------------------
# Stage 1: extract
# ---------------------------------------------------------------------------

def render_page_image(page: pymupdf.Page, dpi: int = IMAGE_DPI) -> Image.Image:
    zoom = dpi / 72
    pixmap = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom))
    return Image.open(io.BytesIO(pixmap.tobytes("png")))


def page_has_diagram(page: pymupdf.Page) -> bool:
    """Heuristic: embedded raster images, or a high count of vector shapes
    (the rectangles/arrows/lines PowerPoint uses to draw boxes and flows)."""
    if page.get_images(full=True):
        return True
    return len(page.get_drawings()) > DIAGRAM_DRAWING_THRESHOLD


def extract_page_text(page: pymupdf.Page) -> tuple[str, bool]:
    """Returns (text, was_ocr)."""
    text = page.get_text("text").strip()
    if text:
        return text, False
    image = render_page_image(page)
    return pytesseract.image_to_string(image).strip(), True


def run_extract(pdf_path: Path, output_root: Path) -> Path:
    """Extracts into output_root/<pdf_stem>/ (auto-named after the PDF)."""
    output_dir = output_root / pdf_path.stem
    pages_dir = output_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)

    manifest: list[dict] = []

    with pymupdf.open(pdf_path) as doc:
        for page_number, page in enumerate(doc, start=1):
            text, was_ocr = extract_page_text(page)
            text_file = pages_dir / f"page_{page_number:03d}.txt"
            text_file.write_text(text, encoding="utf-8")

            has_diagram = page_has_diagram(page)
            image_file = None
            if has_diagram:
                image = render_page_image(page)
                image_file = pages_dir / f"page_{page_number:03d}.png"
                image.save(image_file)

            manifest.append(
                {
                    "page_number": page_number,
                    "text_file": text_file.name,
                    "was_ocr": was_ocr,
                    "has_diagram": has_diagram,
                    "image_file": image_file.name if image_file else None,
                }
            )
            tag = "OCR" if was_ocr else "text"
            diagram_tag = " +diagram" if has_diagram else ""
            print(f"Page {page_number:>3}: {tag}{diagram_tag}")

    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    n_diagrams = sum(1 for m in manifest if m["has_diagram"])
    print(f"\nDone: {len(manifest)} pages, {n_diagrams} with diagrams.")
    print(f"Output written to {output_dir}")
    print(f"Next: python pdf_prep.py package {output_dir} --pages-per-chunk N")
    return output_dir


# ---------------------------------------------------------------------------
# Stage 2: package
# ---------------------------------------------------------------------------

def run_package(output_dir: Path, pages_per_chunk: int) -> None:
    manifest_path = output_dir / "manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"No manifest.json in {output_dir}. Run `extract` first.")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    pages_dir = output_dir / "pages"
    chunks_dir = output_dir / "chunks"
    if chunks_dir.exists():
        shutil.rmtree(chunks_dir)
    chunks_dir.mkdir(parents=True)

    manifest.sort(key=lambda m: m["page_number"])

    for i in range(0, len(manifest), pages_per_chunk):
        batch = manifest[i : i + pages_per_chunk]
        first, last = batch[0]["page_number"], batch[-1]["page_number"]
        chunk_dir = chunks_dir / f"chunk_pages_{first:03d}-{last:03d}"
        chunk_dir.mkdir()

        # Combined text file with page markers.
        combined_parts = []
        image_names: list[str] = []
        for entry in batch:
            page_text = (pages_dir / entry["text_file"]).read_text(encoding="utf-8")
            combined_parts.append(f"--- Page {entry['page_number']} ---\n{page_text}")
            if entry["image_file"]:
                src = pages_dir / entry["image_file"]
                dst = chunk_dir / entry["image_file"]
                shutil.copy(src, dst)
                image_names.append(entry["image_file"])

        (chunk_dir / "combined.txt").write_text("\n\n".join(combined_parts), encoding="utf-8")

        note_lines = [f"Pages {first}-{last}", ""]
        if image_names:
            note_lines.append("Attach these images along with combined.txt:")
            note_lines.extend(f"  - {name}" for name in image_names)
        else:
            note_lines.append("No diagram pages in this chunk — text only.")
        (chunk_dir / "README.txt").write_text("\n".join(note_lines), encoding="utf-8")

        print(f"{chunk_dir.name}: {len(batch)} pages, {len(image_names)} image(s)")

    print(f"\n{len(list(chunks_dir.iterdir()))} chunks written to {chunks_dir}")
    print("For each chunk: open combined.txt + attach any listed images to your LLM chat, in order.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_extract = sub.add_parser("extract", help="Extract text and diagram images from a PDF")
    p_extract.add_argument("pdf", help="Path to the PDF file")
    p_extract.add_argument(
        "-o", "--output-dir", default="work",
        help="Parent directory for output; a subfolder named after the PDF is created inside it (default: work)",
    )

    p_package = sub.add_parser("package", help="Bundle extracted pages into upload-ready chunks")
    p_package.add_argument("output_dir", help="Directory previously used with `extract`")
    p_package.add_argument("--pages-per-chunk", type=int, default=10)

    args = parser.parse_args()

    if args.command == "extract":
        run_extract(Path(args.pdf), Path(args.output_dir))
    elif args.command == "package":
        run_package(Path(args.output_dir), args.pages_per_chunk)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())