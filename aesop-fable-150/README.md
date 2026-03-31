# aesop-fable-150/

## Workspace snapshot

**Work:** Aesop, Fable 150 (The Crab and the Fox)

**Slug:** `aesop-fable-150`

**Mode:** `add`

**Profile:** `add`

**State current stage:** `10-human-review`

## Directory map

| Directory | Usually handled by | What it means |
|---|---|---|
| `clean/` | Stage 3 | Clean normalized text |
| `extracted/` | Stage 2 | Parseable extracted text |
| `interlinear/` | Stage 7/8 | Transliteration, gloss, and constraints |
| `qa/` | QA reports | Human-readable quality reports |
| `raw/` | Stage 2 | Original source downloads |
| `replay/` | Replay runtime | Stage history and invalidation trail |
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

## `clean/cleaning_results.json`

This file records how much cleaning happened for each language.

| Field | Meaning |
|---|---|
| `greek.original_size` | Input byte size before cleaning. |
| `greek.cleaned_size` | Output byte size after cleaning. |
| `greek.contamination` | Detected contamination notes. |
| `greek.changes` | Actual edits applied to Greek. |
| `greek.lines` | Count of non-empty cleaned Greek lines. |
| `english.original_size` | Input byte size before cleaning. |
| `english.cleaned_size` | Output byte size after cleaning. |
| `english.contamination` | Detected contamination notes. |
| `english.changes` | Actual edits applied to English. |
| `english.lines` | Count of non-empty cleaned English lines. |

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

## `versification/alignment.json`

Greek/English structural alignment.

| Field | Meaning |
|---|---|
| `schema_version` | Alignment schema version. |
| `generated_at` | When alignment was generated. |
| `mode` | Alignment mode (`direct`, `dp`, `range`, or `blocked`). |
| `primary_witness` | Primary witness used, if any. |
| `greek_unit_count` | Number of Greek units available. |
| `witness_segment_count` | Number of witness segments available. |
| `mapped_count` | Number of mappings produced. |
| `coverage` | Alignment coverage ratio. |
| `unmatched_greek` | Greek refs left unmatched. |
| `unmatched_witness` | Witness refs left unmatched. |
| `mappings` | Array of mapping records. |
| `notes` | Alignment notes. |
### `mappings[]`

| Field | Meaning |
|---|---|
| `greek_start` | First Greek ref in the mapped span. |
| `greek_end` | Last Greek ref in the mapped span. |
| `witness_ref` | Matching witness reference. |

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

## `versification/english_versified.json`

Some workspaces use `english_versified.json` instead of `english_edition.json`. The schema is the same verse-aligned English segment list.

## `versification/metadata.json`

Run metadata for the verse-aligned English generation.

| Field | Meaning |
|---|---|
| `schema_version` | Metadata schema version. |
| `generated_at` | When metadata was written. |
| `method` | Generation method. |
| `model` | Model name used. |
| `witness_used` / `witness_for_adversarial_review` | Witness involved in review or generation. |
| `source_greek` | Source structured Greek file. |
| `segment_count` | Number of aligned segments. |
| `notes` | Freeform notes. |

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

## `interlinear/candidate-alignment.json`

Machine-built interlinear candidate layer.

| Field | Meaning |
|---|---|
| `schema_version` | Build schema version. |
| `generated_at` | Build time. |
| `strategy` | Builder strategy name. |
| `evidence_sources` | Source artifact paths used by the builder. |
| `provider_notes` | Notes about loaded providers. |
| `segments` | Array of candidate interlinear segments. |
| `unresolved_flags` | Flags that still need attention. |
### `segments[]`

| Field | Meaning |
|---|---|
| `greek_start` | First Greek reference in the segment. |
| `greek_end` | Last Greek reference in the segment. |
| `witness_ref` | Witness reference, if any. |
| `greek` | Greek text for the segment. |
| `transliteration` | Segment transliteration. |
| `witness_text` | Witness text, if any. |
| `words` | Word-level interlinear candidates. |
| `unresolved_flags` | Segment-specific flags. |
### `words[]`

The word records commonly include `reference`, `token_index`, `greek`, `transliteration`, `lemma`, `contextual_gloss`, `pos`, `morphology`, `deprel`, `evidence`, `needs_review`, and `review_flags`.

## `interlinear/ground-truth-benchmark.json`

Benchmark document for gloss-review evaluation.

| Field | Meaning |
|---|---|
| `schema_version` | Benchmark schema version. |
| `generated_at` | When the benchmark was generated. |
| `work` | Human-readable work title. |
| `slug` | Workspace slug. |
| `corpus_id` | Optional ground-truth corpus identifier. |
| `scope` | Corpus scope. |
| `source_path` | Source corpus path, if one was selected. |
| `entry_count` | Number of benchmark entries. |
| `unique_greek_count` | Number of unique Greek forms. |
| `high_confidence_entry_count` | Count of high-confidence entries. |
| `entries` | Array of gloss benchmark entries. |
| `notes` | Benchmark notes. |
### `entries[]`

| Field | Meaning |
|---|---|
| `greek` | Greek token or form. |
| `gloss` | Benchmark gloss. |
| `count` | Frequency/count, when present. |
| `confidence` | Confidence tier. |
| `sources` | Supporting source notes. |

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

## `interlinear/morphology-constraints.json`

Some workspaces keep a morphology-constraint file with the same `TreebankConstraintsDocument` schema as `treebank-constraints.json`.

If both files exist, compare them to see whether the workspace is using the same constraints for both morphology and treebank enrichment.

## `interlinear/chapter_*_llm.json`

Final LLM interlinear output. The exact top-level keys vary a little by workspace, but the shape is consistent:

| Field | Meaning |
|---|---|
| `greek_edition` / `text` | Workspace or edition identifier. |
| `english_edition` / `book` / `run_id` | Run identity fields that vary by workspace. |
| `generator` | Pipeline generator name. |
| `mode` | Run mode, often `agent`. |
| `segments` | Array of interlinear segments. |
### `segments[]`

| Field | Meaning |
|---|---|
| `reference` | Shared reference label. |
| `greek` | Greek segment text. |
| `words` | Array of word-level gloss records. |
### `words[]`

| Field | Meaning |
|---|---|
| `form` | Surface form. |
| `gloss` | Contextual gloss. |
| `lemma` | Lemma. |
| `pos` | Part of speech. |
| `morphology` | Morphological description. |
| `provenance` | Decision trail for the gloss. |
### `provenance`

| Field | Meaning |
|---|---|
| `agent` | Which agent produced or modified the word. |
| `model` | Model name. |
| `challenged` | Whether the word was challenged by the skeptic. |
| `decision` | Referee decision, when challenged. |
| `creator_gloss` | Original creator gloss, if relevant. |
| `skeptic_gloss` | Skeptic proposal, if relevant. |
| `reasoning` | Referee reasoning. |
