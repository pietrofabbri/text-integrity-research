# Resilience and Security Assurance

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Security protocol (Tranche 4 of `SECURITY-MAP.md` §92)
**Authority:** Security. Certification decisions remain with `docs/10-certification/CERTIFICATION-MAP.md`; validation gates with `docs/05-validation/VALIDATION-GATES.md`.
**Parent:** `docs/06-security/SECURITY-MAP.md` §34–35, §63–72, §79–91
**Requirements basis:** `docs/03-scientific-specification/S02-scientific-requirements.md` `REQ-SEC-004`
**Research basis:** `R-0015`, `R-0022`, `R-0040`, `R-0086`, `KB-011` (§8), as propagated from `DCQ-006` and `DCQ-007`
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-009, DEC-012, DEC-046, DEC-050 (this document's execution)

---

# 1. Purpose & Scope

This document formalizes how the system withstands failure, how security is tested and tracked, and how security relates to certification and research. It sets no resource limit, severity scale or deadline. These are requirements, not guarantees: nothing is implemented, and the area's current state remains as `SECURITY-MAP.md` §90 says: boundaries are being defined, with the priority of establishing safe defaults before significant implementation.

---

# 2. Recorded Contradictions and Ambiguities — Not Resolved Here

| ID | Subject | Locations | Finding |
|---|---|---|---|
| RSA-C1 | Status vocabularies | `SECURITY-MAP.md` §67, §71; `DEVELOPMENT-MAP.md` §72, §189 | §71 is another enumeration (`SECURE_BASELINE, MONITORED, EXPERIMENTAL, VULNERABLE, MITIGATION_REQUIRED, DEPRECATED, RETIRED`) sharing terms with lifecycle lists (`CAPABILITY-EVOLUTION-POLICY.md` CEP-C1). §67's interruption states are a further list. Whether §71 is a security dimension separate from lifecycle is not established; deferred per `DEC-012`. |
| RSA-C2 | Conditions before `ACTIVE` | `SECURITY-MAP.md` §86; `DEVELOPMENT-MAP.md` §29; `CAPABILITY-ARCHITECTURE.md` §7 | Three sets of conditions. **INFERENCE:** cumulative. |
| RSA-C3 | Vulnerability severity | `SECURITY-MAP.md` §21, §70, §81 | §70 requires a severity and §81 refers to "critical vulnerabilities". §21's scale classifies changes, not vulnerabilities. No vulnerability severity scale is defined. |

---

# 3. Logging and Errors (§34–35)

Logs record enough for diagnostics without unnecessarily recording user text, preferring hashes, identifiers, sizes, capability IDs, versions, timestamps and error categories (§34). Errors must not expose secrets, credentials, sensitive text, private filesystem information or external-service authentication data (§35).

---

# 4. Resilience (§63–67)

- **Resource exhaustion (§63):** defend against excessive input length, memory, CPU, disk consumption, archive expansion and model loading. Limits are configurable; no value is set.
- **Denial of service (§64):** local processing fails predictably when limits are exceeded. A single input must not consume unlimited resources.
- **Failure isolation (§65):** one failed experiment must not corrupt benchmark datasets, capability registry, configuration, previous results or canonical input.
- **Atomic writes (§66):** where practical, for experiment results, registry updates, configuration changes and generated reports.
- **Recovery (§67):** after interruption the system distinguishes completed, failed, incomplete, corrupted and unavailable. Incomplete results must not be interpreted as successful experiments.

---

# 5. Testing, Vulnerabilities, Exceptions (§68–72)

**Security testing (§68):** malformed and oversized input, malicious archives, path traversal, dependency vulnerabilities, network isolation, unexpected external requests, unsafe deserialization, permission violations.

**Regression (§69):** security tests run after changes affecting dependencies, file handling, network, external integrations, model loading, plugin loading or configuration.

**Vulnerabilities (§70):** recorded with identifier, affected component, severity, exploitability, mitigation, status and affected versions. No register exists yet (RSA-G2).

**Status (§71):** see RSA-C1.

**Exceptions (§72):** granted only when the reason is documented, affected components identified, risk understood, mitigation defined where possible and an expiration or review date exists. Permanent undocumented exceptions are prohibited. Accepting an unresolved security exception normally requires human approval (§19).

---

# 6. Documentation and Certification (§79–81, §86, §89)

**Synchronization (§79):** if code changes permissions, network behavior, dependencies, data handling or trust boundaries, the change queue is updated before the change is complete.

**A security change identifies (§80):** affected component, threat, change, mitigation, tests, dependencies, documentation, residual risk. Substantive changes are traceable (`REQ-SEC-004`).

**Security certification (§81):** a release should not be certified if critical vulnerabilities remain unresolved, external network behavior is undocumented, sensitive credentials are present, trust boundaries are unclear or required security tests fail. Security and scientific certification are distinct (`CERTIFICATION-MAP.md` §147).

**Before `ACTIVE` (§86; see RSA-C2):** dependencies reviewed; permissions defined; input handling and failure behavior tested; network behavior known; data handling documented; relevant security regressions pass.

**Lifecycle (§89):** security is continuous. A capability safe under one dependency version may need reassessment after an update.

---

# 7. Security and Science (§82–85)

- **Reproducibility (§82):** controls must not compromise it. Logs may minimize text, reports may store hashes and external calls may be restricted, but enough metadata must remain to understand the experiment.
- **External detectors (§83):** analytically separated from the trusted core. A provider must not be able to execute arbitrary local code, or modify local configuration, datasets or scientific results.
- **Watermark research (§84):** experimental capabilities that do not automatically receive network access, unrestricted filesystem access or privileged execution. Research relevance does not imply security trust.
- **Transformations (§85):** must not overwrite original input, silently send text externally, modify unrelated files, alter validation configuration or disable integrity checks.

---

# 8. Research Findings Relevant to Security (propagated from `DCQ-006`, `DCQ-007`)

These are research findings, not requirements (`DEC-009`). No decision to expose any detection API has been made.

| Finding | Source | Status of the evidence | Security relevance |
|---|---|---|---|
| A public watermark-detection API may enable oracle-style removal or spoofing, and so be an attack surface in itself | `R-0040`; `R02` §37.2; `R03` §43.4 | Registry marks all specific figures UNVERIFIED (single paper, author-reported). The qualitative trade-off is the better-supported claim | Any future decision to expose such an API must assess this. `R03` §43.4 names rate limiting and access control as the absent protections, and links watermark stealing (`R-0015`) |
| Translation-based evasion is a separate attack class from paraphrasing | `KB-011`; `R-0065`, `R-0066`, `R-0068`, `R-0069` (`R-0067` is INCONCLUSIVE) | Multiple sources, per `KB-011` | Threat assumptions for watermark and detector capabilities must not assume paraphrasing is the only evasion route |
| Detector bias against non-native writers, and prevalence dependence of false positives | `R-0022`, `R-0086`; `REQ-AID-004`, `REQ-STAT-004` | Handled in `STATISTICAL-VALIDATION-METHODOLOGY.md` | Per `DCQ-007`, these must not be silently absent where false-positive rates are discussed. A false accusation arising from a detector result is a harm that security review does not by itself address |

No control, threshold or rate limit is defined here. Those would require a decision about exposure first (RSA-G4).

---

# 9. Incidents and Historical Integrity (§87–88)

**Incident response (§87):** (1) stop affected capability; (2) preserve evidence; (3) identify affected versions; (4) assess scope; (5) mitigate; (6) run regression tests; (7) update documentation; (8) decide whether historical results are affected.

**Historical integrity (§88):** incidents must not silently rewrite historical scientific results; affected results are marked.

---

# 10. Governing Principle (§90–91)

The aim is neither to forbid automation nor to let the agent do anything: automation operates freely inside a clearly defined, automatically verified perimeter, and stops only when that perimeter would change (§91). The perimeter is not yet automatically verified (`AGENT-SECURITY-BOUNDARY.md` ASB-C4).

---

# 11. Gaps

| ID | Gap | Would normally belong in |
|---|---|---|
| RSA-G1 | Resource limit values (§63) are undefined | Per-capability or configuration decision |
| RSA-G2 | No vulnerability register or severity scale exists (RSA-C3) | Implementation tranche |
| RSA-G3 | Who grants and reviews exceptions in practice (§72), beyond §19 | Owner decision |
| RSA-G4 | No decision on exposing a public detection API; `DEC-046` and this document make none | Owner decision if ever proposed |
| RSA-G5 | Translation-based evasion is not yet named in `R02` §37.2 and `R03` §43.4 (recorded by `DCQ-006` as a lower-priority research-layer update) | `02-research` |

No value has been supplied for any of these.

---

# 12. Coverage of the Parent Sections

| Parent sections | Covered in |
|---|---|
| §34–35 | §3 |
| §63–67 | §4 |
| §68–72 | §5 |
| §79–81, §86, §89 | §6 |
| §82–85 | §7 |
| §87–88 | §9 |
| §90–91 | §10 |
