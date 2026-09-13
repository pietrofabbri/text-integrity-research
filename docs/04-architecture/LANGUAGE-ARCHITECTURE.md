# Language Architecture

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Architecture sub-document (Tranche 3a)
**Authority:** Architectural
**Parent:** `docs/04-architecture/ARCHITECTURE-MAP.md` §34-35 (Language
Architecture, Language Capability Registry)
**Scope:** How language-specific resources are isolated behind stable
interfaces, and how a language's overall capability profile is derived
from (not duplicated against) the per-capability, per-language states
`CAPABILITY-ARCHITECTURE.md` §10 already defines.

---

# 1. Purpose

This document formalizes `ARCHITECTURE-MAP.md` §34-35 into a concrete
model for how a language enters the architecture, what a language's
registry entry contains, and how that entry relates to the per-capability
language states `CAPABILITY-ARCHITECTURE.md` already formalizes. It
exists because §58 of that document lists `LANGUAGE-ARCHITECTURE.md` as a
candidate document; §64.4 originally judged it premature for the same
reason as `ANALYSIS-ARCHITECTURE.md` — no per-language evidence record
existed. `docs/00-project/DECISION-LOG.md` DEC-018 supplied that record
(`docs/03-scientific-specification/SPECIFICATION-MAP.md` §22.1), and
DEC-019 reassessed this document as structurally ready on that basis.

Like the other Tranche 1-3a documents, this document selects no specific
tokenizer, linguistic resource, or per-language default beyond what
`SPECIFICATION-MAP.md` §22.1 already records. It defines the mechanism —
a language-centric registry view and the isolation principle behind it —
that any specific language resource would need to plug into.

---

# 2. Relationship to Other Documents

- `ARCHITECTURE-MAP.md` §34-35 is the authoritative parent; this document
  elaborates, it does not supersede.
- `docs/04-architecture/CAPABILITY-ARCHITECTURE.md` §10
  (Language-Scoped Capability State) already formalizes the
  **capability-centric** view: for a given capability, its lifecycle
  state per language. This document formalizes the complementary
  **language-centric** view: for a given language, which capabilities
  apply and at what state. §4 below is explicit that this is a derived
  view, not a second place where states are recorded — there is exactly
  one source of per-capability-per-language state
  (`CAPABILITY-ARCHITECTURE.md` §10's `languages` maps, currently
  populated at the documentation-default level by
  `SPECIFICATION-MAP.md` §22.1), and this document's registry entries are
  computed from it.
- `docs/03-scientific-specification/SPECIFICATION-MAP.md` §20-22
  (Multilingual Specification, Language-Specific Requirements, Language
  Capability States) and §22.1 (the per-language assignment) are
  authoritative for *what* a language's current evidence-grounded default
  state is. This document is authoritative only for *how* that
  information is organized and isolated architecturally.
- `docs/03-scientific-specification/S02-scientific-requirements.md` §8
  (Multilingual Requirements, REQ-LANG-001 through REQ-LANG-006) governs
  the normative requirements this document's mechanism must satisfy.
- `docs/04-architecture/ANALYSIS-ARCHITECTURE.md` and
  `VALIDATION-ARCHITECTURE.md` are the two capability families with the
  richest current per-language evidence (§22.1.1/§22.1.2 and the
  `VALIDATE-FACTUAL-CLAIM` treatment respectively); this document
  cross-references their per-language findings rather than restating
  them.

---

# 3. Modular Isolation Principle

Per `ARCHITECTURE-MAP.md` §34, the core must not assume that all
languages share identical tokenization, segmentation, morphology, syntax,
punctuation, normalization, or detector behavior. Language-specific
resources must therefore be isolated behind stable interfaces, so that:

- adding a language does not require modifying the core orchestration,
  analysis, transformation or validation mechanisms — only registering
  new language-specific resources and capability states, operationalizing
  `S02-scientific-requirements.md` REQ-LANG-005 and REQ-EXT-003 (Language
  Extensibility);
