# Validation Architecture

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Architecture sub-document (Tranche 2)
**Authority:** Architectural
**Parent:** `docs/04-architecture/ARCHITECTURE-MAP.md` §16-20 (Validation
Layer, Semantic/Factual/Structural Validation, Minimality Measurement)
**Scope:** How candidate transformations are checked against declared
constraints, how validation results are reported when evidence is
incomplete, and how factual validation specifically is scoped to avoid
overclaiming multilingual coverage.

---

# 1. Purpose

This document formalizes `ARCHITECTURE-MAP.md` §16-20 into a concrete
validation model. It exists because §58 of that document lists
`VALIDATION-ARCHITECTURE.md` as a candidate document; §64.3 initially
judged it blocked on a scope decision for KB-013's multilingual
factual-consistency gap, which `docs/00-project/DECISION-LOG.md` DEC-015
(2026-09-12) now resolves.

Like `CAPABILITY-ARCHITECTURE.md` and `DATA-MODEL.md` before it, this
document selects no specific metric, model or threshold value as final.
It defines the mechanism — validation families, result schema, and
missing-evidence handling — that any specific metric or model would need
to plug into.

---

# 2. Relationship to Other Documents

- `ARCHITECTURE-MAP.md` §16-20 is the authoritative parent; this document
  elaborates, it does not supersede.
- `docs/03-scientific-specification/S04-fidelity-requirements.md`
  (`FID-xxx`) and `S05-transformation-requirements.md` (`TRN-xxx`) are
  authoritative for *what* must be preserved and by how much. This
  document is authoritative only for *how* validation is architecturally
  organized, reported and gated — it cross-references specific `FID-xxx`
  IDs throughout rather than restating their content.
- `docs/04-architecture/CAPABILITY-ARCHITECTURE.md` governs how a
  validator itself is registered, versioned and gated between
  `EXPERIMENTAL` and `VALIDATED`/`ACTIVE`. A "validation family" in this
  document (§4) is a *category* of capability under that schema, not a
  new registry mechanism.
- `docs/00-project/DECISION-LOG.md` DEC-015 supplies the specific scope
  resolution this document implements in §6.
- `docs/00-project/OPEN-QUESTIONS.md` Q-001 (what constitutes sufficient
  semantic equivalence) remains genuinely open — this document defines
  where a semantic-equivalence metric would plug in (§5) and how its
  result would be reported (§8), but does not answer Q-001 itself.

---

# 3. Candidate Model (Restated)

Per `ARCHITECTURE-MAP.md` §15:

```
ORIGINAL → CANDIDATE → ANALYSIS → VALIDATION → ACCEPTED / REJECTED
```

Validation acts on a candidate transformation, never on the original.
Multiple candidates may be validated independently, and a candidate that
fails validation must not silently become the accepted output.

---

# 4. Validation Families

