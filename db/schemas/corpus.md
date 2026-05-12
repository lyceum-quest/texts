# `corpus.db`

## File

- Runtime/optional: `../reader/data/corpus.db`

## Role

Broad corpus database used for source coverage and fallback/reference data. It shares the same schema as `texts.db`.

## Mutability

Read-only at runtime. Treat as generated/downloaded data.

## Row counts

Observed in `../reader/data/corpus.db`:

| Table | Rows |
|---|---:|
| `authors` | 373 |
| `works` | 1836 |
| `editions` | 2822 |
| `segments` | 707135 |
| `aligned_segments` | 39963 |
| `aligned_words` | 1330287 |
| `text_metadata` | 227 |

## Tables

See [text-family schema](text-family.md).

## Differences from `texts.db`

The schema is identical to `reader/data/texts.db`; data counts differ slightly:

- `texts.db` has 2 more works and 1 more edition net.
- `corpus.db` has more total segments.
- Alignment row counts differ by a few rows.
- `texts.db` contains newer workspace/curated URNs; `corpus.db` reflects broader source corpus data.

## Operational notes

- Large file: observed around 819 MB.
- Optional/historical in the current reader architecture.
- Keep separate from curated `editions.db` semantics.
