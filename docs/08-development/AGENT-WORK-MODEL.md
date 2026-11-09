# Agent Work Model

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Development process protocol (Tranche 1 of `DEVELOPMENT-MAP.md` §202)
**Authority:** Development (primary for development process and engineering workflow, per `docs/99-backlog/DOCUMENT-AUTHORITY-MATRIX.md`). Governance and decision authority remain with `docs/01-governance/P00-project-governance.md`; security boundaries remain with `docs/06-security/SECURITY-MAP.md`.
**Parent:** `docs/08-development/DEVELOPMENT-MAP.md` §2–24, §115–125, §170–173, §188–201
**Governance basis:** `P00-project-governance.md` §1–12, §19–20, §28, §30
**Requirements basis:** `docs/03-scientific-specification/S02-scientific-requirements.md` §26 (Requirement Conflict)
**Research basis:** none specific; see §13
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-001, DEC-004, DEC-005, DEC-006, DEC-010, DEC-012, DEC-036 (tranche precedent), DEC-040 (roadmap), DEC-041 (this document's execution)

---

# 1. Purpose & Scope

This document formalizes how an AI coding agent works on this project: how work is bounded, classified, stopped, reviewed, reported and audited.

It does not add a requirement beyond its sources and does not set any numeric value. Every rule below carries its source. Statements not found in a source are labelled **INFERENCE** or **PROPOSAL**, using the evidence classes of `docs/99-backlog/NO-INVENTION-RULES.md`.

It does not supersede `P00-project-governance.md`. Under `P00` §2, a lower-level artifact may not silently redefine a higher-level one.

**State of the repository (verified 2026-11-09):** it contains no implementation. At that date the only code was two documentation-generating scripts, later retired by `DEC-057`. `DEC-058` adds one audit tool with tests. No capability is implemented. Rules about tests, builds and dependencies are therefore recorded here for use once implementation begins. Until then, documentation batches apply them only as far as they are applicable (§8).

---

# 2. Recorded Contradictions and Gaps of Vocabulary — Not Resolved Here

Per `NO-INVENTION-RULES.md` (Ambiguous Information), `DOCUMENT-AUTHORITY-MATRIX.md` (Interpretation Rule) and `DEC-012`, the following are recorded and left unresolved.

| ID | Subject | Locations | Finding |
|---|---|---|---|
| AWM-C1 | Human approval and authority lists | `DEVELOPMENT-MAP.md` §14, §20; `SECURITY-MAP.md` §19, §77; `P00` §3, §5 | Six lists, different wording and item counts. `CLAUDE-CONSOLIDATION-REPORT.md` SECOND PASS §4S counts four lists in two documents and does not include the two in `P00`, which carry no cross-reference to the other four. |
| AWM-C2 | Change classification | `DEVELOPMENT-MAP.md` §16–20; `SECURITY-MAP.md` §21; `P00` §12 | Two scales: `LOW/MEDIUM/HIGH/CRITICAL` and `C0–C4`. No document maps one to the other. `S02` §26 uses the `C` scale. |
| AWM-C3 | Examples within the `LOW–CRITICAL` scale | `DEVELOPMENT-MAP.md` §18–19; `SECURITY-MAP.md` §21 | "Data pipeline change" is MEDIUM in `DEVELOPMENT-MAP.md` §18; "data-processing change" is HIGH in `SECURITY-MAP.md` §21. Whether these name the same thing is not established. "Scientific methodology change" is HIGH in `SECURITY-MAP.md` §21 and absent from `DEVELOPMENT-MAP.md` §17–20. |
| AWM-C4 | Stop conditions | `DEVELOPMENT-MAP.md` §12; `P00` §7 | Two lists that overlap partially. |
| AWM-C5 | Tranche content and completion | `DEVELOPMENT-MAP.md` §196, §198; `P00` §10, §11 | `P00` §10 also requires authorized changes, Definition of Done, resource budget and stop conditions. `DEVELOPMENT-MAP.md` §196 also requires a verification profile and expected risk. |
| AWM-C6 | Extent of autonomy | `DEVELOPMENT-MAP.md` §10, §18, §19; `P00` §12; `SECURITY-MAP.md` §77 | §10 grants batch autonomy explicitly for LOW-risk batches. `P00` §12 normally allows C0–C2 within a tranche. §18 does not say whether MEDIUM changes need approval. §19 requires HIGH changes to be "clearly reported and isolated"; `SECURITY-MAP.md` §77 triggers human review at HIGH. **Corrected by `DEC-048`:** `SECURITY-MAP.md` §75 permits autonomous batches only at LOW or approved MEDIUM, which this entry originally missed. |
| AWM-C7 | Audit result vocabulary | `DEVELOPMENT-MAP.md` §122, §123 | `PASS/WARN/FAIL` against the "suggested" `PASS/WARNING/BLOCKING`, in adjacent sections. |
| AWM-C8 | Evidence labels | `DEVELOPMENT-MAP.md` §23; `NO-INVENTION-RULES.md` | Five labels (`KNOWN, SUPPORTED, PLAUSIBLE, EXPERIMENTAL, UNKNOWN`) against seven evidence classes. Whether they classify the same thing is not established. |

**How work proceeds meanwhile (INFERENCE from `P00` §2 and §30, and `DEC-012`):** the lists stay separate and are read cumulatively. A trigger on any applicable list applies. This reading selects no list as authoritative and merges none. If two rules require incompatible actions, the procedure is `P00` §30: identify, record, identify affected documents, determine the authority level, stop if human authority is required, otherwise apply the higher-level rule.

---

# 3. Founding Principles (§2–6)

- **Cycle (§2):** DEFINE → IMPLEMENT → VERIFY → INTEGRATE → DOCUMENT → REVALIDATE. Running code is not by itself completion.
- **Role of the agent (§3):** an implementation and maintenance mechanism, not the final authority on scientific truth, security policy, project objectives or empirical validity. `PROJECT-MAP.md` §26 sets the same limit.
- **Runtime independence (§4–5, `DEC-001`):** AI may be used in development. Unless a future capability explicitly specifies otherwise, the core runtime must not require Claude, ChatGPT, an LLM API, an AI coding agent or cloud inference.
- **Local-first (§6):** local execution, local tests, deterministic tools, reproducible environments. External services are optional and explicitly controlled.

---

# 4. Work Batches (§7–11, §13, §15, §125)

Work is organized in bounded batches, so the human does not approve each small operation (§7).

**A batch declares (§8):** objective, scope, expected files, dependencies, validation requirements, security classification, completion criteria.

**Scope (§9):** the agent may modify the files a batch needs, provided they are within the declared project scope, the change stays consistent with the architecture, security boundaries are preserved and scientific assumptions are not silently changed.

**Autonomy (§10):** within a LOW-risk batch the agent may inspect, create and modify files, refactor, create and run tests, and update documentation, manifests and dependency metadata, without stopping after each operation. See AWM-C6 for other risk levels. `P00` §4 lists the agent's general authority.

**Routine decisions (§15):** taken autonomously when they do not change objectives, weaken security or invalidate scientific assumptions, and are reversible and tested.

**Reducing interruption (§13):** group compatible work, validate automatically, settle routine details independently, record uncertainty rather than asking repeatedly, and stop only at predefined boundaries.

**Completion (§11):** implementation exists; tests executed; relevant validation passes; documentation synchronized; dependency changes recorded; security-sensitive changes identified; unresolved issues reported.

**No hidden changes (§125):** unrelated files must not be modified to make a batch pass. Unrelated changes are separated or explicitly documented.

**Prohibitions (`P00` §8, invariants §9, `DEC-005`):** these bind every batch, including: no weakening of a requirement to pass a test, no disabling of validation, no concealed regression, no deletion of evidence required for reproducibility, no modification of audit history to conceal a change.

---

# 5. Change Classification (§16–20)

Every significant change is classified (§16). Because no mapping exists (AWM-C2), a change that needs classifying records **both** labels: `LOW–CRITICAL` per `DEVELOPMENT-MAP.md` §16 and `SECURITY-MAP.md` §21, and `C0–C4` per `P00` §12. The stricter resulting treatment applies (**INFERENCE**, from §2 above).

Effects stated by the sources:

| Label | Stated effect | Source |
|---|---|---|
| LOW | May normally be completed autonomously | §17 |
| MEDIUM | Stronger automated validation | §18 |
| HIGH | Clearly reported and isolated; human review trigger | §19; `SECURITY-MAP.md` §77 |
| CRITICAL | Explicit human approval | §20 |
| C0–C2 | Normally autonomous within an approved tranche | `P00` §12 |
| C3 | Normally requires an approval gate | `P00` §12 |
| C4 | Always requires human authority | `P00` §12 |

The examples for each class are in the cited sections and are not repeated here, per the cross-area guidance of `DOCUMENT-AUTHORITY-MATRIX.md`.

---

# 6. Decision Boundaries and Stop Conditions (§12, §14)

**Human decision is required** when a trigger on any list of AWM-C1 applies.

**The agent stops the batch** when a condition in `DEVELOPMENT-MAP.md` §12 or `P00` §7 occurs. The stop must be precise and actionable (§12). The agent repairs local failures first (`P00` §6).

**Conflicts between requirements** follow `S02` §26. The agent must not silently resolve a C3 or C4 conflict.

---

# 7. Phases and Preconditions for Implementation (§21–24)

- **Phases (§21):** PHASE 0 documentation and research; 1 architecture; 2 infrastructure; 3 core implementation; 4 capability implementation; 5 validation; 6 certification; 7 maintenance. The project may iterate between phases. The phase model is conceptual.
- **Documentation before implementation (§22):** a major capability needs an adequate specification defining purpose, inputs, outputs, constraints, dependencies, validation and failure behavior.
- **Research before capability (§23):** where a capability depends on scientific claims, implementation follows research review, distinguishing the labels of §23 (see AWM-C8).
- **Scientific uncertainty (§24):** an unresolved research question must not become an apparently settled implementation rule without documenting the assumption, in `docs/00-project/ASSUMPTION-REGISTRY.md`. `P00` §28 prohibits fabricated evidence, altered data, omitted unfavorable results, silent changes of statistical method and changing evaluation criteria after seeing results.

---

# 8. Consistency Reviews (§115–123)

At the end of every substantial batch the agent performs a repository-wide consistency check (§115) over: project map, affected architecture documents and specifications, security, data, validation and development documentation, decision log, assumption registry and documentation change queue.

| Review | Checks | Applicable with no implementation |
|---|---|---|
| Dependency (§116) | Imports, declared dependencies, manifests, configuration, capability registry, dataset/model dependencies | Not until code exists |
| Interface (§117) | Callers, implementations, tests, documentation | Documentation part only |
| Documentation (§118) | Obsolete names, old paths, removed capabilities, stale versions, contradictory requirements, references to nonexistent files | Yes |
| Security (§119) | Network calls, permissions, subprocesses, dynamic loading, credentials, external transmission | Not until code exists, except when a document changes a security rule |
| Scientific (§120) | Experimental assumptions, benchmark definitions, acceptance criteria, language scope, interpretation of results | Yes |
| Data (§121) | Dataset identifiers, versions, manifests, checksums, declared dependencies, storage requirements | Documentation part only |

The right-hand column is an **INFERENCE** from §1.

**Automated audit (§122):** the project "should eventually" provide a command for these checks. `tools/verify_docs.py` (`DEC-058`) implements part of it; the remaining checks are performed by the agent directly. Result vocabulary is recorded at AWM-C7. A WARNING may be reported without stopping a batch; a BLOCKING issue prevents completion (§123).

---

# 9. Batch Report and Final States (§124, §188–194)

The agent runs the quality gate before reporting completion and does not rely on the user to discover routine inconsistencies (§188).

**Batch report (§124):** objective; files changed; tests run, passed and failed; dependencies changed; security impact; documentation impact; unresolved questions; recommended next batch.

| Final state (§189) | Meaning |
|---|---|
| `COMPLETE` (§190) | All required checks pass |
| `COMPLETE_WITH_WARNINGS` (§191) | Required checks pass; non-blocking warnings documented |
| `BLOCKED` (§192) | A decision or dependency outside the autonomous boundary prevents progress |
| `FAILED` (§193) | Implementation or validation failed; failure evidence remains available |

**Next batch (§194):** identified where useful; scope is not expanded automatically because more work is obvious.

---

# 10. Audit Trail and Human Review (§170–173)

Material actions must be recoverable from version control, decision log, change queue, experiment metadata and release metadata (§170). It must be possible to determine what the agent changed in a batch (§171).

Human review focuses on architecture, scientific interpretation, security boundaries and major changes (§172; `P00` §19). A review package contains summary, changed files, tests, risk classification, documentation changes and unresolved questions, prepared automatically (§173).

---

# 11. Tranches (§195–200; `P00` §10–11; `DEC-004`)

A tranche is a meaningful unit of work and may contain several batches (§195). The human approves its boundary; the agent then executes within it (§197; `P00` §10). A tranche should be large enough to justify review and bounded enough to control risk (§200).

**A tranche definition carries the fields of both sources (AWM-C5):** objective, scope and authorized changes, expected deliverables, completion criteria and Definition of Done, verification profile and criteria, expected risk, resource budget, stop conditions.

**Completion** requires the criteria of both §198 and `P00` §11. If they cannot be met, the agent reports `BLOCKED` rather than redefining them (`P00` §11).

**Deviation (§199):** a necessary change outside the tranche is implemented only if clearly LOW-risk and within existing architecture. Otherwise it is recorded and the agent stops at the appropriate boundary.

**Operating model (§201):** the human defines objectives and approves boundaries; the agent implements, tests, audits and maintains within them; automated validation checks consistency, correctness, security and reproducibility; documentation preserves context; scientific validation decides whether a capability is scientifically supported.

---

# 12. Operating Context of the Project (recorded per `DEC-010`)

Recorded 2026-11-09. These are facts about the current way of working, not requirements on the software.

- **Owner's instruction (2026-11-09):** the owner works only through the GitHub web interface and does not run terminal commands. The agent performs git operations itself.
- **Access:** a cloud session authorized for this repository can clone and push directly. This replaces the bundle workflow of the 2026-11-08 handoff.
- **Volatility:** session containers are temporary, so work must be pushed. `DEC-010` applies.
- **Git practice (PROPOSAL, derived from `P00` §8 and the 2026-10-05 incident recorded in the project's status notes):** no force pushes or rewriting of published history by the agent. The owner enabled protection of `main` against force push and deletion on 2026-11-09 (verified).
- **Relation to §6 of the map:** whether cloud session containers count as "local" for the purposes of `DEVELOPMENT-MAP.md` §6 is not established. It becomes relevant when tests first run; see AWM-G6.

---

# 13. Evidence Basis and Gaps

No research finding on AI-assisted software development was located in `docs/00-project/RESEARCH-REGISTRY.md` (searched 2026-11-09 for coding-agent and autonomy terms). `R01` §91–92 and §113–114 cover AI assistance in literature review only and are not extended here. The rules above therefore rest on governance, not on empirical evidence about their effectiveness. No `R-XXXX` is cited because none applies.

| ID | Gap | Would normally belong in |
|---|---|---|
| AWM-G1 | No mapping between `LOW–CRITICAL` and `C0–C4` (AWM-C2) | Governance decision |
| AWM-G2 | Corrected by `DEC-048`: `SECURITY-MAP.md` §75 allows autonomy at LOW or approved MEDIUM. Remaining gap: how a MEDIUM batch is approved (`AGENT-SECURITY-BOUNDARY.md` ASB-G3) and how §75 relates to `P00` §12 | `P00` / this document |
| AWM-G3 | Partly addressed by `tools/verify_docs.py` (`DEC-058`); §116, §117, §119–121 are not automated | Implementation tranche |
| AWM-G4 | "Resource budget" in `P00` §7, §10: no definition of unit or convention for a tranche was found. Other uses in the corpus concern storage and runtime (`DATA-MODEL.md` §7) | `P00` |
| AWM-G5 | "Substantial batch" (§115), "significant change" (§16) and "major capability" (§22) have no stated criterion | This document, by decision |
| AWM-G6 | Status of cloud session containers with respect to §6 | Owner decision before implementation |

No value has been supplied for any of these. **Update 2026-11-09:** AWM-G1, AWM-G4 and AWM-G6 are decided by `DEC-057`; see `OPEN-QUESTIONS.md`.

---

# 14. Coverage of the Parent Sections

| Parent sections | Covered in |
|---|---|
| §2–6 | §3 |
| §7–11, §13, §15 | §4 |
| §12, §14 | §6 |
| §16–20 | §5 |
| §21–24 | §7 |
| §115–123 | §8 |
| §124 | §9 |
| §125 | §4 |
| §170–173 | §10 |
| §188–194 | §9 |
| §195–201 | §11 |