- a language's absence of a resource (e.g. no tokenizer registered) must
  surface as an explicit `NOT_SUPPORTED` state (`SPECIFICATION-MAP.md`
  §22), never as a silent fallback to another language's resource — a
  silent fallback would violate `ARCHITECTURE-MAP.md` §45 (Failure
  Isolation: "silent fallback is prohibited when it could change
  scientific interpretation").

---

# 4. Language Registry Entry Schema

Per `ARCHITECTURE-MAP.md` §35, a language's registry entry contains:

- `language_code` — the identifier (this project's 13 target languages
  per `SPECIFICATION-MAP.md` §20, extensible per REQ-LANG-005);
- `display_name`;
- `tokenizer` / `linguistic_resources` — references to the
  language-specific resources registered for this language, per §3's
  isolation principle; the exact resource format is a Development-phase
  decision, not fixed here;
- `supported_operations` — **derived**, not separately recorded: computed
  by enumerating every `CAPABILITY-ARCHITECTURE.md` capability record
  whose `languages` map (§10 of that document) includes this
  `language_code` at any state above `NOT_SUPPORTED`;
- `analyzers` / `validators` — the subset of `supported_operations`
  belonging to the analysis (`ANALYSIS-ARCHITECTURE.md` §3) and
  validation (`VALIDATION-ARCHITECTURE.md` §4) families respectively;
- `known_limitations` — language-level limitations not tied to one
  capability (e.g. a tokenization risk factor, §6 below), distinct from a
  single capability's own `known_limitations` field;
- `validation_status` — **derived**, not separately recorded: the
  language cannot have one project-wide status (per §35: "a language can
  be active for one capability and research-only for another"); this
  field is a summary view over the per-capability states, never a single
  aggregate that conceals a per-capability `EXPERIMENTAL` or absent state
  — directly restating `CAPABILITY-ARCHITECTURE.md` §10's own
  requirement and `RESEARCH-MAP.md` §46 (Multilingual Benchmark: "a
  single aggregate score is insufficient").

---

# 5. Why `supported_operations` and `validation_status` Are Derived, Not Recorded

A language registry entry that separately records its own capability
states, alongside `CAPABILITY-ARCHITECTURE.md` §10's per-capability
`languages` maps, would create two places that could silently disagree —
exactly the kind of duplicated bookkeeping `docs/07-data/DATA-MAP.md` §94
already warns against for the data/capability relationship, and
`ARCHITECTURE-MAP.md` §57 (No Hidden Scientific State) prohibits more
generally. This document therefore requires that a language's entry be
computed at read time (or cached with an explicit invalidation rule, a
Development-phase decision) from the capability registry, never
maintained as an independent copy.

---

# 6. Tokenizer and Script-Level Risk Factors

Distinct from capability-level evidence (§22.1), some findings describe a
language's tokenization or script properties as a general risk factor,
without themselves testing a specific detection or watermarking
capability. Per `docs/02-research/R05-multilingual-linguistic-research.md`
§47.2:

- **Script/resource clustering** (R-0049, EVIDENCE) — Cyrillic languages
  transfer well to each other; Arabic/Chinese are comparatively harder.
- **Tokenizer subword-fragmentation** (STEAM, R-0044/R-0062,
  AUTHOR-REPORTED, unreplicated) — a proposed causal mechanism, not yet
  independently confirmed.
- **Turkish agglutinative fragmentation** (R-0071, background paper) —
  documents tokenization mechanics but does not itself test any
  detection or watermarking capability.

These belong in a language's `known_limitations` (§4) as risk factors,
distinct from — and not a substitute for — a specific capability's own
per-language evidence tier (`ANALYSIS-ARCHITECTURE.md` §4-5). A risk
factor is not itself grounds to lower a capability's registered state; it
is grounds to document why a capability's evidence for that language, if
any, should be read with additional caution.

---

# 7. Adding a New Language

Operationalizing `S02-scientific-requirements.md` REQ-LANG-005 (Language
Extensibility) and REQ-EXT-003, and `ARCHITECTURE-MAP.md` §34: adding a
language to this project means, architecturally:

1. registering a new language entry (§4) with whatever tokenizer/
   linguistic resources are actually available — an entry may exist with
   most fields `NOT_SUPPORTED` if no resources exist yet;
2. no existing capability's implementation changes as a result — each
   relevant capability independently registers (or does not register) a
   state for the new `language_code` in its own `languages` map
   (`CAPABILITY-ARCHITECTURE.md` §10);
3. no core orchestration, analysis, transformation or validation
   mechanism is modified — per §3's isolation principle, this is the
   architectural test that a language was actually added in an extensible
   way rather than by special-casing the core.

This document does not itself add any language beyond the 13 already
named in `SPECIFICATION-MAP.md` §20 — it only defines the mechanism by
which a 14th (or a regional/script variant of an existing one) would be
added.

---

# 8. Illustrative Example (Non-Binding)

Using `SPECIFICATION-MAP.md` §22.1 and `RESEARCH-REGISTRY.md` entries
already on file, purely to make §4-5's derivation mechanism concrete —
not a decision to adopt any specific capability's state as final:

```
language_code: it (Italian)
tokenizer / linguistic_resources: [Development-phase decision, not fixed here]
supported_operations (derived from CAPABILITY-ARCHITECTURE.md §10 languages maps):
  - AI-generated-text detection: RESEARCH_ONLY (per SPECIFICATION-MAP.md
    §22.1.1; R-0047, R-0048, R-0059 — note R-0059 is a *negative* finding,
    not evidence that detection currently works)
  - Watermarking: NOT_SUPPORTED (§22.1.2 — no dedicated study found)
  - Factual/claim-consistency validation: NOT_SUPPORTED (§22.1.3 — no
    evidence-backed option; candidate mDeBERTa-v3-xnli's task-fit is
    unverified, per KB-013)
validation_status: mixed — must not be summarized as a single "supported"
  or "unsupported" flag (§4, §35)
known_limitations: none of the tokenizer/script risk factors in §6
  specifically name Italian
```

The registry entry surfaces Italian's genuinely mixed picture rather than
collapsing it into one number — the same discipline
`VALIDATION-ARCHITECTURE.md` §9 requires for a single validation run.

---

# 9. What This Document Does Not Decide

This document does not: select any specific tokenizer or linguistic
resource for any language; add a 14th language or change the 13-language
list in `SPECIFICATION-MAP.md` §20; assign or change any per-capability
per-language state beyond what `SPECIFICATION-MAP.md` §22.1 already
records (this document derives from that record, it does not extend it);
or resolve DCQ-006, DCQ-007 or DCQ-008 (the External Integration,
Reporting, and Configuration Layers — since resolved by
`EXTERNAL-INTEGRATION-ARCHITECTURE.md`, `REPORTING-ARCHITECTURE.md`, and
`CONFIGURATION-ARCHITECTURE.md`, all drafted after this document). This
document's own `validation_status: mixed` discipline (§8) is, in turn,
generalized by `REPORTING-ARCHITECTURE.md` §5 (drafted after this
document, DEC-024) to every dimension a report covers, not only language
coverage. All of these remain separate, later decisions or research
tasks except where noted above as since resolved.

---

# 10. Final Principle

A language is not "supported" or "not supported" as a single fact about
this project — it is supported for specific capabilities, to specific
degrees, on specific evidence, and the architecture's job is to keep that
texture visible rather than flattening it into a single flag for
convenience. This document's central mechanism — a language registry
that derives its view from the capability registry rather than
duplicating it — exists so that texture stays honest as the project
grows, instead of degrading into two records that quietly drift apart.
