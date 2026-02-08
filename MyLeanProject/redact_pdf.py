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
INPUT_PDF = "input.pdf"  # Change this to your PDF filename
OUTPUT_PDF = "output_redacted.pdf"

# Define what text to look for and redact
# Each rule is a dictionary with:
#   'trigger': the text to search for (e.g., "Policy number")
#   'redact_next': how many words after the trigger to redact
#   'redact_type': 'after_trigger' or 'same_line' or 'contains'
REDACTION_RULES = [
    {
        'trigger': 'Policy number',
        'redact_next': 1,  # Redact the next 1 word after "Policy number"
        'redact_type': 'after_trigger'
    },
    {
        'trigger': 'Total Premium',
        'redact_next': 3,  # Redact the next 3 words (to catch "1,656.00")
        'redact_type': 'after_trigger'
    },
    # Add more rules as needed:
    # {
    #     'trigger': 'Social Security',
    #     'redact_next': 2,
    #     'redact_type': 'after_trigger'
    # },
]

# Padding around redaction boxes (in points)
REDACTION_PADDING = 2

# ============================================================================
# MAIN SCRIPT - YOU SHOULDN'T NEED TO MODIFY BELOW THIS LINE
# ============================================================================

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
    
    for rule in rules:
        trigger = rule['trigger']
        redact_next = rule['redact_next']
        redact_type = rule['redact_type']
        
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
    
    # Extract text with positions using pdfplumber
    with pdfplumber.open(input_path) as pdf:
        # Process first page (modify if you need multiple pages)
        page = pdf.pages[0]
        words = page.extract_words()
        page_width = page.width
        page_height = page.height
        
        # Find words to redact
        redact_boxes = find_words_to_redact(words, rules)
        
        print(f"\nFound {len(redact_boxes)} item(s) to redact:")
        for i, box in enumerate(redact_boxes, 1):
            # Try to show what's being redacted
            matching_word = next((w for w in words if w['x0'] == box['x0']), None)
            if matching_word:
                print(f"  {i}. Redacting: '{matching_word['text']}'")
        
        if len(redact_boxes) == 0:
            print("\nWarning: No items found to redact. Check your REDACTION_RULES.")
            return
    
    # Create overlay with redaction boxes
    overlay_path = "temp_overlay.pdf"
    create_redaction_overlay(redact_boxes, page_width, page_height, overlay_path)
    
    # Merge overlay with original PDF
    print(f"\nCreating redacted PDF...")
    reader = PdfReader(input_path)
    overlay = PdfReader(overlay_path)
    writer = PdfWriter()
    
    # Merge the redaction overlay onto the first page
    page = reader.pages[0]
    page.merge_page(overlay.pages[0])
    writer.add_page(page)
    
    # Add remaining pages if any (without redaction)
    for i in range(1, len(reader.pages)):
        writer.add_page(reader.pages[i])
    
    # Write output
    with open(output_path, "wb") as output:
        writer.write(output)
    
    # Clean up temporary file
    os.remove(overlay_path)
    
    print(f"✓ Redacted PDF saved to: {output_path}")
    print(f"\nSummary:")
    print(f"  - Input: {input_path}")
    print(f"  - Output: {output_path}")
    print(f"  - Items redacted: {len(redact_boxes)}")


if __name__ == "__main__":
    print("=" * 60)
    print("PDF Redaction Tool")
    print("=" * 60)
    
    redact_pdf(INPUT_PDF, OUTPUT_PDF, REDACTION_RULES)