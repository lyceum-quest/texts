# `morph.db`

## Files

- Reader runtime: `../reader/data/morph.db`
- Orchestrator data: `../orchestrator/data/morph.db`
- Release artifact: `../release/lyceum-texts-v2026.04.09/morph.db`

## Role

Greek morphology lookup by surface form, normalized form, and lemma.

## Mutability

Read-only at runtime. Regenerate/download rather than editing in place.

## Row counts

Observed in reader and orchestrator copies:

| Table | Rows |
|---|---:|
| `morphology` | 1546804 |

## Table: `morphology`

| Column | Type | Key | Notes |
|---|---|---|---|
| `id` | INTEGER | PK | Source row id. |
| `form` | TEXT | NOT NULL, indexed | Surface Greek form. |
| `form_normalized` | TEXT | NOT NULL, indexed | Normalized form for lookup. |
| `lemma` | TEXT | NOT NULL, indexed | Lemma. |
| `definition` | TEXT |  | Short/source definition. |
| `pos` | TEXT |  | Part of speech. |
| `morphology` | TEXT |  | Combined morphology string. |
| `tense` | TEXT |  | Verb tense. |
| `voice` | TEXT |  | Verb voice. |
| `mood` | TEXT |  | Verb mood. |
| `person` | TEXT |  | Person. |
| `number` | TEXT |  | Number. |
| `case_name` | TEXT |  | Nominal case. |
| `gender` | TEXT |  | Gender. |
| `degree` | TEXT |  | Adjective/adverb degree. |

## Indexes

- `idx_morph_form` on `morphology(form)`
- `idx_morph_normalized` on `morphology(form_normalized)`
- `idx_morph_lemma` on `morphology(lemma)`

## Logical links

No SQLite foreign keys connect this DB to text/user DBs. Runtime code links by normalized form and lemma:

- `aligned_words.greek` / `vocabulary.form` -> `morphology.form` or `form_normalized`
- `aligned_words.lemma` / `vocabulary.lemma` -> `morphology.lemma`
- `morphology.lemma` -> `lsj.definitions.lemma` / `lemma_normalized`
