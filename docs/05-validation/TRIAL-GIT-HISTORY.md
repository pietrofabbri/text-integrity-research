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

# 7. Addendum: One Owner-Supplied English Pair, Run Blind (2026-11-09)

The owner supplied one original and one edited English text of about 1,770 characters, and gave the list of changes only after the capabilities had been run. The texts are not stored in the repository. This is one case and supports no rate.

| Owner's change | Capability result |
|---|---|
| `30%` changed to `35%` | Detected by numeric integrity (`FAIL`) |
| Fourth item of the second list deleted | Detected by structural validation (`FAIL`, in both formats) |
| Word substitutions without structural or numeric effect | Correctly raised no failure; counted by minimality |
| `significantly` removed, which weakens a claim | Not detected, as expected: no capability assesses meaning |

No failure was raised that the owner's list does not explain. A separate word-level comparison made by the agent found 13 differences, including two the owner's list did not mention (`produces` to `generates`, `investing in` to `developing`); neither raised a failure.

The result shows the two deterministic checks working on one blind case. It does not show how they perform in general, and the undetected weakening confirms that a `PASS` is not evidence of fidelity.

# 8. Addendum: Follow-Up on Dates, Speed and Languages Without Spaces (2026-11-09)

Under `DEC-065`, versions 0.3.0 address weaknesses 3 and 5 of §4: dates are compared as whole items, and token alignment is banded. On synthetic tokens, a 5,000-token text with 50 substitutions went from about 14 s to about 0.2 s, and a 20,000-token text with 200 from about 256 s to about 4 s. These are single runs on one machine.

The same work found a defect that neither owner-supplied pair could have shown: digits directly after kana or CJK ideographs were not read, so `共有300人` yielded no number and `45.5%` was read as `5%`. A changed number in such a text gave `PASS`. It is fixed and covered by unit tests. Earlier results for Japanese and Chinese should be disregarded; the trials on owner-supplied texts were in Italian and English and are not affected by this defect. No trial of 0.3.0 on real texts has been run.

# 9. Addendum: One Owner-Supplied German Pair, Run Blind on 0.3.0 (2026-11-09)

The owner supplied one original and one edited German text of about 1,970 characters, and gave a list of 19 changes only after the capabilities had been run. The texts are not stored in the repository. This is one case and supports no rate.

| Owner's change | Capability result |
|---|---|
| `68 %` changed to `86 %` (item 6, a deliberate alteration) | Detected by numeric integrity (`FAIL`); `2023` paired as unchanged |
| Fourth item of the second list deleted (item 17) | Detected by structural validation (`FAIL`, in both formats, on `lists` only) |
| The other 17 word substitutions | Raised no failure; counted by minimality (19.5% changed tokens, 74% changed sentences, character edit distance 290) |

No failure was raised that the owner's list does not explain.

**Not detected, as expected, since no capability assesses meaning:** `langfristig` to `kurzfristig` (a reversal), `sensible` to `personenbezogene` and `weiter` to `grundlegend` (the agent's reading of these as meaning changes, made before the owner's list was seen). The structural result reports that the list changed; it does not say that a topic was lost, which the owner's note identifies as the effect of item 17.

**Word-level comparison by the agent, not by a capability:** it found 21 differing regions, covering all 19 listed changes, and three the list does not mention: `nutzen zunehmend` to `setzen immer häufiger ... ein`, `nahm` to `stieg`, and `solcher` to `dieser`. As in §7, an owner's list can be incomplete, which is relevant to `ACCEPTANCE-CRITERIA-OPTIONS.md` D3. None of the three raised a failure.

The text contains no dates and no text without spaces, so this trial does not exercise those parts of 0.3.0. Using this pair for later fixes would make it development data (`ACCEPTANCE-CRITERIA-OPTIONS.md` D5).

# 10. Addendum: Agent-Written Cases on Dates and Numbers (2026-11-09)

The agent wrote 50 short cases in Italian, French, Japanese and Chinese, with its own expected outcome for each, plus four on currency. The author knows the code, so this is a software check, not independent evidence, and it supports no rate. Twelve of the 50 differed from expectation.

- **Changes missed:** `500 €` to `500 $` gave `PASS`, because a currency symbol after a number was not read (a defect since the first version), and `15 mar. 2024` to `15 apr. 2024` gave `PASS`. Both are fixed in 0.4.0 (`DEC-066`).
- **False alarms left open:** `14:30` to `14.30`, `15 marzo` to `15/03`, a two-digit year (`'24`), a month name without its accent (`aout`, `fevrier`) and Japanese era years. `€ 1.200,00` to `1.200,00 €` is fixed by the same change.
- **Expected by design:** four cases gave `partially measured` because they depend on a declared convention; the agent's expectation of `PASS` was wrong.

# 11. Addendum: One Owner-Supplied French Pair, Run Blind on 0.4.0 (2026-11-11)

The owner supplied one original and one edited French text of about 2,390 characters, and gave a list of 31 changes only after the capabilities had been run. The texts are not stored in the repository. This is one case and supports no rate.

| Owner's change | Capability result |
|---|---|
| All 31 listed changes, all wording | Numeric integrity `PASS` (`2022`, `75 %`, `80 %`, `2050` paired, in order); structural validation `PASS` in both formats; minimality 30.6% changed tokens, 79% changed sentences, character edit distance 556 |
| `pourrait atteindre 80 %` to `pourrait dépasser 80 %` (item 9, which the owner marks as changing the quantitative meaning) | Not detected: the number is unchanged and the verb that qualifies it is not read |
| `près de 75 %` to `environ 75 %` (item 8) | Not detected, for the same reason |

No failure was raised, and the owner's list contains no change of a digit-written number or of structure, so no failure was expected from these two capabilities.

**What the trial shows:** a quantity can change while its digits stay the same. Words that qualify a number (`atteindre`, `dépasser`, `près de`, `environ`) are outside the scope of numeric integrity as specified (`NUMERIC-INTEGRITY-CAPABILITY.md` §5, "ranges and comparisons"). A numeric `PASS` says that the digits were kept, not what is claimed about them.

**Word-level comparison by the agent, not by a capability:** it found 52 differing regions, covering all 31 listed changes, and at least 13 that the list does not mention, among them `ce qui accentuerait` to `entraînant` (a conditional becomes an indicative participle), `sont exposés aux fortes températures` to `subissent les épisodes de chaleur`, `fondées sur la nature` to `inspirées de la nature` (the first is an established term), `vit` to `réside` and `épisodes` to `événements`. This is the third blind pair whose owner's list is incomplete (§7, §9), which bears on `ACCEPTANCE-CRITERIA-OPTIONS.md` D3.

The text contains no dates or currency amounts, so 0.3.0 and 0.4.0 date and currency reading is still untried on real text.
