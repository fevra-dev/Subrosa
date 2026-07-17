# Record: UAE — PDPL (federal)

| | |
|---|---|
| **Record** | `ae-pdpl` · **Status/Tier:** SCAFFOLD / Tier 3b · **Schema:** v1.0 · **Current as of:** 2026-07-04 |
| **Instrument** | Federal Decree-Law No. 45 of 2021; effective Jan 2 2022 (implementing regulations in force 2023 per source) |
| **Sources** | `skills/data-minimization/references/regulatory-reference.md` §UAE (brief entry + quick-select row "Art. 4 (minimization)") |

> **Jurisdictional split (sourced):** DIFC (DP Law 2020) and ADGM (DP Regulations 2021) run **separate frameworks** — this record covers the federal PDPL only; DIFC/ADGM need their own records when promoted.

## A0 — Scope
Processing of personal data of individuals in the UAE by entities operating in the UAE (sourced). Free-zone carve-outs: DIFC/ADGM (above).

## A1 — Enforcement
UAE Data Office. Penalties: **administrative fines AED 50,000 – 5M** (web check 2026-07-05); Data Office may also suspend/restrict processing; factors: severity, sensitive data, volume, intent, history. *(Correction note: the suite's "up to AED 20M for intentional/systematic" figure was not corroborated by the primary-source check — treat as withdrawn.)* Implementing rules: **Cabinet Decision No. 33 of 2024** (in force 2024).

## A2 — Lawful Basis & Consent
`basis_model:` enumerated-bases — six bases including consent and legitimate interests (sourced). Sensitive escalation: explicit consent (sourced). Tag: `PROCEDURAL`.

## A3 — Collection Limitation
`test_type:` necessity. Minimization hook: **Art. 4** per the quick-select row `[UNVERIFIED — the brief entry gives no article detail; confirm Art. 4's text against primary]`. P-mapping: **P1**. Tag: `ARCH-DISSOLVES`.

## A4 — Purpose Limitation
Implicit in the six-bases + consent structure; dedicated anchor *not located* `[UNVERIFIED]`. P2. Tag: `PROCEDURAL`.

## A5 — Sensitive Categories
`sensitive_model:` prohibitive-list (consent-escalation form). Sourced list: health; financial; genetic; biometric; criminal records; **children's data** (a category, not just a threshold). Explicit consent required. Tag: `ARCH-DISSOLVES` where provable-not-disclosable; else `PROCEDURAL`.

## A6 — Rights
"Data subject rights similar to GDPR" (sourced characterization only). Individual anchors and clocks *not located* `[UNVERIFIED — Arts. 13–18 range; confirm]`. Tag: `PROCEDURAL`.

## A7 — Retention & Erasure
*Not located* `[UNVERIFIED]`. P4. Tag: `ARCH-SATISFIES` pending anchor.

## A8 — Breach Notification
`clock_model:` fixed-clock (de facto) — Data Office operates a **72-hour de facto breach-notification standard**; detailed timelines in Cabinet Decision No. 33 of 2024 (web check 2026-07-05) `[UNVERIFIED at article level — confirm the Decision's breach articles before reliance]`. Tag: duty `PROCEDURAL`.

## A9 — Children
Children's data is a sensitive category (see A5); age threshold *not located*.

## A10 — Cross-Border Transfer
`transfer_model:` approval-based/adequacy — transfer requires UAE Data Office approval or adequacy assessment (sourced). Tag: `PROCEDURAL` + `ARCH-DISSOLVES` for non-personal-before-export.

## A11 — Security Safeguards
*Not located* `[UNVERIFIED]`. **P7**. Tag: `ARCH-SATISFIES` pending anchor.

## A12 — DPIA / PIA
*Not located in suite sources* `[UNVERIFIED — the PDPL contains a DPIA duty for high-risk processing per implementing regs; confirm]`.
