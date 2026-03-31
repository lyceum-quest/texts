#!/usr/bin/env python3
"""
Stage 3 Text Cleaning Script
Marcus Aurelius, Meditations Book 1

Cleans extracted texts and produces clean outputs:
- Greek: Unicode NFC normalization
- Long English: Remove CSS, HTML entities, footnote markers
- Casaubon English: Check and clean if needed
"""

import re
import unicodedata
from pathlib import Path

def normalize_unicode(text):
    """Normalize Unicode to NFC form."""
    return unicodedata.normalize('NFC', text)

def remove_css_code(text):
    """Remove CSS code blocks (typically at start of sections)."""
    # Remove .mw-parser-output CSS blocks
    text = re.sub(r'\.mw-parser-output[^}]+}[^}]*}*', '', text)
    return text

def decode_html_entities(text):
    """Decode common HTML entities."""
    replacements = {
        '&#91;': '[',
        '&#93;': ']',
        '&#160;': ' ',
        '&nbsp;': ' ',
        '&amp;': '&',
        '&lt;': '<',
        '&gt;': '>',
        '&quot;': '"',
    }
    for entity, char in replacements.items():
        text = text.replace(entity, char)
    return text

def remove_footnote_markers(text):
    """Remove footnote markers like [1], [2], etc."""
    # Remove bracketed numbers (footnote markers)
    text = re.sub(r'\[(\d+)\]', '', text)
    return text

def normalize_whitespace(text):
    """Normalize excessive whitespace while preserving structure."""
    # Remove trailing whitespace from lines
    lines = [line.rstrip() for line in text.split('\n')]
    # Remove consecutive blank lines (keep max 2)
    result = []
    blank_count = 0
    for line in lines:
        if line.strip():
            result.append(line)
            blank_count = 0
        else:
            blank_count += 1
            if blank_count <= 2:
                result.append(line)
    return '\n'.join(result)

def clean_greek_text(input_path, output_path):
    """Clean Greek text: primarily Unicode normalization."""
    print(f"Cleaning Greek text: {input_path}")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Normalize Unicode
    text = normalize_unicode(text)
    
    # Normalize whitespace
    text = normalize_whitespace(text)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"✓ Greek text cleaned: {output_path}")

def clean_long_english(input_path, output_path):
    """Clean Long English translation: remove CSS, HTML entities, footnotes."""
    print(f"Cleaning Long English text: {input_path}")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Remove CSS code
    text = remove_css_code(text)
    
    # Decode HTML entities
    text = decode_html_entities(text)
    
    # Remove footnote markers
    text = remove_footnote_markers(text)
    
    # Normalize Unicode
    text = normalize_unicode(text)
    
    # Normalize whitespace
    text = normalize_whitespace(text)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"✓ Long English text cleaned: {output_path}")

def clean_casaubon_english(input_path, output_path):
    """Clean Casaubon English translation: normalize and check."""
    print(f"Cleaning Casaubon English text: {input_path}")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Decode any HTML entities
    text = decode_html_entities(text)
    
    # Normalize Unicode
    text = normalize_unicode(text)
    
    # Normalize whitespace
    text = normalize_whitespace(text)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"✓ Casaubon English text cleaned: {output_path}")

def generate_cleaning_stats(extracted_dir, clean_dir):
    """Generate statistics about what was cleaned."""
    stats = {
        'greek': {},
        'long': {},
        'casaubon': {}
    }
    
    # Greek stats
    with open(extracted_dir / 'greek-book1.txt', 'r', encoding='utf-8') as f:
        raw_greek = f.read()
    with open(clean_dir / 'greek.txt', 'r', encoding='utf-8') as f:
        clean_greek = f.read()
    
    stats['greek']['raw_size'] = len(raw_greek)
    stats['greek']['clean_size'] = len(clean_greek)
    stats['greek']['sections'] = len([l for l in clean_greek.split('\n') if l.startswith('## ')])
    
    # Long stats
    with open(extracted_dir / 'long-book1.txt', 'r', encoding='utf-8') as f:
        raw_long = f.read()
    with open(clean_dir / 'english.txt', 'r', encoding='utf-8') as f:
        clean_long = f.read()
    
    stats['long']['raw_size'] = len(raw_long)
    stats['long']['clean_size'] = len(clean_long)
    stats['long']['sections'] = len([l for l in clean_long.split('\n') if l.startswith('## ')])
    stats['long']['css_removed'] = raw_long.count('.mw-parser-output')
    stats['long']['html_entities'] = raw_long.count('&#')
    stats['long']['footnotes_removed'] = len(re.findall(r'\[\d+\]', raw_long))
    
    # Casaubon stats
    with open(extracted_dir / 'casaubon-book1.txt', 'r', encoding='utf-8') as f:
        raw_casaubon = f.read()
    with open(clean_dir / 'casaubon.txt', 'r', encoding='utf-8') as f:
        clean_casaubon = f.read()
    
    stats['casaubon']['raw_size'] = len(raw_casaubon)
    stats['casaubon']['clean_size'] = len(clean_casaubon)
    stats['casaubon']['sections'] = len([l for l in clean_casaubon.split('\n') if l.startswith('## ')])
    
    return stats

def main():
    # Paths
    workspace = Path(__file__).parent.parent
    extracted_dir = workspace / 'extracted'
    clean_dir = workspace / 'clean'
    
    # Create clean directory
    clean_dir.mkdir(exist_ok=True)
    
    print("=" * 60)
    print("Stage 3: Text Cleaning and Normalization")
    print("Marcus Aurelius, Meditations Book 1")
    print("=" * 60)
    print()
    
    # Clean Greek text
    clean_greek_text(
        extracted_dir / 'greek-book1.txt',
        clean_dir / 'greek.txt'
    )
    print()
    
    # Clean Long English (primary)
    clean_long_english(
        extracted_dir / 'long-book1.txt',
        clean_dir / 'english.txt'
    )
    print()
    
    # Clean Casaubon English (witness)
    clean_casaubon_english(
        extracted_dir / 'casaubon-book1.txt',
        clean_dir / 'casaubon.txt'
    )
    print()
    
    # Generate statistics
    print("=" * 60)
    print("Cleaning Statistics")
    print("=" * 60)
    stats = generate_cleaning_stats(extracted_dir, clean_dir)
    
    print(f"\nGreek:")
    print(f"  Sections: {stats['greek']['sections']}")
    print(f"  Size: {stats['greek']['raw_size']:,} → {stats['greek']['clean_size']:,} bytes")
    
    print(f"\nLong English (primary):")
    print(f"  Sections: {stats['long']['sections']}")
    print(f"  Size: {stats['long']['raw_size']:,} → {stats['long']['clean_size']:,} bytes")
    print(f"  CSS blocks removed: {stats['long']['css_removed']}")
    print(f"  HTML entities decoded: {stats['long']['html_entities']}")
    print(f"  Footnote markers removed: {stats['long']['footnotes_removed']}")
    
    print(f"\nCasaubon English (witness):")
    print(f"  Sections: {stats['casaubon']['sections']}")
    print(f"  Size: {stats['casaubon']['raw_size']:,} → {stats['casaubon']['clean_size']:,} bytes")
    
    print()
    print("=" * 60)
    print("✓ Stage 3 cleaning complete")
    print("=" * 60)

if __name__ == '__main__':
    main()
