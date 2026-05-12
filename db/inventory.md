# Database Inventory

Observed from sibling directories on 2026-05-12.

## Active reader databases

| Database | Path | Mutability | Runtime role | Tables | Row counts |
|---|---|---:|---|---|---|
| `texts.db` | `../reader/data/texts.db` | read-only | Full library browsing and basic reading | `authors`, `works`, `editions`, `segments`, `aligned_segments`, `aligned_words`, `text_metadata` | authors 373; works 1838; editions 2823; segments 706021; aligned_segments 39968; aligned_words 1330342; text_metadata 227 |
| `corpus.db` | `../reader/data/corpus.db` | read-only / optional | Broad corpus source/fallback | same as `texts.db` | authors 373; works 1836; editions 2822; segments 707135; aligned_segments 39963; aligned_words 1330287; text_metadata 227 |
| `editions.db` | `../reader/data/editions.db` | read-only / optional | Curated Lyceum editions, interlinear alignments, contextual glosses | same logical text-family tables | authors 3; works 4; editions 10; segments 98; aligned_segments 32; aligned_words 1973; text_metadata 0 |
| `morph.db` | `../reader/data/morph.db` | read-only | Greek morphology lookup | `morphology` | morphology 1546804 |
| `lsj.db` | `../reader/data/lsj.db` | read-only | LSJ and short definitions | `definitions`, `shortdefs` | definitions 110826; shortdefs 100207 |
| `users.db` | `../reader/data/users.db` | read-write | Local learner state: vocabulary, SRS, reading progress, tags, settings | user/SRS tables | users 2; vocabulary 62; review_history 11; reading_progress 3; schema_migrations 2 |

## Orchestrator databases

| Database | Path | Role | Notes |
|---|---|---|---|
| `editions.db` | `../orchestrator/data/editions.db` | Pipeline output | Same counts as orchestrator `texts.db`; has curated-edition columns except `parent_work_urn`. |
| `texts.db` | `../orchestrator/data/texts.db` | Pipeline/import output | Same 3-author/4-work dataset; older/simple `editions` table. |
| `morph.db` | `../orchestrator/data/morph.db` | Morphology lookup | Same schema/count as reader `morph.db`. |

## Release artifacts

`../release/lyceum-texts-v2026.04.09/` contains release copies of:

- `texts.db`
- `morph.db`
- `lsj.db`

Treat release DBs as artifacts. Do not make schema changes there directly; change the import/build pipeline and publish a new release.

## Empty, backup, or legacy files

- `../reader/lyceum.db` was observed as an empty 0-byte file. Treat it as legacy/unused unless code proves otherwise.
- `../reader/data/texts.db.bak` is a backup file and is excluded from the active schema inventory.
