# marcus-aurelius-meditations-book-1/

## Workspace snapshot

**Work:** Marcus Aurelius, Meditations Book 1

**Slug:** `marcus-aurelius-meditations-book-1`

**Mode:** `add`

**Profile:** `add`

**State current stage:** `10-human-review`

## Directory map

| Directory | Usually handled by | What it means |
|---|---|---|
| `clean/` | Stage 3 | Clean normalized text |
| `extracted/` | Stage 2 | Parseable extracted text |
| `interlinear/` | Stage 7/8 | Transliteration, gloss, and constraints |
| `logs/` | Ad hoc | Optional runtime logs |
| `qa/` | QA reports | Human-readable quality reports |
| `raw/` | Stage 2 | Original source downloads |
| `replay/` | Replay runtime | Stage history and invalidation trail |
| `scripts/` | Ad hoc | Optional workspace-local helper scripts |
| `sources/` | Stage 1 | Source catalogs and provenance |
| `structured/` | Stage 4 | Reference-keyed segmentation |
| `versification/` | Stage 6 | Verse-aligned English output |
| `witnesses/` | Stage 5 | English witnesses and witness catalogs |

## Files in this workspace

- `manifest.json`
- `provenance.md`
- `state.json`

## JSON field guide

## `manifest.json`

This is the workspace identity document.

| Field | Meaning |
|---|---|
| `schema_version` | Manifest schema version. |
| `created_at` | When the workspace was first created. |
| `updated_at` | Last time the manifest was refreshed. |
| `slug` | Stable workspace directory name. |
| `work` | Human-readable work title. |
| `author` | Optional author name. |
| `author_urn` | Optional author URN. |
| `work_urn` | Optional work URN. |
| `mode` | Pipeline mode: `add` or `apply`. |
| `profile` | Replay profile name. |
| `existing_edition_urn` | Existing edition URN for apply mode. |
| `requested_stages` | Stage IDs requested at intake. |
| `target_output` | Desired output label. |
| `base_greek_edition_strategy` | Note describing the base Greek edition strategy. |
| `target_reference_system` | Note describing the reference system target. |
| `success_criteria` | Intake success criteria. |
| `risks` | Intake risks. |
| `blockers` | Known blockers. |
| `open_questions` | Open questions that need answering. |

## `state.json`

This is the live stage state snapshot.

| Field | Meaning |
|---|---|
| `schema_version` | State schema version. |
| `created_at` | When the state record was created. |
| `updated_at` | Last state refresh time. |
| `current_stage` | Most recently active stage, if any. |
| `last_profile` | Last replay profile that ran. |
| `invalidated_stages` | Stages invalidated by the latest replay. |
| `stages` | Array of stage records. |
### `stages[]`

| Field | Meaning |
|---|---|
| `stage` | Stage ID. |
| `requested` | Whether the stage was requested. |
| `status` | Stage status (`done`, `blocked`, `pending`, etc.). |
| `decision` | Optional stage decision. |
| `decision_at` | When the decision was recorded. |
| `last_run_at` | When the stage last ran. |
| `inputs` | Input artifact paths. |
| `invalidates` | Downstream stages invalidated by this stage. |
| `outputs` | Output artifact paths. |
| `sub_stages` | Optional nested sub-stage states. |
| `notes` | Human-readable notes about the stage. |

## `replay/stage-history.json`

This is the replay/event log for the workspace.

| Field | Meaning |
|---|---|
| `schema_version` | History schema version. |
| `events` | Chronological list of stage events. |
### `events[]`

| Field | Meaning |
|---|---|
| `at` | Event timestamp. |
| `stage` | Stage that emitted the event. |
| `action` | Event action name. |
| `profile` | Replay profile associated with the event. |
| `affected_stages` | Stages touched by the event. |
| `notes` | Freeform note text. |

## `sources/greek_candidates.json`

Ranked Greek source candidates.

