# Trial on Real Documents from Git History

**Status:** ACTIVE (record of a trial)
**Version:** 0.1
**Document type:** Experiment record. Not a benchmark and not a validation.
**Date:** 2026-11-09
**Procedure:** `tools/trial_on_history.py`, read-only, deterministic; run on the repository as of `DEC-063`
**Capabilities:** the three `EXPERIMENTAL` capabilities of `DEC-060`–`DEC-062`
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-063

---

# 1. What Was Done

No real text had yet been passed through these capabilities. This trial uses the only real revision history available without new data: the project's own documents. The texts are public, English, and written mostly by AI agents.

**History:** every modified Markdown file in every commit: 193 before/after pairs, about 8.6 million characters.

**Controlled edits on the 70 current documents:** modal verbs swapped outside code (structure and numbers must not change); one unique heading deleted (headings must change); heading counts compared with a simple independent count.

# 2. Observations

| Check | Result |
|---|---|
| Crashes on 193 pairs | 0 |
| A text compared with itself (first run, all pairs, numeric and structural) | always `PASS` |
| Reworded text, structural | 70 of 70 `PASS` |
| Reworded text, numeric | 70 of 70 `PASS` |
| Deleted heading | 70 of 70 `FAIL`, naming `headings` |
| Heading count against the simple count | 69 equal, 1 higher (`SPECIFICATION-MAP.md`) |
| Slowest minimality measurement | about 9 seconds |
| History, structural | 183 `FAIL`, 10 `PASS` |
| History, numeric | 186 `FAIL`, 7 `PASS` |

# 3. Interpretation and Its Limits

**The many `FAIL` results are expected and say little.** These commits mostly add content, so new numbers and structure genuinely appear. They are not same-content rewrites, so they do not estimate how often the capabilities would be right on real paraphrases.

**Supported by this trial:** the code runs without error on long real Markdown, is deterministic on identical inputs, and responds correctly to the two controlled edits on real documents.

**Not supported:** any statement about accuracy, false-positive or false-negative rates, other languages, or texts in other styles. The controlled edits are easy cases and were designed by the same agent that wrote the code.

# 4. Defects and Findings

1. **Identifiers counted as numbers.** Most small numeric differences were project identifiers and paths (`DEC-058`, `00-project`). Excluding them would also hide real quantities (`10-year` to `20-year`), so they still count, and the result now reports `identifier_like_changes` separately.
2. **Numeric order check, found by unit tests before this trial:** a permitted rounding was wrongly reported as a change of order. Fixed.
3. **Minimality is slow on long texts with changes spread throughout.** Recorded as a limitation; no limit value is set.
4. **Text that happens to be Markdown syntax.** In `SPECIFICATION-MAP.md`, three lines consisting of a lone `=` under a word are read as headings. That is what Markdown syntax says, but not what the author meant. Structural results follow the syntax.
5. **Dates count as separate numbers.** Already listed as a limitation; it is frequent in real text.

# 5. What Is Still Needed

Pairs of real texts with the same content and known differences, in several languages, with an independent judgment of what really changed. That needs data and acceptance criteria, which are reserved to the owner (`DEC-057`).

# 6. Addendum: One Owner-Supplied Italian Pair (2026-11-09)

The owner supplied one original and one reworded Italian text of about 1,650 characters, with a list of the changes. The texts are not stored in the repository. This is one case and supports no rate.

**As supplied:** structure `PASS`, numbers `PASS` (`2022` and `513` unchanged), consistent with the owner's list. Minimality reported 43% changed tokens and a character edit distance of 552, also consistent with a heavy rewording.

**Controlled edits on the same text, by the agent:** removing a list item, changing `513` or `2022`, and removing a title line were each detected.

**Weaknesses shown:**

1. **`513 kg` changed to `513 g` gives `PASS`.** Units are not read (already a listed limitation), and this case shows how serious it is.
2. A meaning reversal (`non riciclate` to `riciclate`) passes both checks, as expected: these capabilities do not assess meaning.
3. Ordered-list markers (`1.` to `5.`) are counted as numbers in the text.
4. Titles without Markdown syntax are read as paragraph text, merged with adjacent lines, so the paragraph count does not match what a reader sees. Plain-text input is the likely common case.

**Follow-up (`DEC-064`):** weaknesses 1, 3 and 4 are addressed, in versions 0.2.0 of the capabilities. `513 kg` changed to `513 g` now fails. Weakness 2 is out of scope. The fixes are checked by unit tests modelled on these cases; the original pair was not re-run, because it was not stored.
