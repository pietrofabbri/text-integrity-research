# Knowledge Backlog

## Purpose

This document captures potentially relevant ideas, observations,
hypotheses, concerns, research findings and design proposals that have
not yet been fully classified or incorporated into the project.

Nothing important should be lost merely because its final location
is not yet known.

---

# Statuses

Each item may have one of the following statuses:

- UNTRIAGED
- TRIAGED
- INCORPORATED
- DUPLICATE
- REJECTED
- SUPERSEDED
- DEFERRED

---

# Priority

- CRITICAL
- HIGH
- MEDIUM
- LOW

---

# Item Template

## KB-XXX — Title

### Source

Where the idea originated.

### Observation

What was observed.

### Proposal / Hypothesis

What might follow from the observation.

### Potential Impact

Which parts of the project may be affected.

### Candidate Areas

Potential documentation areas.

### Related Research

Relevant research identifiers.

### Related Decisions

Relevant decision identifiers.

### Status

UNTRIAGED

### Priority

MEDIUM

### Required Action

What should eventually happen.

---

# Current Items

## KB-001 — Effectiveness Must Be Versioned

### Observation

The scientific landscape around watermarking, provenance and AI-content
detection changes over time.

### Proposal

Effectiveness must be defined through versioned evaluation profiles rather
than through a permanent binary claim.

### Potential Impact

- Research
- Scientific Specification
- Validation
- Certification
- Release Governance

### Status

TRIAGED

### Priority

CRITICAL

---

## KB-002 — External Detector Results Are Evidence, Not Truth

### Observation

Third-party detectors may change behavior, thresholds or implementations.

### Proposal

External detector output must be represented as versioned evidence with
provider, timestamp, configuration and provenance metadata where possible.

### Potential Impact

- Validation
- External Evidence
- Research Registry
- Reproducibility

### Status

TRIAGED

### Priority

HIGH

---

## KB-003 — Capability Lifecycle Must Include Removal

### Observation

A continuously evolving system can accumulate obsolete components.

### Proposal

Every major component must have a lifecycle including deprecation,
retirement and removal.

### Potential Impact

- Architecture
- Development
- Operations
- Certification

### Status

TRIAGED

### Priority

HIGH

---

## KB-004 — Documentation Must Be Incrementally Maintainable

### Observation

New knowledge may invalidate or affect documents created earlier.

### Proposal

Use a project map, knowledge backlog, decision log, assumption registry,
open-question registry and documentation change queue.

### Status

TRIAGED

### Priority

CRITICAL

---

## KB-005 — Agent Must Perform Impact Analysis

### Observation

A new change may affect documents and components not explicitly named
in the original task.

### Proposal

Claude Code must perform repository-wide impact analysis before closing
a substantive change.

### Status

TRIAGED

### Priority

CRITICAL

---

## KB-006 — Runtime Must Be Independent of Generative AI Services

### Observation

The production runtime is intended to execute without requiring an
external generative AI service.

### Proposal

Separate development/maintenance intelligence from runtime execution.

### Status

TRIAGED

### Priority

CRITICAL

---

## KB-007 — Local Storage Is a Hard Constraint

### Observation

The project has approximately 30 GB available for local project assets.

### Proposal

Treat storage as a first-class engineering constraint.

### Status

TRIAGED

### Priority

HIGH

### Update (2026-09-12, Q-008 research pass)

A dedicated research pass (`docs/02-research/R09-local-deployment-
feasibility-research.md`, confirmed domain per DECISION-LOG.md DEC-013;
RESEARCH-REGISTRY.md R-0102-R-0121) found this constraint, while still
real, is **not the
binding limitation** for most of the project's local validation needs: a
lightweight multi-task stack (semantic similarity + multilingual
factual/entailment signal + a quantized general-purpose fallback model)
totals well under 10GB using only components with verified disk sizes.
The exception is AI-text detection, where the best-evidenced open detector
(Binoculars) alone costs ~28.87GB — nearly the entire budget. See KB-014
below and OPEN-QUESTIONS.md Q-008's updated evidence: for two of the
project's three local-validation sub-tasks, evidence quality — not
storage — is now the open constraint.

