# Sectoral Record: EU — DORA

| | |
|---|---|
| **Record** | `eu-dora` · **Status:** SECTORAL-OVERLAY (S-profile v1.1) · **Current as of:** 2026-07-05 |
| **Instruments** | Regulation (EU) 2022/2554 (Digital Operational Resilience); applies from Jan 17 2025 |
| **Sources** | `data-minimization--regulatory-reference.md` §DORA |

## S0 — Scope Trigger
**Financial entities** — credit/payment/investment institutions, insurers, credit-rating agencies, crowdfunding, **crypto-asset service providers (CASPs) under MiCA** — plus their **critical ICT third-party providers** (directly supervised). Web3 relevance is direct: a CASP using AI tooling or cloud must run DORA third-party due diligence on it (sourced).

## S1 — Enforcement
National financial supervisors (ECB for significant institutions, BaFin, etc.).

## S2 — Obligation Spine
- **Art. 9:** information-security policy; **encryption of data at rest and in transit (Art. 9(2))**; access control; strong authentication; data classification.
- **Art. 10:** ICT ops security — logging, anomaly detection, documented incident management.
- **Art. 17:** incident classification (clients >10%/50k; duration >24h; data loss >0.1% AUM; ≥3 member states; reputation) with reporting: **initial within 4 hours of major-incident classification** (or 24h of awareness) → intermediate **72h** → final **1 month**. The 4-hour clock is the tightest in the suite.
- **Arts. 28–30:** ICT third-party risk — contracts must cover data location, audit rights, security standards, incident reporting.

## S3 — Overlay Map (when S0 fires)
| Axis | Override |
|---|---|
| A8 | **4-hour initial notification** for classified major incidents — plan the pipeline against this, not GDPR's 72h |
| A11 | Art. 9(2) encryption mandated (P7 as regulation) |
| A10 | data-location terms contractualized with every ICT provider |
| A7 | Art. 10 logging mandates → conflict **C2** party |

## S4 — Interactions
Layered with GDPR (PI-breach clock runs separately), NIS2 (DORA lex specialis for financials `[UNVERIFIED — standard rule, not in suite sources]`), MiCA (defines the CASP class). C2 resolution (field-level log minimization) applies.

## S5 — Defined Lists
Art. 17 classification criteria table; financial-entity class list.

**Tags:** encryption/authentication `ARCH-SATISFIES`; classification + reporting cadence + third-party contract program `PROCEDURAL`; minimized client-data holdings shrink the "data affected" classification criterion — dissolution logic operating inside a resilience regulation.
