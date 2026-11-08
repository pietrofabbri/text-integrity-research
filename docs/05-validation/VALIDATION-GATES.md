# Validation Gates

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Validation methodology and governance protocol (Tranche 4)
**Authority:** Validation (Primary for acceptance-threshold, release-validation, and evidence-package governance)
**Parent:** `docs/05-validation/VALIDATION-MAP.md` §44–46, §55–59, §73
**Requirements basis:** `docs/03-scientific-specification/S02-scientific-requirements.md` §11 (`REQ-STAT-001`–`007`), §14 (`REQ-PROV-001`–`003`), §13 (`REQ-REPRO-001`–`005`), §16 (`REQ-LIFE-001`–`005`), §21 (`REQ-VAL-001`–`003`)
**Research basis:** `docs/02-research/R07-evaluation-statistical-methodology.md` §80 (cited selectively below)
**Architectural basis:** `docs/04-architecture/CAPABILITY-ARCHITECTURE.md` §6–7 (lifecycle states, Activation Gate), `docs/04-architecture/EVALUATION-ARCHITECTURE.md` §6–8, 10
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-012, DEC-029, DEC-030, DEC-035 (the governing precedent for how this project handles unresolved vocabulary contradictions), DEC-036 (Tranche roadmap), DEC-037 (Tranche 2 precedent), DEC-039 (this document's execution)

---

# 1. Purpose & Scope

This document formalizes `VALIDATION-MAP.md` §44–46 (Acceptance Thresholds, Threshold Versioning, Confidence), §55–59 (Capability Validation Gate, Release Validation, Release Status, Certification Boundary, Evidence Package), and §73 (Validation Quality Gate).

It governs the point at which a capability's accumulated evidence is judged sufficient to change that capability's declared status — the gate itself — and the package of evidence that decision must leave behind. It does not itself decide any specific threshold value, benchmark, or metric for any capability; per `NO-INVENTION-RULES.md`, those remain decisions made elsewhere (the research layer, `STATISTICAL-VALIDATION-METHODOLOGY.md`, `FIDELITY-VALIDATION-PROTOCOL.md`, `DETECTOR-VALIDATION-PROTOCOL.md`), applied through the gate this document defines.

---

# 2. A Known, Deliberately Deferred Vocabulary Contradiction — Recorded, Not Resolved Here

This document's scope sits directly on top of a lifecycle/status-vocabulary contradiction that the project has already found, documented, and explicitly deferred. Per `NO-INVENTION-RULES.md`'s Ambiguous Information protocol (*"preserve both statements; identify the locations; do not silently select one"*) and its Historical Integrity principle (*"do not rewrite history to make the repository appear more coherent... historical contradictions are evidence"*), this document states the contradiction precisely rather than quietly adopting one vocabulary as if it were settled.

**Two vocabularies describe what appears to be the same underlying concept, and neither has been reconciled with the other:**

- `VALIDATION-MAP.md` §57 "Release Status": `NOT_EVALUATED, EXPERIMENTAL, CONDITIONALLY_VALIDATED, VALIDATED, DEGRADED, DEPRECATED, RETIRED`.
- `CERTIFICATION-MAP.md` §3 "Certification Levels": `UNTESTED, EXPERIMENTAL, VALIDATED, CERTIFIED, DEPRECATED, RETIRED`.

Both `VALIDATION-MAP.md` §55 and `CERTIFICATION-MAP.md` §3 cross-reference each other and state that which vocabulary is authoritative is a **HUMAN DECISION REQUIRED** item, citing `docs/99-backlog/CLAUDE-CONSOLIDATION-REPORT.md`, "SECOND PASS, §5S/§13S," as the source. That source exists and is exactly as cited: §5S ("Contradictions (second pass)") records this release-status pair alongside the lifecycle-state (`SPECIFICATION-MAP.md` §5 vs. `S02-scientific-requirements.md` §24) and network-mode (`SECURITY-MAP.md` §14 vs. `OPERATIONS-MAP.md` §136) vocabulary mismatches, and states plainly that none of the three "were classified by the audit as a scientific or security contradiction... they are terminology/vocabulary drift between documents describing related but not always identical state machines." §13S records that this item was already put to the owner and resolved — not by picking a vocabulary, but by explicit deferral: *"Resolved 2026-08-29 — see DEC-012... Owner confirmed all four items below by explicit answer, matching this report's own recommendations: defer vocabulary reconciliation..."* `DECISION-LOG.md` DEC-012 is that decision: *"deferred until 04-architecture through 10-certification leave structural-definition phase. The cross-references added 2026-08-29 stand as the interim state — divergence documented and traceable, not unified."*

This document's scope (05-validation) has now left structural-definition phase with the completion of this four-tranche roadmap, but `06-security` through `10-certification` have not — so DEC-012's own stated trigger for revisiting the reconciliation ("until 04-architecture through 10-certification leave structural-definition phase") is not yet met project-wide. This document therefore continues DEC-012's deferral rather than treating 05-validation's own completion as sufficient grounds to force a reconciliation.

**A third vocabulary, not flagged in `CLAUDE-CONSOLIDATION-REPORT.md` §5S alongside the other three term families (lifecycle-state, network-mode, release-status), though that section does separately note "8–10 non-identical capability-lifecycle enumerations scattered across the corpus" without itemizing them file-by-file:** `CAPABILITY-ARCHITECTURE.md` §6 defines a capability lifecycle of `DISCOVERED → EXPERIMENTAL → VALIDATED → ACTIVE → DEPRECATED → RETIRED` (with a `DEGRADED` branch from `ACTIVE`). This shares `EXPERIMENTAL`, `VALIDATED`, `DEGRADED`, `DEPRECATED`, `RETIRED` with `VALIDATION-MAP.md`'s vocabulary, and `EXPERIMENTAL`/`VALIDATED`/`DEPRECATED`/`RETIRED` with `CERTIFICATION-MAP.md`'s, but adds `DISCOVERED` and `ACTIVE`, which neither other vocabulary has. This document records that fact explicitly: there are at least three partially-overlapping, never-fully-reconciled lifecycle vocabularies in the current corpus (`VALIDATION-MAP.md` §57, `CERTIFICATION-MAP.md` §3, `CAPABILITY-ARCHITECTURE.md` §6), plus a fourth, structurally identical instance of the same pattern at the requirement level (`S02-scientific-requirements.md` §24 vs. `SPECIFICATION-MAP.md` §5).

**How this document proceeds given the above:** consistent with DEC-012's own deferral and with `DECISION-LOG.md` DEC-029 (which recorded a related contradiction without resolving it) and DEC-030 (which resolved a narrower, adjacent question while explicitly declining to resolve the broader one), this document adopts `VALIDATION-MAP.md`'s own vocabulary (`NOT_EVALUATED, EXPERIMENTAL, CONDITIONALLY_VALIDATED, VALIDATED, DEGRADED, DEPRECATED, RETIRED`) for the remainder of its text, because this document's Parent is `VALIDATION-MAP.md` itself — not because that vocabulary has been determined to be authoritative over `CERTIFICATION-MAP.md`'s or `CAPABILITY-ARCHITECTURE.md`'s. Wherever this document says `VALIDATED`, a reader applying `CERTIFICATION-MAP.md`'s or `CAPABILITY-ARCHITECTURE.md`'s own vocabulary to the same capability must not assume the terms are interchangeable without checking which document's state machine actually governs that capability. This document does not pick a winner; per DEC-012, the reconciliation itself is deliberately deferred, not undecided-by-default, and should be revisited once `06-security` through `10-certification` also leave structural-definition phase — at which point the newly-identified third (`CAPABILITY-ARCHITECTURE.md` §6) and fourth (`S02-scientific-requirements.md` §24 / `SPECIFICATION-MAP.md` §5) vocabulary pairs should be folded into that same reconciliation decision.

---

# 3. Acceptance Thresholds and Threshold Versioning (§44–45)

Per `VALIDATION-MAP.md` §44: thresholds must be justified by research evidence, benchmark distributions, domain requirements, error costs, and statistical analysis — arbitrary thresholds must not be presented as scientific facts. Per §45, every threshold must carry an identifier, version, rationale, source, date, affected capabilities, affected languages, and replacement history; changing a threshold may change certification status.

This document does not itself fix any threshold value — per `NO-INVENTION-RULES.md`'s Numerical Values rule (*"Never invent: thresholds... confidence levels; performance targets. If a value is not documented, report it as unspecified"*), threshold values are set by the capability-specific protocols (`STATISTICAL-VALIDATION-METHODOLOGY.md`, `FIDELITY-VALIDATION-PROTOCOL.md`, `DETECTOR-VALIDATION-PROTOCOL.md`) and carried into the gate below unchanged. What this document requires is that every such threshold, wherever set, be versioned per §45's six fields before it is used in a gate decision under §4.

`R07-evaluation-statistical-methodology.md` §80.1 (`R-0086`) supplies the mathematical grounding for why a threshold cannot be evaluated in isolation from base-rate: *"a Bayes'-theorem base-rate argument showing that FPR/accuracy alone is mathematically meaningless without knowing the (typically unknown, low) real-world prevalence of AI-generated text."* Any acceptance threshold expressed as an FPR or accuracy figure must be accompanied by the prevalence assumption it was evaluated under (already required by `REQ-STAT-004`'s DCQ-007 note), or it does not satisfy this section.

---

# 4. The Capability Validation Gate (§55) and the Activation Gate

`VALIDATION-MAP.md` §55 states that a capability may progress from `EXPERIMENTAL` to `VALIDATED` only when nine conditions hold: its objective, inputs/outputs, evidence, benchmark, and metrics are defined; its limitations are known; its regression tests exist; its dependencies are documented; its reproducibility status is known.

**This document does not duplicate `CAPABILITY-ARCHITECTURE.md` §7's Activation Gate — it names it as the mechanism that already implements this requirement.** §7's six-point test (a capability record exists; its declared validation requirements have been run and passed; its scientific sources include at least one entry not solely `UNVERIFIED`; dependency verification succeeds; regression tests and documentation exist; licensing has been checked) is, point for point, a concrete operationalization of §55's nine conditions. A capability that passes `CAPABILITY-ARCHITECTURE.md` §7's Activation Gate has, by construction, satisfied `VALIDATION-MAP.md` §55's gate for the purposes of that document's own (`DISCOVERED → EXPERIMENTAL → VALIDATED`) vocabulary — but see §2 above: this equivalence is stated at the level of *gate mechanics*, not as a claim that `CAPABILITY-ARCHITECTURE.md`'s `VALIDATED` and `VALIDATION-MAP.md`'s `VALIDATED` are formally the same status, since the two vocabularies have never been reconciled.

The Activation Gate's regression-test condition (point 5) is itself implemented downstream by `EVALUATION-ARCHITECTURE.md` §7 (Regression Analysis), which distinguishes pass/fail regression (`VALIDATION-ARCHITECTURE.md` §12) from measured-performance-change regression (its own concern) — a capability can remain validated under the former while the latter shows decline, which is exactly the condition `CAPABILITY-ARCHITECTURE.md` §6's `DEGRADED` state exists to capture. This document requires that a `DEGRADED` determination always be traceable to a specific `EVALUATION-ARCHITECTURE.md` §7 regression-analysis result, never asserted without one.

---

# 5. Release Validation and Release Status (§56–57)

Per `VALIDATION-MAP.md` §56, a release should be validated against a declared evaluation profile specifying required capabilities, supported languages, datasets, benchmarks, thresholds, detector versions where applicable, mandatory regression tests, and resource constraints. Per §57, release states are `NOT_EVALUATED, EXPERIMENTAL, CONDITIONALLY_VALIDATED, VALIDATED, DEGRADED, DEPRECATED, RETIRED` — the vocabulary this document adopts per §2 above.

This document does not populate a concrete evaluation profile (per `VALIDATION-ARCHITECTURE.md` §15's own disclaimer, which this document inherits: no metric, threshold, or specific validation profile is selected here). It requires that any release-status determination name the evaluation profile it was checked against, by identifier and version, rather than asserting a release status without a traceable profile.

---

# 6. Certification Boundary and Evidence Package (§58–59)

Per `VALIDATION-MAP.md` §58: *"Validation determines evidence. Certification determines whether the evidence satisfies a declared release profile. These must remain separate."* This document is the validation side of that boundary; `CERTIFICATION-MAP.md` governs the certification side, under its own (separately-vocabularied, per §2 above) state machine. This document does not define certification criteria or certification states — only the evidence package certification would consume.

Per `VALIDATION-MAP.md` §59, a certification evidence package should contain: software version, capability registry snapshot, dataset versions, model versions, evaluation profiles, benchmark results, regression results, known failures, known limitations, external-service observations, and reproducibility information.

This document requires that every item in that list trace to a specific artifact already defined elsewhere, rather than restating or re-defining any of them:

- Benchmark results, regression results, and external-service observations are produced under `DETECTOR-VALIDATION-PROTOCOL.md` (Tranche 3) and `FIDELITY-VALIDATION-PROTOCOL.md` (Tranche 2), using the Minimum Experiment Record schema already defined in `STATISTICAL-VALIDATION-METHODOLOGY.md` §7 (Tranche 1), which that document states satisfies `VALIDATION-MAP.md` §66 and `EVALUATION-ARCHITECTURE.md` §7.
- Raw measurements underlying any benchmark or regression result must be preserved separately from derived scores, per `EVALUATION-ARCHITECTURE.md` §6 (*"derived scores must never replace the underlying observations"*) — this is the same raw-measurement-preservation discipline `DETECTOR-VALIDATION-PROTOCOL.md` §10 and `FIDELITY-VALIDATION-PROTOCOL.md` §9 already require; this document does not restate it a third time, only confirms it is a precondition for a valid evidence package.
- Known failures and known limitations must be reported using the `not measurable`/`unsupported`/`not applicable` three-state discipline of `VALIDATION-ARCHITECTURE.md` §9, not omitted.
- Reproducibility information follows `REQ-REPRO-001`–`005`, including the explicit acknowledgment (`REQ-REPRO-005`) that external-service mutability may make exact reproduction impossible — an evidence package is not deficient merely because an external-service-dependent result cannot be exactly reproduced, provided that limitation is disclosed.

**Citation-precision note, carried forward rather than silently corrected:** `STATISTICAL-VALIDATION-METHODOLOGY.md` §8 cites `EVALUATION-ARCHITECTURE.md` §9 for raw-measurement preservation; the section that actually defines this is `EVALUATION-ARCHITECTURE.md` §6 (§9 there is a non-binding illustrative example). This document flags the discrepancy rather than silently fixing another document's citation; correcting it is left to a future editing pass of `STATISTICAL-VALIDATION-METHODOLOGY.md` itself.

---

# 7. Confidence and Uncertainty Propagation (§46–47)

Per `VALIDATION-MAP.md` §46: validation results must distinguish `pass`, `fail`, `inconclusive`, `unavailable`; where a probability or confidence score exists, its meaning must be documented. Per §47: uncertainty should propagate through the evaluation pipeline — a highly uncertain analytical result must not become a definitive downstream conclusion merely because the system converts it to a Boolean.

`R07-evaluation-statistical-methodology.md` §80.4–80.5 is directly relevant and must be carried forward with its own stated tension intact, not smoothed into a single narrative: formal statistical guarantees exist for watermark false-positive control under idealized conditions (`R-0093`, `R-0094`, `R-0095`), while a separate, independently-evidenced finding (`R-0097`) shows real deployed watermarking schemes (KGW, Unigram, SynthID) fail forensic (Daubert) admissibility standards in practice, with 100% conditional removal after paraphrasing and 70–83% pre-attack false-negative rates in that study, and that SynthID's own confidence signal was unreliable 80% of the time on unambiguous ground truth in the same study. `R07` §80.4 states directly: *"The theory... and the practice... are both real findings... and should not be collapsed into a single narrative."* A confidence value reported under this protocol must not imply the formal guarantees of `R-0093`–`R-0095` apply unconditionally to a deployed system's real-world behavior, given `R-0097`'s contrary finding.

**Evidence gap, recorded rather than filled:** `R07` §80.5 and §80.7 record that no formal ECE/reliability-diagram study and no field-specific evidence for pseudoreplication correction or effect-size/practical-significance reporting were found; those items rest on general statistical principle rather than domain-specific evidence, and this document does not invent domain-specific studies to ground them further.

---

# 8. Validation Quality Gate (§73)

Per `VALIDATION-MAP.md` §73, before publishing or relying on a major scientific conclusion, the following must be verified: correct dataset, correct language, correct versions, no obvious leakage, appropriate controls, appropriate sample size, appropriate metrics, uncertainty reported, limitations reported, competing explanations considered.

This is the final check this document requires before any gate decision in §4–6 is acted on. It is a checklist, not a new measurement protocol; the measurements it checks are produced by Tranches 1–3. `R07` §80.6's recommendation — *"fix a primary-metric convention... before comparing results across... future experiments, rather than inheriting the field's fragmentation"* — is the governing instance of "appropriate metrics" for this project specifically, already adopted as the TPR@fixed-FPR convention since Tranche 1.

---

# 9. Governance & Traceability

This document does not resolve the vocabulary contradiction recorded in §2; that remains a HUMAN DECISION REQUIRED item, exactly as `DECISION-LOG.md` DEC-012 deferred it. Any future reconciliation of `VALIDATION-MAP.md` §57, `CERTIFICATION-MAP.md` §3, and `CAPABILITY-ARCHITECTURE.md` §6 must be recorded as its own decision, not inferred from this document's choice (§2) to write its own text in `VALIDATION-MAP.md`'s vocabulary.

No threshold, evaluation profile, or evidence-package content produced under this document may be selected post-hoc to favor a particular release or certification outcome (`NO-INVENTION-RULES.md` Forbidden Behaviors).

This document closes the four-tranche `05-validation` roadmap `VALIDATION-MAP.md` §76 established under `DECISION-LOG.md` DEC-036. With this document, all four candidate sub-documents named in that roadmap (`STATISTICAL-VALIDATION-METHODOLOGY.md`, `FIDELITY-VALIDATION-PROTOCOL.md`, `DETECTOR-VALIDATION-PROTOCOL.md`, `VALIDATION-GATES.md`) are drafted and active; `06-security` through `10-certification` remain the project's largest outstanding structural-definition gap.
