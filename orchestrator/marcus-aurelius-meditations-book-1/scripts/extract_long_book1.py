#!/usr/bin/env python3
"""
Extract Book 1 from Long translation (Wikisource HTML).
"""

import re
import sys
from pathlib import Path
from html.parser import HTMLParser

class WikisourceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_content = False
        self.in_paragraph = False
        self.current_section = None
        self.sections = {}
        self.current_text = []
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # Look for the main content area
        if tag == 'div' and attrs_dict.get('class') == 'mw-parser-output':
            self.in_content = True
        
        # Look for paragraphs
        if self.in_content and tag == 'p':
            self.in_paragraph = True
    
    def handle_endtag(self, tag):
        if tag == 'p' and self.in_paragraph:
            self.in_paragraph = False
            if self.current_text:
                text = ' '.join(self.current_text).strip()
                # Check if this starts with a section number
                match = re.match(r'^(\d+)\.\s+(.*)', text)
                if match:
                    section_num = int(match.group(1))
                    section_text = match.group(2)
                    self.sections[section_num] = section_text
                elif self.current_section:
                    # Continue previous section
                    if self.current_section in self.sections:
                        self.sections[self.current_section] += ' ' + text
                
                self.current_text = []
    
    def handle_data(self, data):
        if self.in_paragraph:
            text = data.strip()
            if text:
                self.current_text.append(text)

def extract_book1(input_path, output_path):
    """Extract Book 1 text from Long Wikisource HTML."""
    
    html = input_path.read_text(encoding='utf-8')
    
    # Simple regex-based extraction
    # Find all numbered sections
    sections = {}
    
    # Look for patterns like "1. Text..." or "<p>1. Text</p>"
    # Extract content between <p> tags
    paragraphs = re.findall(r'<p>(.*?)</p>', html, re.DOTALL)
    
    for para in paragraphs:
        # Remove HTML tags
        clean_text = re.sub(r'<[^>]+>', '', para)
        clean_text = clean_text.strip()
        
        # Check if it starts with a number
        match = re.match(r'^(\d+)\.\s+(.*)', clean_text, re.DOTALL)
        if match:
            section_num = int(match.group(1))
            section_text = match.group(2)
            
            # Clean up whitespace
            section_text = re.sub(r'\s+', ' ', section_text).strip()
            
            if 1 <= section_num <= 17:
                if section_num not in sections:
                    sections[section_num] = section_text
                else:
                    # Append if section continues
                    sections[section_num] += ' ' + section_text
        # Check for the unnumbered first section (starts with "FROM my grandfather Verus")
        elif 'grandfather Verus' in clean_text and 1 not in sections:
            # This is section 1
            section_text = re.sub(r'\s+', ' ', clean_text).strip()
            sections[1] = section_text
    
    output_lines = []
    output_lines.append("# Marcus Aurelius, Meditations Book 1 (English - Long 1862)")
    output_lines.append("# Source: Wikisource")
    output_lines.append("# Translator: George Long")
    output_lines.append("# Extracted: Book 1, sections 1-17")
    output_lines.append("")
    
    # Write sections in order
    for i in range(1, 18):
        if i in sections:
            output_lines.append(f"## 1.{i}")
            output_lines.append("")
            output_lines.append(sections[i])
            output_lines.append("")
    
    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text('\n'.join(output_lines), encoding='utf-8')
    print(f"Wrote {len(output_lines)} lines to {output_path}")
    print(f"Extracted {len(sections)} sections")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_html> <output_txt>")
        sys.exit(1)
    
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    
    if not input_path.exists():
        print(f"ERROR: Input file not found: {input_path}")
        sys.exit(1)
    
    extract_book1(input_path, output_path)
