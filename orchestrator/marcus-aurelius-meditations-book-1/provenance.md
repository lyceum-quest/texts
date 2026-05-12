# Provenance

- Work: Marcus Aurelius, Meditations Book 1
- Workspace slug: `marcus-aurelius-meditations-book-1`
- CTS URN: `urn:cts:greekLit:tlg0562.tlg001`
- Mode: `add`
- Profile: `add`
- Created: 2026-03-23T08:52:10Z
- Stage 1 completed: 2026-03-23T09:00:00Z

## Greek sources

| status | title | url | editor | year | license | format | extraction | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **recommended** | M. Antoninus Imperator Ad Se Ipsum | [Perseus GitHub](https://raw.githubusercontent.com/PerseusDL/canonical-greekLit/master/data/tlg0562/tlg001/tlg0562.tlg001.perseus-grc2.xml) | Jan Hendrik Leopold | 1908 | CC-BY-SA-4.0 | TEI XML | XML parsing | Teubner edition, CTS URN: `urn:cts:greekLit:tlg0562.tlg001.perseus-grc2`. Excellent structure with book.chapter.section hierarchy. |

## English witnesses

| status | title | url | translator | year | license | format | extraction | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **recommended** | The Thoughts of Marcus Aurelius Antoninus | [Standard Ebooks](https://standardebooks.org/ebooks/marcus-aurelius/meditations/george-long) | George Long | 1862 | PD / CC0 | EPUB/HTML | HTML/EPUB parsing | Primary witness. Most scholarly translation, excellent alignment with Greek structure. |
| recommended | Meditations | [Gutenberg #2680](https://www.gutenberg.org/cache/epub/2680/pg2680.txt) | Meric Casaubon | 1634 | PD | Plain text | Text parsing | Secondary witness. First English translation, archaic style, historical value. |
| available | Meditations | [Gutenberg #55317](https://www.gutenberg.org/cache/epub/55317/pg55317.txt) | George W. Chrystal | 1902 | PD | Plain text | Text parsing | Tertiary resource. Less commonly used, available for comparison. |

## Auxiliary resources

- **Internet Archive**: Leopold 1908 source edition scan at https://archive.org/details/mantoninusimpera00marcuoft/page/n6 (note: some missing pages; HathiTrust alternative available)
- **Treebanks**: None found. Marcus Aurelius not covered in Perseus AGDT2 or PROIEL treebanks. Morphological analysis will rely on computational tools.
- **C.R. Haines Loeb (1916)**: Not found in standard PD repositories; not pursued (George Long superior choice).

## Decisions

- **Base Greek edition**: Perseus TEI XML (Leopold 1908) - `urn:cts:greekLit:tlg0562.tlg001.perseus-grc2`
- **Primary English witness**: George Long (1862) from Standard Ebooks
- **Target reference system**: Book.Chapter.Section (following Perseus structure; Book 1 has chapters 1-17)
- **Text type**: Prose, philosophical meditation
- **Structural notes**: Each chapter in Book 1 is a discrete meditation/reflection, numbered 1.1 through 1.17

## Licensing notes

- Greek source: CC-BY-SA-4.0 (Perseus/Open Greek and Latin project)
- English witnesses: Public domain (all pre-1928)
- Standard Ebooks edition: CC0 (content) + proprietary layout/typography
- All sources suitable for educational/open-access use

## Source discovery rationale

**Greek**: Perseus TEI XML chosen as sole base source due to:
- Scholarly provenance (Teubner critical edition)
- Machine-readable TEI format with explicit structural markup
- CTS URN compatibility
- Open license (CC-BY-SA-4.0)
- Excellent parseability
- No competing sources of comparable quality found

**English primary witness (George Long)**: Chosen due to:
- Most widely-used scholarly translation
- Known for accuracy and readability
- Structure aligns well with Greek text (section-by-section)
- Clean modern edition available (Standard Ebooks)
- Excellent alignment fitness for word-level work

**English secondary witnesses**:
- Casaubon (1634): Historical significance, different translation tradition, useful for comparison
- Chrystal (1902): Available but less established; included for completeness

**Treebank absence noted**: No gold-standard morphological annotations available. Stage 8 will need to rely on computational morphology tools and/or manual annotation.
