# `lsj.db`

## Files

- Reader runtime: `../reader/data/lsj.db`
- Release artifact: `../release/lyceum-texts-v2026.04.09/lsj.db`

## Role

Dictionary lookup database containing LSJ definitions and curated/short definitions.

## Mutability

Read-only at runtime. Regenerate/download rather than editing in place.

## Row counts

Observed in `../reader/data/lsj.db`:

| Table | Rows |
|---|---:|
| `definitions` | 110826 |
| `shortdefs` | 100207 |

## Table: `definitions`

Full LSJ-style definition entries.

| Column | Type | Key | Notes |
|---|---|---|---|
| `id` | INTEGER | PK | Source row id. |
| `lemma` | TEXT | NOT NULL, indexed | Lemma as stored/displayed. |
| `lemma_normalized` | TEXT | NOT NULL, indexed | Normalized lemma for lookup. |
| `definitions` | TEXT | NOT NULL | Definition text, often serialized/combined. |

## Table: `shortdefs`

Short definition lookup table.

| Column | Type | Key | Notes |
|---|---|---|---|
| `lemma` | TEXT | PK | Lemma key. |
| `lemma_normalized` | TEXT | NOT NULL, indexed | Normalized lemma for lookup. |
| `definition` | TEXT | NOT NULL | Concise definition. |

## Indexes

- `idx_def_lemma` on `definitions(lemma)`
- `idx_def_normalized` on `definitions(lemma_normalized)`
- `idx_shortdef_normalized` on `shortdefs(lemma_normalized)`

## Logical links

No SQLite foreign keys connect this DB to text/user DBs. Runtime code links by lemma/normalized lemma from:

- `morphology.lemma`
- `aligned_words.lemma`
- `vocabulary.lemma`
