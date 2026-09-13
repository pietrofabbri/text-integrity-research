# Reporting Architecture

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Architecture sub-document (Tranche 4)
**Authority:** Architectural
**Parent:** `docs/04-architecture/ARCHITECTURE-MAP.md` §38 (Reporting
Layer), with §21 (Evaluation Layer) as a closely related parent for the
raw-measurement/derived-score distinction this document also formalizes.
**Scope:** How the obligations already scattered across every other
04-architecture sub-document — failure/eligibility states, output-category
tags, missing-evidence states, external observations, raw-versus-derived
measurements — are unified into one report schema, without inventing any
new reporting concept the corpus does not already require.

---

# 1. Purpose

This document formalizes `ARCHITECTURE-MAP.md` §38 into a concrete report
schema. It exists because §58 of that document lists
`REPORTING-ARCHITECTURE.md` as a candidate; §64.4 originally left it, and
five other candidates, unevaluated, "recommended to revisit after
Tranches 1-2." `DECISION-LOG.md` DEC-023 (Tranche 4, continued) assessed
it as structurally ready for a reason distinct from every prior tranche
document: its content is not merely conceptually well-specified in
`ARCHITECTURE-MAP.md` §38 itself, it is already scattered, concretely,
across every sub-document drafted so far. `CORE-ARCHITECTURE.md` §9
already defines a failure/eligibility taxonomy a report must carry;
`ANALYSIS-ARCHITECTURE.md` §7 already requires every analysis result be
tagged with an output category that must "travel wherever it travels";
`VALIDATION-ARCHITECTURE.md` §9 already requires missing-evidence states
and directly cites this document's parent section by name;
`EXTERNAL-INTEGRATION-ARCHITECTURE.md` §5-7 already requires
data-transfer logging and a fifth failure state at the reporting level.
This document's task is therefore to unify these already-required
obligations into one coherent, versioned schema — not to invent a new
reporting concept none of them anticipated.

Like every prior tranche document, this document selects no specific
serialization format, storage technology, or human-readable rendering. It
defines the schema's required content and the discipline governing how
that content may be presented, not the concrete file format or UI.

---

# 2. Relationship to Other Documents

- `ARCHITECTURE-MAP.md` §38 is the authoritative parent; §21 (Evaluation
  Layer), §51 (Storage Architecture — reports as a distinct storage
  category), §56 (Schema-First Principle — reports need an explicit,
  versioned schema), and §57 (No Hidden Scientific State) are the other
  sections this document elaborates. This document supersedes none of
  them.