---

## KB-008 — Multilingual AI-Detection Evidence Is Thin for Most Target Languages

### Source

R04 literature research pass, 2026-08-23
(`docs/02-research/R04-ai-generated-text-detection-research.md` §39.4).

### Observation

Of the project's 13 target languages (SPECIFICATION-MAP.md §20), no
independently verified, non-vendor detection study was found during this
research pass for German, Italian, Portuguese, Russian, Japanese, Polish,
Dutch, Turkish, or Indonesian (9 of 13). The only multilingual-by-design
benchmarks found (M4, R-0019; BLUFF, R-0021) either lack extracted
per-language detail or have unverified figures. Commercial vendors claim
broad coverage without publishing checkable per-language studies.

### Proposal / Hypothesis

Multilingual detector capability states (SPECIFICATION-MAP.md §22) for
most of the 13 target languages should default to RESEARCH_ONLY or
NOT_SUPPORTED rather than any validated tier, until language-specific
evidence is found or produced. This is a literature-confirmed gap, not
merely an internal project assumption.

### Potential Impact

- Scientific Specification §20-22 (realistic initial capability-state
  assignment per language)
- Research (R05 — prioritize search effort on the 9 under-evidenced
  languages, or commission targeted evaluation)
- Certification (no language should be certified beyond what evidence
  supports)

### Candidate Areas

03-scientific-specification, 02-research (R05), 10-certification

### Related Research

R-0019, R-0021, R-0029

### Related Decisions

None yet — this is evidence, not a decision.

### Status

TRIAGED

### Priority

HIGH

### Required Action

When R05 (Multilingual and Linguistic Research) is populated, cross-check
against this gap; when 03-scientific-specification assigns initial
per-language capability states, do not assign beyond RESEARCH_ONLY for the
9 languages listed here without new evidence.

### Correction (2026-08-24, R05 literature pass)

The R05 pass (`docs/02-research/R05-multilingual-linguistic-research.md`
§47.1) found this observation **no longer holds as originally stated for
AI-text detection**: dedicated or benchmark-level detection evidence now
exists for all 13 target languages (see R-0046 through R-0060 for the
specific per-language sources). What still holds: evidence *depth* varies
enormously (mostly single-study or benchmark-inclusion-level, not
English-scale multi-lab convergence), and **watermarking** evidence (as
distinct from detection) remains thin for nearly every non-English
language — no dedicated per-language watermarking study was found for
German, Italian, Portuguese, Russian, Japanese, Polish, Dutch, or Turkish.
The original observation and proposal below are left intact for
traceability; they should be read together with this correction, not
in place of it. The practical revision: capability-state defaults
(SPECIFICATION-MAP.md §20-22) should be assessed per-language against the
specific evidence in R05 §47.1 rather than applying a uniform
RESEARCH_ONLY/NOT_SUPPORTED default across all 9 originally-flagged
languages — but watermarking capability states specifically should stay
conservative for nearly all non-English languages regardless of this
correction.

### Status (updated)

TRIAGED — corrected, not resolved; still requires 03-scientific-
specification action per DCQ-006.

### Update (2026-09-12, DCQ-006 propagation, per DECISION-LOG.md DEC-016)

`SPECIFICATION-MAP.md` §20 and §22 now carry evidence-cited notes
reflecting this correction (citing R-0046-R-0073). This is a cross-
reference, not the per-language capability-state assignment itself — that
remains separate implementation/validation work, so this item's
`Required Action` is not yet satisfied and the item remains `TRIAGED`.

### Further update (2026-09-12, DEC-018)

