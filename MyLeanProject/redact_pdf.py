"""
PDF Redaction Tool
==================
This script redacts (blacks out) sensitive information from PDF files.

Requirements:
    pip install pypdf reportlab pdfplumber

Usage:
    python redact_pdf.py

Customize the REDACTION_RULES list below to specify what to redact.
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import black
import pdfplumber
import os

# ============================================================================
# CONFIGURATION - CUSTOMIZE THESE VALUES
# ============================================================================

# Input and output file paths
INPUT_PDF = "file.path"  # Change this to your PDF filename
OUTPUT_PDF = "file.path"

# Define what text to look for and redact
# Each rule is a dictionary with:
#   'trigger': the text to search for (e.g., "Policy number")
#   'redact_next': how many words after the trigger to redact (for 'after_trigger')
#   'redact_type': 'after_trigger' | 'same_line' | 'contains' | 'line_after_chars'
#   'chars': for 'line_after_chars' only - redact the rest of the line after this many characters
REDACTION_RULES = [
    {
        'trigger': 'text',
        'redact_next': 0,  # Redact the next 3 words (to catch "1,656.00")
        'redact_type': 'after_trigger'
    },
    # Add more rules as needed:
]

# Padding around redaction boxes (in points)
REDACTION_PADDING = 2

# ============================================================================
# MAIN SCRIPT - YOU SHOULDN'T NEED TO MODIFY BELOW THIS LINE
# ============================================================================

def _words_on_same_line(words, ref_top, tolerance=2):
    """Return indices of words that share the same line as ref_top (same vertical position)."""
    return [idx for idx, w in enumerate(words) if abs(w['top'] - ref_top) <= tolerance]


def find_words_to_redact(words, rules):
    """
    Find words that need to be redacted based on the rules.
    
    Args:
        words: List of word dictionaries from pdfplumber
        rules: List of redaction rules
    
    Returns:
        List of word bounding boxes to redact
    """
    redact_boxes = []
    line_tolerance = 2  # points; words within this vertical distance are same line

    for rule in rules:
        trigger = rule['trigger']
        redact_type = rule['redact_type']
        redact_next = rule.get('redact_next', 0)

        # Split trigger into words for multi-word matching
        trigger_words = trigger.split()

        # Search for the trigger text
        for i in range(len(words) - len(trigger_words) + 1):
            # Check if we found the trigger phrase
            match = True
            for j, trigger_word in enumerate(trigger_words):
                if trigger_word.lower() not in words[i + j]['text'].lower():
                    match = False
                    break

            if match:
                # Found the trigger, now redact based on type
                if redact_type == 'after_trigger':
                    # Redact the next N words after the trigger
                    start_idx = i + len(trigger_words)

                    # Skip over colons, whitespace, etc.
                    while start_idx < len(words) and words[start_idx]['text'].strip() in [':', '', '-']:
                        start_idx += 1

                    # Collect the next N words to redact
                    for k in range(start_idx, min(start_idx + redact_next, len(words))):
                        if words[k]['text'].strip():  # Only redact non-empty words
                            redact_boxes.append({
                                'x0': words[k]['x0'],
                                'x1': words[k]['x1'],
                                'top': words[k]['top'],
                                'bottom': words[k]['bottom']
                            })

                elif redact_type == 'line_after_chars':
                    # Redact the rest of the line after N characters
                    char_limit = rule.get('chars', 0)
                    ref_top = words[i]['top']
                    line_indices = _words_on_same_line(words, ref_top, line_tolerance)
                    # Order by x0 so we read left-to-right
                    line_indices.sort(key=lambda idx: words[idx]['x0'])
                    count = 0
                    for idx in line_indices:
                        w = words[idx]
                        text = w['text']
                        # Redact this word if we're already past the character limit
                        if count >= char_limit:
                            redact_boxes.append({
                                'x0': w['x0'],
                                'x1': w['x1'],
                                'top': w['top'],
                                'bottom': w['bottom']
                            })
                        count += len(text) + 1  # +1 for space between words
    return redact_boxes


def create_redaction_overlay(redact_boxes, page_width, page_height, output_path):
    """
    Create a PDF with black rectangles over sensitive areas.
    
    Args:
        redact_boxes: List of boxes to redact
        page_width: Width of the PDF page
        page_height: Height of the PDF page
        output_path: Where to save the overlay PDF
    """
    c = canvas.Canvas(output_path, pagesize=(page_width, page_height))
    c.setFillColor(black)
    
    for box in redact_boxes:
        # Convert coordinates (PDF coordinates start from bottom-left)
        x = box['x0'] - REDACTION_PADDING
        y = page_height - box['bottom'] - REDACTION_PADDING
        width = (box['x1'] - box['x0']) + (2 * REDACTION_PADDING)
        height = (box['bottom'] - box['top']) + (2 * REDACTION_PADDING)
        
        # Draw black rectangle
        c.rect(x, y, width, height, fill=1, stroke=0)
    
    c.save()


def redact_pdf(input_path, output_path, rules):
    """
    Main function to redact a PDF file.
    
    Args:
        input_path: Path to input PDF
        output_path: Path to save redacted PDF
        rules: List of redaction rules
    """
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found!")
        print("Please update INPUT_PDF variable at the top of this script.")
        return
    
    print(f"Reading PDF: {input_path}")
    
    # Process all pages
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    with pdfplumber.open(input_path) as pdf:
        total_redactions = 0
        
        for page_num, page in enumerate(pdf.pages):
            print(f"\nProcessing page {page_num + 1}...")
            
            words = page.extract_words()
            page_width = page.width
            page_height = page.height
            
            # Find words to redact on this page
            redact_boxes = find_words_to_redact(words, rules)
            
            if redact_boxes:
                print(f"  Found {len(redact_boxes)} item(s) to redact on page {page_num + 1}")
                total_redactions += len(redact_boxes)
                
                # Create overlay for this page
                overlay_path = f"temp_overlay_page_{page_num}.pdf"
                create_redaction_overlay(redact_boxes, page_width, page_height, overlay_path)
                
                # Merge overlay with this page
                pdf_page = reader.pages[page_num]
                overlay = PdfReader(overlay_path)
                pdf_page.merge_page(overlay.pages[0])
                writer.add_page(pdf_page)
                
                # Clean up temporary file
                os.remove(overlay_path)
            else:
                # No redactions needed, add page as-is
                writer.add_page(reader.pages[page_num])
    
    if total_redactions == 0:
        print("\nWarning: No items found to redact. Check your REDACTION_RULES.")
        return
    
    # Write output
    print(f"\nCreating redacted PDF...")
    with open(output_path, "wb") as output:
        writer.write(output)
    
    print(f"✓ Redacted PDF saved to: {output_path}")
    print(f"\nSummary:")
    print(f"  - Input: {input_path}")
    print(f"  - Output: {output_path}")
    print(f"  - Total pages: {len(reader.pages)}")
    print(f"  - Total items redacted: {total_redactions}")

if __name__ == "__main__":
    print("=" * 60)
    print("PDF Redaction Tool")
    print("=" * 60)
    
    redact_pdf(INPUT_PDF, OUTPUT_PDF, REDACTION_RULES)