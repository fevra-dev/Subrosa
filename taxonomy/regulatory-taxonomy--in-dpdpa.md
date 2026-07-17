# Record: India — DPDPA

| | |
|---|---|
| **Record** | `in-dpdpa` · **Status/Tier:** FULL / Tier 3a · **Schema:** v1.0 · **Current as of:** 2026-07-04 |
| **Instrument** | Digital Personal Data Protection Act, 2023 (Act No. 22 of 2023); assent Aug 11 2023 |
| **Sources** | `skills/data-minimization/references/regulatory-reference.md` §DPDPA |

> **⚠ NOT IN FORCE as of June 2026** (per source): operative provisions await Central Government notification under s. 1(2); implementing Rules pending (monitor MeitY). Every obligation below is *anticipated* — run a currency check before any downstream use.

**Distinctive:** the only modeled regime with a **statutory ban on behavioral tracking and targeted advertising directed at children** (§ 9) — this moves the A9 floor from convergent guidance to statute.

## A0 — Scope
Data Fiduciaries processing digital personal data. **§ 10 — Significant Data Fiduciaries:** Central Government may designate by volume, sensitivity, national-security implication — attracting additional obligations (periodic DPIA, audits, DPO). Extraterritorial reach: *not located* in suite sources `[UNVERIFIED — s. 3(b) extends to processing abroad in connection with offering goods/services in India; confirm]`.

## A1 — Enforcement
Data Protection Board of India (**DPBI**). Penalties: up to **INR 250 Cr (~USD 30M) per breach per instance**, scaled by category. Private right of action: *not located*.

## A2 — Lawful Basis & Consent
`basis_model:` enumerated-bases (two-track): **§ 4** — consent, or enumerated "legitimate uses." Sensitive-category escalation: **none — the Act defines no special-category tier** `[UNVERIFIED — the Act's single-tier design (all "digital personal data") is its known structure but the absence is not stated in suite sources; confirm]`. Children (§ 9) are the escalation class instead. Tag: `PROCEDURAL`.

## A3 — Collection Limitation
`test_type:` necessity. **§ 8(3):** a Data Fiduciary shall ensure personal data collected is limited to what is necessary for the specified purpose. P-mapping: **P1**. Tag: `ARCH-DISSOLVES`.

## A4 — Purpose Limitation
**§ 6:** personal data processed only for the purposes for which it was collected ("§ 6(1) purpose limitation" per the source quick-select). P2. Tag: `PROCEDURAL` + `ARCH-SATISFIES`.

## A5 — Sensitive Categories
`sensitive_model:` **none** — single-tier by design (see A2) `[UNVERIFIED — confirm no Rules-based tiering emerges]`. The protective escalations run through § 9 (children) and § 10 (SDF designation) instead of data categories.

## A6 — Rights
*Not located in suite sources* — the source covers fiduciary obligations, not the rights chapter `[UNVERIFIED — §§ 11–14: access to summary, correction/erasure, grievance redressal, nomination; confirm]`. Response clock: *not located* (Rules pending). Tag: `PROCEDURAL`.

## A7 — Retention & Erasure
**§ 8(7):** personal data shall not be retained beyond the period necessary for the specified purpose; **delete upon purpose fulfillment or consent withdrawal** (subject to legal retention obligations). P4. Tag: `ARCH-SATISFIES` (TTL keyed to purpose + consent-state is direct performance).

## A8 — Breach Notification
*Not located in suite sources* `[UNVERIFIED — s. 8(6) requires intimation to the Board and affected Data Principals; clocks live in the pending Rules; confirm]`. `clock_model:` pending Rules. Tag: duty `PROCEDURAL`.

## A9 — Children
**Under 18** (§ 9): verifiable parental/guardian consent; **statutory prohibition on behavioral tracking and targeted advertising directed at children**; same protections for persons with disabilities via guardians. Highest statutory threshold among modeled regimes (ties LGPD/POPIA) and the only statutory ad-tracking ban. Tag: consent mechanics `PROCEDURAL`; the tracking ban is `ARCH-SATISFIES` (no-tracking is an architecture property, not a policy).

## A10 — Cross-Border Transfer
*Not located in suite sources* `[UNVERIFIED — s. 16 negative-list model (transfers allowed except to Centrally-notified restricted countries); confirm]`. `transfer_model:` pending confirmation.

## A11 — Security Safeguards
Reasonable security safeguards duty `[UNVERIFIED — s. 8(5); the safeguard duty is implicit in the sourced §10 audit/DPIA structure but its anchor is not in suite sources]`. **P7**. Tag: `ARCH-SATISFIES`.

## A12 — DPIA / PIA
`dpia_model:` mandatory-for-designated-entities — **§ 10:** Significant Data Fiduciaries must conduct **periodic DPIAs**, periodic audits, and appoint a DPO (sourced). Non-SDF fiduciaries: no DPIA duty in source. Tag: `PROCEDURAL`.