`SPECIFICATION-MAP.md` §22.1 now performs the per-language capability-
state assignment itself (documentation-default `RESEARCH_ONLY`/
`NOT_SUPPORTED` states, since no capability is yet project-implemented).
This satisfies this item's `Required Action` at the documentation level;
the item remains `TRIAGED` because the underlying evidence gaps
(uneven depth, several languages at benchmark-inclusion-only tier) are
unresolved research questions, not something a documentation update can
close.

---

## KB-009 — Unverified Secondary-Sourced Figures From R04 Literature Pass

### Source

R04 literature research pass, 2026-08-23
(`docs/02-research/R04-ai-generated-text-detection-research.md` §39.5).

### Observation

Several specific numeric claims surfaced during the R04 literature pass
could only be traced to secondary sources (e.g. Wikipedia, education-press
summaries) rather than confirmed directly against the primary paper's own
tables/body text: the R-0022 "61.3% false-positive rate" figure, a claimed
91.3%→27.8% accuracy drop after a humanizer tool, and a claim that Black
students are markedly more likely to be falsely flagged (attributed to a
Common Sense Media report not directly located). Additionally, BLUFF
(R-0021) has internally inconsistent language-count figures across
sources, and one paper (arXiv:2603.23146) was confirmed to exist but its
content could not be extracted.

### Proposal / Hypothesis

None of these should be cited as established fact in any normative
document (specification, validation, certification) until directly
verified against their primary source.

### Potential Impact

Research Registry accuracy; any future document citing R-0021/R-0022 or
these unverified figures.

### Candidate Areas

02-research, 00-project/RESEARCH-REGISTRY.md

### Related Research

R-0021, R-0022

### Resolution Update (2026-08-24, R05 literature pass)

The R-0022 "61.3% false-positive rate" item is now RESOLVED: the R05 pass
fetched the Liang et al. paper directly and confirmed the correct figure
is **61.22%** (the "61.3%" figure was a secondary-source rounding
artifact, not a fabrication, but was unconfirmed until this pass). See
the updated R-0022 registry entry.

**Second resolution (2026-08-24, R07 literature pass):** arXiv:2603.23146
was fetched and fully read (Pudasaini, Miralles-Pechuán, Lillis, Llorens
Salvador, "Why AI-Generated Text Detection Fails: Evidence from
Explainable AI Beyond Benchmark Accuracy") — now registered as R-0089.
Its content is no longer unextracted: it documents a leaderboard-
competitive detector (F1=0.9734) failing under cross-domain/cross-
generator evaluation via SHAP analysis. See R07 §80.2.

The remaining items (humanizer 91.3%→27.8% drop, the Common Sense Media
claim, BLUFF's inconsistent counts) remain unresolved.

### Status

TRIAGED — two of four unverified items resolved; two remain open

### Priority

MEDIUM

### Required Action

A follow-up research pass should fetch and directly read: (1) the Liang et
al. paper's results tables, (2) the BLUFF paper's full body text, (3) the
primary Common Sense Media report if it exists, (4) arXiv:2603.23146's
full text. Update RESEARCH-REGISTRY.md entries and this item's status once
done.

---

## KB-010 — Watermarking Field Confirms the Multilingual Evidence Gap (KB-008) and Adds Unverified Figures of Its Own

### Source

R02/R03 literature research pass, 2026-08-23
(`docs/02-research/R02-watermark-research.md` §37.4-37.5,
`docs/02-research/R03-watermark-detection-research.md` §43.6).

### Observation

The watermarking/watermark-detection literature pass independently confirms
KB-008's finding (evidence for multilingual robustness is thin for most of
the project's 13 target languages) via a different source: R-0044 found
existing multilingual watermarking methods fail to remain robust under
translation attacks in medium/low-resource languages, root-caused to
tokenizer subword fragmentation, with no verified logographic-script
(Chinese/Japanese) benchmark found. Separately, this pass surfaced its own
set of AUTHOR-REPORTED, not-yet-independently-verified numeric claims:
R-0040's specific attack-success percentages (piggyback spoofing >90%,
key-based removal 97%+, oracle attack ~3 queries/token), R-0041's
perplexity/MMLU cost figures (9%-2000%+ range, technique-specific), and
R-0044's proposed-fix improvement figures (+0.23 AUC, +37% TPR@1%FPR).
Additionally, two "detection without prior key knowledge" papers and four
other papers (WaterMax, a cross-lingual watermarking fairness audit,
BanglaLorica, an EMNLP 2025 tokenization-inconsistency paper) were
confirmed to exist and be on-topic but were not deep-read in this pass.

### Proposal / Hypothesis

(1) KB-008's proposed default (RESEARCH_ONLY/NOT_SUPPORTED capability
states pending language-specific evidence) should apply to watermarking
and watermark-detection capability states as well as AI-text-detection
ones — this is now a two-source-confirmed gap, not a single-domain
observation. (2) None of the R-0040/R-0041/R-0044 specific figures listed
above should be cited as established fact in any normative document until
independently verified against primary sources.