| Field | Meaning |
|---|---|
| `schema_version` | Catalog schema version. |
| `kind` | Catalog type, here `greek`. |
| `generated_at` | Catalog generation time. |
| `candidates` | Array of candidate source records. |
### `candidates[]`

| Field | Meaning |
|---|---|
| `id` | Stable candidate identifier. |
| `title` | Human-readable source title. |
| `language` | Language code. |
| `url` | Source URL. |
| `editor` | Editor name, if relevant. |
| `translator` | Translator name, if relevant. |
| `publication_year` | Publication year or range. |
| `license` | License or rights note. |
| `format` | Source format (HTML, DJVU, wikitext, etc.). |
| `extraction_method` | How text should be or was extracted. |
| `quality_notes` | Human notes about quality. |
| `confidence_notes` | Notes about confidence or caveats. |
| `recommended` | Whether this source is recommended. |
| `ranking_score` | Numeric ranking score when present. |
| `ranking_rationale` | Why the candidate ranks where it does. |

## `sources/english_candidates.json`

Ranked English witness candidates.

| Field | Meaning |
|---|---|
| `schema_version` | Catalog schema version. |
| `kind` | Catalog type, here `english`. |
| `generated_at` | Catalog generation time. |
| `candidates` | Array of candidate source records. |
### `candidates[]`

The fields match `sources/greek_candidates.json`, plus optional witness-specific notes such as `alignment_fitness`.

## `sources/auxiliary_resources.json`

Auxiliary non-source references such as index systems and commentary.

| Field | Meaning |
|---|---|
| `schema_version` | Catalog schema version. |
| `kind` | Catalog type, here `auxiliary`. |
| `generated_at` | Catalog generation time. |
| `candidates` | Array of auxiliary resource records. |
### `candidates[]`

| Field | Meaning |
|---|---|
| `id` | Stable resource identifier. |
| `title` | Resource title. |
| `type` | Resource type such as `reference-system`, `morphology`, or `commentary`. |
| `url` | Resource URL. |
| `description` | Short description of the resource. |
| `format` | Resource format. |
| `usefulness` | Why the resource matters to the pipeline. |
| `notes` | Extra context or caveats. |

## `structured/greek.json`

Segmented Greek text.

| Field | Meaning |
|---|---|
| `schema_version` | Segmentation schema version. |
| `generated_at` | When segmentation was generated. |
| `reference_system` | Reference system name. |
| `unit` | Unit type used for segmentation. |
| `source_path` | Clean-text file that was segmented. |
| `units` | Array of reference-keyed units. |
### `units[]`

| Field | Meaning |
|---|---|
| `ref` | Canonical reference for the unit. |
| `text` | Text of the unit. |

## `structured/segments.json`

Some workspaces use `segments.json` instead of `greek.json`. The schema is the same segmented-Greek layout.

## `structured/reference-inventory.json`

Map from source text files to structured reference ranges.

| Field | Meaning |
|---|---|
| `schema_version` | Inventory schema version. |
| `generated_at` | When the inventory was generated. |
| `reference_system` | Reference system name. |
| `unit` | Unit type used for segmentation. |
| `entries` | Array of source-to-structure mappings. |
### `entries[]`

| Field | Meaning |
|---|---|
| `source_path` | Clean source file path. |
| `structured_path` | Structured JSON path. |
| `unit_count` | Number of units in the structured file. |
| `first_ref` | First reference in that file. |
| `last_ref` | Last reference in that file. |

## `witnesses/catalog.json`

Witness registry plus role classification.

| Field | Meaning |
|---|---|
| `schema_version` | Catalog schema version. |
| `work` | Workspace work title. |
| `generated_at` | Catalog generation time. |
| `witnesses` | Array of witness records. |
| `summary` | Roll-up counts and readiness notes. |
### `witnesses[]`

