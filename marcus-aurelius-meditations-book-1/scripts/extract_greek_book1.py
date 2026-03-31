#!/usr/bin/env python3
"""
Extract Book 1 from Perseus TEI XML for Marcus Aurelius Meditations.
"""

import xml.etree.ElementTree as ET
import sys
from pathlib import Path

def extract_book1(xml_path, output_path):
    """Extract Book 1 text from Perseus TEI XML."""
    
    # Parse the XML
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    # Define namespace
    ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
    
    # Find all div elements
    output_lines = []
    output_lines.append("# Marcus Aurelius, Meditations Book 1 (Greek)")
    output_lines.append("# Source: Perseus Digital Library, Leopold 1908 edition")
    output_lines.append("# Extracted: Book 1, sections 1-17")
    output_lines.append("")
    
    # Find the body and look for Book 1
    body = root.find('.//tei:body', ns)
    if body is None:
        print("ERROR: Could not find body element")
        return
    
    # Look for div with subtype="book" and n="1"
    book1 = None
    for div in body.findall('.//tei:div', ns):
        if div.get('subtype') == 'book' and div.get('n') == '1':
            book1 = div
            break
    
    if book1 is None:
        print("ERROR: Could not find Book 1")
        return
    
    print(f"Found Book 1")
    
    # Extract chapters (each chapter is a numbered section in Book 1)
    chapters = book1.findall('.//tei:div[@subtype="chapter"]', ns)
    print(f"Found {len(chapters)} chapters in Book 1")
    
    for chapter in chapters:
        chapter_n = chapter.get('n')
        if chapter_n:
            output_lines.append(f"## 1.{chapter_n}")
            output_lines.append("")
            
            # Get the text from the section within this chapter
            sections = chapter.findall('.//tei:div[@subtype="section"]', ns)
            for section in sections:
                # Get all paragraph text
                paras = section.findall('.//tei:p', ns)
                for para in paras:
                    # Get all text content
                    text_parts = []
                    for elem in para.iter():
                        if elem.text:
                            text_parts.append(elem.text.strip())
                        if elem.tail:
                            text_parts.append(elem.tail.strip())
                    
                    # Join and clean up
                    text = ' '.join(part for part in text_parts if part)
                    if text:
                        output_lines.append(text)
            
            output_lines.append("")
    
    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text('\n'.join(output_lines), encoding='utf-8')
    print(f"Wrote {len(output_lines)} lines to {output_path}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_xml> <output_txt>")
        sys.exit(1)
    
    xml_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    
    if not xml_path.exists():
        print(f"ERROR: Input file not found: {xml_path}")
        sys.exit(1)
    
    extract_book1(xml_path, output_path)
