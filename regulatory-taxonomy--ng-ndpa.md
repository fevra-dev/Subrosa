# Record: Nigeria — NDPA

| | |
|---|---|
| **Record** | `ng-ndpa` · **Status/Tier:** SCAFFOLD / Tier 3b · **Schema:** v1.0 · **Current as of:** 2026-07-04 |
| **Instrument** | Nigeria Data Protection Act 2023 (signed June 2023; replaces NDPR 2019) |
| **Sources** | `data-minimization--regulatory-reference.md` §Nigeria (brief entry + quick-select row "Sec. 24 (minimization)") |

## A0 — Scope
Extraterritorial: applies to processing of PI of persons in Nigeria regardless of controller location (sourced). Context note (sourced): 220M+ population, Africa's largest economy.

## A1 — Enforcement
Nigeria Data Protection Commission (**NDPC**). Penalties: up to NGN 10M (~USD 13K) **or 2% of annual gross revenue**, whichever higher (sourced). Private right of action: *not located*.

## A2 — Lawful Basis & Consent
`basis_model:` enumerated-bases — GDPR-aligned six bases (sourced). Sensitive escalation: *not located* `[UNVERIFIED — s. 30 sensitive-data conditions; confirm]`. Tag: `PROCEDURAL`.

## A3 — Collection Limitation
`test_type:` necessity (GDPR-aligned, sourced). Minimization hook: **Sec. 24** per the quick-select row `[UNVERIFIED — the brief entry gives no article text; s. 24 is the data-protection-principles section in the canonical Act; confirm]`. P-mapping: **P1**. Tag: `ARCH-DISSOLVES`.

## A4 — Purpose Limitation
Within the GDPR-aligned principles (sourced characterization); dedicated anchor *not located* `[UNVERIFIED]`. P2. Tag: `PROCEDURAL`.

## A5 — Sensitive Categories
*Not located in suite sources* `[UNVERIFIED — s. 30: health, race/ethnicity, religious/similar beliefs, sex life, political opinions/affiliations, criminal records, genetic/biometric; confirm]`. `sensitive_model:` pending confirmation.

## A6 — Rights
"Data subject rights" (sourced characterization only); anchors and clocks *not located* `[UNVERIFIED — ss. 34–38 range; confirm]`. Tag: `PROCEDURAL`.

## A7 — Retention & Erasure
*Not located* `[UNVERIFIED]`. P4.

## A8 — Breach Notification
`clock_model:` fixed-clock — **72-hour breach notification** (sourced) `[UNVERIFIED anchor — s. 40 to NDPC within 72h; confirm]`. Tag: duty `PROCEDURAL`.

## A9 — Children
*Not located in suite sources* `[UNVERIFIED — s. 31: child = under 18 per the Child Rights Act; verifiable parental consent; confirm]`.

## A10 — Cross-Border Transfer
*Not located in suite sources* `[UNVERIFIED — ss. 41–43 adequacy-or-safeguards model; confirm]`.

## A11 — Security Safeguards
Implicit in GDPR-aligned principles; anchor *not located* `[UNVERIFIED]`. **P7**. Tag: `ARCH-SATISFIES` pending anchor.

## A12 — DPIA / PIA
**DPO required for large-scale or sensitive processing** (sourced — a governance-roles fact; parked for the v1.1 A1 field). DPIA duty: *not located* `[UNVERIFIED — s. 28 DPIA for high-risk processing; confirm]`.