| Field | Meaning |
|---|---|
| `id` | Stable witness ID. |
| `title` | Witness title. |
| `translator` | Translator name. |
| `year` | Publication year. |
| `license` | Rights/license note. |
| `file` | Witness text file name. |
| `format` | Text format. |
| `roles` | Roles such as `reader-display`, `glossing-reference`, `adversarial-comparison`. |
| `literalness` | Qualitative literalness note when present. |
| `url` | Source URL. |
| `publisher` | Publisher or hosting site. |
| `segment_count` | How many reference segments the witness has. |
| `notes` | Freeform witness notes. |
### `summary`

| Field | Meaning |
|---|---|
| `total_witnesses` | Total number of witness records. |
| `versification_candidates` | Number of witnesses usable for direct versification. |
| `adversarial_comparison_witnesses` | Witnesses useful for adversarial review. |
| `glossing_reference_witnesses` | Witnesses useful for glossing. |
| `reader_display_witnesses` | Witnesses suitable for the reader sidebar. |
| `recommended_versification` | Best direct versification witness, if any. |
| `stage_5_complete` | Whether Stage 5 finished. |
| `stage_6_ready` | Whether Stage 6 can proceed. |
| `notes` | Roll-up notes. |

## `versification/english_edition.json`

Verse-aligned English generated by translation synthesis.

| Field | Meaning |
|---|---|
| `schema_version` | Document schema version. |
| `generated_at` | When the translation was generated. |
| `edition_urn` | URN for the generated English edition. |
| `method` | Generation method, usually `translation-synthesis`. |
| `model` | Model name used to generate the translation. |
| `witness_for_adversarial_review` | Witness used during adversarial review, if any. |
| `segments` | Array of aligned English segments. |
### `segments[]`

| Field | Meaning |
|---|---|
| `reference` | Shared segment reference. |
| `text` | English segment text. |

## `interlinear/transliteration.json`

Deterministic Greek transliteration.

| Field | Meaning |
|---|---|
| `schema_version` | Transliteration schema version. |
| `generated_at` | When transliteration was generated. |
| `standard` | Transliteration standard name. |
| `lines` | Array of transliterated lines. |
### `lines[]`

| Field | Meaning |
|---|---|
| `ref` | Shared reference. |
| `greek` | Greek source text. |
| `transliteration` | Latin transliteration. |

## `interlinear/treebank-constraints.json`

Treebank-derived structural constraints.

| Field | Meaning |
|---|---|
| `schema_version` | Constraint schema version. |
| `generated_at` | When the constraints were generated. |
| `source_path` | Source treebank path. |
| `scope` | Scope label, often `import`. |
| `reference_count` | Number of reference entries. |
| `token_count` | Number of tokens across all entries. |
| `references` | Array of reference-level constraints. |
| `validation_notes` | Validation notes produced during parsing. |
### `references[]`

| Field | Meaning |
|---|---|
| `sentence_id` | Sentence ID from the source treebank, if present. |
| `reference` | Canonical reference label. |
| `reference_refs` | Alternative reference refs, if present. |
| `text` | Sentence text. |
| `tokens` | Token-level treebank constraints. |
### `tokens[]`

| Field | Meaning |
|---|---|
| `id` | Token ID inside the sentence, if present. |
| `form` | Surface form. |
| `lemma` | Lemma, if present. |
| `pos` | Universal POS tag, if present. |
| `morphology` | Morphology string, if present. |
| `head` | Head token index, if present. |
| `deprel` | Dependency relation, if present. |

## `interlinear/chapter_01_llm.json`

This JSON artifact is present in the workspace, but no dedicated field guide was added yet.

## `structured/casaubon.json`

This JSON artifact is present in the workspace, but no dedicated field guide was added yet.

## `structured/english.json`

This JSON artifact is present in the workspace, but no dedicated field guide was added yet.

## `versification/chapter_1.json`

This JSON artifact is present in the workspace, but no dedicated field guide was added yet.

## `witnesses/casaubon-1634.json`

This JSON artifact is present in the workspace, but no dedicated field guide was added yet.

## `witnesses/long-1862.json`

This JSON artifact is present in the workspace, but no dedicated field guide was added yet.
