# CoNLL-U Data

This directory contains Ancient Greek dependency treebank data for Lyceum texts, copied from the `conllu-viz` project.

## Contents

- `aesop/fables/` — 52 Aesop fables as individual `.conllu` files, named with Perry number and reading-difficulty order.
  - `perry-difficulty-map.csv` / `.json` rank the fables by estimated difficulty.
  - `conllu-edition-map.json` maps Aesop CoNLL-U files to CTS/Lyceum edition metadata.
- `aristotle/poetics/aristotle.poetics.tb.conllu` — Aristotle's *Poetics* treebank.
- `xenophon/anabasis/book-01.tb.conllu` — Xenophon's *Anabasis*, Book 1 treebank.

## Format

Files use [CoNLL-U](https://universaldependencies.org/format.html): one token per tab-separated row with the standard 10 columns:

```text
ID FORM LEMMA UPOS XPOS FEATS HEAD DEPREL DEPS MISC
```

The annotations follow Universal Dependencies v2.x conventions adapted for Ancient Greek. Rows include lemmas, UPOS tags, morphology, dependency heads/relations, and context-aware English glosses in `MISC`.

Sentence comments commonly include:

- `text` or source citation metadata
- `translation_lang = en`
- `prose_translation`
- `literal_translation`
- work-specific IDs such as `sent_id`, `sentence_id`, `parallel_id`, `document_id`, `subdoc`, and `Ref`

## Provenance and licensing

These files were produced for the Lyceum Digital Library / related Greek treebanking work and include a mix of manual, LLM-assisted, and Glaux-derived annotations. File headers contain per-work provenance, editor/annotator, source edition, and license metadata. Preserve those headers when modifying or redistributing individual files.
