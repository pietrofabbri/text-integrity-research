# Fidelity Validation Protocol

**Status:** ACTIVE  
**Version:** 0.1  
**Document type:** Validation methodology and experimental protocol (Tranche 2)  
**Authority:** Validation (Primary for fidelity/preservation measurement protocols)  
**Parent:** `docs/05-validation/VALIDATION-MAP.md` §12–21  
**Research basis:** `docs/02-research/R06-transformation-preservation-research.md` §58 (`R-0024`, `R-0074` through `R-0085`)  
**Requirements basis:** `docs/03-scientific-specification/S04-fidelity-requirements.md` (`FID-001` through `FID-100`, cited selectively below), `docs/03-scientific-specification/S05-transformation-requirements.md` (`TRN-007`, `TRN-011`, `TRN-065`–`TRN-067`)  
**Architectural basis:** `docs/04-architecture/VALIDATION-ARCHITECTURE.md`, `docs/04-architecture/EVALUATION-ARCHITECTURE.md` (§6–7), `docs/04-architecture/CAPABILITY-ARCHITECTURE.md` (Activation Gate, §7)  
**Related decision:** `docs/00-project/DECISION-LOG.md` DEC-015 (structured/claim factual split), DEC-037 (this document's execution)

---

# 1. Purpose & Scope

This document formalizes the empirical measurement protocols required to validate preservation ("fidelity") of any controlled textual transformation produced by this project, satisfying `VALIDATION-MAP.md` §12–21.

It exists to enforce `VALIDATION-MAP.md` §2 (the Fundamental Validation Principle) for the specific case of fidelity: **a transformation is not entitled to a passing fidelity determination merely because a convenient similarity score clears a threshold.** `S04-fidelity-requirements.md` FID-100 (Final Fidelity Principle) states the governing objective directly: the goal is not to prove a transformation is good, but to determine, with the strongest available evidence, whether it preserves required source properties under specified conditions.

This document governs:
1. Input/output integrity and the fidelity fields of the Minimum Experiment Record (`STATISTICAL-VALIDATION-METHODOLOGY.md` §7);
2. Semantic preservation measurement and semantic acceptance criteria;
3. Factual preservation, split into a structured tier and a claim tier per `DECISION-LOG.md` DEC-015;
4. Numerical and entity integrity checks;
5. Structural integrity checks;
6. Linguistic quality — including an explicit, uncorrected evidence gap this document does not paper over;
7. Minimality measurement and transformation-budget enforcement.

Per `NO-INVENTION-RULES.md`, every protocol rule below is grounded in a specific `FID-*`/`TRN-*` requirement or a specific `R-XXXX` finding in `R06-transformation-preservation-research.md` §58. Where §58's own literature pass found no supporting evidence for a plausible-sounding metric, this document says so explicitly rather than selecting one anyway — see §6 below.

---

# 2. Input/Output Integrity (`VALIDATION-MAP.md` §12)

Per `VALIDATION-MAP.md` §12 and `TRN-001`/`TRN-002` (Source Preservation, Output Independence), every fidelity-validation experiment must retain, as distinct artifacts:

1. the original input, unmodified;
2. the output;
3. a structured diff between them (§8 below defines its minimum content);
4. transformation metadata (`TRN-032` Provenance: transformation identifier/version, configuration identifier, timestamp, language);
5. the validation results produced by this document's protocols.

**The original input must never be reconstructed from the output.** This is a hard requirement, not a style preference: `FID-024` (No Hidden Content Modification) requires every material modification to be observable in the experiment record, and `TRN-015` (No Silent Deletion) requires any substantive deletion to be identifiable independently of the output text itself. A fidelity-validation pipeline that only stores the output and a similarity score violates both.

These five artifacts populate the fidelity-relevant fields of the Minimum Experiment Record schema already defined in `STATISTICAL-VALIDATION-METHODOLOGY.md` §7; this document does not redefine that schema, only the measurement protocols whose outputs fill it.

---

# 3. Semantic Preservation Measurement (`VALIDATION-MAP.md` §13)

## 3.1 No Single Semantic-Preservation Metric

`FID-001` requires semantic preservation to be evaluated independently from surface similarity, and `FID-037` (Metric Diversity) requires that important fidelity claims not rest on one metric alone. This is not merely a design preference — `R06` §58.2 found it directly, empirically confirmed across the literature actually surveyed:

> DIPPER (`R-0024`, updated) uses P-SP with a 0.76 threshold; DEPO (`R-0074`) uses BERTScore F1; StealthRL (`R-0076`) uses E5 cosine similarity *and* an LLM-as-judge Likert scale that visibly diverges from the embedding metric on the same outputs (0.901 similarity vs. 2.64/5 LLM-judge rating). No single standardized semantic-preservation metric exists in this literature.

**Protocol requirement:** every semantic-preservation determination must report at least two methodologically distinct metrics — one embedding/similarity-based (e.g. an E5- or BERTScore-family metric) and one from a materially different methodology (entailment/contradiction-style NLI, or a human/LLM-judge protocol per `FID-036`). Per `FID-092` (Conflicting Metrics), a material disagreement between the two — as the StealthRL finding above demonstrates can occur on identical outputs — must be exposed and recorded as uncertainty, never resolved by silently preferring the more favorable metric.

## 3.2 Semantic Acceptance (`VALIDATION-MAP.md` §14)

A candidate must not be accepted merely because a similarity score exceeds a threshold (`VALIDATION-MAP.md` §14: "high lexical similarity does not guarantee semantic equivalence"). Acceptance evaluation must separately consider, per `FID-006` (Negation), `FID-007` (Modality), and `FID-002` (Claim Preservation):

- contradictions introduced relative to the source;
- claims silently removed, weakened, strengthened, rescoped, or re-attributed;
- changed modality (possibility silently becoming certainty, or vice versa);
- changed negation, negation scope, or negative quantification;
- changed conditions or causal relationships.

Each of these is evaluated as a distinct, reportable dimension — not folded into the similarity score from §3.1 — consistent with `FID-047` (Aggregation: an aggregate must never conceal a hard-constraint violation).

---

# 4. Factual Preservation: Structured and Claim Tiers (`VALIDATION-MAP.md` §15)

`DECISION-LOG.md` DEC-015 splits factual-preservation validation into two distinct capability categories, specifically to avoid blocking the deterministic half of factual validation on an evidence gap that applies only to the holistic half. This document formalizes both tiers' measurement protocols separately; it does not merge them.

## 4.1 Structured Tier (`VALIDATE-FACTUAL-STRUCTURED`, `FID-003`)

Per `FID-003`, `FID-008` (Quantitative Preservation), `FID-009` (Temporal Preservation), and `FID-012` (Citation and Reference Preservation), the structured tier is a deterministic extract-and-compare protocol over:

- numbers, quantities, percentages, units, currencies (`FID-008`);
- dates, times, durations, relative temporal expressions (`FID-009`);
- names, organizations, locations, identifiers (`FID-003`, `FID-010`);
- citations and bibliographic references (`FID-012`).

Per `VALIDATION-MAP.md` §16, numerical comparison must distinguish exact equality, mathematically equivalent representation, unit conversion, rounding, and genuine changed value — a transformation must not be allowed to silently convert a factual change into a formatting difference. Unauthorized changes to any structured-tier element are classified `CRITICAL` per `FID-046` (Severity) and treated as hard-constraint violations per `FID-041`, consistent with `TRN-066`/`TRN-067` (Protected Spans / Protection Failure): if a protected span cannot be preserved, the transformation must fail explicitly rather than silently modify it.

Because this tier is deterministic extraction rather than holistic entailment, `DECISION-015` establishes that it is **not** blocked by `KNOWLEDGE-BACKLOG.md` KB-013's multilingual evidence gap (§4.2 below); it may pursue `CAPABILITY-ARCHITECTURE.md`'s Activation Gate per language on ordinary entity/number-extraction evidence.

## 4.2 Claim Tier (`VALIDATE-FACTUAL-CLAIM`, `FID-002`)

Per DEC-015, the claim tier is the holistic, proposition-level consistency territory `FID-002` describes. Its evidentiary status differs sharply by language:

- **English:** MiniCheck (`R-0109`) is a well-evidenced candidate eligible to pursue the Activation Gate.
- **All 12 other target languages:** per DEC-015 and `KNOWLEDGE-BACKLOG.md` KB-013, no capability may reach `VALIDATED` on this dimension today. A candidate such as mDeBERTa-v3-xnli (`R-0111`) may be registered only as `EXPERIMENTAL`.

Separately, `R06` §58.3 confirms this gap is not merely an architectural scoping question but a genuine, searched-for-and-not-found evidence gap even for the underlying toolkit, English included:

> An established factuality-metric toolkit exists for summarization (FactCC, SummaC, QAFactEval, AlignScore — `R-0085`, EVIDENCE tier for existence). **No evidence found** of any of these, or an LLM-as-judge factuality protocol, being applied specifically to detector-evasion or watermark-removal paraphrasing — a genuine, confirmed gap between an available toolkit and this project's actual use case, not a search failure.

**Protocol requirement:** per `FID-043` (Missing Evidence) and DEC-015's own point 3, any validation run for a language/capability pair lacking a `VALIDATED` `VALIDATE-FACTUAL-CLAIM` capability must report the claim-tier dimension as `not measurable` or `unsupported` — never silently omitted, and never defaulted to a pass. This document does not select a specific claim-tier tool or threshold for production use beyond what DEC-015 already authorized (MiniCheck for English); doing so for any other language, or for the evasion-paraphrasing use case specifically, would assert evidence `R06` §58.3 explicitly found absent.

---

# 5. Numerical and Entity Integrity (`VALIDATION-MAP.md` §16–17)

Named entities are compared where reliably extractable (`VALIDATION-MAP.md` §17, `FID-010`); entity substitutions require explicit handling, not silent pass-through. Numerical values require the exact/equivalent/unit-conversion/rounding/changed-value distinction already stated in §4.1 above.

**This protocol's evidentiary basis is thin, and this document records that plainly rather than overstating confidence.** `R06` §58.4 found only a single illustrative anecdote, not a systematic rate:

> The clearest evidence found is a single illustrative example (`R-0079`) of DIPPER paraphrasing inconsistently transforming a financial figure ("$1.1218") across rounds, directly paralleling the watermark-driven numeric-drift concern already documented in R02 §37.2 (`R-0041`), but here for plain, non-watermark paraphrasing. This is anecdotal, not a systematic quantified accuracy rate. **No evidence found** of a dedicated, large-N numeric- or entity-preservation-rate study for detector-evasion/watermark-removal paraphrasing specifically.

Per `FID-090` (Scientific Interpretation) and `FID-091` (Evidence Hierarchy), this means: the numerical/entity integrity check below establishes that the failure mode *exists and recurs* (corroborated independently by R02's watermark-side finding, R-0041), which justifies requiring the check at all — but a `PASS` on this dimension must be reported as a deterministic extraction result under declared conditions, never as evidence that numeric drift is rare or well-characterized in general. Any future claim about numeric-drift *rates* for non-watermark paraphrasing would need its own dedicated study; this document does not manufacture one.

---

# 6. Structural Integrity (`VALIDATION-MAP.md` §18)

Per `FID-016` (Structural Preservation) and `FID-017` (Formatting Preservation), document structure is compared across:

- paragraph count, headings, list structure, table structure;
- quotation boundaries, references, markup, formulas, code blocks (`FID-033`, `FID-034`).

Structural changes must be intentional and measurable (`VALIDATION-MAP.md` §18); per `TRN-021`–`TRN-023` (Content-Type Awareness, Structured Content Protection, Boundary Awareness), a generic transformation must not blindly modify machine-readable content, and must not unintentionally cross section, quotation, table, code-block, or metadata boundaries. `FID-035` (Mixed-Content Documents) requires that a document be segmented into its distinct content types before structural comparison, since each may carry different applicable fidelity criteria.

---

# 7. Linguistic Quality — An Acknowledged Evidence Gap (`VALIDATION-MAP.md` §19)

`FID-013` (Linguistic Correctness), `FID-014` (Register Preservation), and `FID-015` (Stylistic Preservation) define what linguistic-quality validation should assess: grammar, fluency, coherence, register, terminology, and the explicit warning that a detector outcome is not evidence of linguistic quality.

Per `NO-INVENTION-RULES.md`, this document does not select a specific linguistic-quality metric or tool. `R06` §58 registers no `R-XXXX` citation addressing fluency or linguistic-quality measurement for this project's transformation use case at all — this absence was noted explicitly by the research pass itself, not merely unaddressed by omission. Selecting a plausible-sounding metric here (a perplexity-based fluency score, a grammaticality classifier) would assert research grounding this project does not currently have.

**This document therefore records, rather than resolves, a genuine gap:** linguistic-quality measurement (`FID-013`–`FID-015`) has no `R-XXXX` grounding in the current corpus. Per `FID-043` (Missing Evidence), any validation run must report this dimension as `not measurable` until a dedicated literature pass or project-internal study establishes a specific method, language-aware per `FID-027`/`TRN-018`. This gap is a candidate for `docs/00-project/KNOWLEDGE-BACKLOG.md`; recording it there is a separate step this document does not take unilaterally.

---

# 8. Minimality and Transformation Budget (`VALIDATION-MAP.md` §20–21)

## 8.1 Minimality Is Constraint-Satisfaction, Not a Primary Objective

Per `FID-057` (Minimality versus Fidelity) and `TRN-008` (Preservation Priority), the governing optimization order is: (1) satisfy hard preservation constraints, (2) avoid unacceptable linguistic/structural degradation, (3) minimize unnecessary transformation, (4) optimize secondary objectives. A transformation that changes fewer tokens but damages meaning is not preferred — minimality must never override fidelity.

This ordering is not an abstract preference; `R06` §58.1 found it is how the literature that actually measures this trade-off already frames the problem:

> DEPO (`R-0074`) frames semantic preservation as an explicit constraint (BERTScore ≥ 0.85) in a constrained optimization, rather than a scalarized soft objective, and shows naive linear-weighting baselines fail to satisfy the constraint. **No evidence found** of any paper whose stated objective is literally "minimize edit distance subject to evasion success" — the closest work uses a semantic-similarity floor or an explicit deletion-percentage knob (`R-0075`) instead of edit-distance minimization per se.

**Protocol requirement:** minimality must be implemented as a secondary objective evaluated only among candidates that already satisfy the applicable hard constraints (§3–6 above), per `TRN-009`/`TRN-010` (Hard Constraints / Soft Objectives) — never as a scalarized term traded off directly against fidelity in a single combined score.

## 8.2 Minimality Metrics (`VALIDATION-MAP.md` §20)

Per `VALIDATION-MAP.md` §20 and `FID-037`'s metric-diversity requirement applied to this dimension, no single metric defines minimality universally. Required, reported together:

- character and token edit distance;
- changed-token ratio and changed-sentence ratio;
- lexical substitution rate;
- structural change rate (§6 above);
- semantic deviation (§3 above).

## 8.3 Transformation Budget (`VALIDATION-MAP.md` §21, `TRN-011`, `FID-022`)

Where an experiment defines a transformation budget, it must be explicit and versioned (`FID-088`), expressed in one or more of: maximum changed tokens, maximum changed sentences, maximum structural changes, maximum semantic deviation. Per `TRN-011`, a budget is a configurable constraint, **not proof of fidelity** — satisfying a budget does not substitute for passing §3–6's preservation checks.

## 8.4 Reporting the Minimality/Fidelity Trade-off as a Trade-off

`R06` §58.5 is this project's strongest evidence in the entire literature pass, and it is a trade-off finding, not a single-number result:

> **The Mark Fades** (`R-0075`, peer-reviewed, *Findings of ACL 2026*): genetic-algorithm Pareto-front optimization of watermark removal; near-100% attack success at BERTScore 0.73–0.77 (moderate), ASR ~97% but BERTScore collapsing to 0.56 at an aggressive 80%-deletion setting... **Cross-paper pattern (EVIDENCE tier, independently corroborated across `R-0074`/`R-0075`/`R-0076`/`R-0080` despite each individual number being AUTHOR-REPORTED):** aggressive evasion or obfuscation reliably buys detection/evasion success at a measurable, sometimes steep, quality cost, and RL/preference-optimization method choice measurably shifts the operating point on that trade-off.

Per `FID-040` (Pareto Evaluation), this project's reports must therefore present the minimality/fidelity relationship as an explicit multi-objective curve (minimality on one axis, the relevant fidelity dimension(s) from §3–6 on the other) rather than collapsing it into one score — consistent with how the corroborating literature itself reports it.

---

# 9. Governance & Traceability

1. **No Post-Hoc Metric or Threshold Selection:** per `FID-097`/`FID-098`, the metrics and thresholds applicable to a given experiment (§3.1, §8.2) must be declared before evaluating the final result. Changing them afterward to favor a result is prohibited under `P00-project-governance.md` §9 (`I-001`), the same rule `STATISTICAL-VALIDATION-METHODOLOGY.md` §8.1 applies to statistical methodology.
2. **Hard Constraints Take Priority:** per `FID-041`/`FID-042` and `TRN-009`/`TRN-010`, no secondary objective — minimality included — may override a violated hard constraint (unauthorized factual, numerical, entity, or structural change).
3. **Missing Evidence Is Reported, Not Hidden:** per `FID-043`, the claim-tier factual dimension outside English (§4.2) and the entire linguistic-quality dimension (§7) must be reported as `not measurable`/`unsupported` wherever the underlying capability has not reached `VALIDATED`, rather than silently defaulted to a pass or omitted from the report.
4. **Raw Measurements Are Preserved:** per `EVALUATION-ARCHITECTURE.md` §6, the per-dimension measurements this document defines (not only an aggregate fidelity verdict) must be retained in the experiment record, consistent with `FID-047`'s prohibition on an aggregate concealing a hard-constraint violation.
5. **Preservation Before Optimization:** per `FID-094`, the conceptual execution order for any transformation experiment is PRESERVE → VERIFY → MEASURE CHANGE → EVALUATE EXPERIMENTAL OBJECTIVE → REPORT. This document's protocols (§2–7) implement PRESERVE/VERIFY/MEASURE CHANGE; `VALIDATION-GATES.md` (Tranche 4, candidate) will formalize the transition criteria that consume their output.
