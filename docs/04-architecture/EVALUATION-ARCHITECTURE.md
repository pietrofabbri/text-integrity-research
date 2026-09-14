# Evaluation Architecture

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Architecture sub-document (post-Tranche-4, per
`docs/00-project/DECISION-LOG.md` DEC-032)
**Authority:** Architectural
**Parent:** `docs/04-architecture/ARCHITECTURE-MAP.md` §21-22 (Evaluation
Layer, Experimental Matrix)
**Scope:** How raw analysis/validation/external-integration observations
are combined into reproducible, comparable experiment results — benchmark
execution, detector/transformation comparison, robustness experiments,
regression analysis, and statistical analysis — without selecting any
specific benchmark, metric, statistical test, or acceptance threshold.

---

# 1. Purpose

This document formalizes `ARCHITECTURE-MAP.md` §21-22 into a concrete
architectural mechanism. It exists because `DECISION-LOG.md` DEC-026
(2026-09-13) found, while resolving `PIPELINE-ARCHITECTURE.md` as not
needed, that the Evaluation Layer was a genuine, previously unflagged gap:
`CORE-ARCHITECTURE.md` §3 explicitly disclaims formalizing it beyond
result-aggregation, `CORE-ARCHITECTURE.md` §4 lists it as "not yet
formalized beyond `ARCHITECTURE-MAP.md` §21-22, §37," and
`REPORTING-ARCHITECTURE.md` formalizes only the *reporting* of results,
not the evaluation/benchmarking mechanics that produce them. DEC-026
deliberately did not add this as a new candidate unilaterally, reasoning
that doing so would itself be an unrequested scope decision. `DEC-032`
records the owner's explicit confirmation to add it as a candidate and
draft it now.

Like every prior 04-architecture sub-document, this document selects no
specific benchmark, metric, statistical test, or acceptance threshold. It
defines the mechanism — what an experiment is, what dimensions it varies
along, what must be preserved, and how it differs from the analysis,
validation, and reporting mechanisms already formalized — that any
specific benchmark or metric would need to plug into.

---

# 2. Relationship to Other Documents

- `ARCHITECTURE-MAP.md` §21-22 are the authoritative parent sections;
  §57 (No Hidden Scientific State) and §56 (Schema-First Principle) are
  the other sections this document elaborates. This document supersedes
  none of them.
- This document is deliberately narrow relative to what it might seem to
  cover. It is **not** the Analysis Layer: `ANALYSIS-ARCHITECTURE.md`
  governs how a single detector, watermark analyzer, or validator
  produces one measurement for one input; this document governs how many
  such measurements, gathered across an experimental matrix (§4 below),
  are compared, aggregated, and checked for regression. A single
  analysis result is this document's raw input, not its subject.
- This document is **not** the Validation Layer: `VALIDATION-ARCHITECTURE.md`
  governs whether a specific transformation or output passes declared
  constraints for one request (§4-9 of that document); this document
  governs whether a *capability's* measured performance, across many
  requests and conditions, has changed or compares favorably to
  alternatives. `VALIDATION-ARCHITECTURE.md` §12's "Regression
  Validation" already covers one specific regression concern — whether a
  changed capability still passes previously-passing validation outcomes
  for affected language/dimension pairs — and this document does not
  restate or duplicate it; §7 below states the narrower, distinct
  regression concern this document adds.
- This document is **not** the Reporting Layer: `REPORTING-ARCHITECTURE.md`
  defines the schema a report must use to present results, including
  evaluation results, once produced; this document defines how those
  results are produced in the first place. §8 below states this boundary
  precisely.
