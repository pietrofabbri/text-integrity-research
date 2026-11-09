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

Status: RESOLVED

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

### Resolution (2026-10-01, Tranche 4 / DEC-022 / DEC-024)

Resolved by the drafting and acceptance of
`docs/04-architecture/EXTERNAL-INTEGRATION-ARCHITECTURE.md` (DEC-022) and
`docs/04-architecture/REPORTING-ARCHITECTURE.md` (DEC-024).

The architecture adopts Possible Answers (a) and (c):
1. **Preservation of Individual Observations:** External detector outputs
   are preserved individually in an observation tier with provider,
   timestamp, version, and external observation tag (`EXTERNAL_OBSERVATION`),
   never collapsed into an aggregate majority verdict or substituted for a
   local result.
2. **Disagreement as Uncertainty:** Disagreements between external detectors
   are recorded explicitly as uncertainty in reporting rather than forced
   into an artificial consensus.
3. **No Ground Truth Status:** No external detector output is presented as
   ground truth in the certification or evaluation path.

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

### Resolution & Status (2026-10-01)

Status: PARTIALLY RESOLVED (Storage resolved; Quality/Robustness tracked in KB-013/KB-014)

Per R09 §10.6 and DEC-013, the storage budget dimension of this question is **resolved**:
- **Storage Sub-question (RESOLVED):** Local storage (~30GB) is comfortably
  sufficient for a lightweight multi-task validation stack (well under 10GB for
  multilingual embedding/semantic similarity and local factual checking). The
  storage budget is binding only if attempting to run unquantized dual-7B
  detectors (Binoculars at ~28.87GB).
- **Quality & Multilingual Robustness Sub-question (OPEN):** The remaining open
  aspects are quality limitations, not storage. These are tracked in:
  - `KB-013` (No evidence-backed multilingual factual-consistency model);
  - `KB-014` (Local detection bounded by accuracy/cross-lingual robustness);
  - `KB-015` (Quantization impact on non-English capability).

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

---

## Q-010 — How do the LOW–CRITICAL and C0–C4 change scales relate?

### Question

How do the LOW–CRITICAL and C0–C4 change scales relate?

### Why It Matters

Every significant change must be classified, and the two scales set different approval effects.

### Relevant Areas

01-governance, 06-security, 08-development

### Current Evidence

No mapping exists. `AGENT-WORK-MODEL.md` AWM-C2, AWM-G1. Meanwhile both labels are recorded and the stricter treatment applies.

### Possible Answers

(a) define a mapping; (b) keep both as separate dimensions; (c) retire one. These are options, not recommendations or decisions.

### Blocking

YES, for implementation; NO, for documentation tranches.

### Owner

Human

### Resolution

Option (b): the scales stay as two separate dimensions. `LOW–CRITICAL` measures risk; `C0–C4` measures breadth of impact. Every classified change carries both, and the stricter treatment applies. No mapping is defined. Decided 2026-11-09 by `DEC-057`, on the owner's delegation.

### Status

RESOLVED


---

## Q-011 — How is approval given and recorded for MEDIUM batches and CRITICAL changes?

### Question

How is approval given and recorded for MEDIUM batches and CRITICAL changes?

### Why It Matters

`SECURITY-MAP.md` §75 requires an approved MEDIUM and §24 explicit approval, without saying what counts.

### Relevant Areas

01-governance, 06-security, 08-development

### Current Evidence

`AGENT-SECURITY-BOUNDARY.md` ASB-G3, ASB-G4. `DEC-046` records one delegated approval of tranche boundaries.

### Possible Answers

(a) approval at tranche level covers MEDIUM batches inside it; (b) per batch; (c) a stricter explicit form for CRITICAL. These are options, not recommendations or decisions.

### Blocking

YES, for implementation; NO, for documentation tranches.

### Owner

Human

### Resolution

Options (a) and (c): approval of a tranche covers the MEDIUM batches inside it. A CRITICAL change needs an owner statement naming that specific change; a general delegation does not count. Decided 2026-11-09 by `DEC-057`, on the owner's delegation.

### Status

RESOLVED


---

## Q-012 — What is a tranche's resource budget?

### Question

What is a tranche's resource budget?

### Why It Matters

`P00-project-governance.md` §7 and §10 require one; no unit or convention exists.

### Relevant Areas

01-governance, 08-development

### Current Evidence

`AGENT-WORK-MODEL.md` AWM-G4.

### Possible Answers

(a) define a unit; (b) declare not applicable to documentation tranches; (c) amend `P00`. These are options, not recommendations or decisions.

### Blocking

YES, for implementation; NO, for documentation tranches.

### Owner

Human

### Resolution

Not applicable to documentation tranches. An implementation tranche states in its definition any limit on storage or paid external services, or states `none`. No unit or value is set here. Decided 2026-11-09 by `DEC-057`, on the owner's delegation.

### Status

RESOLVED


---

## Q-013 — Do cloud sessions count as local development, and which commands are approved?

### Question

Do cloud sessions count as local development, and which commands are approved?

### Why It Matters

`DEVELOPMENT-MAP.md` §6 and `SECURITY-MAP.md` §17 assume local execution and approved local commands, while the owner now works only through GitHub and cloud sessions.

### Relevant Areas

06-security, 08-development

### Current Evidence

`AGENT-WORK-MODEL.md` §12, AWM-G6; `AGENT-SECURITY-BOUNDARY.md` ASB-C5, ASB-G2.

### Possible Answers

(a) treat the session container as the local environment; (b) require a separate local environment for tests. These are options, not recommendations or decisions.

### Blocking

YES, for implementation; NO, for documentation tranches.

### Owner

Human

### Resolution