Restating and organizing `ARCHITECTURE-MAP.md` §16, each family
corresponds to one or more `CAPABILITY-ARCHITECTURE.md` capability
categories (that document's §5):

- **Semantic validation** (`VALIDATE-SEMANTIC`) — `FID-001` (Semantic
  Preservation), `FID-002` (Claim Preservation, propositional level).
- **Factual validation**, split per DEC-015 into:
  - `VALIDATE-FACTUAL-STRUCTURED` — `FID-003` (Factual Preservation:
    names, entities, dates, quantities, units, identifiers, citations).
  - `VALIDATE-FACTUAL-CLAIM` — holistic claim/proposition consistency,
    overlapping with `FID-002`. See §6 for why these are architecturally
    distinct.
- **Structural validation** (`VALIDATE-STRUCTURAL`) — `FID-016`
  (Structural Preservation), `FID-017` (Formatting Preservation).
- **Numerical / entity validation** — the quantitative and identity-
  bearing subset of `FID-003`, `FID-008` (Quantitative Preservation),
  `FID-010` (Entity Preservation); architecturally these may be
  implemented as part of `VALIDATE-FACTUAL-STRUCTURED` (§6) rather than
  as separate families, since both are deterministic-leaning checks over
  the same categories of content.
- **Linguistic validation** — `FID-013` (Linguistic Correctness),
  `FID-014` (Register Preservation), `FID-027` (Multilingual Fidelity).
- **Minimality validation** — `FID-021` (Minimality),
  `S05-transformation-requirements.md` TRN-007 (Minimal Intervention),
  per `ARCHITECTURE-MAP.md` §20.
- **Regression validation** — whether a change (to a capability, model,
  or dependency) altered previously-passing validation outcomes; not tied
  to a specific `FID-xxx` ID, applies across all families.

Per `ARCHITECTURE-MAP.md` §16, validation must be independent from the
component that generated the candidate whenever practical — a
transformation capability and the validator that checks its output
should be separately registered capabilities (`CAPABILITY-ARCHITECTURE.md`
§4), not the same component grading its own work.

---

# 5. Validator Plug-In Point

A validation family (§4) is satisfied by one or more registered
validator capabilities. Architecturally, a validator:

1. declares which `FID-xxx`/`TRN-xxx` requirement(s) it addresses;
2. declares its language coverage as a per-language map, per
   `CAPABILITY-ARCHITECTURE.md` §10 — not a single flag;
3. declares its evidence basis as one or more `R-XXXX` registry entries
   with their confidence tags, per `CAPABILITY-ARCHITECTURE.md` §11;
4. returns a structured result (§8), never a bare pass/fail, per
   `FID-043`/`FID-044`.

More than one validator may exist for the same family and language, per
`CAPABILITY-ARCHITECTURE.md` §13 (Multiple Candidates per Category) — the
project does not commit to "the" semantic-similarity metric or "the"
factual checker, consistent with Q-001 remaining open and
`ARCHITECTURE-MAP.md` §2 ("no single algorithm should define the
architecture").

---

# 6. Factual Validation Split (Implements DEC-015)

Factual validation is architecturally two categories, not one, because
their evidence bases are different in kind, not merely in completeness:

- **`VALIDATE-FACTUAL-STRUCTURED`** targets `FID-003`'s explicit,
  largely enumerable categories (names, dates, quantities, entities,
  units, identifiers, citations). These are addressable by deterministic
  or near-deterministic extraction (named-entity recognition, pattern
  matching, unit/number parsing), consistent with
  `ARCHITECTURE-MAP.md` §18's own guidance to "prioritize deterministic
  checks where possible." Per-language coverage for this category is a
  separate, not-yet-researched evidence question — R09 did not
  investigate NER/extraction tooling by language, and this document does
  not assume it is solved; it only establishes that this category is
  not blocked by KB-013's specific finding (§6.1 below).
- **`VALIDATE-FACTUAL-CLAIM`** targets the holistic, entailment-style
  consistency question `FID-002` and R09's research addressed
  (MiniCheck, mDeBERTa-v3-xnli, mFACT — `RESEARCH-REGISTRY.md`
  R-0109/R-0111/R-0112). Per DEC-015: English may pursue `VALIDATED`
  status through the Activation Gate; all other 12 target languages may
  register only `EXPERIMENTAL` candidates until a bridging study
  resolves KB-013's task-fit gap.

## 6.1 Why the Split Is Not Itself a New Research Claim

This split does not assert that `VALIDATE-FACTUAL-STRUCTURED` is solved
for all 13 languages — it asserts only that its evidence question is
*different* from, and not blocked by, `VALIDATE-FACTUAL-CLAIM`'s
specifically-researched gap (KB-013). Whether NER-style extraction is
adequately evidenced per target language remains open and should be
raised as its own knowledge-backlog item if and when
`VALIDATE-FACTUAL-STRUCTURED` capabilities are actually proposed for
activation — this document does not do so here, to avoid inventing a
research finding that has not been produced.

---

# 7. Hard Constraints vs. Soft Objectives (FID-041/042)

A validation result must distinguish:

- **Hard constraints** — per `FID-041`, violation invalidates the
  candidate regardless of performance elsewhere (e.g. a factual change
  flagged by `VALIDATE-FACTUAL-STRUCTURED`).
- **Soft objectives** — per `FID-042`, optimization targets that must
  never override a hard constraint (e.g. stylistic similarity).

Which specific dimensions are hard vs. soft for a given transformation is
declared by the experiment or capability configuration (`FID-041`
requires this be explicit) — this document does not fix a universal
list, since `ARCHITECTURE-MAP.md` §14 already notes constraints vary by
transformation.

Where multiple hard-constraint-eligible dimensions genuinely conflict
(rare, but possible if a transformation's own declared constraints are
inconsistent), the architecture surfaces this as a Pareto trade-off
(`FID-040`) rather than silently resolving it by an implicit priority
order.

---

# 8. Validation Result Schema

Every validator invocation returns a structured result containing, at
minimum:

- `family` and `capability_id` (§4, §5);
- `outcome` — one of `PASS`, `FAIL`, or a Missing-Evidence state (§9);
- `constraint_type` — `HARD` or `SOFT` (§7), as declared by the
  invoking capability/experiment;
- `confidence` — retained when the validator provides it, never inferred
  when absent (`FID-044`: confidence must not be confused with
  correctness, and a high-confidence report does not imply high
  scientific reliability);
- `evidence_basis` — the `R-XXXX` sources and confidence tags behind the
  validator (`CAPABILITY-ARCHITECTURE.md` §11);
- `language` — the specific language this result applies to, never a
  project-wide aggregate (`RESEARCH-MAP.md` §46, restated at the
  capability level in `CAPABILITY-ARCHITECTURE.md` §10).

Raw measurements must be preserved alongside any derived score
(`ARCHITECTURE-MAP.md` §21: "derived scores must never replace the
underlying observations").

---

# 9. Missing-Evidence Reporting (Implements FID-043)

When a validation family/language pair has no `VALIDATED` capability
(§5) — the current state of `VALIDATE-FACTUAL-CLAIM` for 12 of 13
target languages, per DEC-015 — the architecture must report that
dimension using one of `FID-043`'s explicit states: `not measurable`,
`unsupported`, or `not applicable`. It must never:

- silently omit the dimension from the report;
- default the dimension to `PASS`;
- substitute an `EXPERIMENTAL`-only validator's result and present it
  with the same status as a `VALIDATED` one.

This is the single architectural mechanism that makes DEC-015's scope
decision safe: a pipeline run on, say, Italian text is not silently
missing factual-claim validation — it explicitly reports that dimension
as unsupported for that language, which downstream reporting
(`ARCHITECTURE-MAP.md` §38) and certification (`ARCHITECTURE-MAP.md`
§61) must surface rather than suppress.

---

# 10. Multi-Metric Requirement (FID-037)

Per `FID-037`, an important fidelity claim should not rest on a single
metric. Architecturally, this means a validation family (§4) should
support more than one validator being consulted for the same
language/dimension, with results retained individually (§8) rather than
collapsed into one number before being recorded — collapsing may happen
for reporting convenience (`ARCHITECTURE-MAP.md` §38: human-readable
summaries may be generated from the same underlying data), but the
underlying per-validator results must remain available.

---

# 11. Metric and Threshold Documentation (FID-038/039)

Any validator proposed for `VALIDATED` status must, per `FID-038`,
document what it measures, what it does not measure, language coverage,
known biases, known failure modes, validation evidence, version and
implementation — this is exactly the information already required by
`CAPABILITY-ARCHITECTURE.md` §4's `known_limitations` and
`scientific_sources` fields, so no separate schema is introduced here.
Any acceptance threshold must, per `FID-039`, be scientifically justified
and versioned, and must not be adjusted merely to make a method pass —
threshold values themselves are not decided in this document.

---

# 12. Regression Validation

When a capability, dependency, or resource changes (per
`CAPABILITY-ARCHITECTURE.md` §12 versioning), previously-passing
validation outcomes for affected language/dimension pairs should be
re-checked before the change reaches `ACTIVE` status broadly. This
operationalizes `ARCHITECTURE-MAP.md` §44 (Testing Architecture:
regression tests) within the validation layer specifically, and connects
to `DATA-MAP.md` §113 (Data Drift: "a dataset update may require
benchmark revalidation").

---

# 13. Illustrative Example (Non-Binding)

Using DEC-015's resolution, purely to make §9's reporting behavior
concrete — not a decision to adopt this specific configuration:

```
Input: Italian text, candidate transformation output
VALIDATE-SEMANTIC (it):        EXPERIMENTAL capability, outcome: FAIL/PASS per its own threshold
VALIDATE-FACTUAL-STRUCTURED (it): not yet proposed — reported as "not applicable" (no capability registered)
VALIDATE-FACTUAL-CLAIM (it):   no VALIDATED capability exists — reported as "unsupported" (FID-043),
                                 NOT as PASS, even though an EXPERIMENTAL mDeBERTa-v3-xnli
                                 candidate (R-0111) may exist and be logged separately for research purposes
VALIDATE-STRUCTURAL (it):      EXPERIMENTAL capability, outcome: PASS
```

The report as a whole must make clear that this candidate has not
received factual-claim validation for Italian — it must not read as a
clean pass across all dimensions.

---

# 14. What This Document Does Not Decide

This document does not: select any specific semantic-similarity metric
(Q-001 remains open), resolve KB-013's underlying multilingual evidence
gap (DEC-015 only scopes around it), fix concrete acceptance thresholds
for any `FID-xxx` requirement, or decide whether
`VALIDATE-FACTUAL-STRUCTURED` is adequately evidenced per language (§6.1
— an open question this document deliberately does not answer). All of
these remain separate, later decisions or research tasks.

---

# 15. Final Principle

A validation architecture is trustworthy only if what it does not know is
as visible as what it does. This document's central mechanism —
explicit missing-evidence states (§9) rather than silent omission or
default success — exists so that DEC-015's scope decision, and any future
one like it, makes the project's real coverage honest rather than merely
convenient to report.