- `docs/04-architecture/ANALYSIS-ARCHITECTURE.md` §8 (Cross-Analyzer
  Independence) already states that "a disagreement between two
  `CAP-DETECT-*` or `CAP-WATERMARK-*` capabilities for the same input is
  itself a measurable, reportable result (mirroring `ARCHITECTURE-MAP.md`
  §21's Evaluation Layer treatment of multi-detector evaluation)" — this
  document is the parent mechanism that sentence already assumes exists;
  §5 below formalizes it.
- `docs/04-architecture/CAPABILITY-ARCHITECTURE.md` §7 (Activation Gate)
  already requires "regression tests and documentation exist" before a
  capability may move to `VALIDATED`; this document does not redefine
  that gate, it defines the mechanism by which a regression is actually
  detected and measured (§7 below).
- `docs/07-data/DATA-MAP.md` governs the datasets an experiment draws on
  (identifiers, manifests, licensing, activation gates) exactly as it
  does for any other resource; this document does not restate that
  governance, only names it as the dependency an experimental matrix's
  "input corpus" dimension (§4) resolves against.

---

# 3. Evaluation as a Distinct Layer (Restated)

Per `ARCHITECTURE-MAP.md` §21, "the evaluation layer combines
measurements into reproducible experiment results." This document reads
"measurements" as the analysis-layer and validation-layer results already
formalized elsewhere — a detector's score, a watermark analyzer's signal,
a validator's pass/fail outcome — and "experiment results" as a distinct,
higher-level object: a comparison, aggregation, or trend computed across
more than one measurement, along one or more dimensions of the
Experimental Matrix (§4). A single measurement is not itself an
experiment result; an experiment result exists only once measurements are
combined for a specific comparative purpose (which detector performs
better on which language; whether a capability's performance has
regressed; whether an attack degrades robustness).

---

# 4. The Experimental Matrix (Restated)

Per `ARCHITECTURE-MAP.md` §22, "the architecture should support
experiments across multiple dimensions": language, input corpus, text
length, domain, analyzer, detector, model, transformation, configuration,
version. This document requires that an experiment record, at minimum,
which value it holds for each dimension that varies in that experiment
and which it holds fixed — an experiment that varies detector while
comparing across languages without recording the fixed input corpus and
configuration is not reproducible, which §22 requires ("an experiment
should be reproducible from its recorded configuration").

This document does not fix a concrete schema for recording these
dimensions (`ARCHITECTURE-MAP.md` §43 reserves concrete data structures
for Development), and it does not add dimensions beyond §22's list — the
"configuration" dimension is exactly `CONFIGURATION-ARCHITECTURE.md`'s
subject (a request's configuration, per that document's §3, already
includes language, pipeline, and enabled capabilities, all of which are
also Experimental Matrix dimensions); the "version" dimension refers to
`CAPABILITY-ARCHITECTURE.md` §12's capability versioning, applied at the
experimental-comparison level rather than the single-capability level.

---

# 5. Benchmark Execution and Detector/Transformation Comparison

Per `ARCHITECTURE-MAP.md` §21's "benchmark execution," "detector
comparison," and "transformation comparison" requirements, and directly
implementing `ANALYSIS-ARCHITECTURE.md` §8's Cross-Analyzer Independence
principle: this document requires that when multiple `CAP-DETECT-*` or
`CAP-WATERMARK-*` capabilities are registered for the same language and
category, their comparison — not merely their individual outputs — is
itself a first-class evaluation result, retained per §6 below rather than
collapsed into a single "winner" before recording. This is grounded in
`docs/02-research/R02-watermark-research.md` §37.1 and
`docs/02-research/R03-watermark-detection-research.md` §43.5's
independence concerns, which `ANALYSIS-ARCHITECTURE.md` §8 already cites
for the same reason.

A benchmark, for this document's purposes, is an experiment (§3) whose
Experimental Matrix (§4) holds a fixed input corpus and set of conditions
constant while varying detector, analyzer, or transformation — precisely
so that the comparison is not confounded by an uncontrolled dimension.
This document does not select any specific benchmark corpus, task, or
scoring method; `docs/02-research/RESEARCH-MAP.md` and
`docs/00-project/RESEARCH-REGISTRY.md` remain authoritative for what
benchmarks and evidence currently exist.

---

# 6. Raw-Measurement Preservation and Derived Scores

Per `ARCHITECTURE-MAP.md` §21, "evaluation must preserve raw measurements"
and "derived scores must never replace the underlying observations." This
document requires that every experiment result retain a pointer back to
the individual measurements it was computed from (each itself already
carrying `ANALYSIS-ARCHITECTURE.md` §7's output-category tag and
`REPORTING-ARCHITECTURE.md` §7's raw-observation/derived-score
distinction) — an aggregate accuracy figure, a mean robustness score, or
a comparative ranking is a derived score under this same discipline, and
must never be presented, stored, or reported in a way that discards the
per-condition measurements it summarizes. This is the same principle
`VALIDATION-ARCHITECTURE.md` §10 (Multi-Metric Requirement) already
applies at the validation level and `REPORTING-ARCHITECTURE.md` §7
applies at the report-schema level; this document is where it applies at
the point an experiment result is first computed, upstream of both.

---

# 7. Regression Analysis (Evaluation-Level, Distinct from Validation-Level Regression)

Per `ARCHITECTURE-MAP.md` §21's "regression analysis" requirement, this
document defines a narrower, distinct concern from
`VALIDATION-ARCHITECTURE.md` §12's "Regression Validation." §12 asks
whether a changed capability still *passes* previously-passing validation
outcomes (a pass/fail question, per language/dimension pair). This
document's regression analysis asks whether a capability's *measured
performance* — an accuracy figure, a robustness score, a comparative
ranking against other capabilities (§5) — has changed relative to a prior
experiment result for the same Experimental Matrix (§4) coordinates,
independent of whether either result crosses any pass/fail threshold.
A capability can remain `VALIDATED` under §12 (still passing its
declared constraints) while this document's regression analysis shows its
measured accuracy has declined — that decline is exactly the kind of
finding `CAPABILITY-ARCHITECTURE.md` §6's `DEGRADED` state exists to
capture ("an `ACTIVE` capability whose scientific or operational quality
has declined... but immediate retirement is not yet justified"). This
document is the mechanism that produces the evidence a `DEGRADED`
determination would be grounded in; it does not itself decide when a
capability should move to `DEGRADED` (that remains
`CAPABILITY-ARCHITECTURE.md` §6's determination).

This document also implements `CAPABILITY-ARCHITECTURE.md` §7's
Activation Gate requirement that "regression tests... exist" before a
capability may reach `VALIDATED`: it is the mechanism by which such a
regression test is actually run and its result recorded, connecting to
`docs/07-data/DATA-MAP.md` §113 (Data Drift: "a dataset update may
require benchmark revalidation") for the case where the regression is
driven by a changed dependency rather than a changed capability.

---

# 8. Statistical Analysis and the Boundary with Reporting

Per `ARCHITECTURE-MAP.md` §21's "statistical analysis" and "report
generation" requirements: this document covers the former, not the
latter. A statistical analysis — a significance test between two
detectors' measured accuracy, a confidence interval on a robustness
score, a trend across capability versions — is itself an experiment
result under §3 and is subject to §6's raw-measurement-preservation
discipline (the statistical summary must never replace the measurements
it was computed from). Once produced, that result flows into
`REPORTING-ARCHITECTURE.md`'s schema exactly as any other analysis or
validation result does — via the same observation-tier/summary-tier
structure that document's §3 defines, and subject to the same
output-category tagging `ANALYSIS-ARCHITECTURE.md` §7 requires, applied
here to an evaluation-layer result rather than a single-analyzer one.
This document does not define, restate, or extend
`REPORTING-ARCHITECTURE.md`'s schema; it only produces the results that
schema must be able to carry.

---

# 9. Illustrative Example (Non-Binding)

Purely to make §4-7's mechanism concrete — not a decision to adopt any
specific benchmark, metric, or threshold:

```
Experiment: detector comparison, Italian text
Experimental Matrix: language=it (fixed), input corpus=[benchmark set X]
  (fixed), analyzer=[CAP-DETECT-A, CAP-DETECT-B] (varying),
  configuration=[default validation profile] (fixed), version=[A v1.2,
  B v0.9] (recorded)
Raw measurements: per-sample scores for both CAP-DETECT-A and
  CAP-DETECT-B, retained individually (§6)
Derived result: CAP-DETECT-A accuracy 0.81, CAP-DETECT-B accuracy 0.74
  on this corpus — a comparison result (§5), not a claim that A is
  universally superior (SPECIFICATION-MAP.md §27, No Universal Success
  Claim, applies here exactly as it does to a single detector's result)
Regression check (§7): compared against the last recorded result for
  the same matrix coordinates with CAP-DETECT-A v1.1 (accuracy 0.83) —
  a 0.02 decline, flagged for CAPABILITY-ARCHITECTURE.md §6 to consider
  for a DEGRADED determination, not silently absorbed into the new
  baseline
```

---

# 10. What This Document Does Not Decide

This document does not: select any specific benchmark corpus, dataset, or
task; fix a concrete metric, statistical test, or significance threshold
for any comparison; decide when a measured decline is large enough to
justify `CAPABILITY-ARCHITECTURE.md` §6's `DEGRADED` state (that remains
a separate, later decision informed by, not made by, this document); fix
a concrete storage or serialization format for experiment results
(`ARCHITECTURE-MAP.md` §43 reserves this for Development); or resolve
`PLUGIN-ARCHITECTURE.md`'s still-open scoping question, which is
unrelated to this document.

---

# 11. Final Principle

An evaluation layer earns its name only if a comparison between two
capabilities, or between a capability's past and present performance, is
as traceable back to its raw measurements as a single detector's score
already must be. This document's role is to make that traceability
structural — an experiment result that cannot be traced back to the
individual measurements it summarizes is not evidence this project can
act on, only a number that looks like evidence.
