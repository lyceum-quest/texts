# Contributing to Lyceum Texts

Welcome! 🏛️

Lyceum is an open-source project to help the ancient authors speak again with their own voices. The interlinear translations in this repository are AI-generated and need human review—**your expertise can make them better for everyone**.

Whether you're a classicist, a developer, or a Greek student, there's a way for you to contribute.

## 🎓 For Classicists & Greek Scholars

You don't need to know git, JSON, or programming to help. If you can read Ancient Greek, **you're exactly who we need**.

### How to review translations

Each text directory (e.g., `homer-iliad-proem-1-1-5/`) contains an `interlinear/` folder with word-by-word glosses and morphological analyses. The main file is `chapter_01_llm.json`.

**What we need reviewed:**
- **Glosses**: Are the English translations accurate for the context?
- **Lemmata**: Is the dictionary headword correct?
- **Parts of speech**: Is the word tagged correctly (noun, verb, adjective, etc.)?
- **Morphology**: Are the grammatical forms correct (case, number, tense, mood, etc.)?

You can browse the files directly on GitHub, or clone the repo and open them in any text editor.

### Reporting errors

Found a mistake? **[Open a translation error report](../../issues/new?template=translation-error.yml)**.

You'll be asked for:
- Which text (e.g., `homer-iliad-proem-1-1-5`)
- The reference (e.g., `1.1`)
- The Greek word (e.g., `μῆνιν`)
- What's wrong with the current translation
- Your suggested correction
- Brief reasoning (optional but helpful!)

We'll review it and update the data. Every correction improves the corpus for all learners and researchers.

### Submitting corrections directly (advanced)

If you're comfortable with git and JSON:

1. **Fork** this repository
2. Edit the `interlinear/chapter_01_llm.json` file for the text
3. Find the word in the `segments[].words[]` array
4. Update the `gloss`, `lemma`, `pos`, or `morphology` fields
5. **Commit** with message format: `fix: correct gloss for μῆνιν in homer-iliad-proem-1-1-5 1.1`
6. Open a **pull request** with your reasoning

We'll review and merge it. Thank you!

---

## 💻 For Developers

### Repository structure

Each text is a self-contained directory with:

```
text-slug/
├── manifest.json              # Metadata (title, author, edition)
├── state.json                 # Pipeline completion status
├── provenance.md              # Sources, licenses, editorial decisions
├── raw/                       # Original source files
├── clean/                     # Cleaned/normalized Greek text
├── structured/                # JSON-structured text with citations
├── interlinear/               # ⭐ The main data
│   ├── chapter_01_llm.json    # Word-by-word analyses
│   ├── transliteration.json   # Latin transliteration
│   └── ground-truth-corpus.jsonl  # Holdout evaluation data
├── versification/             # Verse-aligned translations
├── witnesses/                 # Public domain translation witnesses
├── qa/                        # Quality assurance reports (12+ per text)
├── replay/                    # LLM interaction logs
└── sources/                   # Source candidate rankings
```

### Data format: `chapter_01_llm.json`

```json
{
  "segments": [
    {
      "reference": "1.1",
      "greek": "μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος",
      "words": [
        {
          "form": "μῆνιν",
          "gloss": "wrath",
          "lemma": "μῆνις",
          "pos": "noun",
          "morphology": "fem acc sg",
          "provenance": {
            "agent": "creator",
            "model": "claude-sonnet-4-20250514",
            "challenged": false
          }
        },
        {
          "form": "ἄειδε",
          "gloss": "sing",
          "lemma": "ἀείδω",
          "pos": "verb",
          "morphology": "imperf ind act 3rd sg",
          "provenance": {
            "agent": "referee",
            "model": "claude-opus-4-20250514",
            "challenged": true,
            "decision": "accept-skeptic",
            "creator_gloss": "sing",
            "skeptic_gloss": "sing",
            "reasoning": "The form is aorist imperative..."
          }
        }
      ]
    }
  ]
}
```

**Fields:**
- `form`: The Greek word as it appears in the text
- `gloss`: Context-sensitive English translation (single word or hyphenated phrase)
- `lemma`: Dictionary headword (citation form)
- `pos`: Part of speech (`noun`, `verb`, `adj`, `adv`, `particle`, `conj`, `prep`, `pron`)
- `morphology`: Grammatical analysis (case, number, tense, mood, voice, etc.)
- `provenance`: Who generated this analysis (creator, skeptic, referee) and whether it was challenged

### Ground-truth JSONL format

The `ground-truth-corpus.jsonl` file is a flattened, referee-approved subset for evaluation:

