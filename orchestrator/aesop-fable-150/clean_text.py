#!/usr/bin/env python3
"""Text cleaning and normalization for aesop-fable-150"""

import unicodedata
import re
import json
from pathlib import Path

def normalize_unicode(text):
    """Normalize to NFC form"""
    return unicodedata.normalize('NFC', text)

def normalize_whitespace(text):
    """Normalize whitespace while preserving paragraph structure"""
    # Replace various whitespace characters with standard space
    text = re.sub(r'[\t\xa0\u2000-\u200b\u202f\u205f\u3000]', ' ', text)
    # Replace multiple spaces with single space
    text = re.sub(r' +', ' ', text)
    # Normalize line endings
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    # Remove trailing whitespace from each line
    lines = [line.rstrip() for line in text.split('\n')]
    # Remove empty lines at start and end, but preserve internal structure
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return '\n'.join(lines) + '\n'

def check_contamination(text, lang):
    """Check for common contamination patterns"""
    issues = []
    
    # Check for HTML tags
    if re.search(r'<[^>]+>', text):
        issues.append("HTML tags found")
    
    # Check for curly quotes (should be straight quotes or Greek punctuation)
    if re.search(r'[\u2018\u2019\u201c\u201d]', text):
        issues.append("Curly quotes found")
    
    # Check for common header/footer patterns
    if re.search(r'(page \d+|chapter \d+|^\d+$)', text, re.IGNORECASE | re.MULTILINE):
        issues.append("Potential page/chapter markers")
    
    # Language-specific checks
    if lang == 'greek':
        # Check for Latin alphabet contamination (excluding punctuation and numbers)
        latin_words = re.findall(r'\b[a-zA-Z]{2,}\b', text)
        if latin_words:
            issues.append(f"Latin alphabet words found: {', '.join(set(latin_words[:5]))}")
    
    if lang == 'english':
        # Check for Greek alphabet contamination in English
        if re.search(r'[\u0370-\u03ff\u1f00-\u1fff]', text):
            issues.append("Greek characters found in English text")
    
    return issues

def analyze_changes(original, cleaned):
    """Analyze what changed between original and cleaned"""
    changes = []
    
    if original != cleaned:
        # Check Unicode normalization
        if unicodedata.normalize('NFC', original) != original:
            changes.append("Unicode normalized to NFC")
        
        # Check whitespace changes
        orig_ws = re.findall(r'\s+', original)
        clean_ws = re.findall(r'\s+', cleaned)
        if orig_ws != clean_ws:
            changes.append(f"Whitespace normalized ({len(orig_ws)} -> {len(clean_ws)} sequences)")
        
        # Character count differences
        orig_len = len(original)
        clean_len = len(cleaned)
        if orig_len != clean_len:
            changes.append(f"Length changed: {orig_len} -> {clean_len} chars ({clean_len - orig_len:+d})")
    
    return changes

def clean_text(input_path, output_path, lang):
    """Clean and normalize a text file"""
    # Read original
    with open(input_path, 'r', encoding='utf-8') as f:
        original = f.read()
    
    # Apply cleaning steps
    text = original
    text = normalize_unicode(text)
    text = normalize_whitespace(text)
    
    # Check for contamination
    contamination = check_contamination(text, lang)
    
    # Analyze changes
    changes = analyze_changes(original, text)
    
    # Write cleaned text
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    return {
        'original_size': len(original),
        'cleaned_size': len(text),
        'contamination': contamination,
        'changes': changes,
        'lines': len(text.split('\n'))
    }

def main():
    workspace = Path('.')
    
    # Clean Greek text
    print("Cleaning Greek text...")
    greek_result = clean_text(
        workspace / 'extracted/greek.txt',
        workspace / 'clean/greek.txt',
        'greek'
    )
    
    # Clean English text
    print("Cleaning English text...")
    english_result = clean_text(
        workspace / 'extracted/english.txt',
        workspace / 'clean/english.txt',
        'english'
    )
    
    # Save results for report generation
    results = {
        'greek': greek_result,
        'english': english_result
    }
    
    with open(workspace / 'clean/cleaning_results.json', 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print("\nResults:")
    print(f"Greek: {greek_result['original_size']} -> {greek_result['cleaned_size']} bytes")
    print(f"  Contamination: {greek_result['contamination'] or 'None detected'}")
    print(f"  Changes: {greek_result['changes'] or 'No changes needed'}")
    print(f"\nEnglish: {english_result['original_size']} -> {english_result['cleaned_size']} bytes")
    print(f"  Contamination: {english_result['contamination'] or 'None detected'}")
    print(f"  Changes: {english_result['changes'] or 'No changes needed'}")

if __name__ == '__main__':
    main()