### Potential Impact

- Scientific Specification §20-22 (per-language capability states,
  watermarking-specific)
- Research (R03 §43.2 follow-up on key-agnostic detection; a dedicated
  pass to read the four not-yet-deep-read papers)
- Research Registry accuracy (R-0040, R-0041, R-0044)

### Candidate Areas

03-scientific-specification, 02-research (R02, R03, R05), 00-project/RESEARCH-REGISTRY.md

### Related Research

R-0040, R-0041, R-0044

### Related Decisions

None yet — this is evidence, not a decision.

### Status

TRIAGED

### Priority

MEDIUM

### Required Action

When R05 is populated, cross-check against this item alongside KB-008. A
follow-up pass should independently verify the R-0040/R-0041/R-0044
figures and deep-read the four identified-but-unread papers listed above
before any of their specific claims are relied upon.

---

## KB-011 — Translation-Based Evasion Is a Distinct, Materially Significant Attack Class Not Yet Reflected in R02/R03

### Source

R05 literature research pass, 2026-08-24
(`docs/02-research/R05-multilingual-linguistic-research.md` §47.3).

### Observation

The R02/R03 literature pass (2026-08-23) documented monolingual
paraphrasing (R-0039) as the dominant watermark-evasion method. The R05
pass found that translation-based evasion (round-trip translation,
translate-and-edit, or translation combined with summarization) is a
separately evidenced attack class, converged on by four independent
sources: CWRA/X-SIR (R-0065, AUC 0.95→0.67), "Uncovering the Hidden
Threat" (R-0066, AUC as low as 0.55-0.57, with a directionality effect —
into-English survives better than out-of-English), ESPERANTO (R-0068,
peer-reviewed, extends the finding to plain AI-detection, not just
watermarking), and the SynthID robustness study (R-0069, F1 0.711-0.819
depending on language). A fifth source, CLSA (R-0067), reports even more
dramatic near-chance AUROC collapse but is a single-author, non-peer-
reviewed, unreplicated preprint and should be weighted accordingly (kept
at INCONCLUSIVE status in the registry).

### Proposal / Hypothesis

R02 §37.2 (Robustness and Attack Evidence) should eventually name
translation-based evasion as a distinct category alongside paraphrasing,
and R03's detector-robustness discussion (§43.4) should note that
detectors and watermarks tested only against monolingual paraphrasing
have not been tested against this separate attack class. This is folded
into DCQ-006's existing scope (propagation pending 03-scientific-
specification/06-security moving past definition phase) rather than
treated as a new queue item.

### Potential Impact

- Research (R02 §6-7, R03 §25 — both currently silent on translation as
  a distinct attack vector)
- Security (06-security, once past definition phase — public
  translation-then-detect pipelines are a realistic, low-effort attack
  surface)

### Candidate Areas

02-research (R02, R03), 06-security

### Related Research

