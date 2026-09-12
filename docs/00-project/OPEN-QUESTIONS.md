# Open Questions

## Purpose

This document records unresolved questions.

An unresolved question must not be silently converted into an assumption,
requirement or implementation decision.

---

# Statuses

- OPEN
- UNDER_RESEARCH
- BLOCKED
- RESOLVED
- SUPERSEDED

---

# Template

## Q-XXX — Title

### Question

What remains unresolved?

### Why It Matters

Impact on project.

### Relevant Areas

Affected macroareas.

### Current Evidence

What is currently known.

### Possible Answers

Known alternatives.

### Blocking

YES / NO

### Owner

Human / Claude Code / Research

### Status

OPEN

---

# Initial Questions

## Q-001 — What constitutes sufficient semantic equivalence?

Status: OPEN

The project requires extremely high source fidelity, but the exact
multidimensional metric has not yet been finalized.

### Current Evidence (added 2026-08-24)

R06 §58.2 found that the literature itself has no standardized answer:
DIPPER (R-0024) uses P-SP at a 0.76 threshold, DEPO (R-0074) uses
BERTScore F1 at 0.85, StealthRL (R-0076) uses E5 cosine similarity *and*
an LLM-as-judge Likert scale that visibly disagree with each other on the
same outputs (0.901 embedding similarity vs. 2.64/5 LLM-judge rating).
This is not merely an unanswered question this project hasn't gotten to
— it is a genuine, unresolved methodological problem in the field it is
drawing from. No amount of further literature search will hand this
project a single validated threshold; the field has not converged on one.

### Possible Answers (not yet decided)

(a) Adopt one metric (e.g. BERTScore, being the most widely reused across
R-0074/R-0075/R-0080) as the project's own primary metric and document
the choice as a project decision, not a literature-derived fact; (b)
require multiple metrics to agree within a band before accepting
"sufficient" equivalence, following R06 §27's own principle that no
single metric should define preservation universally; (c) use a
task-based/extrinsic protocol (per R-0083's reading-comprehension
approach) instead of a similarity score. None of these has been decided.

---

## Q-002 — How should conflicting external detector evidence be represented?

Status: OPEN

Different detectors may disagree, use different thresholds or measure
different phenomena.

### Current Evidence (added 2026-08-24)

R07 §80.3/§80.5 (R-0090, Van Vlasselaer et al., peer-reviewed, 2026)
directly evidences this problem rather than just anticipating it: an
independent 4-tool test (GPTZero, Pangram, Copyleaks, Turnitin) on 160
ground-truthed documents found Turnitin scoring 100% false-negative on
fully-AI papers while Pangram scored far higher on the same documents,
with confidence-score outputs inconsistently calibrated across tools
(Turnitin ~0%, GPTZero median <20%, Pangram closest to the true 100%
value on known-AI text). R07 §80.6 (R-0091, R-0092) adds that published
detector rankings vary by dataset/metric choice even before considering
disagreement on a single document. This confirms RESEARCH-MAP.md §22's
existing principle (contradictory evidence must be preserved, not
resolved by picking the favorable result) is directly load-bearing here,
not a theoretical concern.

### Possible Answers (not yet decided)

(a) Report per-tool results individually rather than an aggregate/
majority verdict, with each tool's version and test date (R03 §16-17,
Cloud/External Detectors, Detector Drift); (b) treat disagreement itself
as a signal (e.g., flag for human review whenever tools disagree, rather
than forcing a resolution); (c) do not present any single external
detector's output as ground truth in the certification-relevant path.

---

## Q-003 — What minimum evidence is required before a capability enters production?

Status: OPEN

### Current Evidence (added 2026-08-24)

R07 §80.1 (R-0086, Bassett et al., peer-reviewed, 2026) supplies a formal
argument directly relevant to this question: a detector's false-positive
rate alone is mathematically insufficient to judge production-readiness
— the same FPR yields a 97.5% or a 47.6% real-world correctness rate
depending purely on the (typically unknown) prevalence of AI-generated
text in the deployment population. This means "minimum evidence" cannot
be defined as a threshold on a single metric (accuracy, FPR, or AUROC)
without also requiring an estimate of deployment-population prevalence —
a requirement not yet reflected in SPECIFICATION-MAP.md §25-26.
Separately, KB-008/KB-010 establish that evidence depth varies enormously
by language and by capability (detection vs. watermarking), so a single
project-wide evidence bar would either be too permissive for
under-evidenced languages or too strict for well-evidenced ones.

### Possible Answers (not yet decided)

(a) Require, for each capability/language pair, both a performance
metric (TPR@fixed-FPR per R07 §80.1) and a documented estimate or
plausible range of deployment prevalence before production release; (b)
default to RESEARCH_ONLY for any capability/language pair without
independently verified (not vendor-only) evidence, per KB-008's original
proposal; (c) require a minimum evidence *class* (per NO-INVENTION-RULES —
at least RESEARCH EVIDENCE, not merely INFERENCE or PROPOSAL) rather than
a numeric threshold.

