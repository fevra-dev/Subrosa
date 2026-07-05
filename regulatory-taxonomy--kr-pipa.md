# Record: South Korea — PIPA

| | |
|---|---|
| **Record** | `kr-pipa` · **Status/Tier:** SCAFFOLD / Tier 3b · **Schema:** v1.0 · **Current as of:** 2026-07-04 |
| **Instrument** | Personal Information Protection Act (개인정보 보호법), Act No. 11990 (2011); substantially amended 2023 (Act No. 19234) |
| **Sources** | `data-minimization--regulatory-reference.md` §Korea PIPA |

**Distinctive (sourced):** among the world's strictest biometric/sensitive regimes — Art. 23 requires separate consent **and separate storage** for sensitive PI; Art. 3(7) mandates anonymous processing where possible; Art. 21 requires irreversible destruction.

## A0 — Scope
Extraterritorial: applies to processing of PI of Korean nationals regardless of processor location (sourced).

## A1 — Enforcement
PIPC. Penalties: up to KRW 300M per violation; **up to 3% of annual revenue for data breach**; criminal up to 5 years / KRW 50M (personal liability). Private right of action: *not located*.

## A2 — Lawful Basis & Consent
`basis_model:` consent-centric hybrid — historically consent-dominated; **2023 amendment added a legitimate-interests basis** (sourced). Sensitive escalation: **Art. 23 — explicit separate consent + storage with technical/administrative safeguards distinct from other PI** (separate consent AND separate storage — the only modeled regime making P6 separation statutory for sensitive data). Tag: `PROCEDURAL` (consent) + the storage-segregation limb is `ARCH-SATISFIES`.

## A3 — Collection Limitation
`test_type:` minimum-necessary. **Art. 3(1)/(3)** principles + **Art. 16** — collect the minimum PI necessary for the stated purpose. **Art. 3(7): process anonymously to the extent possible** — a statutory preference for the architecture. P-mapping: **P1** (+ P5 via 3(7)). Tag: `ARCH-DISSOLVES`; Art. 3(7) is statutory endorsement of the dissolution itself.

## A4 — Purpose Limitation
Art. 3(1) clear purpose specification; collection bound to it. P2. Tag: `PROCEDURAL` + `ARCH-SATISFIES`.

## A5 — Sensitive Categories
`sensitive_model:` prohibitive-list (separate-consent + segregation form). **Art. 23:** ideology; religion; labor-union/political-party membership; political views; health/medical; sexual life; genetic information; criminal records; **biometrics for unique identification**; racial/ethnic origin. Tag: `ARCH-DISSOLVES` where provable-not-disclosable; segregation limb `ARCH-SATISFIES`.

## A6 — Rights
**Arts. 35–40:** access, correction, deletion, suspension of processing; **portability added 2023 (Art. 35-2, machine-readable, transfer to other controllers)**. Response clock: *not located*. Pseudonymization safe harbor expanded (Art. 28-2, 2023). Tag: `PROCEDURAL`.

## A7 — Retention & Erasure
**Art. 21:** destroy PI without delay when retention period expires or purpose achieved; **destruction method must be irreversible** (sourced) — the strongest statutory fit for crypto-erasure among modeled regimes, and a new party to conflict C1. P4. Tag: `ARCH-SATISFIES`.

## A8 — Breach Notification
`clock_model:` promptness-standard with guidance clock — **Art. 34:** notify individuals "without delay" (PIPC guidance: within **5 days**); notify PIPC for breaches over **1,000 individuals**. Tag: duty `PROCEDURAL`; the 1,000-threshold is holdings-dependent.

## A9 — Children
*Not located in suite sources* `[UNVERIFIED — Art. 22-2 / Art. 39-3 lineage: under-14 requires legal-representative consent; confirm anchor]`.

## A10 — Cross-Border Transfer
`transfer_model:` adequacy+mechanisms (2023 update, sourced): adequacy decisions and **Standard Protection Clauses (SPCs — Korea's SCC equivalent)**. Tag: `PROCEDURAL` + `ARCH-DISSOLVES` for non-personal-before-export (Art. 28-2 pseudonymization ladder).

## A11 — Security Safeguards
Art. 3(6) technical/managerial/physical safeguards; Art. 23 adds the distinct-storage requirement for sensitive PI. **P7 + P6**. Tag: `ARCH-SATISFIES`.

## A12 — DPIA / PIA
*Not located in suite sources* `[UNVERIFIED — PIPA mandates PIAs for public institutions (Art. 33); private-sector status differs; confirm]`.
