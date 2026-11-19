# Acceptance Criteria: Options for the Owner

**Status:** DECIDED in part (`DEC-075`, 2026-11-19), on the owner's delegation. D1–D6 are decided as recorded in §5; D7 is decided as "no threshold" (descriptive form). The rest of this document is kept as the record of the options.
**Version:** 0.1
**Document type:** Decision support
**Parent:** `docs/05-validation/VALIDATION-GATES.md` §3–4; `VALIDATION-MAP.md` §44–45, §55
**Applies to:** `CAP-VALIDATE-FACTUAL-STRUCTURED-NUMERIC`, `CAP-VALIDATE-STRUCTURAL-MARKDOWN`, `CAP-VALIDATE-MINIMALITY-LEXICAL`
**Related decisions:** DEC-004, DEC-012, DEC-057, DEC-063, DEC-064, DEC-065

---

# 1. Purpose

All three capabilities are `EXPERIMENTAL`. Their record says `validation_requirements`: "Not yet defined". This document lists what must be decided before any of them can be evaluated against a criterion. **It fixes no threshold** (`NO-INVENTION-RULES.md`). Recommendations are the agent's proposals, marked as such, and concern procedure only.

# 2. What Blocks `VALIDATED` Today

| Condition | State | Who can resolve it |
|---|---|---|
| Declared validation requirements and benchmark (`VALIDATION-MAP.md` §55) | Missing | Owner, through this document |
| A scientific source not solely `UNVERIFIED` (`CAPABILITY-ARCHITECTURE.md` §7) | Minimality has none; numeric integrity has failure-mode evidence only | Research work, then owner |
| Licensing check (`CAPABILITY-ARCHITECTURE.md` §7) | No external dependency; texts in a benchmark would need one | Owner (`Q-007`) |
| Which `VALIDATED` is meant: three vocabularies exist (`VALIDATION-GATES.md` §2) | Deferred by `DEC-012` | Owner |

# 3. Decisions

## D1. What is being claimed

The three capabilities need different kinds of claim. Minimality gives no `PASS` or `FAIL`, so it can only be judged on whether its measurements are computed as defined.

- **A.** Numeric integrity and structural validation only, as detectors of changes. Minimality stays a measurement, checked by tests.
- **B.** All three, with a separate criterion for each.

*Proposal: A.*

## D2. What counts as an error

| Case | Options |
|---|---|
| Real change, result `PASS` (missed) | Always an error |
| No real change, result `FAIL` (false alarm) | Error, possibly of a lower class than a miss |
| Result `partially measured` | **a)** counted as a miss when a real change exists; **b)** a third class, reported separately; **c)** excluded, with the exclusion rate reported |
| Change outside the capability's scope (a meaning reversal) | Excluded from its error count, and reported, since a `PASS` is not evidence of fidelity |

**Decided (`DEC-068`):** removing the year, or another part, from a date is an alteration of data, not a change of form.

`FID-046` classifies structured-tier changes as `CRITICAL`, which argues for treating a miss as more costly than a false alarm. How much more is a domain judgment. *Proposal: option b, because it hides nothing.*

## D3. Who establishes what really changed

The English trial showed the need: the owner's list omitted two word changes that a comparison found (`TRIAL-GIT-HISTORY.md` §7).

- **A.** The owner's list. Cheapest, one judge, can be incomplete.
- **B.** Two independent annotators, with a procedure for disagreements. Strongest, needs people for each language.
- **C.** Synthetic changes injected by a script into real texts. Ground truth is known and it scales to all 13 languages, but it only contains the changes someone thought of.
- **D.** C for volume, plus B on a smaller real sample.

The author of the code must not be the judge: the unit tests are already written by the same agent. *Proposal: D.*

## D4. Which texts, and where they live

To decide: languages in scope first (all 13, or a declared subset; `STATISTICAL-VALIDATION-METHODOLOGY.md` §5.3 requires reporting per language); genres; sources and licences (`Q-007`); and storage. The owner's texts are currently not stored, but `VALIDATION-MAP.md` §59 expects an evidence package that can be reproduced.

- **A.** Public-licence texts only, stored in the repository.
- **B.** Private texts in a private store, with only hashes and results in the repository.
- **C.** Both, reported separately.

## D5. Texts already used cannot be evidence