R-0065, R-0066, R-0067, R-0068, R-0069

### Related Decisions

None yet — this is evidence, not a decision.

### Status

TRIAGED

### Priority

MEDIUM

### Required Action

Fold into the R02/R03 update scoped under DCQ-006 when that work is
picked up; until then, any downstream document that asserts watermark or
detector robustness should not assume translation-based evasion has been
accounted for merely because paraphrasing robustness has been discussed.

### Update (2026-09-12, DCQ-006 propagation, per DECISION-LOG.md DEC-016)

`SPECIFICATION-MAP.md` §23 now carries a note citing R-0065/R-0066/
R-0068/R-0069 alongside R-0039, so downstream specification-level
robustness claims are on notice. The R02/R03 research-layer-internal
naming update (§37.2, §43.4) described above remains not yet performed —
this item's `Required Action` is not fully satisfied and it remains
`TRIAGED`.

---

## KB-012 — Factual-Consistency Metrics Are Unvalidated, and Certainty/Hedging Is an Unnamed Preservation Dimension

### Source

R06 literature research pass, 2026-08-24
(`docs/02-research/R06-transformation-preservation-research.md` §58.3,
§58.6).

### Observation

Two distinct gaps surfaced in the R06 pass. (1) An established factual-
consistency metric toolkit exists for summarization (FactCC, SummaC,
QAFactEval, AlignScore — R-0085), but no evidence was found of any of
these, or an LLM-as-judge factuality protocol, being applied specifically
to detector-evasion or watermark-removal paraphrasing — the toolkit and
this project's actual use case have not been bridged by any study found.
(2) A separate, rigorous paper (Belem et al., R-0078) measures certainty/
hedging distortion during LLM rewriting as a dimension explicitly distinct
from factuality — models inflate certainty 1.5-2x more often than they
deflate it, with domain-dependent compounding over iterative rewrites
(medical-domain: 20%→40% over 5 iterations for one tested model). This
dimension (does a rewrite silently change how certain a claim sounds,
independent of whether the claim itself became false) is not currently
named in R06 §3's preservation-dimension list (semantic, factual,
structural, linguistic, stylistic, terminological, numerical,
entity-level, formatting).

### Proposal / Hypothesis

(1) The project should not assume factual-preservation measurement is a
solved problem merely because tools exist elsewhere — a validation study
bridging FactCC/SummaC/QAFactEval/AlignScore (or an LLM-judge protocol)
to this project's transformation/evasion use case is required before any
is adopted as a fidelity metric. (2) Certainty/hedging preservation is a
candidate ninth-or-later preservation dimension for R06 §3 — this is
flagged as a candidate, not incorporated unilaterally, since changing the
project's core preservation-dimension taxonomy is a specification-level
decision.

### Potential Impact

- Research (R06 §7, §41 Factual Consistency; §3 Preservation Dimensions)
- Scientific Specification (S04-fidelity-requirements.md — a candidate
  new fidelity dimension; validation of factuality metrics before
  adoption)

### Candidate Areas

02-research (R06), 03-scientific-specification (S04-fidelity-requirements.md)

### Related Research

R-0078, R-0085

### Related Decisions

None yet — this is evidence, not a decision.

### Status

TRIAGED

### Priority

MEDIUM

### Required Action

When 03-scientific-specification's fidelity requirements (S04) are next
revisited, evaluate whether to add certainty/hedging as a named
preservation dimension, and do not treat FactCC/SummaC/QAFactEval/
AlignScore as validated for this project's use case without a bridging
study.

---

## KB-013 — No Evidence-Backed Multilingual Factual-Consistency Option Exists

### Source

Q-008 research pass, 2026-09-12
(`docs/02-research/R09-local-deployment-feasibility-research.md` §10.3).

### Observation

