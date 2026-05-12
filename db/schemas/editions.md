# `editions.db`

## Files

- Reader runtime: `../reader/data/editions.db`
- Orchestrator output: `../orchestrator/data/editions.db`

## Role

Curated Lyceum pipeline editions. This is the authoritative source for curated/interlinear Lyceum editions, contextual glosses, and word-level alignments.

## Mutability

Read-only at reader runtime. Regenerate via orchestrator/import pipeline.

## Reader row counts

Observed in `../reader/data/editions.db`:

| Table | Rows |
|---|---:|
| `authors` | 3 |
| `works` | 4 |
| `editions` | 10 |
| `segments` | 98 |
| `aligned_segments` | 32 |
| `aligned_words` | 1973 |
| `text_metadata` | 0 |

## Tables

See [text-family schema](text-family.md).

## Curated edition fields

`reader/data/editions.db` extends the base text-family `editions` table:

| Column | Type | Notes |
|---|---|---|
| `is_lyceum_curated` | BOOLEAN DEFAULT 0 | Marks editions produced/curated by the Lyceum pipeline. |
| `parent_edition_id` | INTEGER REFERENCES `editions(id)` | Links a derived/curated edition to a parent/source edition in the same DB. |
| `parent_work_urn` | TEXT DEFAULT NULL | Links curated work back to a source work URN. Present in reader `editions.db`; not present in the observed orchestrator copy. |

## Differences from full corpus schema

- `aligned_segments.id` and `aligned_words.id` are autoincrement.
- `aligned_segments.translation_urn` is `NOT NULL`.
- `aligned_segments.transliteration` is nullable.
- `aligned_words.transliteration` is nullable.
- `segments` has a unique index on `(edition_id, reference)`.
- Full-corpus alignment indexes are not all present in the small curated DB.

## Indexes

- `idx_segments_edition_ref` on `segments(edition_id, reference)`
- `idx_segments_edition_ref_unique` unique on `segments(edition_id, reference)`
- `idx_editions_work` on `editions(work_id)`
- `idx_works_author` on `works(author_id)`

## Operational notes

- Small file: observed around 320 KB.
- The reader should tolerate this DB being absent and disable curated Lyceum Editions gracefully.
- Do not mix broad library browsing semantics with curated-interlinear semantics; use `texts.db` for the library and `editions.db` for curated alignments.
