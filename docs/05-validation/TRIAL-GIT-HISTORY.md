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
| Heading count against the simple count | 69 equal, 1 higher (setext heading) |
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
4. **Dates count as separate numbers.** Already listed as a limitation; it is frequent in real text.

# 5. What Is Still Needed

Pairs of real texts with the same content and known differences, in several languages, with an independent judgment of what really changed. That needs data and acceptance criteria, which are reserved to the owner (`DEC-057`).
