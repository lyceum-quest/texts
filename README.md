# Lyceum Texts

This repository stores data outputs and data documentation for [lyceum.quest](https://lyceum.quest), a digital library and reader for Ancient Greek.

It is organized as a small set of data subprojects. The top-level README gives the map; each subdirectory README documents that subproject in more detail.

## Subprojects

| Path | Purpose | Start here |
|---|---|---|
| [`db/`](db/) | SQLite database documentation for reader, corpus, morphology, dictionary, and learner-state databases. The large `.db` artifacts are release assets, not normal git-tracked files. | [`db/README.md`](db/README.md) |
| [`conllu/`](conllu/) | Ancient Greek CoNLL-U dependency treebank data used by the CoNLL-U visualizer and related Lyceum tooling. Includes Aesop fables, Aristotle's *Poetics*, and Xenophon's *Anabasis* Book 1. | [`conllu/README.md`](conllu/README.md) |
| [`orchestrator/`](orchestrator/) | Archived per-text workspaces from the deprecated orchestrator pipeline. These are historical snapshots with raw sources, structured text, interlinear output, and QA artifacts where present. | [`orchestrator/README.md`](orchestrator/README.md) |

## Release assets

Runtime database files are distributed through GitHub Releases rather than checked into this repository:

- `texts.db` — reader text library and alignments
- `editions.db` — curated Lyceum editions and source tracking
- `morph.db` — Greek morphology lookup data
- `lsj.db` — LSJ dictionary data

Download current artifacts from the [latest release](https://github.com/lyceum-quest/texts/releases/latest). See [`db/`](db/) for schema notes, inventories, and regeneration policy.

## Usage

For tooling that expects this repository on disk, set:

```bash
export LYCEUM_TEXTS_DIR=/path/to/texts
```

Then consult the relevant subproject README for file layout, provenance, and maintenance rules.

## Versioning

Releases use Calendar Versioning:

```text
vYYYY.MM.DD
```

Each release may include updated database assets, data snapshots, and documentation for the corresponding data state.
