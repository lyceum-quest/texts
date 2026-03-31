# Stage 2: Acquisition and Extraction Report

**Workspace**: aesop-fable-150  
**Date**: 2026-03-23  
**Stage**: 2-acquisition-extraction

## Fable Identification

**CRITICAL DISCOVERY**: Chambry 150 is **NOT** "The Ass and the Mule" as initially assumed.

- **Actual fable**: Καρκῖνος καὶ ἀλώπηξ (The Crab and the Fox)
- **Perry Index**: Perry 116
- **Chambry number**: 150

## Greek Source

### Primary Source: mythfolklore.net (Laura Gibbs Aesopica)
- **URL**: http://mythfolklore.net/aesopica/chambry/150.htm
- **Edition**: Chambry (Belles Lettres, 1925/6)
- **Format**: HTML
- **Extraction mode**: Direct text extraction from HTML
- **Quality**: HIGH - Clean digital text
- **Confidence**: HIGH - Authoritative scholarly edition

### Raw file
- `raw/mythfolklore_chambry_150_http.html` (6.4 KB)

### Extracted file
- `extracted/greek.txt` (407 bytes)

### Text content
The fable text includes:
- Title: Καρκῖνος καὶ ἀλώπηξ
- Narrative text (5 sentences)
- Moral/application (ὁ μῦθος δηλοῖ)

## English Source

### Primary Source: Project Gutenberg - Vernon Jones (1912)
- **URL**: https://www.gutenberg.org/cache/epub/11339/pg11339.txt
- **Translator**: V.S. Vernon Jones
- **Year**: 1912
- **Format**: Plain text
- **Extraction mode**: Direct extraction from plain text file
- **Quality**: HIGH - Clean digital text
- **Confidence**: HIGH - Public domain, verified translation

### Raw file
- `raw/gutenberg_jones_11339.txt` (237 KB)

### Extracted file
- `extracted/english.txt` (466 bytes)

### Text content
The fable includes:
- Title: THE CRAB AND THE FOX
- Narrative text (3 sentences)
- Moral: "Be content with your lot."

## Secondary English Source Attempted

### Gutenberg - Townsend (1867)
- **URL**: https://www.gutenberg.org/cache/epub/28/pg28.txt
- **Status**: Downloaded (100 KB)
- **Result**: This fable not present in Townsend collection
- **Note**: Townsend does not include Perry 116 / Chambry 150

## Extraction Path Used

### Greek
1. Attempted Perseus Digital Library - failed (URL redirected to wrong text)
2. Attempted Greek Wikisource - page doesn't exist
3. SUCCESS: mythfolklore.net HTML extraction
4. Extracted clean Greek text from HTML using grep/sed
5. Verified against Perry Index cross-reference on source page

### English
1. Downloaded full Gutenberg files for both Jones and Townsend
2. Searched for fable by title keywords
3. Located "THE CRAB AND THE FOX" in Vernon Jones at line 4480
4. Extracted complete fable text including moral
5. Confirmed Townsend does not include this fable

## Structural Preservation Notes

### Greek
- Title preserved
- Paragraph structure maintained
- Moral/application included inline (not separated)
- No critical apparatus or variant readings in source
- No headers, footers, or navigation elements

### English
- Title preserved
- Paragraph structure maintained (3 sentences as one paragraph)
- Moral separated as standalone line
- No editorial notes or illustrations
- Clean extraction with no boilerplate

## Quality Confidence

### Greek: HIGH
- Source is authoritative Chambry edition
- Digital-native text (not OCR)
- No suspect characters or encoding issues
- Complete fable text with no gaps
- Cross-referenced with Perry Index

### English: HIGH
- Authoritative 1912 translation
- Digital-native text (not OCR)
- No suspect characters or encoding issues
- Complete fable with moral
- Public domain, widely used translation

## Warnings / Issues

1. **CRITICAL**: Initial assumption about fable identity was INCORRECT
   - User specified "The Ass and the Mule" but Chambry 150 is "The Crab and the Fox"
   - This is now corrected in all artifacts

2. **Minor**: Perseus Digital Library source failed
   - Text ID 1999.01.0130 does not point to Aesop's fables
   - Fell back to mythfolklore.net successfully

3. **Minor**: Townsend translation does not include this fable
   - Only one English witness available (Vernon Jones)
   - This is sufficient for pipeline progress

4. **Note**: Greek Wikisource page for Aesop's fables does not exist yet
   - Not a blocker - primary source (Chambry via mythfolklore.net) is excellent

## Stage 3 Readiness

**Status**: READY

All required artifacts present:
- ✅ Raw Greek source preserved
- ✅ Extracted Greek text clean and complete
- ✅ Raw English source preserved
- ✅ Extracted English text clean and complete
- ✅ Extraction paths documented
- ✅ Quality confidence assessed

**Recommendation**: Proceed to Stage 3 (cleaning-normalization)

## Files Created

### Raw artifacts
- `raw/mythfolklore_chambry_150_http.html` - Greek source (HTML)
- `raw/gutenberg_jones_11339.txt` - English source (full collection)
- `raw/gutenberg_townsend_28.txt` - English source (full collection, fable not present)
- `raw/perseus_chambry_150.html` - Failed attempt (empty)
- `raw/wikisource_greek_aesop.html` - Failed attempt (index page only)

### Extracted artifacts
- `extracted/greek.txt` - Clean Greek text of Chambry 150
- `extracted/english.txt` - Clean English text from Vernon Jones

### Reports
- `qa/extraction-report.md` - This file

## Verification Checklist

- [x] Raw sources preserved for all extracted texts
- [x] Extraction mode documented
- [x] Sample spot-check confirms extracted text matches source
- [x] Greek text complete with title and moral
- [x] English text complete with title and moral
- [x] No OCR issues (digital-native sources)
- [x] No headers/footers/navigation in extracted text
- [x] Perry Index cross-reference confirmed (Perry 116)
- [x] Fable identity corrected from initial assumption

## Next Steps

1. Run `/text-cleaning run aesop-fable-150` for Stage 3
2. Update manifest.json with correct fable title
3. Consider adding Perry Index number to metadata
4. Stage 4 segmentation should be straightforward (prose fable, ~3-5 sentences)
