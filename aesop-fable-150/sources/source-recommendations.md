# Source Recommendations for Aesop, Fable 150

**Generated:** 2026-03-23  
**Stage:** 1-source-discovery  
**Status:** Complete - recommendations ready for Stage 2

---

## Executive Summary

**Recommended Greek Source:** Perseus Digital Library - Chambry Edition  
**Recommended English Witnesses:** Townsend (1867), Vernon Jones (1912)  
**Critical Next Step:** Verify fable numbering - map Chambry 150 to Perry Index

---

## Greek Source Recommendation

### PRIMARY: Perseus Chambry Edition
- **Source ID:** `perseus-chambry`
- **URL:** http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0130
- **Editor:** Émile Chambry (1925-1926)
- **Score:** 95/100

**Rationale:**
- Most authoritative modern scholarly edition
- Clean, parseable text with stable structure
- Standard reference for Aesopic fables
- Perseus provides good extraction infrastructure
- Numbered fables for easy reference

**Extraction Strategy:**
- Check Perseus API/CTS capabilities first
- Fall back to structured HTML scraping if needed
- Text should be clean with minimal post-processing

**Known Risks:**
- Numbering verification: Need to confirm which specific fable is "150" in Chambry
- May need Perry Index mapping to cross-reference with English translations
- Fable may be very short (single paragraph in some cases)

### BACKUP: Internet Archive Chambry
- **Source ID:** `archive-org-chambry`
- **Score:** 70/100
- Only if Perseus extraction fails
- Requires OCR or manual transcription

---

## English Witness Recommendations

### PRIMARY: George Fyler Townsend (1867)
- **Source ID:** `townsend-1867`
- **URL:** https://www.gutenberg.org/ebooks/28
- **Score:** 90/100

**Rationale:**
- Classic public domain translation
- Clean Project Gutenberg text
- Well-known and widely cited
- Prose style suitable for learners

**Alignment Fitness:**
- MODERATE - Prose translation may not match Greek structure line-by-line
- May require sentence-level rather than verse-level alignment
- Good for meaning but not structural parallelism

**Extraction Strategy:**
- Use Gutenberg plain text API
- Parse by fable title or number
- Cross-reference with Perry Index if numbering differs

### SECONDARY: V.S. Vernon Jones (1912)
- **Source ID:** `vernon-jones-1912`
- **URL:** https://www.gutenberg.org/ebooks/11339
- **Score:** 85/100

**Rationale:**
- More modern English than Townsend
- Also public domain and on Gutenberg
- Good alternative witness for comparison

**Alignment Fitness:**
- MODERATE - Similar structural challenges to Townsend
- May have different fable selection
- Useful for providing alternative phrasing

### NOT RECOMMENDED (but noted):
- **L'Estrange (1692):** Too archaic for modern learners
- **Croxall (1722):** Adds moralizing commentary that diverges from source
- Both available as historical references only

---

## Auxiliary Resources

### CRITICAL: Perry Index Mapping
- **Purpose:** Cross-reference numbering systems
- **Why Essential:** "Chambry 150" may be numbered differently in English translations
- **Action Required:** Look up Perry number for Chambry 150 before extraction

### USEFUL: Perseus Morphology
- **Purpose:** Word-level morphological analysis
- **Integration:** Perseus provides click-through morphology
- **Stage 8 Note:** May supplement treebank data if treebank unavailable for this fable

### REFERENCE: Laura Gibbs Aesopica
- **URL:** https://mythfolklore.net/aesopica/
- **Purpose:** Comprehensive cross-reference of fable numbers and titles
- **Use Case:** Essential for identifying which specific fable is "150"

---

## Provenance Notes

### Licensing
- **Greek:** Chambry edition (1925-1926) is public domain
- **English:** Both recommended translations pre-1928, confirmed PD
- **No licensing blockers identified**

### Quality Assessment
- **Greek text quality:** HIGH - scholarly edition, stable text tradition
- **English text quality:** HIGH - both are well-edited PD texts on Gutenberg
- **OCR risk:** LOW - using digital-native sources (Perseus, Gutenberg)

### Reproducibility
- **Perseus:** Stable URLs, canonical text IDs
- **Gutenberg:** Stable ebook numbers
- **All sources:** Publicly accessible, no authentication required
- **Extraction:** Highly reproducible

---

## Verification Blockers & Warnings