---

## Q-004 — How should multilingual validation thresholds vary by language?

Status: OPEN

### Current Evidence (added 2026-08-23, corrected 2026-08-24)

A first literature pass (R04 §39.4, R02 §37.4; see KB-008, KB-010) found
no independently verified, non-vendor AI-detection or watermarking study
for 9 of the project's 13 target languages (German, Italian, Portuguese,
Russian, Japanese, Polish, Dutch, Turkish, Indonesian).

A second pass (R05 §47.1, see KB-008's Correction note) found this no
longer holds for AI-text *detection* specifically — dedicated or
benchmark-level detection evidence now exists for all 13 languages, at
varying depth (mostly single-study or benchmark-inclusion-level, not
English-scale multi-lab convergence). **Watermarking** evidence remains
thin for nearly every non-English language regardless. The practical
constraint on this question is now: a validated detection threshold could
plausibly be derived, with appropriate caution about evidence depth, for
most of the 13 languages; a validated watermarking threshold currently
cannot be derived from independent evidence for almost any of them.

---

## Q-005 — What is the optimal representation of minimality?

Status: OPEN

### Current Evidence (added 2026-08-24)

R06 §58.1 found that the strongest recent work (DEPO, R-0074) frames
minimality/preservation not as a magnitude to minimize (edit distance,
token-count change) but as a **hard constraint** a transformation must
satisfy (e.g., BERTScore ≥ 0.85) while optimizing a separate primary
objective — and that naive linear-weighting approaches (treating
minimality as one term in a weighted sum) empirically fail to satisfy the
constraint reliably. **No evidence found** of any paper whose objective
is literally "minimize edit distance subject to success" — the field has
moved toward constraint-based framings rather than distance-minimization
ones.

### Possible Answers (not yet decided)

(a) Represent minimality as a constraint (a preservation-metric floor a
transformation must clear) rather than a magnitude to minimize,
following the DEPO precedent; (b) represent it as an explicit Pareto
trade-off dimension (R06 §20, §54) rather than a single number, given
R-0075/R-0076/R-0080's convergent finding that transformation
strength and preservation move in opposite directions; (c) representation
may need to differ by transformation family (R06 §16) rather than have
one universal answer.

---

## Q-006 — How should detector/model drift be detected and recorded?

Status: OPEN

### Current Evidence (added 2026-08-24)

Two independent findings confirm drift is an active, not theoretical,
concern. R07 §80.3 (R-0090) found a single independent study already
surfaces meaningful cross-tool and (by implication) cross-version
disagreement for commercial detectors that are updated on vendor
schedules the project cannot control (R03 §17, Detector Drift). R07
§80.4 (R-0097, Tamim & Khan) found that real deployed watermark schemes
(KGW, Unigram, SynthID) fail forensic robustness tests at rates that
would very plausibly change as vendors patch these schemes — meaning
"detector/model drift" in this project's sense should explicitly include
watermark-scheme drift, not just AI-text-detector drift, since both are
externally-controlled, versioned, actively-updated systems.

### Possible Answers (not yet decided)

(a) Record a mandatory version/date stamp with every external
detector or watermark-scheme evaluation (already required by R03 §16,
§39, Temporal Evaluation) and treat any evaluation without one as
non-comparable to a later one; (b) schedule periodic re-evaluation of
externally-controlled tools/schemes rather than treating a one-time
evaluation as durable; (c) this may require its own dedicated
research/monitoring process (a "watch registry" per RESEARCH-MAP.md §36)
rather than a one-time documentation decision.

---

## Q-007 — Which datasets can be distributed legally within the project?

Status: OPEN

### Current Evidence (added 2026-08-24)

A first literature pass (R08 §69.1; see RESEARCH-REGISTRY.md R-0016,
R-0020, R-0049, R-0088, R-0099) found: RAID is MIT-licensed, HC3 is
CC-BY-SA-4.0 (but inherits the *stricter* of its own license or any
source dataset's license), MULTITuDE/v2 is CC-BY-4.0, ARB is Apache-2.0
(but explicitly disclaims responsibility for its own source corpora's
licensing terms, some of which are undeclared). M4 and DetectRL state no
license anywhere checked. The officially licensed TOEFL-essay corpus
(ETS/LDC2014T06) is gated behind a paid LDC license and not freely
redistributable — notably, the field's most-cited detector-bias study
(R-0022) did not use this corpus at all, instead scraping essays from a
public forum without a stated license or consent process. This does not
resolve the question but establishes: (1) a benchmark's own top-line
license is not sufficient evidence of distributability without checking
its source-corpus chain, and (2) at least RAID, MULTITuDE, and (with
caveats) HC3 and ARB appear distributable under their stated terms,
pending a legal read of the source-corpus chains this pass could not
perform.

---

## Q-008 — Which local models can provide sufficient validation quality
within the storage/resource budget?

Status: OPEN

### Current Evidence (added 2026-08-24)

None of the eight literature-research passes completed so far (R01-R08)
specifically investigated locally-deployable model sizes, quantization
trade-offs, or resource footprints for the validation tasks this project
needs (semantic-similarity scoring, factual-consistency checking,
detection). This is an explicit, confirmed gap — recorded here rather
than answered by inference from adjacent findings — and is a strong
candidate for a dedicated future research task, since KB-007's ~30GB
storage constraint (docs/00-project/KNOWLEDGE-BACKLOG.md) makes this a
concrete engineering question the project will need to answer before
04-architecture can leave its definition phase.

### Current Evidence (added 2026-09-12, targeted research pass)

A dedicated research pass now fills the gap noted above. Full findings,
with citations, are in the confirmed research domain document
`docs/02-research/R09-local-deployment-feasibility-research.md` (domain
confirmed 2026-09-12 per `DECISION-LOG.md` DEC-013 — see `RESEARCH-MAP.md`
§38); 20 new sources are registered as `R-0102`-`R-0121`
in `RESEARCH-REGISTRY.md`. Headline finding: **the question as originally
posed conflates two questions with different answers.** Storage is
comfortably sufficient for a lightweight multi-task stack (an illustrative,
non-exhaustive combination of small, EVIDENCE-sized components totals well
under 10GB against the ~30GB budget — R09 §10.1) — *except* that the
best-evidenced open AI-text detector (Binoculars, R-0117) alone costs
~28.87GB, nearly the entire budget. Quality, not storage, is where the
open questions actually are: (1) semantic similarity is well solved by a
small model (multilingual-e5-large-instruct, R-0103, ~1.14GB, independently
ranked #1 on MMTEB ahead of 7B-class models — R-0106); (2) factual
consistency has a strong English-only solution (MiniCheck, R-0109, within
0.6 points of GPT-4) but **no evidence-backed multilingual option** — the
only open multilingual candidate (mDeBERTa-v3-xnli, R-0111) has unverified
task-fit, and a separate study (mFACT, R-0112) shows English factuality
metrics do not transfer cross-lingually; (3) AI-text detection is bounded
by accuracy and cross-lingual robustness, not storage — independent
benchmarks (RAID, R-0113; M4GT-Bench, R-0118) show open detectors either
collapse toward chance accuracy on several target languages or cost nearly
the entire storage budget for the one detector that performs well, with
its quantization-compatibility explicitly untested.

### Possible Answers (not yet decided)

(a) Split this question into a storage sub-question (answerable now: yes,
comfortably, for a stack that excludes full-precision Binoculars) and one
or more quality sub-questions (still open: is there an acceptable
multilingual factual-consistency option; is there a local detector that is
simultaneously accurate, multilingual-robust, and storage-affordable) —
proposed in R09 §10.6, not decided; (b) commission targeted follow-up
experiments identified as concrete, low-cost gaps rather than further
literature search: measuring actual quantized disk size for the
semantic-similarity candidates (R09 §10.2), and testing whether a
quantized Falcon-7B pair preserves Binoculars' detection quality (R09
§10.4); (c) treat the multilingual factual-consistency and multilingual
detection gaps as inputs to Q-004 (multilingual validation thresholds)
rather than resolving them independently, since both bear directly on
what "validated" can mean per language and per capability.

---

## Q-009 — How should newly published scientific findings affect an
already-certified release?

Status: OPEN

### Current Evidence (added 2026-08-24)

This session's own research passes are a live illustration of the
problem this question anticipates: the R05 pass materially corrected a
finding (KB-008) that the R04 pass had recorded only a day earlier, and
R07's own findings (R-0093-R-0097) show that even *formal, peer-reviewed
statistical guarantees* for watermarking do not survive real-world
attack conditions once tested empirically (R-0097) — i.e., a capability
could be "certified" against the literature available at one point in
time and have that basis revised within weeks as the field moves,
independent of any change to the project's own code. KB-001 (already
TRIAGED, CRITICAL priority) already proposes versioned effectiveness
profiles as the mechanism for this, but that proposal has not yet been
connected to a concrete re-certification trigger or process.

### Possible Answers (not yet decided)

(a) Tie re-certification review to new entries in RESEARCH-REGISTRY.md
that materially affect a certified capability's evidence base (per
RESEARCH-MAP.md §21, Research Change Protocol) rather than to a fixed
calendar schedule; (b) require every certification to record the
research-registry state (e.g., last R-XXXX id) it was certified against,
so a later reviewer can see exactly what evidence has since changed; (c)
this project's own experience in this session (KB-008 revised within 24
hours by R05) suggests re-certification triggers may need to fire more
often, at least early on, than a mature/stable field would require.