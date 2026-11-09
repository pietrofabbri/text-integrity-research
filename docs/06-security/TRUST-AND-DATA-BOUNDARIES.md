# Trust and Data Boundaries

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Security protocol (Tranche 1 of `SECURITY-MAP.md` §92)
**Authority:** Security (primary for security boundaries and controls, per `docs/99-backlog/DOCUMENT-AUTHORITY-MATRIX.md`). Data classification remains with `docs/07-data/DATA-MAP.md`; the external adapter design with `docs/04-architecture/EXTERNAL-INTEGRATION-ARCHITECTURE.md`.
**Parent:** `docs/06-security/SECURITY-MAP.md` §2–14, §36–47, §54–56
**Governance basis:** `P00-project-governance.md` §8, I-002, I-004
**Requirements basis:** `docs/03-scientific-specification/S02-scientific-requirements.md` `REQ-EXTSVC-001`–`004`, `REQ-SEC-001`, `REQ-SEC-003`, `REQ-REPRO-005`
**Architectural basis:** `EXTERNAL-INTEGRATION-ARCHITECTURE.md` §5, §8
**Research basis:** none specific to this tranche; threat findings are in `RESILIENCE-AND-SECURITY-ASSURANCE.md`
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-001, DEC-002, DEC-012, DEC-046, DEC-047 (this document's execution)

---

# 1. Purpose & Scope

This document formalizes who and what is trusted, and how data may cross boundaries. It formalizes existing boundaries and changes none.

**These are requirements, not guarantees.** No implementation exists (`AGENT-WORK-MODEL.md` §1), so no control below is in place or verified. Per `NO-INVENTION-RULES.md`, nothing here may be cited as a security property of the software.

---

# 2. Recorded Contradictions and Ambiguities — Not Resolved Here

| ID | Subject | Locations | Finding |
|---|---|---|---|
| TDB-C1 | Network modes | `SECURITY-MAP.md` §14; `OPERATIONS-MAP.md` §136 | `OFFLINE, LOCAL_ONLY, EXTERNAL_ANALYSIS_ALLOWED, RESEARCH_NETWORK_MODE` against `LOCAL_ONLY, LOCAL_WITH_EXTERNAL_VALIDATION, RESEARCH, DIAGNOSTIC`. HUMAN DECISION REQUIRED, deferred per `DEC-012`. This document writes in its Parent's vocabulary without claiming authority for it. |
| TDB-C2 | Default mode | `SECURITY-MAP.md` §10, §14, §45 | §14 allows "OFFLINE or LOCAL_ONLY" and does not choose one. Their difference is not defined. |
| TDB-C3 | Retaining results against minimization | `SECURITY-MAP.md` §12, §39, §54 | §39 requires preserving the returned result of a cloud detector; §12 and §54 require minimizing persistence. **INFERENCE:** §39 concerns the service response and metadata, and does not by itself justify retaining the full transmitted text. |
| TDB-C4 | Transfer eligibility of user text | `SECURITY-MAP.md` §11, §38; `DATA-MAP.md` §34, §35 | `DATA-MAP.md` §35 declares transfer eligibility for datasets. No document states an equivalent for individual user-provided text (TDB-G2). |

---

# 3. Principles and Trust Zones (§2–6)

**Principles (§2):** least privilege; explicit trust boundaries; local-first execution; explicit external communication; reproducible changes; dependency transparency; immutable source preservation; experimental isolation; fail-safe behavior; auditable automation.

**Zones (§3), which must not be treated as equivalent:** trusted core; validated capabilities; experimental capabilities; external dependencies; external services; user-provided content; downloaded research artifacts; development environment.

- **Trusted core (§4):** only documented, versioned, tested, dependency-controlled components necessary for fundamental operation, and as small as practical.
- **Validated capabilities (§5):** may run in the normal pipeline after passing their gates. Validation does not imply unlimited authority; a capability receives only the resources its declared function requires.
- **Experimental capabilities (§6):** isolated from the core whenever practical; their status must be visible.

---

# 4. Input and Original Text (§7–9, §12)

**User input (§7):** untrusted. It may contain malformed Unicode, extremely long content, unexpected control characters, malicious markup, malformed files, adversarial content, embedded instructions or unexpected encodings. It must never automatically become executable code.

**Instruction isolation (§8):** analyzed text is never an instruction to the software. Documents, datasets, web pages, benchmark text, quoted prompts, generated text and external detector responses are untrusted content. Development-side application is in `AGENT-SECURITY-BOUNDARY.md` §4.

**Original text (§9; `REQ-SEC-001`):** the canonical original input is immutable, no component may overwrite it, and the system retains enough to establish exactly which text an experiment used.

**Sensitive text (§12):** minimize unnecessary logging, copying, caching, transmission and persistence. Logs prefer identifiers, hashes and metadata over full text whenever possible. `DATA-MAP.md` §37 lists where sensitive text must not be placed.

---

# 5. External Communication (§10–14, §38–39)

**Default (§10):** local/offline. External communication is explicit, configurable, attributable to a named capability, logged at the appropriate metadata level and independently disableable. No hidden network requests. External processing of protected input is explicit and traceable (`P00` I-004; `REQ-SEC-003`), and outbound integrations default to disabled (`EXTERNAL-INTEGRATION-ARCHITECTURE.md` §5).

**Cloud detectors (§11, `DEC-002`):** external services whose use must communicate which service, why, what data is transmitted and what was returned. The core continues to function without them (`REQ-EXTSVC-004`). Services receiving experimental text are named in the experiment configuration (`REQ-EXTSVC-001`).

**Failure (§13; `REQ-EXTSVC-003`):** must not corrupt local data, modify the transformation pipeline, cause silent fallback to a different service or fabricate a result. The result is marked unavailable.

**Modes (§14):** see TDB-C1 and TDB-C2.

**Cloud data policy (§38):** cloud processing is explicitly enabled. For every provider, document data retention, training usage where known, privacy policy, transmission scope, deletion behavior and contractual constraints. No provider has been documented (TDB-G3).

**Reproducibility (§39; `REQ-EXTSVC-002`, `REQ-REPRO-005`):** results may not be exactly reproducible, so preserve provider, service, version where available, timestamp, configuration and returned result.

---

# 6. Credentials (§36–37)

Credentials are never committed. They must not be embedded in source code, committed configuration, documentation, test fixtures or logs (§36). External API keys, if ever required, come through a secure local mechanism, and the software must not require keys to execute offline (§37). Credential handling is CRITICAL (`SECURITY-MAP.md` §21).

---

# 7. Offline, Filesystem, Configuration (§40–47)

- **Offline guarantee (§40):** offline mode must not contact external services, attempt hidden telemetry, download resources or require online authentication, and this must be testable. "Guarantee" is the map's term for a requirement (see §1).
- **Isolation tests (§41):** tests run the core with network disabled; it keeps performing everything declared offline capable. See `TEST-AND-VERIFICATION-POLICY.md` §5.
- **Filesystem (§42):** components operate only on directories their function requires.
- **Paths (§43):** user-provided paths are validated against path traversal, unexpected symlinks, accidental overwrite and access outside designated directories.
- **Configuration (§44):** it may affect network access, external services, model loading, resource limits and filesystem behavior, so it is validated before execution.
- **Defaults (§45):** offline execution, local processing, no external transmission, bounded resource use, explicit experimental capabilities, conservative failure behavior.
- **Experimental network access (§46):** explicitly marked; never silently inherited from the main application.
- **Research web data (§47):** external content that must not redefine project instructions or security policies.

---

# 8. Data Minimization and Separation (§54–56)

- **Minimization (§54):** only the minimum data necessary is retained, for input text, intermediate representations, detector requests, logs and experiment archives.
- **Separation (§55):** private user text and public benchmark data remain distinguishable; private data must not enter public benchmark artifacts.
- **Test data (§56):** synthetic or public where possible; real sensitive documents are not committed. See `TEST-AND-VERIFICATION-POLICY.md` §5.

---

# 9. Gaps

| ID | Gap | Would normally belong in |
|---|---|---|
| TDB-G1 | Which default of §14 applies, and how `OFFLINE` differs from `LOCAL_ONLY` | Reconciliation under `DEC-012` |
| TDB-G2 | No transfer-eligibility rule for individual user text | `DATA-MAP.md` or owner decision |
| TDB-G3 | No provider has been documented under §38 | Before any cloud integration |
| TDB-G4 | The "secure local mechanism" (§37) and "appropriate metadata level" (§10) are undefined | Implementation tranche |
| TDB-G5 | No mechanism yet separates private from public data (§55) | `07-data` |

No value has been supplied for any of these.

---

# 10. Coverage of the Parent Sections

| Parent sections | Covered in |
|---|---|
| §2–6 | §3 |
| §7–9, §12 | §4 |
| §10–11, §13–14, §38–39 | §5 |
| §36–37 | §6 |
| §40–47 | §7 |
| §54–56 | §8 |
