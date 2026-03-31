# Provenance

- Work: Aesop, Fable 150
- Workspace slug: `aesop-fable-150`
- Mode: `add`
- Profile: `add`
- Created: 2026-03-23T16:36:22Z

## Greek sources

| status | title | url | editor | year | license | format | extraction | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| recommended | Aesopica (Chambry) | http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0130 | Émile Chambry | 1925-1926 | public-domain | HTML | perseus-api-or-scrape | Standard scholarly edition, score: 95/100 |
| backup | Aesopica (Chambry) - Archive.org | https://archive.org/details/aesopifabulae00aeso | Émile Chambry | 1925 | public-domain | DjVu/PDF | ocr-manual | Scanned edition if Perseus unavailable, score: 70/100 |
| reference | Greek Wikisource | https://el.wikisource.org/wiki/Αισώπου_μύθοι | Community | various | CC-BY-SA | wikitext | wikisource-api | Verification only, score: 60/100 |

## English witnesses

| status | title | url | translator | year | license | format | extraction | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| recommended | Aesop's Fables | https://www.gutenberg.org/ebooks/28 | George Fyler Townsend | 1867 | public-domain | plain-text | gutenberg-api | Primary witness, score: 90/100 |
| recommended | Aesop's Fables | https://www.gutenberg.org/ebooks/11339 | V.S. Vernon Jones | 1912 | public-domain | plain-text | gutenberg-api | Secondary witness, score: 85/100 |
| reference | Fables (L'Estrange) | https://archive.org/details/fables-of-aesop-and-other-eminent-mythologists | Roger L'Estrange | 1692 | public-domain | DjVu/PDF | ocr-manual | Historical reference only (archaic), score: 60/100 |
| reference | Fables (Croxall) | https://archive.org/details/fables-of-aesop-croxall | Samuel Croxall | 1722 | public-domain | DjVu/PDF | ocr-manual | Historical reference only, score: 65/100 |

## Auxiliary resources

- **Perry Index**: Standard numbering cross-reference for Aesopic fables
- **Perseus Morphology**: Word-level morphological analysis available
- **Laura Gibbs Aesopica** (https://mythfolklore.net/aesopica/): Comprehensive fable cross-reference
- **Fable title index**: Need to map Chambry 150 to Perry number and English equivalents

## Decisions

- **Base Greek edition strategy**: Perseus Digital Library - Chambry edition (1925-1926)
- **Target reference system**: Chambry numbering (fable 150), with Perry Index cross-reference
- **Critical verification required**: Map Chambry 150 to Perry number before Stage 2 extraction
- **English witness strategy**: Use both Townsend and Jones for comparison
- **Structural approach**: Prose text, likely paragraph-level alignment

## Licensing notes

- All Greek sources public domain (pre-1926)
- All recommended English translations public domain (pre-1928)
- No copyright restrictions on extraction or derivative works
- CC-BY-SA attribution required for Wikisource if used
- No licensing blockers identified

## Stage 1 completion notes

- **Fable identification**: CRITICAL - must verify which fable is Chambry 150 in Stage 2
- **Numbering discrepancy risk**: MODERATE - Chambry, Perry, and English translation numbering may differ
- **Fable length**: Unknown - may be very short (assess pedagogical value if <10 sentences)
- **Quality confidence**: HIGH - all sources are authoritative and well-maintained
- **Extraction confidence**: HIGH - digital-native sources with good structure

## Stage 2 completion notes (2026-03-23)

### CRITICAL DISCOVERY: Fable Identity Corrected

**Initial assumption was INCORRECT**: Chambry 150 is NOT "The Ass and the Mule"

**Actual fable**: 
- Greek: Καρκῖνος καὶ ἀλώπηξ (The Crab and the Fox)
- Perry Index: Perry 116
- Chambry: 150

### Greek source acquired

**Primary source used**: mythfolklore.net (Laura Gibbs Aesopica)
- URL: http://mythfolklore.net/aesopica/chambry/150.htm
- Edition: Chambry (Belles Lettres, 1925/6)
- Format: HTML
- Extraction: Direct text extraction
- Quality: HIGH - authoritative digital text
- Status: ✅ Acquired and extracted

**Perseus attempt**: FAILED
- URL attempted: http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0130:fable=150
- Issue: Text ID redirected to Hesiod's Theogony, not Aesop
- Resolution: Used mythfolklore.net as primary source instead

**Greek Wikisource attempt**: FAILED
- URL: https://el.wikisource.org/wiki/Αισώπου_μύθοι
- Issue: Page does not exist yet on Wikisource
- Resolution: Not needed - primary source is excellent

### English source acquired

**Primary source used**: Project Gutenberg - Vernon Jones (1912)
- URL: https://www.gutenberg.org/cache/epub/11339/pg11339.txt
- Translator: V.S. Vernon Jones
- Year: 1912
- Format: Plain text
- Extraction: Direct extraction from line 4480
- Quality: HIGH - clean public domain text
- Status: ✅ Acquired and extracted

**Townsend (1867) check**: NOT PRESENT
- URL: https://www.gutenberg.org/cache/epub/28/pg28.txt
- Status: Downloaded but fable not included in this collection
- Note: Only one English witness available (Vernon Jones)

### Extraction path summary

- Greek: HTML scraping from mythfolklore.net
- English: Plain text extraction from Gutenberg
- Both sources: digital-native (no OCR)
- Both extractions: clean with no boilerplate
- Confidence: HIGH for both

### Files created

**Raw artifacts**:
- `raw/mythfolklore_chambry_150_http.html` (6.4 KB)
- `raw/gutenberg_jones_11339.txt` (237 KB)
- `raw/gutenberg_townsend_28.txt` (100 KB)

**Extracted artifacts**:
- `extracted/greek.txt` (407 bytes) - Chambry 150 text
- `extracted/english.txt` (466 bytes) - Vernon Jones translation

**Quality assurance**:
- `qa/extraction-report.md` - Full extraction documentation

### Stage 3 readiness

**Status**: ✅ READY

- Greek text: complete, clean, digital-native
- English text: complete, clean, digital-native
- No OCR issues
- No structural cleanup needed
- Fable identity confirmed via Perry Index cross-reference
