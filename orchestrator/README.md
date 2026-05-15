# Archived Orchestrator Workspaces

This directory contains legacy per-text workspaces produced by the old Lyceum orchestrator workflow.

They are kept for historical reference, reproducibility, and inspection of earlier text-generation artifacts. They are not the canonical source for current reader data. New text data should flow through the current Lyceum text-generation, database, and release workflow instead of adding or updating workspaces here.

## Workspaces

| Path | Work | Notes |
|---|---|---|
| [`aesop-fable-150/`](aesop-fable-150/) | Aesop, Fable 150, "The Crab and the Fox" | Legacy add-mode workspace through human-review stage. |
| [`homer-iliad-proem-1-1-5/`](homer-iliad-proem-1-1-5/) | Homer, *Iliad* proem 1.1–5 | Legacy add-mode workspace with interlinear and QA artifacts. |
| [`homer-odyssey-proem-1-1-5/`](homer-odyssey-proem-1-1-5/) | Homer, *Odyssey* proem 1.1–5 | Smaller legacy workspace snapshot with structured, versification, and interlinear artifacts. |
| [`marcus-aurelius-meditations-book-1/`](marcus-aurelius-meditations-book-1/) | Marcus Aurelius, *Meditations* Book 1 | Legacy add-mode workspace through human-review stage. |

Each workspace has its own README with artifact-specific field guides.

## Common workspace layout

Not every workspace contains every directory, but the legacy pipeline commonly produced:

| Path | Meaning |
|---|---|
| `manifest.json` | Workspace identity: author, work, URNs, mode, requested stages, and success criteria. |
| `state.json` | Stage state snapshot from the orchestrator replay system. |
| `provenance.md` | Source, license, and editorial notes. |
| `sources/` | Ranked Greek sources, English witnesses, and auxiliary references. |
| `raw/` | Original source downloads or captures. |
| `extracted/` | Parseable text extracted from raw sources. |
| `clean/` | Cleaned and normalized Greek text. |
| `structured/` | Reference-keyed segmented Greek. |
| `witnesses/` | English witness texts and witness catalogs. |
| `versification/` | Verse- or segment-aligned English output. |
| `interlinear/` | Word-by-word glosses, lemmata, morphology, transliteration, and run summaries. |
| `qa/` | Human-readable quality and consistency reports. |
| `replay/` | Replay/event logs and invalidation trail. |

## Status

- Deprecated for new work.
- Safe to read for provenance and historical debugging.
- Do not treat these snapshots as authoritative runtime data; use the current database release assets and documented schemas instead.