The defects found on the owner's pairs were fixed using those pairs, so they no longer test anything independently. *Proposal: keep a development set and a held-out set; the agent never sees the held-out set before the criteria and the code version are frozen (`FIDELITY-VALIDATION-PROTOCOL.md`, no post-hoc selection).*

## D6. Form of the criterion

- **A. Fixed checklist:** a curated list of cases that must all be right. It works as a regression test, but gives no rate.
- **B. Estimated rates:** miss and false-alarm rates with confidence intervals, compared to a threshold per language.
- **C. Descriptive only:** rates are published with no threshold, which supports at most a weaker status such as `CONDITIONALLY_VALIDATED`.

*Proposal: A as a precondition, then B or C.*

## D7. Threshold values and sample size

**Left blank on purpose.** `VALIDATION-MAP.md` §44 requires each threshold to be justified by evidence, benchmark distributions, domain requirements, error costs or statistical analysis, and §45 requires it to be versioned.

| Threshold | Value | Justification |
|---|---|---|
| Maximum miss rate | unspecified | unspecified |
| Maximum false-alarm rate | unspecified | unspecified |
| Confidence level | `STATISTICAL-VALIDATION-METHODOLOGY.md` §6.1 sets 95% two-sided for reported estimates; whether it applies here is to be confirmed | |
| Independent documents per language | unspecified | unspecified |

**How sample size limits what can be claimed** (arithmetic, not a recommendation). With zero errors in *n* independent documents, the one-sided 95% upper bound on the error rate is 1 − 0.05^(1/n):

| Documents with no error | The true error rate could still be as high as |
|---|---|
| 30 | 9.5% |
| 60 | 4.9% |
| 100 | 3.0% |
| 300 | 1.0% |
| 1,000 | 0.3% |

These counts are **per language**. The unit is the independent document; several changes in one text are correlated (`STATISTICAL-VALIDATION-METHODOLOGY.md` §3.1).

# 4. Proposed Order

Proposal only: settle D1 and D2, then D3–D5, and build the checklist of D6; decide D7 last but before any held-out text is run. Each answer should be recorded as a numbered decision, with thresholds in the form required by `VALIDATION-MAP.md` §45.

# 5. Decisions (`DEC-075`, 2026-11-19)

The owner delegated these decisions ("fai la cosa che ti sembra più sensata"). The agent took its own proposals where it had made them, and adjusted D3 to the experience of the test kit.

| Decision | Choice |
|---|---|
| D1 | **A.** Claims are made for numeric integrity and structural validation as detectors of changes. Minimality stays a measurement, checked by unit tests. |
| D2 | A miss and a false alarm are both errors, reported separately. `partially measured` is a third class, reported separately (**option b**). A change outside a capability's scope is excluded from its error count and reported. Removing part of a date is an alteration (`DEC-068`). |
| D3 | Text pairs generated from written prompts, each with the generator's list of changes, reconciled with an automatic word- or character-level comparison before results are scored; disagreements are resolved by the owner. Synthetic changes injected by a script may add volume. Two independent annotators are deferred, for lack of people per language. |
| D4 | All 13 languages are reported separately. Texts are kept outside the repository; only their SHA-256, the lists of changes and the results are recorded (**option B**). Generated, fictional texts raise no licensing question; real texts need `Q-007`. |
| D5 | Cases sent to the agent are development data. The held-out set is the owner's reserve series (R01–R15, `09-serie-di-riserva.md`, kept by the owner) and any later reserve; it is run only on a frozen, tagged code version, after this table is fixed, and not used to change the code. |
| D6 | **A** as a precondition (the unit tests modelled on every kit case form the checklist), then **C**: results are descriptive. |
| D7 | **No threshold is set.** Miss and false-alarm rates are published per language with 95% intervals computed per document, and no rate is compared to a pass mark. Under `VALIDATION-MAP.md` §44 a threshold needs a justification the project does not have. |

**Consequence:** with no threshold, no capability can be declared `VALIDATED` (`VALIDATION-MAP.md` §55); descriptive results can support at most `CONDITIONALLY_VALIDATED`, and that vocabulary question is itself still deferred (`DEC-012`, `VALIDATION-GATES.md` §2). Fifteen reserve cases give no useful rate per language (§3, D7 table): they can only show whether the frozen version behaves as on the development cases.
