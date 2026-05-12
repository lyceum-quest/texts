#!/usr/bin/env python3
"""
Convert greek.json to the plain text format expected by import_workspace.go
Format: [ref] text content
"""

import json
from pathlib import Path

def main():
    workspace = Path('output/texts/marcus-aurelius-meditations-book-1')
    greek_json_path = workspace / 'structured' / 'greek.json'
    greek_txt_path = workspace / 'structured' / 'greek.txt'
    
    # Read greek.json
    with open(greek_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Write greek.txt in [ref] content format
    with open(greek_txt_path, 'w', encoding='utf-8') as f:
        for seg in data.get('segments', []):
            ref = seg['ref']
            text = seg['text']
            # Replace newlines with spaces for single-line format
            text = text.replace('\n', ' ')
            f.write(f'[{ref}] {text}\n')
    
    print(f'✓ Created {greek_txt_path} with {len(data.get("segments", []))} segments')

if __name__ == '__main__':
    main()