Option (a): the session container counts as the local environment for execution. It is not offline, so the `OFFLINE` profile must disable network access itself. Approved commands: git without history rewriting, the project's validation commands, and installation of already authorized dependencies. The two `update_*_map.py` scripts are excluded. Decided 2026-11-09 by `DEC-057`, on the owner's delegation.

### Status

RESOLVED


---

## Q-014 — Which implementation language and tooling will the project use?

### Question

Which implementation language and tooling will the project use?

### Why It Matters

Phase 2 cannot begin without it.

### Relevant Areas

04-architecture, 08-development

### Current Evidence

No project document selects one. `ENGINEERING-STANDARDS.md` ENG-G1.

### Possible Answers

Not yet evaluated. These are options, not recommendations or decisions.

### Blocking

YES, for implementation; NO, for documentation tranches.

### Owner

Human

### Resolution

Python. Runtime dependencies are added only with a recorded reason (`DEVELOPMENT-MAP.md` §78). Tests start on the standard library `unittest`; `ruff` and `mypy` are development-only checks. This is an engineering judgment, based on the ecosystem around the models named in `R09`, and no comparative evaluation was carried out. The version is set by the first manifest. Decided 2026-11-09 by `DEC-057`, on the owner's delegation.

### Status

RESOLVED


---

## Q-015 — What happens to `update_project_map.py` and `update_research_map.py`?

### Question

What happens to `update_project_map.py` and `update_research_map.py`?

### Why It Matters

If run, each overwrites a maintained document with an older, shorter text.

### Relevant Areas

00-project, 02-research, 08-development

### Current Evidence

`ENGINEERING-STANDARDS.md` ENG-R1, ENG-G4. Must not be run meanwhile.

### Possible Answers

(a) retire them; (b) correct them; (c) keep them with a warning. These are options, not recommendations or decisions.

### Blocking

YES, for implementation; NO, for documentation tranches.

### Owner

Human

### Resolution

Option (a): both scripts are retired and removed from the working tree. They remain recoverable from Git history. Decided 2026-11-09 by `DEC-057`, on the owner's delegation.

### Status

RESOLVED


---

## Q-016 — What should the empty README contain?

### Question

What should the empty README contain?

### Why It Matters

`DEVELOPMENT-MAP.md` §134 lists it first, and the repository is public.

### Relevant Areas

00-project, 08-development

### Current Evidence

`DOCUMENTATION-AND-MAINTENANCE-POLICY.md` DMP-G3.

### Possible Answers

(a) a short pointer to `START-HERE.md`; (b) a full project description. These are options, not recommendations or decisions.

### Blocking

YES, for implementation; NO, for documentation tranches.

### Owner

Human

### Resolution

Option (a): a short description with a pointer to `START-HERE.md`. Decided 2026-11-09 by `DEC-057`, on the owner's delegation.

### Status

RESOLVED


---

## Q-017 — Who performs security reviews and grants security exceptions?

### Question

Who performs security reviews and grants security exceptions?

### Why It Matters

`SECURITY-MAP.md` §72 and §73 require them without naming who.

### Relevant Areas

06-security

### Current Evidence

`AGENT-SECURITY-BOUNDARY.md` ASB-G1; `RESILIENCE-AND-SECURITY-ASSURANCE.md` RSA-G3.

### Possible Answers

(a) the owner; (b) an agent review with owner sign-off for HIGH and CRITICAL. These are options, not recommendations or decisions.

### Blocking

YES, for implementation; NO, for documentation tranches.

### Owner

Human

### Resolution

Option (b): the agent performs the review and reports it; HIGH and CRITICAL findings and every security exception require owner sign-off. Decided 2026-11-09 by `DEC-057`, on the owner's delegation.

### Status

RESOLVED


---

## Q-018 — What are the branching model and backup location?

### Question

What are the branching model and backup location?

### Why It Matters

`main` has no protection, and §59–60 of `SECURITY-MAP.md` leave both open.

### Relevant Areas

06-security, 08-development

### Current Evidence

`SUPPLY-CHAIN-AND-ARTIFACT-SECURITY.md` SCS-G2, SCS-G3.

### Possible Answers

(a) protect `main` against force push and deletion, with branches for code; (b) current direct push; a second copy for backup is undecided. These are options, not recommendations or decisions.

### Blocking

YES, for implementation; NO, for documentation tranches.

### Owner

Human

### Partial Resolution

Decided by `DEC-057`, on the owner's delegation: documentation may be pushed directly to `main`; code goes through branches; history is never rewritten. Still open: protection of `main` (a repository setting this agent's session cannot change, so it needs the owner) and the location of a second copy.

### Status

OPEN


---

## Q-019 — What is the default network mode, and may individual user text be sent externally?

### Question

What is the default network mode, and may individual user text be sent externally?

### Why It Matters

`SECURITY-MAP.md` §14 does not choose a default, and transfer eligibility is declared only for datasets.

### Relevant Areas

06-security, 07-data, 09-operations

### Current Evidence

`TRUST-AND-DATA-BOUNDARIES.md` TDB-G1, TDB-G2.

### Possible Answers

(a) `OFFLINE` default, opt-in per text; (b) `LOCAL_ONLY` default; to be settled with the `DEC-012` reconciliation. These are options, not recommendations or decisions.

### Blocking

YES, for implementation; NO, for documentation tranches.

### Owner

Human

### Resolution

`OFFLINE` is the default mode, the most restrictive §14 allows. Individual user text is treated as `UNKNOWN` under `DATA-MAP.md` §35: never sent externally without an explicit opt-in for that run. The network-mode vocabulary stays unreconciled under `DEC-012`. Decided 2026-11-09 by `DEC-057`, on the owner's delegation.

### Status

RESOLVED