### ⚠️ CRITICAL: Fable Identification
**Issue:** "Fable 150" is edition-specific numbering  
**Risk:** May not correspond to same fable in other editions  
**Mitigation Required:**
1. Identify actual fable title/subject in Chambry 150
2. Map to Perry Index number
3. Verify same fable exists in English translations
4. Document cross-reference in provenance

**Example Scenario:**
- Chambry 150 might be "The Fox and the Grapes"
- Perry Index: P15
- Townsend: Fable 33
- Need to track all three numbering systems

### ⚠️ MODERATE: Fable Length
**Issue:** Some Aesop fables are very short (3-5 lines Greek)  
**Impact on Pipeline:**
- May have minimal structure to segment
- Alignment might be trivial (1:1 paragraph)
- Interlinear generation straightforward but limited pedagogical value
- Consider whether standalone fable or should be part of collection

**Recommendation:** Assess fable length in Stage 2 and consider:
- If <10 Greek sentences: May want to bundle multiple fables
- If very short: Flag for user review about pedagogical utility

### ℹ️ NOTE: Verse vs Prose
**Greek:** Chambry presents prose versions  
**English:** Townsend/Jones are prose  
**Impact:** No verse alignment challenges, simpler structure  
**Stage 6 Note:** Versification may be straightforward paragraph-level

---

## Stage 2 Handoff

### Ready to Extract:
✅ Primary Greek source identified (Perseus Chambry)  
✅ Primary English witnesses identified (Townsend, Jones)  
✅ Extraction methods defined  
✅ No licensing blockers  

### Action Items for Stage 2:
1. **FIRST:** Verify fable identity
   - Look up Chambry 150 title/content
   - Find Perry number
   - Confirm existence in English translations
   
2. **Extract Greek:**
   - Perseus Chambry fable 150
   - Preserve source structure
   - Record exact Perseus citation
   
3. **Extract English:**
   - Gutenberg Townsend - find matching fable by title/Perry
   - Gutenberg Jones - find matching fable
   - Document cross-reference mapping

4. **Provenance:**
   - Record Perry number in provenance.md
   - Document title in all sources
   - Note any textual variants

### Potential Blockers:
- Fable 150 does not exist in Chambry (numbering gap)
- English translations don't include this specific fable
- Fable identity uncertain due to numbering discrepancies

**If blocked:** Return to Stage 1 for alternative source discovery or fable re-selection.

---

## Ranking Criteria Applied

### Greek Sources
1. **Provenance:** Chambry is standard scholarly edition ✓
2. **Parseability:** Perseus HTML is clean and structured ✓
3. **License:** Public domain, no restrictions ✓
4. **Structural fitness:** Numbered fables, clear divisions ✓
5. **Reproducibility:** Stable Perseus URLs ✓

### English Witnesses
1. **Provenance:** Townsend and Jones are established translations ✓
2. **Parseability:** Gutenberg plain text is excellent ✓
3. **License:** Both pre-1928 PD ✓
4. **Alignment fitness:** Moderate (prose, may need sentence-level) ⚠️
5. **Reproducibility:** Stable Gutenberg ebook numbers ✓

### Decision Rule Applied
- Did NOT choose "easiest to fetch" over "best source"
- Perseus Chambry is both accessible AND authoritative
- Archive.org scans rejected despite availability due to OCR requirements
- L'Estrange/Croxall rejected despite PD status due to archaic language

---

## Confidence Assessment

**Overall Stage 1 Confidence:** MODERATE-HIGH

**High Confidence:**
- Source quality (Chambry, Townsend, Jones are all solid)
- Extraction feasibility (Perseus and Gutenberg are reliable)
- Licensing (all clear PD)

**Moderate Confidence:**
- Fable identification (need to verify numbering)
- English alignment fitness (prose may not match structure perfectly)

**Mitigation:**
- Stage 2 must verify fable identity BEFORE full extraction
- Consider extracting multiple English versions for comparison
- Document all numbering cross-references carefully

---

## References

- Perry, B.E. (1952). *Aesopica: A Series of Texts Relating to Aesop or Ascribed to Him*. University of Illinois Press.
- Chambry, Émile (1925-1926). *Aesopi Fabulae*. Paris: Les Belles Lettres.
- Perseus Digital Library: http://www.perseus.tufts.edu
- Project Gutenberg: https://www.gutenberg.org
- Laura Gibbs Aesopica: https://mythfolklore.net/aesopica/

---

*Stage 1 source discovery complete. Recommend advancing to Stage 2 with noted verification requirements.*
