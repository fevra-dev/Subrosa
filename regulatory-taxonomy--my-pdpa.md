# Record: Malaysia — PDPA

| | |
|---|---|
| **Record** | `my-pdpa` · **Status/Tier:** SCAFFOLD / Tier 2 · **Schema:** v1.0 · **Current as of:** 2026-07-05 (web-upgraded) |
| **Instruments** | Personal Data Protection Act 2010 (Act 709) + PDP (Amendment) Act 2024 (Act A1727 — royal assent Oct 9 2024, gazetted Oct 17 2024, **in force in three phases: Jan 1 / Apr 1 / Jun 1 2025**) + Commissioner's Guidelines on breach notification and DPO appointment (2025) |
| **Sources** | Originally authored with **no suite source** (all cells [UNVERIFIED]); **upgraded 2026-07-05 with web-sourced facts** (pdp.gov.my Act A1727 text; Data Protection Report/NRF; Mayer Brown; DLA Piper; Lexology — see reconciliation log). Statutory **section numbers remain `[UNVERIFIED]`** unless stated; amounts, dates, and thresholds below are web-verified. |

## A0 — Scope `[section anchors UNVERIFIED]`
Processing of personal data in respect of **commercial transactions**; Federal/State Governments excluded. 2024 Amendment renames "data user" → **"data controller"** and extends direct obligations to **data processors** (security). Extraterritorial reach: limited (established-in-Malaysia or equipment-in-Malaysia model).

## A1 — Enforcement
Personal Data Protection Commissioner (JPDP/PDPD). Penalties (web-verified): Data Protection Principles breaches raised **RM300,000 → RM1,000,000** and imprisonment **2 → 3 years** (A1727). Private right of action: *not located*.

## A2 — Lawful Basis & Consent `[section anchors UNVERIFIED]`
`basis_model:` consent-centric — General Principle requires consent unless a listed necessity ground applies (contract, legal obligation, vital interests, justice, public functions). Seven Personal Data Protection Principles structure the Act (General; Notice & Choice; Disclosure; Security; Retention; Data Integrity; Access). Sensitive personal data: explicit consent. Tag: `PROCEDURAL`.

## A3 — Collection Limitation `[section anchors UNVERIFIED]`
`test_type:` necessity — personal data must not be excessive in relation to purpose. P-mapping: **P1**. Tag: `ARCH-DISSOLVES`.

## A4 — Purpose Limitation `[section anchors UNVERIFIED]`
Notice & Choice fixes the purpose set; Disclosure Principle bars other-purpose disclosure without consent. P2. Tag: `PROCEDURAL`.

## A5 — Sensitive Categories
`sensitive_model:` prohibitive-list (consent-escalation form): physical/mental health; political opinions; religious or similar beliefs; commission/alleged commission of an offence; **+ biometric data (added by A1727, web-verified — "personal data resulting from technical processing of physical, physiological or behavioural characteristics")**. Explicit consent required. Tag: `PROCEDURAL`.

## A6 — Rights
Access + correction (Act 709 principles) `[section anchors UNVERIFIED]`; consent withdrawal; direct-marketing cessation. **Data portability: NEW from June 1 2025 (A1727, web-verified)** — direct controller-to-controller transmission on request, subject to technical feasibility and format compatibility. Response clocks: *not located*. Tag: `PROCEDURAL`.

## A7 — Retention & Erasure `[section anchors UNVERIFIED]`
Retention Principle: no longer than necessary; reasonable steps to destroy or permanently delete thereafter. P4. Tag: `ARCH-SATISFIES`.

## A8 — Breach Notification
`clock_model:` **fixed-clock (web-verified, from June 1 2025):** notify the Commissioner as soon as practicable and **no later than 72 hours** from becoming aware of the breach; notify affected individuals **without unnecessary delay where significant harm is likely** (Commissioner's Guidelines, 2025). Pre-2024 the Act had no breach duty. Tag: duty `PROCEDURAL`.

## A9 — Children
No statutory age threshold or child-consent regime — *not located*. Tag: —.

## A10 — Cross-Border Transfer
`transfer_model:` transitioning — the s. 129 ministerial whitelist mechanism was removed by A1727 in favor of receiving-jurisdiction assessment `[UNVERIFIED at section level]`; **Cross-Border Transfer Guidelines issued 2025 (web-verified existence; contents not reviewed)**. Tag: `PROCEDURAL`.

## A11 — Security Safeguards `[section anchors UNVERIFIED]`
Security Principle: practical protective steps; A1727 extends security obligations **directly to data processors** (web-verified). **P7**. Tag: `ARCH-SATISFIES`.

## A12 — DPIA / PIA + Governance
`dpia_model:` none in the Act. **DPO mandatory from June 1 2025 (web-verified)** for controllers *and* processors meeting thresholds: **>20,000 data subjects; or >10,000 sensitive-data subjects; or regular and systematic monitoring** — Commissioner notified of appointments. (Governance-roles fact — parked for the v1.1 A1 field.) Tag: `PROCEDURAL`.
