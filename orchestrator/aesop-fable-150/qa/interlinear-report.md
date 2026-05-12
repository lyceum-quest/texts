# Interlinear report

## Scope

- Work: Aesop, Fable 150 (The Crab and the Fox)
- Workspace: `output/texts/aesop-fable-150`
- Command: `promote`
- Strategy: `llm-adversarial`
- Decision: `promoted`

## Metrics

- Segments: 5
- Words: 55
- Glossed words: 55
- Missing contextual glosses: 0
- Words needing review: 0
- Segment unresolved flags: 0
- Document unresolved flags: 0
- Completeness: 1.00

## Benchmark

- Status: `promoted`
- No ground-truth corpus available for Aesop fables
- LLM interlinear produced via Creator→Skeptic→Referee adversarial loop
- Challenge rate: 34.5% (19 of 55 words challenged)
- All challenges adjudicated by Referee
- 100% gloss completeness, 100% lemma completeness
- Zero dictionary-style glosses — all contextual

## Evidence sources

- `interlinear/chapter_150_llm.json` (LLM adversarial interlinear)
- `interlinear/transliteration.json`
- `versification/english_edition.json`
- `interlinear/ground-truth-benchmark.json`

## Blocking issues

- None

## Quality notes

- All 55 words have contextual glosses (e.g., "crab", "having-come-up", "sea")
- All words have lemma entries
- All words have part-of-speech tags
- Agent mode used (pi subprocesses), total cost: $0.38
- Imported to texts.db: 5 aligned segments, 55 aligned words
