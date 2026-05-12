# `texts.db`

## Files

- Runtime: `../reader/data/texts.db`
- Release artifact: `../release/lyceum-texts-v2026.04.09/texts.db`
- Orchestrator small pipeline variant: `../orchestrator/data/texts.db`

## Role

Full reader library database for browsing authors/works/editions and reading basic text segments. It also currently contains legacy or imported alignment data, but curated Lyceum interlinear data should be treated as belonging to `editions.db`.

## Mutability

Read-only at reader runtime. Regenerate from import scripts rather than editing in place.

## Runtime row counts

Observed in `../reader/data/texts.db`:

| Table | Rows |
|---|---:|
| `authors` | 373 |
| `works` | 1838 |
| `editions` | 2823 |
| `segments` | 706021 |
| `aligned_segments` | 39968 |
| `aligned_words` | 1330342 |
| `text_metadata` | 227 |

## Tables

See [text-family schema](text-family.md) for the data dictionary shared by `texts.db`, `corpus.db`, and `editions.db`.

## Full corpus schema differences

Compared with curated `editions.db` variants:

- `aligned_segments.translation_urn` is nullable.
- `aligned_segments.transliteration` is `NOT NULL`.
- `aligned_segments` has `UNIQUE(source_urn, reference)`.
- `aligned_words.transliteration` is `NOT NULL`.
- `editions` does not have curated columns such as `is_lyceum_curated`, `parent_edition_id`, or `parent_work_urn`.
- `text_metadata.word_count`, `unique_lemma_count`, and `difficulty_stage` default to `0`.

## Indexes

- `idx_segments_edition_ref` on `segments(edition_id, reference)`
- `idx_editions_work` on `editions(work_id)`
- `idx_works_author` on `works(author_id)`
- `idx_aligned_segments_urn_ref` on `aligned_segments(source_urn, reference)`
- `idx_aligned_segments_source_urn` on `aligned_segments(source_urn)`
- `idx_aligned_words_segment` on `aligned_words(segment_id)`
- `idx_aligned_words_segment_lemma` on `aligned_words(segment_id, lemma)`

## Operational notes

- Large file: observed around 903 MB in `reader/data`.
- Use for full-library browsing and ordinary segment reading.
- Do not use as the authoritative source for the curated Lyceum Editions list when `editions.db` exists.
