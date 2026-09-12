# Capability Architecture

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Architecture sub-document (Tranche 1)
**Authority:** Architectural
**Parent:** `docs/04-architecture/ARCHITECTURE-MAP.md` §23-26 (Capability
Registry, Lifecycle, Activation, Retirement)
**Scope:** The capability record schema, identifier convention, and
lifecycle state machine that let analytical, transformation and
validation components evolve independently of the core.

---

# 1. Purpose

This document formalizes `ARCHITECTURE-MAP.md` §23-26 into a concrete
schema and state machine. It exists because §58 of that document lists
`CAPABILITY-ARCHITECTURE.md` as a candidate document, and
`docs/04-architecture/ARCHITECTURE-MAP.md` §64 (2026-09-12) judged this
document "structurally ready now": the mechanism it describes is generic
and does not depend on which specific detector, watermark scheme, or
model is eventually registered under it.

This document does not select, endorse or rank any specific detector,
watermark scheme, model or algorithm. It defines the record format and
rules that would apply to *any* of them, per DEC-009 (a research finding
does not automatically become a system requirement) and §2 of
`ARCHITECTURE-MAP.md` ("no single algorithm should define the
architecture").

---

# 2. Relationship to Other Documents

- `ARCHITECTURE-MAP.md` §23-26 is the authoritative parent for the
  concepts formalized here; this document elaborates, it does not
  supersede.
- `docs/07-data/DATA-MAP.md` §94 (Data and Capability Registry) and §95
  (Dependency Graph) already define how a capability declares a
  dependency on a dataset or model resource. This document does not
  restate those rules — it defines the capability side of that
  relationship; §9 below cross-references rather than duplicates.
- `docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md` DCQ-006/DCQ-007/DCQ-008
  track the actual propagation of research findings into specific
  capability states (e.g., which languages get a validated AI-detection
  capability). This document defines the *mechanism* those propagations
  will use; it does not itself perform any of that propagation, and does
  not resolve any of DCQ-006/007/008.
- `docs/99-backlog/NO-INVENTION-RULES.md` and the R0x confidence-tag
  convention (EVIDENCE / AUTHOR-REPORTED / VENDOR / UNVERIFIED) govern
  what evidence a capability record may cite — see §11.

---

# 3. Capability Identifier

Recommended structure, chosen for consistency with `DATA-MAP.md` §12's
existing `DATA-[CATEGORY]-[SHORT-NAME]` convention:

```
CAP-[FAMILY]-[SHORT-NAME]
```

Example: `CAP-DETECT-BINOCULARS`, `CAP-EMBED-E5-LARGE-INSTRUCT`,
`CAP-WATERMARK-KGW`.

`[FAMILY]` should be one of the analytical/transformation/validation
families already named in `ARCHITECTURE-MAP.md` §9, §13, §16 (e.g.
`DETECT`, `WATERMARK`, `PROVENANCE`, `TRANSFORM`, `VALIDATE-SEMANTIC`,
`VALIDATE-FACTUAL`, `VALIDATE-STRUCTURAL`). The exact identifier
convention may evolve, matching `DATA-MAP.md` §12's own hedge.

---

# 4. Capability Record Schema

Every capability record contains, at minimum, the fields already listed
in `ARCHITECTURE-MAP.md` §23, made explicit here:

- `id` — a Capability Identifier (§3).
- `name` — human-readable name.
- `category` — the family (§3).
- `version` — the capability's own version, distinct from any underlying
  model/dataset version (see §12).
- `status` — a Lifecycle State (§6).
- `languages` — a per-language status map (§10), not a single flag.
- `dependencies` — references to `DATA-MAP.md` manifest entries (dataset
  and/or model IDs, per `DATA-MAP.md` §12) this capability requires.
- `input_requirements` / `output_schema` — per `ARCHITECTURE-MAP.md` §56
  (Schema-First Principle).
- `validation_requirements` — which validation families (§16 of
  `ARCHITECTURE-MAP.md`) must pass before this capability may reach
  `VALIDATED` (§6).
- `scientific_sources` — one or more `R-XXXX` identifiers from
  `docs/00-project/RESEARCH-REGISTRY.md`, each carrying its own
  confidence tag (§11).
- `known_limitations` — carried forward from the cited research entries,
  not re-derived.
- `resource_requirements` — a reference to the corresponding `DATA-MAP.md`
  manifest's size/compatibility fields (§80-82 of that document), not a
  duplicate copy of them.

The exact storage format (a file-based manifest, an embedded database, or
something else) is a Development-phase decision, deferred per §16 below —
this schema is format-agnostic.

---

# 5. Capability Categories

Categories correspond to the analytical, transformation and validation
families already named in `ARCHITECTURE-MAP.md`:

- Analysis-layer categories (§9-12 of that document): language
  identification, segmentation, stylometric analysis, watermark signal
  analysis, provenance analysis, AI-generation assessment, and others as
  they are identified.
- Transformation-layer categories (§13-15): grammar/spelling correction,
  terminology normalization, style normalization, translation, and
  others as they are identified.
- Validation-layer categories (§16-20): semantic, factual, structural,
  numerical, entity, linguistic, minimality, regression.

New categories may be added without redesigning this schema, per
`ARCHITECTURE-MAP.md` §2 ("algorithms are replaceable components") and
`RESEARCH-MAP.md` §28 (New Methodology Rule).

---

# 6. Capability Lifecycle States

Restates and details `ARCHITECTURE-MAP.md` §24:

```
DISCOVERED → EXPERIMENTAL → VALIDATED → ACTIVE → DEPRECATED → RETIRED
                                              ↘ DEGRADED ↗
```

- **DISCOVERED** — a candidate method or model has been identified in the
  research layer (an `R-XXXX` entry exists) but no capability record has
  been created yet.
- **EXPERIMENTAL** — a capability record exists and the component is
  implemented, but has not passed the Activation Gate (§7).
- **VALIDATED** — the Activation Gate (§7) has been passed for at least
  one specific language/scope; the capability is not yet serving default
  pipeline runs.
- **ACTIVE** — the capability is available for default use for the
  language/scope for which it was validated. Per §10, a capability may be
  `ACTIVE` for one language and `EXPERIMENTAL` or absent for another —
  this is not a contradiction, it is the intended model.
- **DEGRADED** — an `ACTIVE` capability whose scientific or operational
  quality has declined (e.g. a new benchmark shows regression, an
  external dependency changed behavior) but immediate retirement is not
  yet justified. A `DEGRADED` capability must not be silently treated as
  equivalent to `ACTIVE` in reports (`ARCHITECTURE-MAP.md` §38).
- **DEPRECATED** — scheduled for retirement; per `ARCHITECTURE-MAP.md`
  §48, must record reason, replacement if available, affected
  capabilities/experiments, and intended removal.
- **RETIRED** — removed from default use; per `ARCHITECTURE-MAP.md` §54
  and `DATA-MAP.md` §109, historical results referencing this capability
  must remain interpretable.

---

# 7. Activation Gate (DISCOVERED/EXPERIMENTAL → VALIDATED)

Expanding `ARCHITECTURE-MAP.md` §25, a capability may not move to
`VALIDATED` for a given language/scope unless:

1. it has a complete capability record (§4);
2. its declared `validation_requirements` (§4) have actually been run and
   passed, per `ARCHITECTURE-MAP.md` §16-20;
3. its `scientific_sources` (§4) include at least one entry that is not
   solely `UNVERIFIED` in `RESEARCH-REGISTRY.md`'s confidence tagging —
   an `UNVERIFIED` claim alone (e.g. R-0115's unconfirmed leaderboard
   claim, R09 §10.4) is not sufficient grounds for `VALIDATED`;
4. dependency verification (§9) succeeds — all declared
   `DATA-MAP.md`-registered dependencies are `ACTIVE` per that document's
   own Model/Dataset Activation Gates (`DATA-MAP.md` §84-85);
5. regression tests and documentation exist, per
   `ARCHITECTURE-MAP.md` §25;
6. licensing has been checked where applicable, per
   `ARCHITECTURE-MAP.md` §25 and `DATA-MAP.md` §38-40.

Moving from `VALIDATED` to `ACTIVE` (making the capability available by
default) is a separate, later step that may additionally require a
recorded decision in `docs/00-project/DECISION-LOG.md` when the
capability is scientifically or operationally significant — consistent
with `DECISION-LOG.md` DEC-009 (a research finding does not automatically
become a requirement) and DEC-004 (human approval at macro-tranche
boundaries).

---

# 8. Retirement Gate (ACTIVE/DEGRADED → DEPRECATED → RETIRED)

Expanding `ARCHITECTURE-MAP.md` §26 and §54:

1. a reason is recorded (one of: scientific obsolescence, superior
   replacement, unavailable dependency, licensing change, security issue,
   insufficient validation, excessive resource requirements, loss of
   maintenance viability — per `ARCHITECTURE-MAP.md` §26);
2. affected capabilities and experiments are identified;
3. a replacement is identified where one exists (`DATA-MAP.md` §97
   applies: a replacement does not automatically inherit the retired
   capability's validated status);
4. historical results remain interpretable after retirement
   (`ARCHITECTURE-MAP.md` §54, `DATA-MAP.md` §109);
5. the change enters `docs/00-project/DOCUMENTATION-CHANGE-QUEUE.md` if it
   has documentation consequences beyond the registry itself.

---

# 9. Dependency Declaration (Cross-Reference, Not Duplication)

A capability record's `dependencies` field (§4) references one or more
`DATA-MAP.md`-registered dataset/model identifiers (that document's §12
convention). This document does not redefine how those identifiers are
structured, versioned, licensed or activated — `DATA-MAP.md` §80-85, §94-95
already do so and remain authoritative. The only addition this document
makes is the reverse link: a capability record must name every resource
it depends on, so that `DATA-MAP.md` §94's "what breaks if a dataset is
removed" question can be answered by traversing capability records rather
than by inspecting implementation code.

---

# 10. Language-Scoped Capability State

A single capability identifier may have a different lifecycle state per
language. This formalizes `ARCHITECTURE-MAP.md` §35 ("a language can be
active for one capability and research-only for another") and is
directly grounded in confirmed evidence gaps: KB-008/KB-010 (watermarking
and detection evidence varies sharply by language) and R09 §10.3-§10.4
(no evidence-backed multilingual factual-consistency option; detection
accuracy collapses toward chance for several target languages).

A capability record's `languages` field (§4) is therefore a map from
language code to lifecycle state (§6), not a single value. A capability
must not report an aggregate "supported" status that conceals a
language-specific `EXPERIMENTAL` or absent state — this directly
implements `RESEARCH-MAP.md` §46 (Multilingual Benchmark: "a single
aggregate score is insufficient") at the architecture level.

---

# 11. Evidence Requirements (No-Invention Rules at the Architecture Level)

A capability record's `scientific_sources` field must cite specific
`R-XXXX` registry entries, not restate a finding unsourced — the same
rule R04 §39, R08 §69, and R09 §10 already apply within the research
layer itself. Consuming a source registered with an `UNVERIFIED` or
`VENDOR` confidence tag does not disqualify a capability from
`EXPERIMENTAL` status, but does disqualify it from `VALIDATED` on that
source alone (§7, point 3). This is the architectural enforcement point
for `docs/99-backlog/NO-INVENTION-RULES.md`'s evidence-class discipline —
without it, the distinction between "a paper claims X" and "this project
verified X" would exist only in prose, not in the system that decides
what actually runs by default.

---

# 12. Capability Versioning

A capability's own `version` (§4) is distinct from:

- the version of any underlying model or dataset it depends on
  (`DATA-MAP.md` §13, §81);
- the version of the research finding that justified its creation (an
  `R-XXXX` entry does not have its own version number, but a later
  registry entry can supersede or correct an earlier one, as KB-008's
  correction by R05 illustrates).

The exact versioning scheme (semantic versioning or otherwise) is left to
Development, per `ARCHITECTURE-MAP.md` §43 (Development/Runtime
Separation) — this document only requires that a version exists and
changes when the capability's behavior changes.

---

# 13. Multiple Candidates per Category

Per `ARCHITECTURE-MAP.md` §2 and §29 (Independent Detectors), more than
one capability record may exist in the same category (e.g. multiple
`DETECT-*` capabilities). This is expected, not an anomaly: R09 §10.4
found no single local AI-detection candidate that is simultaneously
accurate, multilingual-robust and storage-affordable, meaning several
`DETECT-*` capability records may coexist at different lifecycle states
and language coverages rather than one being selected as "the" detector.

---

# 14. Illustrative Example (Non-Binding)

To make the abstract schema concrete, a hypothetical capability record
using an entry already in `RESEARCH-REGISTRY.md` — presented only as an
illustration of the schema, not as a decision to adopt this specific
model:

```
id: CAP-EMBED-E5-LARGE-INSTRUCT
category: VALIDATE-SEMANTIC
status: EXPERIMENTAL
languages: {en: EXPERIMENTAL, it: EXPERIMENTAL, ...}
dependencies: [DATA-MODEL-E5-LARGE-INSTRUCT]  # illustrative DATA-MAP.md ID
scientific_sources: [R-0103, R-0106]
known_limitations: "fp16 storage-format artifact; MMTEB rank does not
  measure this project's actual task (R09 §10.2)"
```

This example does not constitute adoption of multilingual-e5-large-
instruct as the project's semantic-validation component — that remains a
separate, later decision.

---

# 15. What This Document Does Not Decide

Per DEC-009 and `ARCHITECTURE-MAP.md` §64.5: this document does not
select any specific detector, watermark scheme, embedding model, or
factual-consistency checker; does not resolve DCQ-006, DCQ-007 or
DCQ-008; does not fix the concrete storage format of the capability
registry (file-based vs. database); and does not decide the exact
identifier/versioning syntax beyond the illustrative convention in §3
and §12.

---

# 16. Final Principle

A capability registry is only as trustworthy as the discipline behind
what enters it. This document's purpose is to make sure that discipline —
evidence-class citation (§11), language-scoped honesty (§10), and an
explicit gate between "implemented" and "active by default" (§7) — is
part of the architecture itself, not something left to be remembered
separately for each new detector or model the project adds.