```jsonl
{"greek": "μῆνιν", "reference": "1.1", "text": "homer-iliad-proem-1-1-5", "gloss": "wrath", "lemma": "μῆνις", "pos": "noun", "confidence": "referee-approved", "model": "claude-sonnet-4-20250514"}
```

### How to contribute

**Fixing data:**
1. Fork this repo
2. Edit the JSON files
3. Run the QA checks (see below)
4. Commit with `--no-gpg-sign`: `git commit --no-gpg-sign -m "fix: correct lemma for ἄειδε"`
5. Open a pull request

**Adding new texts:**

You can't directly add texts to this repo—they must be generated by the [orchestrator](https://github.com/lyceum-quest/orchestrator) pipeline.

To request a new text:
1. **[Open a text request](../../issues/new?template=text-request.yml)** describing what you want
2. Or, if you want to generate it yourself:
   - Clone the [orchestrator repo](https://github.com/lyceum-quest/orchestrator)
   - Follow its README to set up the pipeline
   - Generate the text
   - Submit a pull request with the new directory

**Running the pipeline:**

See the [orchestrator README](https://github.com/lyceum-quest/orchestrator#readme) for full instructions. You'll need:
- Python 3.11+
- An Anthropic API key (for LLM-generated glosses)
- The text source (Perseus TEI XML, Project Gutenberg, etc.)

The orchestrator handles:
- Text ingestion and validation
- Morphological analysis (Perseus/Morpheus integration)
- Interlinear translation generation (multi-agent LLM workflow)
- Quality assurance and consistency checks
- Output in the format used by this repo

### QA checks

Each text includes 12+ quality assurance reports in the `qa/` directory:
- `interlinear-report.md` — Coverage, gloss quality, morphology consistency
- `alignment-report.md` — Greek-English witness alignment quality
- `transliteration-report.md` — Latin transliteration accuracy
- `reliability-report.md` — Holdout evaluation metrics
- `final-review-pack.md` — Human-readable summary for final review

Review these before submitting a PR to ensure data quality.

---

## 📖 For Greek Students & General Contributors

### Requesting new texts

Want to see a specific work added to Lyceum? **[Open a text request](../../issues/new?template=text-request.yml)**.

Tell us:
- Author and title
- Specific passage (e.g., "Plato, Apology 17a–18a")
- Why you'd like to see it (learning, research, etc.)

We'll prioritize based on:
- Community interest (upvote requests with 👍)
- Availability of public domain sources
- Text length and complexity

### Helping with provenance research

Every text needs:
- A **Greek source** (preferably from Perseus or another CC-licensed corpus)
- One or more **English translation witnesses** (public domain, ideally pre-1929)

If you find good sources for a requested text, comment on the issue with:
- Title and URL
- Author/editor and year
- License status (public domain, CC-BY-SA, etc.)
- Format (TEI XML, plain text, PDF, etc.)

This speeds up the pipeline setup significantly!

### Join the community

**Discord**: [https://discord.gg/mnvAS6WUzz](https://discord.gg/mnvAS6WUzz)

Ask questions, share corrections, request texts, or just chat about Ancient Greek. We're a friendly bunch!

---

## 📜 Commit Guidelines

- **Format**: `type: description`
  - `fix:` — Corrections to glosses, lemmata, morphology
  - `feat:` — New texts or major additions
  - `docs:` — Documentation updates
  - `chore:` — Regeneration, reformatting, etc.
- **Use `--no-gpg-sign`**: `git commit --no-gpg-sign -m "fix: ..."`
- **Do NOT add `Co-Authored-By` lines**

Examples:
```bash
git commit --no-gpg-sign -m "fix: correct gloss for θεὰ in homer-iliad-proem-1-1-5 1.1"
git commit --no-gpg-sign -m "feat: add xenophon-anabasis-1-1-1-10"
git commit --no-gpg-sign -m "docs: update CONTRIBUTING with QA workflow"
```

---

## 🌟 Why This Matters

Every correction you make, every text you help add, every translation you audit—**it all makes Ancient Greek more accessible**.

The goal of Lyceum is not to replace human expertise, but to amplify it. AI can draft glosses quickly, but only a trained reader can catch the nuances, the poetic register, the contextual meaning.

**Help us hear the ancient authors speak again with their own voices.**

Thank you for contributing! 🙏

---

## Links

- **Main site**: [lyceum.quest](https://lyceum.quest)
- **Reader repo**: [github.com/lyceum-quest/reader](https://github.com/lyceum-quest/reader)
- **Orchestrator repo**: [github.com/lyceum-quest/orchestrator](https://github.com/lyceum-quest/orchestrator)
- **Discord**: [discord.gg/mnvAS6WUzz](https://discord.gg/mnvAS6WUzz)
- **GitHub org**: [github.com/lyceum-quest](https://github.com/lyceum-quest)
