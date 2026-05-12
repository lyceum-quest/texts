#!/usr/bin/env python3
"""
Segment Marcus Aurelius Meditations Book 1 by sections (1.1, 1.2, etc.)
Each section becomes one segment.
"""

import json
import re
from datetime import datetime, timezone
from pathlib import Path

def parse_sections(filepath):
    """Parse a clean file into sections based on ## headers."""
    sections = []
    current_ref = None
    current_lines = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            
            # Check for section header
            match = re.match(r'^##\s+(1\.\d+)\s*$', line)
            if match:
                # Save previous section if any
                if current_ref and current_lines:
                    text = '\n'.join(current_lines).strip()
                    if text:
                        sections.append({
                            'ref': current_ref,
                            'text': text
                        })
                
                # Start new section
                current_ref = match.group(1)
                current_lines = []
            elif current_ref is not None:
                # Skip blank lines at start of section
                if not current_lines and not line.strip():
                    continue
                current_lines.append(line)
    
    # Save final section
    if current_ref and current_lines:
        text = '\n'.join(current_lines).strip()
        if text:
            sections.append({
                'ref': current_ref,
                'text': text
            })
    
    return sections

def create_structured_file(source_path, output_path, reference_system='section', unit='section'):
    """Create a structured JSON file from a clean file."""
    sections = parse_sections(source_path)
    
    data = {
        'schema_version': 1,
        'generated_at': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        'reference_system': reference_system,
        'unit': unit,
        'source_path': str(source_path),
        'segments': sections
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(sections)

def create_reference_inventory(structured_dir):
    """Create reference-inventory.txt listing all refs."""
    refs = []
    
    # Read greek.json to get canonical refs
    greek_path = structured_dir / 'greek.json'
    if greek_path.exists():
        with open(greek_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            refs = [seg['ref'] for seg in data.get('segments', [])]
    
    # Write inventory
    inventory_path = structured_dir / 'reference-inventory.txt'
    with open(inventory_path, 'w', encoding='utf-8') as f:
        f.write('# Reference Inventory - Marcus Aurelius, Meditations Book 1\n')
        f.write(f'# Generated: {datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")}\n')
        f.write(f'# Reference system: section\n')
        f.write(f'# Total sections: {len(refs)}\n\n')
        for ref in refs:
            f.write(f'{ref}\n')
    
    return len(refs)

def main():
    workspace = Path('output/texts/marcus-aurelius-meditations-book-1')
    clean_dir = workspace / 'clean'
    structured_dir = workspace / 'structured'
    structured_dir.mkdir(exist_ok=True)
    
    # Process each clean file
    files = {
        'greek.txt': 'greek.json',
        'english.txt': 'english.json',
        'casaubon.txt': 'casaubon.json'
    }
    
    counts = {}
    for clean_file, structured_file in files.items():
        source = clean_dir / clean_file
        output = structured_dir / structured_file
        if source.exists():
            count = create_structured_file(source, output)
            counts[clean_file] = count
            print(f'✓ {clean_file}: {count} sections → {structured_file}')
    
    # Create reference inventory
    inv_count = create_reference_inventory(structured_dir)
    print(f'✓ reference-inventory.txt: {inv_count} refs')
    
    # Create segments.json (combined view with greek + english)
    greek_path = structured_dir / 'greek.json'
    english_path = structured_dir / 'english.json'
    
    if greek_path.exists() and english_path.exists():
        with open(greek_path, 'r') as f:
            greek_data = json.load(f)
        with open(english_path, 'r') as f:
            english_data = json.load(f)
        
        # Build lookup for english by ref
        english_by_ref = {seg['ref']: seg['text'] for seg in english_data.get('segments', [])}
        
        # Combine
        combined = []
        for seg in greek_data.get('segments', []):
            combined_seg = {
                'ref': seg['ref'],
                'greek_text': seg['text']
            }
            if seg['ref'] in english_by_ref:
                combined_seg['english_text'] = english_by_ref[seg['ref']]
            combined.append(combined_seg)
        
        segments_output = {
            'schema_version': 1,
            'generated_at': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            'reference_system': 'section',
            'unit': 'section',
            'segments': combined
        }
        
        segments_path = structured_dir / 'segments.json'
        with open(segments_path, 'w', encoding='utf-8') as f:
            json.dump(segments_output, f, ensure_ascii=False, indent=2)
        print(f'✓ segments.json: {len(combined)} combined segments')
    
    print(f'\nSegmentation complete: {len(counts)} files processed')

if __name__ == '__main__':
    main()
