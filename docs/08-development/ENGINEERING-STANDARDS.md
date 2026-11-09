# Engineering Standards

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Development process protocol (Tranche 3 of `DEVELOPMENT-MAP.md` §202)
**Authority:** Development (engineering workflow). Security controls on dependencies remain with `docs/06-security/SECURITY-MAP.md`; data and model provenance with `docs/07-data/DATA-MAP.md`.
**Parent:** `docs/08-development/DEVELOPMENT-MAP.md` §67–82, §104–109, §126–132
**Governance basis:** `P00-project-governance.md` I-006
**Requirements basis:** `docs/03-scientific-specification/S02-scientific-requirements.md` `REQ-REPRO-002`, `REQ-REPRO-003`
**Research basis:** none specific; these are engineering rules and no `R-XXXX` applies
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-005, DEC-012, DEC-040, DEC-041, DEC-043 (this document's execution)

---

# 1. Purpose & Scope

This document formalizes code quality, result reporting, builds, dependencies, change history, release candidates and generated files. It selected no language or tool when written (ENG-G1); `DEC-057` has since selected Python and the first tools. It sets no numeric value.

---

# 2. Recorded Contradictions, Duplications and Risks — Not Resolved Here

| ID | Subject | Locations | Finding |
|---|---|---|---|
| ENG-C1 | Release readiness | `DEVELOPMENT-MAP.md` §108; `OPERATIONS-MAP.md` §183; `DATA-MAP.md` §117; `CERTIFICATION-MAP.md` §149 | Four area-specific checklists. `DEC-012` keeps them separate and cross-referenced. **INFERENCE:** a release must satisfy each one that applies. |
| ENG-C2 | Result vocabularies | `DEVELOPMENT-MAP.md` §72; `REPORTING-ARCHITECTURE.md` §5 | §72: `SUCCESS, PARTIAL, FAILED, UNAVAILABLE, INVALID, NOT_EVALUATED`, for operations. Reporting: `not measurable, unsupported, not applicable`, for dimensions in a report. Whether they should correspond is not established. |
| ENG-C3 | Dependency metadata | `DEVELOPMENT-MAP.md` §77; `SECURITY-MAP.md` §25 | Overlapping field lists. §77 adds compatibility information; §25 adds dependency relationship and security status, and applies to runtime dependencies. **INFERENCE:** record the fields of both. |
| ENG-C4 | Update classes | `DEVELOPMENT-MAP.md` §79; `SECURITY-MAP.md` §27 | §79 sets a procedure; §27 adds a required distinction between patch, minor, major and security updates. Compatible; both apply. |
| ENG-R1 | **Generator scripts that would overwrite maintained documents** | `update_project_map.py`, `update_research_map.py` (repository root); §126–128 | Each script writes a fixed embedded text over its target. Verified 2026-11-09: the embedded texts are older and shorter than the current documents (17,131 against 22,387 characters for `PROJECT-MAP.md`; 14,703 against 17,614 for `RESEARCH-MAP.md`). Running either would discard later edits. Disposition is an owner decision (ENG-G4). Until then the agent must not run them. **Update:** retired by `DEC-057` and removed; recoverable from Git history. |

---

# 3. Code Quality (§67–71, §74)

- **Automated checks (§67):** syntax, formatting, linting, type consistency where applicable, dependency integrity, tests.
- **Static analysis (§68):** where it materially improves reliability; stronger inspection for security-sensitive code.
- **Types (§69):** explicit types preferred for important interfaces where the language supports them.
- **Errors (§70):** explicit, categorized, actionable, non-destructive. Silent failure is discouraged.
- **Fail-safe (§71):** when an operation cannot be established as safe or valid, prefer explicit failure, degraded capability or an unavailable result to fabricated success.
- **Logging (§74):** enough for diagnostics, respecting the security and privacy maps.

---

# 4. Honest Results (§72–73)

Important operations distinguish `SUCCESS`, `PARTIAL`, `FAILED`, `UNAVAILABLE`, `INVALID` and `NOT_EVALUATED` (§72; see ENG-C2).

The software must never infer a successful scientific result merely because a pipeline completed technically (§73). `TEST-AND-VERIFICATION-POLICY.md` §8 states the corresponding rule for verification.

---

# 5. Builds and Environment (§75–76, §132)

- **Reproducible builds (§75):** where practical, from source, dependency versions, configuration and declared artifacts.
- **Environment (§76):** runtime versions, operating system assumptions, system dependencies and package dependencies are declared.
- **Reproducibility for others (§132):** another developer or agent can understand how to install, test, run offline, validate and reproduce a result.

---

# 6. Dependencies (§77–82)

Every dependency has purpose, version, license, source and compatibility information (§77); see ENG-C3. New dependencies are recorded and validated (`P00` I-006). `P00` §4 allows the agent to install only previously authorized dependencies.

- **Minimization (§78):** avoid dependencies for functionality safely implementable with existing components. Each adds maintenance cost, security surface, compatibility risk and storage cost.
- **Updates (§79):** deliberate; afterwards run tests, inspect the changelog where available, inspect security implications, verify scientific regressions where relevant. See ENG-C4.
- **Pinning:** `SECURITY-MAP.md` §26 and `OPERATIONS-MAP.md` §30 govern it. `REQ-REPRO-003` requires scientifically relevant dependency versions to be recorded.
- **Supply chain:** downloaded packages, models, datasets, binaries and scripts are untrusted until provenance and intended use are evaluated (`SECURITY-MAP.md` §28).
- **Retirement (§80):** unused dependencies are removed.
- **Models (§81):** versioned like software dependencies, because an update may change scientific behavior with unchanged code. `DATA-MAP.md` §9 requires provenance and version metadata.
- **Datasets (§82):** dataset version is part of experiment identity.

---

# 7. Change History and Reversibility (§104–107)

- **Commits (§104–105):** logically grouped, ideally one coherent engineering purpose; messages describe the purpose rather than list files.
- **Revertability (§106):** important changes are reversible, and before risky changes the previous state must be reconstructable.
- **Rollback (§107):** mechanisms exist for capability activation, dependency updates, configuration changes and migrations.

History rewriting is addressed in `AGENT-WORK-MODEL.md` §12.

---

# 8. Release Candidate and Release Artifact (§108–109)

**Before a release (§108):** tests pass, security checks pass, data manifests validate, documentation is synchronized, dependencies are recorded and certification status is known. See ENG-C1. Release approval is reserved to the human (`P00` §3, §5). Release validation is governed by `VALIDATION-GATES.md`.

**A release identifies (§109):** software version, source revision, dependency versions, dataset versions, model versions, configuration and validation status.

---

# 9. Generated Files and Repository Cleanliness (§126–131)

- **Generated files (§126):** distinguishable from authoritative sources, and documented as generated.
- **Source of truth (§127):** identified for every important artifact, for example specification → documentation; generated configuration → source template; benchmark manifest → benchmark definition; compiled artifact → source code.
- **Regeneration (§128):** reproducible from the source of truth where practical. See ENG-R1 for the case where the embedded source is out of date.
- **Build artifacts (§129):** not normally authoritative.
- **Temporary artifacts (§130):** must not silently become dependencies.
- **Cleanliness (§131):** before completing a batch, remove unnecessary temporary files, debug outputs, caches and generated artifacts not required for reproducibility. This does not authorize removing evidence (`P00` I-003). `docs/03-scientific-specification/_to_delete` remains in place per `DEC-012`.

---

# 10. Gaps

| ID | Gap | Would normally belong in |
|---|---|---|
| ENG-G1 | Implementation language and tooling are not selected | Decision before Phase 2 (`DEVELOPMENT-MAP.md` §21) |
| ENG-G2 | The "project's reproducibility policy" cited by `SECURITY-MAP.md` §26 was not located as a named document | `06-security` or this area |
| ENG-G3 | Which dependencies are "scientifically relevant" (`REQ-REPRO-003`) or "important" (§26, §69, §106) has no stated criterion | Per-capability specification |
| ENG-G4 | Disposition of the two generator scripts (ENG-R1): retire, correct or keep | Owner decision |
| ENG-G5 | No dependency register exists yet | Implementation tranche |

No value has been supplied for any of these. **Update 2026-11-09:** ENG-G1 and ENG-G4 are decided by `DEC-057`; see `OPEN-QUESTIONS.md`.

---

# 11. Coverage of the Parent Sections

| Parent sections | Covered in |
|---|---|
| §67–71, §74 | §3 |
| §72–73 | §4 |
| §75–76, §132 | §5 |
| §77–82 | §6 |
| §104–107 | §7 |
| §108–109 | §8 |
| §126–131 | §9 |
