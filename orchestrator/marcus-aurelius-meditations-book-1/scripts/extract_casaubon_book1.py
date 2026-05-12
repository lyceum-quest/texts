#!/usr/bin/env python3
"""
Extract Book 1 from Casaubon translation (Gutenberg plain text).
"""

import re
import sys
from pathlib import Path

def extract_book1(input_path, output_path):
    """Extract Book 1 text from Casaubon Gutenberg file."""
    
    text = input_path.read_text(encoding='utf-8')
    
    # Find the start of THE FIRST BOOK
    start_match = re.search(r'THE FIRST BOOK\s*\n', text)
    if not start_match:
        print("ERROR: Could not find 'THE FIRST BOOK'")
        return
    
    start_pos = start_match.end()
    
    # Find the start of THE SECOND BOOK
    end_match = re.search(r'THE SECOND BOOK', text[start_pos:])
    if not end_match:
        print("ERROR: Could not find 'THE SECOND BOOK'")
        return
    
    end_pos = start_pos + end_match.start()
    
    # Extract Book 1 content
    book1_text = text[start_pos:end_pos].strip()
    
    # Add a marker at the start if it begins with a roman numeral
    if re.match(r'^[IVX]+\.\s+', book1_text):
        book1_text = '\n' + book1_text
    
    # Split into sections by Roman numerals (at start of line or after double newline)
    sections = re.split(r'\n+([IVX]+\.)\s+', book1_text)
    
    output_lines = []
    output_lines.append("# Marcus Aurelius, Meditations Book 1 (English - Casaubon 1634)")
    output_lines.append("# Source: Project Gutenberg #2680")
    output_lines.append("# Translator: Meric Casaubon")
    output_lines.append("# Extracted: Book 1, sections 1-17")
    output_lines.append("")
    
    # Process sections
    current_section = None
    for i in range(1, len(sections), 2):
        if i < len(sections):
            section_num = sections[i].rstrip('.')
            section_text = sections[i + 1].strip() if i + 1 < len(sections) else ""
            
            # Clean up the text
            section_text = re.sub(r'\s+', ' ', section_text)
            section_text = section_text.strip()
            
            # Convert Roman numeral to Arabic
            roman_to_int = {
                'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
                'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10,
                'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15,
                'XVI': 16, 'XVII': 17
            }
            
            section_int = roman_to_int.get(section_num, 0)
            if section_int > 0 and section_int <= 17:
                output_lines.append(f"## 1.{section_int}")
                output_lines.append("")
                output_lines.append(section_text)
                output_lines.append("")
    
    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text('\n'.join(output_lines), encoding='utf-8')
    print(f"Wrote {len(output_lines)} lines to {output_path}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_txt> <output_txt>")
        sys.exit(1)
    
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    
    if not input_path.exists():
        print(f"ERROR: Input file not found: {input_path}")
        sys.exit(1)
    
    extract_book1(input_path, output_path)