- `docs/04-architecture/CORE-ARCHITECTURE.md` §9 already defines the
  four-state taxonomy (ran and produced a result; eligible but not
  invoked; not eligible for the request's language; invoked and failed)
  that this document requires every report to be able to express per
  capability (§4 below) — this document does not redefine that taxonomy,
  it requires the report schema actually carry it.
- `docs/04-architecture/EXTERNAL-INTEGRATION-ARCHITECTURE.md` §7 adds a
  fifth state ("eligible and invoked, but the external boundary itself
  was unreachable") and §5-6 require data-transfer logging and tagged
  external observations; this document requires the report schema carry
  both, and does not restate their definitions.
- `docs/04-architecture/ANALYSIS-ARCHITECTURE.md` §7 (Output Category
  Tagging) and `docs/04-architecture/VALIDATION-ARCHITECTURE.md` §7-9
  (per-result fields including `evidence_basis`, `known_limitations`, and
  the `FID-043` missing-evidence states) define what a single analysis or
  validation result must carry; this document requires the report to
  preserve those fields when aggregating results, never to strip or
  collapse them (§6-7 below).
- `docs/04-architecture/CAPABILITY-ARCHITECTURE.md` §10 and
  `docs/04-architecture/LANGUAGE-ARCHITECTURE.md` §4 govern per-language,
  per-capability state; this document's "not eligible for this language"
  state (inherited from `CORE-ARCHITECTURE.md` §9) is populated from
  those records, not computed independently.
- `ARCHITECTURE-MAP.md` §61 (Relationship With Other Project Areas)
  identifies Certification as the area that "determines whether the
  complete architecture and release satisfy the declared certification
  profile" — a certification decision consumes this document's report
  schema as input; this document does not itself define certification
  criteria, which remain `docs/10-certification/`'s authoritative
  territory.
- `ARCHITECTURE-MAP.md` §36 (Configuration Layer) and §37 (Evaluation
  Profiles) are cross-referenced (§3 below, the report's `configuration`
  and `evaluation profile` fields) but not formalized by this document.
  At the time this document was drafted, `ARCHITECTURE-MAP.md` §64.7
  (`DECISION-LOG.md` DEC-023) recorded an unresolved scoping overlap
  between those two sections; this document required only that a report
  be able to record whatever configuration and evaluation-profile
  information exists, without depending on how the two related.
  `DECISION-LOG.md` DEC-025 has since resolved that overlap and drafted
  `CONFIGURATION-ARCHITECTURE.md` — this document's requirement is
  unaffected by, and did not need to anticipate, that resolution.

---

# 3. Report Schema (Restated and Consolidated)

Per `ARCHITECTURE-MAP.md` §38, a report must be able to contain: input
identifier/hash, language, enabled capabilities, versions,
transformations, changes, validation results, detector observations,
watermark-analysis observations, uncertainty, warnings, errors, and final
status. This document requires the schema be organized around two tiers,
consistent with §21's "derived scores must never replace the underlying
observations":

- **the observation tier** — every individual analysis result
  (`ANALYSIS-ARCHITECTURE.md` §4-6), validation result
  (`VALIDATION-ARCHITECTURE.md` §7), and external observation
  (`EXTERNAL-INTEGRATION-ARCHITECTURE.md` §6), retained individually,
  with every field those documents already require (output category,
  evidence basis, known limitations, language, evidence tier) intact;
- **the summary tier** — any human-readable rollup or aggregate view,
  which per §38 "may be generated from the same underlying data" as the
  machine-readable observation tier, and per this document's §7 below
  must be generated *from* it, never stored as an independent,
  potentially divergent second record.

Per `ARCHITECTURE-MAP.md` §56 (Schema-First Principle), this schema must
be explicit and its changes versioned; this document does not fix the
concrete serialization (JSON, protocol buffers, or otherwise) — that
remains a Development-phase decision (§43).

---

# 4. The Failure and Eligibility Taxonomy in the Report

Per `CORE-ARCHITECTURE.md` §9, extended by
`EXTERNAL-INTEGRATION-ARCHITECTURE.md` §7, the report must be able to
distinguish, for every capability relevant to a request:

1. ran and produced a result;
2. eligible but not invoked (cancelled, or skipped due to a resource
   limit);
3. not eligible for the request's language at all
   (`CAPABILITY-ARCHITECTURE.md` §10's `NOT_SUPPORTED` state);
4. invoked and failed;
5. eligible and invoked, but the external boundary itself was
   unreachable or unavailable (external integrations only).

This document requires that these five states be first-class values in
the report schema — not inferred by a reader from the absence of a
result — and that no two of them ever be conflated into a generic "no
result" outcome. This is the report-level enforcement point for the
missing-evidence discipline `CORE-ARCHITECTURE.md` §9 and
`VALIDATION-ARCHITECTURE.md` §9 already require elsewhere; this document
does not weaken or duplicate that discipline, it is the schema that makes
it visible to whoever reads the report.

---

# 5. Missing-Evidence and Unsupported-Dimension States

Per `VALIDATION-ARCHITECTURE.md` §9 (implementing `FID-043`), when a
validation family/language pair has no `VALIDATED` capability, the report
must use one of `not measurable`, `unsupported`, or `not applicable` —
and must never silently omit the dimension, default it to a pass, or
substitute an `EXPERIMENTAL`-only result presented with the same status
as a `VALIDATED` one. This document requires the same three-state
discipline apply uniformly to every dimension a report covers, not only
validation: an analysis dimension with no registered capability for the
request's language (`ANALYSIS-ARCHITECTURE.md` §4-6,
`SPECIFICATION-MAP.md` §22.1's `NOT_SUPPORTED` cells) must be reported as
`unsupported` for that language, exactly as a missing factual-claim
validator is, never left as a silent gap a reader could mistake for "the
analysis found nothing."

A report covering multiple languages or capabilities will typically show
a genuinely mixed picture — some dimensions measured, some unsupported,
some not applicable. Per `LANGUAGE-ARCHITECTURE.md` §4's `validation_status`
field ("mixed — must not be summarized as a single supported/unsupported
flag"), this document requires the summary tier (§3) preserve that
mixed picture rather than collapsing it into one project-wide or
one-language verdict.

---

# 6. Output Category and Evidence Fields Must Travel Into the Report

Per `ANALYSIS-ARCHITECTURE.md` §7 (implementing `S02-scientific-requirements.md`
§27, the Scientific Ground-Truth Rule), every analysis result carries an
output-category tag (known ground truth, experimentally established
observation, detector output, inferred classification, hypothesis,
assumption, or unknown) that "must never be silently conflated." Per
`VALIDATION-ARCHITECTURE.md` §7-8, every validation result carries
`evidence_basis`, `known_limitations`, and `language` fields, with raw
measurements preserved alongside any derived score. This document
requires the report's observation tier (§3) preserve every one of these
fields on every individual result — aggregating results into the summary
tier must never drop, average away, or otherwise obscure a result's
output category, evidence basis, or language-specific known limitation.
A detector's score reported without its output-category tag, or a
language-specific reliability gap (e.g. `ANALYSIS-ARCHITECTURE.md` §9's
Russian illustrative example) reported without the `known_limitations`
note that must sit "next to the score, not merely retrievable from a
separate document," would violate this section.

---

# 7. Raw Observations, Derived Scores, and Multi-Metric Results

Per `ARCHITECTURE-MAP.md` §21, "derived scores must never replace the
underlying observations." Per `VALIDATION-ARCHITECTURE.md` §10 (`FID-037`,
Multi-Metric Requirement), when more than one validator is consulted for
the same language/dimension, results must be retained individually in the
observation tier; collapsing into one number is permitted only "for
reporting convenience" in the summary tier, per §38's own text, and only
when the underlying per-validator results remain available alongside it.
This document requires that the summary tier's derivation from the
observation tier be reconstructible: a reader who distrusts a summary
figure must be able to trace it back to the specific observations it was
computed from, rather than the summary standing as an unaccountable,
independently-asserted number.

Per `ANALYSIS-ARCHITECTURE.md` §8 (Cross-Analyzer Independence), a
disagreement between two analyzers registered for the same language and
category "is itself a measurable, reportable result" and "must not be
silently resolved by picking one analyzer's output as authoritative."
This document requires the report schema be able to represent such a
disagreement directly — both results present, neither suppressed —
rather than forcing an implicit choice at the reporting layer that
`ANALYSIS-ARCHITECTURE.md` §8 already prohibits at the analysis layer.

---

# 8. External Observations and Data-Transfer Records

Per `EXTERNAL-INTEGRATION-ARCHITECTURE.md` §5-6, a cloud detector's
result must be written into the same observation schema as any local
analysis result, tagged by source and evidence character, and reported
alongside a local capability's own result — never substituting for it.
The same document's §5 requires that a data transfer (category, provider,
and — per this document's cross-reference — the preservation-snapshot
hash identifying what was sent, `CORE-ARCHITECTURE.md` §8) be logged.
This document requires the report's observation tier carry both: the
external result itself, tagged as external, and a record that the
transfer occurred, satisfying `ARCHITECTURE-MAP.md` §30's data-transfer-
logging requirement at the point where a reader would actually look for
it — the report — rather than only in a separate operational log this
document does not otherwise define.

---

# 9. Schema Stability and Versioning

Per `ARCHITECTURE-MAP.md` §56, schema changes must be versioned. Per §55
(Interface Stability), core interfaces should remain stable even when
implementations change, and explicitly lists "experiment results" among
the interfaces the architecture should favor stability around. This
document requires the report schema be one such stable interface: a
capability, detector, or validator may be added, replaced, or retired
(§46-48) without changing the report schema's own shape — only the
content populating it changes. A genuine schema change (a new required
field, a changed state taxonomy) must be versioned per §56 and must not
silently break a previously-valid report's interpretability, echoing
`ARCHITECTURE-MAP.md` §54's requirement that "historical experiment
results must remain interpretable after removal."

---

# 10. Illustrative Example (Non-Binding)

Composing the illustrative examples already on file in
`ANALYSIS-ARCHITECTURE.md` §9, `VALIDATION-ARCHITECTURE.md` §13, and
`EXTERNAL-INTEGRATION-ARCHITECTURE.md` §9 into a single report — purely
to make §3-8's consolidation concrete, not a decision to adopt any
specific capability, threshold, or format:

```
report for: Italian text, single request
observation tier:
  - CAP-DETECT-EXAMPLE (it): RESEARCH_ONLY (SPECIFICATION-MAP.md §22.1.1);
    output_category: detector output (S02 §27); ran and produced a result
  - cloud AI-detector (external, outbound): tagged external observation
    (EXTERNAL-INTEGRATION-ARCHITECTURE.md §6); reported alongside the
    local result above, not substituted for it; data-transfer logged
  - VALIDATE-SEMANTIC (it): EXPERIMENTAL capability; ran and produced a
    result (PASS/FAIL per its own threshold)
  - VALIDATE-FACTUAL-CLAIM (it): no VALIDATED capability exists —
    reported as "unsupported" (FID-043), state 3 (not eligible), NOT as
    a pass
  - VALIDATE-STRUCTURAL (it): EXPERIMENTAL capability; ran, PASS
summary tier (derived from the above, not a separate record):
  - overall picture: genuinely mixed — must not be presented as a clean
    pass across all dimensions (VALIDATION-ARCHITECTURE.md §13)
  - every derived statement traceable back to one or more rows above
```

---

# 11. What This Document Does Not Decide

This document does not: select any specific serialization format,
storage technology, or human-readable rendering/UI for a report
(`ARCHITECTURE-MAP.md` §43 reserves this for Development); resolve the
`CONFIGURATION-ARCHITECTURE.md`/Evaluation-Profile scoping overlap
`ARCHITECTURE-MAP.md` §64.7 records — this document requires a report be
able to carry whatever configuration and evaluation-profile information
exists, whichever way that overlap is eventually resolved; define
certification criteria (`docs/10-certification/`'s own territory,
`ARCHITECTURE-MAP.md` §61); decide whether `PIPELINE-ARCHITECTURE.md` is
a separate document (`CORE-ARCHITECTURE.md` §10's open question, unrelated
to this one); or resolve DCQ-006, DCQ-007, or DCQ-008.

---

# 12. Final Principle

A report is the one artifact every other document in this corpus
ultimately writes for — the failure states `CORE-ARCHITECTURE.md` defines,
the output-category tags `ANALYSIS-ARCHITECTURE.md` requires, the
missing-evidence states `VALIDATION-ARCHITECTURE.md` enforces, the
external-observation tagging `EXTERNAL-INTEGRATION-ARCHITECTURE.md`
requires, all exist so that a reader looking only at a report can tell
what happened, what did not happen, what is uncertain, and what was
never even attempted — without having to already know, from some other
document, what question to ask. A report that collapses this texture for
convenience does not simplify the project's findings; it manufactures a
confidence the underlying observations do not support.
