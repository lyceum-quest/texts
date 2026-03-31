# Witness Collection Summary

**Text:** Aesop, Fable 150 (The Crab and the Fox / Καρκῖνος καὶ ἀλώπηξ)  
**Stage:** 5-witness-normalization-ranking  
**Status:** ✅ COMPLETE  
**Date:** 2026-03-23

## Collected Witnesses

### 1. Vernon Jones (1912)
- **File:** `jones-1912.txt`
- **Source:** Project Gutenberg #11339
- **License:** Public Domain
- **Roles:** adversarial-comparison, glossing-reference, reader-display

## Key Findings

✅ **Adversarial comparison witness available** — jones-1912 is sufficiently literal for Stage 6a error detection  
✅ **Glossing reference available** — jones-1912 provides good vocabulary for Stage 8 interlinear work  
✅ **Reader display witness available** — jones-1912 suitable as optional literary view  
❌ **No versification candidates** — jones-1912 lacks native reference markers; prose structure incompatible with Greek sentence segmentation

## Pipeline Impact

### Stage 6 (Translation)
- **6a (Synthesis):** REQUIRED — no fast-path versification available
- **6b (Versify):** Will validate generated translation (not witness)
- **Comparison material:** jones-1912 available for adversarial review

### Stage 8 (Interlinear)
- **Glossing reference:** jones-1912 available for contextual sense disambiguation

### Reader Display
- **Display witness:** jones-1912 will appear in sidebar as optional alternative
- **Display format:** Prose (as-is, not verse-aligned)

## Notes

The Vernon Jones translation is a high-quality, accessible English prose version that serves well for comparison and reference, but cannot be directly versified due to:
1. Absence of native reference markers (no sentence/verse numbering)
2. Structural mismatch: 2 prose paragraphs vs 5 Greek segments (60% divergence)
3. Prose combines multiple Greek sentences into flowing narrative

Stage 6a translation generation is mandatory for this text to produce the verse-aligned English required for row view in the reader.

## Verification

Automated verification passed: 7/7 checks (see `../qa/witness-report.md` for details)

---

For catalog schema and role definitions, see `catalog.json` in this directory.