The strongest factual-consistency model found (MiniCheck, R-0109, within
0.6 points of GPT-4 on LLM-AggreFact) is explicitly English-only per its
own authors. The only open, small, genuinely multilingual candidate found
(mDeBERTa-v3-xnli, R-0111) has unverified task-fit — it is evaluated on
sentence-pair entailment (XNLI), a substantially easier and different task
than document-level factual-consistency checking. A separate peer-reviewed
study (mFACT, R-0112) found English faithfulness metrics do not transfer
well to other languages, directly undermining the assumption that an
English-trained checker could simply be used cross-lingually.

### Proposal / Hypothesis

The project should not assume a multilingual factual-consistency capability
exists merely because an English one does. This gap should be weighed
alongside KB-012's related finding (factual-consistency metrics generally
unvalidated for this project's transformation/evasion use case, even in
English) when 03-scientific-specification's fidelity requirements are next
revisited.

### Potential Impact

- Scientific Specification (S04-fidelity-requirements.md — realistic
  per-language capability-state assignment for factual preservation)
- Research (a bridging study evaluating mDeBERTa-v3-xnli, or an
  LLM-as-judge protocol, against the project's actual task, ideally
  multilingual)

### Candidate Areas

02-research (R09), 03-scientific-specification

### Related Research

R-0109, R-0110, R-0111, R-0112

### Related Decisions

None yet — this is evidence, not a decision.

### Status

TRIAGED

### Priority

MEDIUM

### Required Action

Do not assign a validated factual-consistency capability state to any
non-English language without new evidence bridging mDeBERTa-v3-xnli (or an
equivalent) to this project's actual task.

### Update (2026-09-12, DCQ-008 propagation, per DECISION-LOG.md DEC-016)

`S04-fidelity-requirements.md` FID-002 and `SPECIFICATION-MAP.md` §21-22
now carry notes citing this finding (R-0109-R-0112), and
`docs/04-architecture/VALIDATION-ARCHITECTURE.md` §6 (per `DECISION-LOG.md`
DEC-015) gives it an architectural consequence (`VALIDATE-FACTUAL-CLAIM`
ineligible for `VALIDATED` outside English). This is propagation of the
existing finding, not new evidence resolving it — the bridging study this
item's `Required Action` calls for has not been performed, so the item
remains `TRIAGED`.

### Further update (2026-09-12, DEC-018)

`SPECIFICATION-MAP.md` §22.1 now assigns `NOT_SUPPORTED` for this
capability across all 12 non-English target languages (English:
`RESEARCH_ONLY`), explicitly distinguishing "a candidate model exists"
from "an evidence-backed capability exists" per this item's own finding.
The bridging study remains not performed; the item remains `TRIAGED`.

---

## KB-014 — Local AI-Text Detection Is Bounded by Accuracy and Cross-Lingual Robustness, Not Storage

### Source

Q-008 research pass, 2026-09-12
(`docs/02-research/R09-local-deployment-feasibility-research.md` §10.4).

### Observation

Independent benchmarks confirm the local-detection sub-task's binding
constraint is not the ~30GB storage budget (KB-007). RAID (R-0113) found
accuracy at FPR=5% for the best open detector (Binoculars) at 79.6%, with
severe generalization collapse for a related architecture (96.3%→33.8%
from GPT-2 to GPT-4) and adversarial fragility (30-75 point losses to
simple attacks). M4GT-Bench (R-0118) found leave-one-language-out accuracy
for a trained multilingual detector collapses toward chance (~53%) for
Bulgarian, Russian and Indonesian, with the detector degenerating into
labeling nearly everything as machine-generated — a failure mode worse
than no detector. Separately, Binoculars itself (R-0117), the best-
evidenced open option, costs ~28.87GB (two 7B models) to run at full
precision — nearly the entire storage budget for this one sub-task — and
its quantization-compatibility is explicitly untested.

### Proposal / Hypothesis

No local AI-text-detection capability should be treated as validated
merely because a candidate model exists and fits (or can be made to fit)
the storage budget. Accuracy and cross-lingual robustness evidence must be
evaluated per candidate and per language, independent of the storage
question, before any local detection capability is assigned a validated
state (SPECIFICATION-MAP.md §20-22).

