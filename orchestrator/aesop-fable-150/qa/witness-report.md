# Stage 5 Witness Collection Report

**Text:** Aesop, Fable 150 (The Crab and the Fox)  
**Stage:** 5-witness-normalization-ranking  
**Generated:** 2026-03-23T17:30:00Z  
**Status:** ✅ PASS

## Collected Witnesses

### Vernon Jones (1912)

**Source:** Project Gutenberg (#11339)  
**Translator:** V. S. Vernon Jones  
**Year:** 1912  
**License:** Public Domain  
**File:** `witnesses/jones-1912.txt`

**Roles:**
- ✅ adversarial-comparison
- ✅ glossing-reference  
- ✅ reader-display
- ❌ versification-candidate

**Literalness:** Moderately literal

**Structural Analysis:**
- Greek segments: 5 (title + 4 sentences)
- English segments: 2 (title + 1 narrative paragraph + 1 moral)
- Mapping: Prose combines 150.1-150.3 into flowing narrative; moral simplified

**Quality Notes:**
- Clear, natural English prose
- Faithful to Greek content and meaning
- Good vocabulary choices for learner comprehension
- Accessible 20th century English style

**Versification Assessment:**
Vernon Jones translation is **NOT** a versification candidate because:
1. ❌ No native reference markers (no sentence/verse numbering)
2. ❌ Structural mismatch: 2 prose paragraphs vs 5 Greek segments (60% divergence)
3. ❌ Combines multiple Greek sentences into flowing prose
4. ⚠️  Moral is paraphrased ("Be content with your lot" vs full Greek statement)

According to pipeline policy, versification requires:
- Native reference markers matching Greek reference system
- Segment count within 10% of Greek
- No forced segmentation or structural modification

Vernon Jones fails criteria 1 and 2. Stage 6a generation is required.

## Role Coverage

| Role | Coverage | Status |
|------|----------|--------|
| adversarial-comparison | 1 witness (jones-1912) | ✅ Required minimum met |
| glossing-reference | 1 witness (jones-1912) | ✅ Recommended |
| reader-display | 1 witness (jones-1912) | ✅ Optional |
| versification-candidate | 0 witnesses | ⚠️  Stage 6a required |

## Downstream Impact

### Stage 6a (Translation Synthesis)
**Status:** REQUIRED  
**Comparison witness:** jones-1912 available for adversarial review  
**Confidence:** Moderate (single witness limits cross-validation)

### Stage 6b (Versification)
**Status:** Required to validate generated translation  
**Input:** Stage 6a generated translation (not witness)

### Stage 8 (Interlinear)
**Status:** Ready  
**Glossing reference:** jones-1912 available for contextual disambiguation

### Reader Display
**Status:** Ready  
**Display witness:** jones-1912 available as optional alternative view  
**Note:** Displayed as-is (prose form) - NOT aligned to Greek verses

## Verification

- ✅ Witness catalog created with schema v2
- ✅ Provenance recorded (Gutenberg URL, translator, year, license)
- ✅ Each witness has `roles` array with ≥1 classification
- ✅ At least one adversarial-comparison witness exists
- ✅ Witnesses preserved as-is (not structurally modified)
- ✅ Versification-candidate absence documented
- ✅ Stage 6a requirement explicitly noted

## Recommendations

1. **Single witness limitation:** Consider searching for additional PD Aesop translations (Townsend, Temple, Jacobs) to improve adversarial comparison confidence
2. **Stage 6a priority:** No versification fast-path available - translation generation is mandatory
3. **Moral handling:** Pay attention to moral (150.4) during Stage 6a - Jones simplifies it significantly

## Next Steps

1. Advance to Stage 6a (translation-synthesis)
2. Use jones-1912 for adversarial comparison during generation
3. Ensure generated translation preserves full moral statement (150.4)
4. Validate generated translation in Stage 6b before proceeding

---

**Stage 5 Status:** COMPLETE  
**Stage 6 Ready:** YES (with Stage 6a generation required)
