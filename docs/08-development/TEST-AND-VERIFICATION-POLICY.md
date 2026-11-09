# Test and Verification Policy

**Status:** ACTIVE
**Version:** 0.1
**Document type:** Development process protocol (Tranche 2 of `DEVELOPMENT-MAP.md` §202)
**Authority:** Development (test and verification workflow). Scientific validation methodology remains with `docs/05-validation/`; security boundaries with `docs/06-security/SECURITY-MAP.md`.
**Parent:** `docs/08-development/DEVELOPMENT-MAP.md` §46–66, §159–169, §187
**Requirements basis:** `docs/03-scientific-specification/S02-scientific-requirements.md` `REQ-REPRO-004`, `REQ-REPRO-005`, `REQ-VAL-003`
**Research basis:** `docs/02-research/R07-evaluation-statistical-methodology.md` §28–30, §80.2 (`R-0087`, `R-0088`, `R-0089`)
**Related decisions:** `docs/00-project/DECISION-LOG.md` DEC-005, DEC-036–DEC-039, DEC-040, DEC-041, DEC-042 (this document's execution)

---

# 1. Purpose & Scope

This document formalizes how software is tested and verified. It sets no threshold, tolerance, sample size or coverage target (`NO-INVENTION-RULES.md`). No test suite exists yet (`AGENT-WORK-MODEL.md` §1), so its rules apply from the first implementation batch.

**Boundary with `05-validation`:** tests here establish that software behaves as specified. Whether a scientific conclusion holds is governed by `STATISTICAL-VALIDATION-METHODOLOGY.md`, `FIDELITY-VALIDATION-PROTOCOL.md`, `DETECTOR-VALIDATION-PROTOCOL.md` and `VALIDATION-GATES.md`, whose content is not restated. §53 states the same distinction: scientific tests are distinct from ordinary software correctness tests.

---

# 2. Recorded Contradictions and Gaps of Vocabulary — Not Resolved Here

| ID | Subject | Locations | Finding |
|---|---|---|---|
| TVP-C1 | Severity vocabulary | `DEVELOPMENT-MAP.md` §122, §123, §167 | §167 uses "blocking check" and "non-blocking warning", compatible with §123 but not with §122's `PASS/WARN/FAIL` (`AGENT-WORK-MODEL.md` AWM-C7). |
| TVP-C2 | Two quality gates of different scope | `DEVELOPMENT-MAP.md` §187; `VALIDATION-MAP.md` §73 | §187 judges a development batch; §73 judges reliance on a major scientific conclusion. **INFERENCE:** they are not duplicates, and passing §187 says nothing about §73. |
| TVP-C3 | Test isolation and network tests | `DEVELOPMENT-MAP.md` §59, §61 | §59 says tests should not depend on network availability; §61 admits network-dependent tests if clearly identified. **INFERENCE:** read together, network-dependent tests are identified exceptions outside the §60 offline suite. |

---

# 3. Test Categories (§46–55)

Tests are written before or alongside implementation where practical, and the project should not depend exclusively on manual inspection (§46).

| Category (§47) | Requirement | Section |
|---|---|---|
| Unit | Isolated behavior; deterministic wherever possible | §48 |
| Integration | Interactions between capabilities, such as preprocessing → transformation, transformation → validation, dataset → experiment, detector adapter → result normalization | §49 |
| Regression | Every important discovered failure becomes a regression test when practical. `REQ-VAL-003` requires that accepted scientific behaviour is not invalidated without detection | §50 |
| Security | Cover the boundaries of the security map; `SECURITY-MAP.md` §68 lists the content | §51 |
| Data | Manifests, checksums, expected schemas, encodings, resource availability | §52 |
| Scientific | Properties relevant to the research hypothesis | §53 |
| Performance | Execution time, memory, storage, throughput, scalability; not optimized at the expense of scientific validity without explicit justification | §54 |
| Reproducibility | Repeat with the same input, dataset, configuration, software version and resource versions, within defined tolerances | §55 |

---

# 4. Determinism, Seeds and Tolerances (§56–58)

Components are identified as `DETERMINISTIC` or `STOCHASTIC`. For stochastic components record seed, sampling parameters, model version and relevant environment (§56; `REQ-REPRO-004`).

Tests use fixed seeds when deterministic behavior is required; experimentation may intentionally use multiple seeds (§57).

Floating-point comparisons use defined tolerances where appropriate (§58). No project document defines these values (TVP-G1).

Experiments depending on mutable external services record that exact historical reproduction may be impossible (`REQ-REPRO-005`).

---

# 5. Isolation, Offline Operation and External Services (§59–63)

- **Isolation (§59):** tests do not depend on previous execution, undeclared local files, network availability or developer-specific configuration (see TVP-C3).
- **Offline suite (§60):** a test mode runs without network access. It must be able to demonstrate the behavior required by `SECURITY-MAP.md` §40.
- **Network (§61):** changes must not introduce hidden network access. Network-dependent tests are clearly identified.
- **External services (§62):** mocks, fixtures, recorded responses and controlled integration tests where practical. The complete suite must not depend on a third-party service being available.
- **Fixtures (§63):** versioned, small, deterministic, representative. Sensitive real-world documents are not used unnecessarily.

---

# 6. Benchmark Integrity, Holdout and Contamination (§64–66)

- **Benchmark integrity (§64):** benchmarks must not be modified merely to make a new implementation perform better. Changes to benchmark data require explicit versioning.
- **Holdout (§65):** where a holdout set is defined, development must not silently optimize against it. `R07` §28 and §30 give the methodological basis.
- **Contamination (§66):** tests should not accidentally become training or tuning data for capabilities being evaluated.

**Research context:** `R07` §80.2 records benchmark-artifact contamination (`R-0087`), construct-validity failure (`R-0088`) and a leaderboard score that does not reflect generalizable detection (`R-0089`), and reports no evidence found of literal train/test leakage in the sources it examined. `DETECTOR-VALIDATION-PROTOCOL.md` records train/test separation for detector evaluation as a gap. These rules therefore prevent known failure types; they do not assert that any particular benchmark is clean.

---

# 7. Verification Profiles (§159–166)

The project should eventually provide a single command performing most checks (§159): tests, linting, type checks, security checks, documentation checks, data manifest checks and dependency checks. `tools/verify_docs.py` (`DEC-058`) covers documentation checks only (TVP-G3).

| Profile (§160) | Content | Section |
|---|---|---|
| `FAST` | Rapid feedback during development | §161 |
| `FULL` | The broad project validation suite | §162 |
| `OFFLINE` | Must run without network access | §163 |
| `SECURITY` | Dependency security, network isolation, filesystem boundaries, unsafe execution, data handling | §164 |
| `SCIENTIFIC` | Benchmark integrity, reproducibility, language coverage, experimental validity, result consistency | §165 |
| `RELEASE` | All relevant checks combined | §166 |

**Documentation-only batches:** the profiles above do not yet apply. Those batches use the documentation and scientific reviews of `AGENT-WORK-MODEL.md` §8.

---

# 8. Failure Policy and Evidence (§167–169)

- A failed blocking check prevents release or capability activation; a non-blocking warning remains visible (§167).
- **No greenwashing (§168):** a system must not report `PASS` merely because execution succeeded. Scientific and security checks retain their own status, so a batch report must not fold them into one result.
- Important validation produces machine-readable or otherwise persistable evidence where practical (§169).
- A test or validation must not be weakened or disabled to obtain a pass (`P00-project-governance.md` §8, I-001; `DEC-005`).

---

# 9. Development Quality Gate (§187)

A development batch is successful only if scope is satisfied, tests pass, security is preserved, documentation is synchronized and no blocking inconsistency remains. The final state is reported per `AGENT-WORK-MODEL.md` §9. See TVP-C2 for its relation to `VALIDATION-MAP.md` §73.

---

# 10. Gaps

| ID | Gap | Would normally belong in |
|---|---|---|
| TVP-G1 | Numerical and reproducibility tolerances (§55, §58) are undefined | Per-capability specification |
| TVP-G2 | Which checks are blocking in which profile (§160, §167) is undefined | Tranche or capability definition |
| TVP-G3 | The verification command of §159 and the test tooling do not exist | Implementation tranche |
| TVP-G4 | "Practical", "important" and "representative" (§46, §50, §63, §169) have no stated criterion | Per-capability judgment, recorded in the batch report |
| TVP-G5 | Train/test separation for detector benchmarks lacks research grounding (recorded in `DETECTOR-VALIDATION-PROTOCOL.md`) | `R08` |

No value has been supplied for any of these.

---

# 11. Coverage of the Parent Sections

| Parent sections | Covered in |
|---|---|
| §46–55 | §3 |
| §56–58 | §4 |
| §59–63 | §5 |
| §64–66 | §6 |
| §159–166 | §7 |
| §167–169 | §8 |
| §187 | §9 |