### Potential Impact

- Scientific Specification (per-language, per-capability detection
  capability states)
- Certification (10-certification, once past definition phase — bears
  directly on what detection claims could ever be certified)
- Research (a concrete, low-cost follow-up experiment: test whether a
  quantized Falcon-7B/Falcon-7B-Instruct pair preserves Binoculars'
  detection quality)

### Candidate Areas

02-research (R04, R09), 03-scientific-specification, 10-certification

### Related Research

R-0113, R-0114, R-0115, R-0116, R-0117, R-0118

### Related Decisions

None yet — this is evidence, not a decision.

### Status

TRIAGED

### Priority

HIGH

### Required Action

When a local detection component is scoped in 04-architecture, do not
select a candidate on storage-fit alone; require accuracy and
cross-lingual-robustness evidence per RAID/M4GT-Bench-style methodology
first.

### Update (2026-09-12, DCQ-008 propagation, per DECISION-LOG.md DEC-016)

`SPECIFICATION-MAP.md` §21-22 and `S02-scientific-requirements.md`
REQ-LANG-006 now carry notes citing this finding (R-0113-R-0118). The
`04-architecture` portion of this item's `Required Action` (a local
detection component being scoped) remains not applicable —
`ARCHITECTURE-MAP.md` and its sub-documents do not yet select any
candidate model, per `DECISION-LOG.md` DEC-016 point 3 — so this item
remains `TRIAGED`.

### Further update (2026-09-12, DEC-018)

`SPECIFICATION-MAP.md` §22.1 now assigns per-language `RESEARCH_ONLY`/
`NOT_SUPPORTED` states for AI-text detection, explicitly flagging Russian
and Indonesian's near-chance leave-one-language-out accuracy collapse
(R-0118) as a failure-mode caveat rather than treating them as merely
thin-evidence languages. The item remains `TRIAGED`.

---

## KB-015 — Quantization's Interaction With Multilingual Capability Is Unstudied

### Source

Q-008 research pass, 2026-09-12
(`docs/02-research/R09-local-deployment-feasibility-research.md` §10.5).

### Observation

The clearest evidence found on quantization quality trade-offs (R-0120,
peer-reviewed-track, downstream-benchmark evaluation, not perplexity
alone) shows moderate quantization (Q4_K_M) costs only ~1 MMLU point
relative to F16 for Llama-3.1-8B-Instruct. **All benchmarks used are
English-only**, and the paper explicitly does not test whether
quantization degrades multilingual performance faster than English
performance — the authors name this as an open question. Quantization is
known in general to affect distribution tails most, and non-English
capability in a primarily-English-trained model often lives in that tail,
making this a plausible, not merely theoretical, risk for this project's
13-language target.

### Proposal / Hypothesis

The project should not assume a quantized model's English-benchmark
quality retention (e.g. "Q4_K_M loses ~1 MMLU point") generalizes to its
non-English capability. This is a candidate for the project's own
targeted evaluation once a local-LLM component is scoped, rather than
something further literature search is likely to resolve, since the field
itself has not yet studied it.

### Potential Impact

- Research (a candidate project-run experiment: compare quantized vs.
  full-precision multilingual benchmark performance for any locally-run
  general-purpose model)
- Architecture (quantization-level defaults, once 04-architecture leaves
  definition phase, should not be chosen on English-only evidence alone
  if the component is used for non-English text)

### Candidate Areas

02-research (R09), 04-architecture

### Related Research

R-0119, R-0120, R-0121

### Related Decisions

None yet — this is evidence, not a decision.

### Status

TRIAGED

### Priority

MEDIUM

### Required Action

Flag as an open item for whichever future work scopes a local
general-purpose LLM component; do not select a quantization level based
solely on English-benchmark quality-retention figures.