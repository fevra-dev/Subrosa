# Record: India — DPDPA

| | |
|---|---|
| **Record** | `in-dpdpa` · **Status/Tier:** FULL / Tier 3a · **Schema:** v1.0 · **Current as of:** 2026-07-17 (currency sweep, web-verified) |
| **Instrument** | Digital Personal Data Protection Act, 2023 (Act No. 22 of 2023); assent Aug 11 2023 · **DPDP Rules, 2025 (MeitY, notified Nov 14 2025)** |
| **Sources** | `skills/data-minimization/references/regulatory-reference.md` §DPDPA |

> **⚠ PHASED COMMENCEMENT UNDERWAY** (web-verified 2026-07-17): **DPDP Rules, 2025 notified Nov 14 2025**; provisions commence in three phases — **Nov 14 2025** (definitions, Data Protection Board, administrative machinery) · **Nov 14 2026** (Consent Manager registration) · **May 13 2027** (core operative duties: notice, security, breach notification, SDF obligations, Data Principal rights). Obligations below become enforceable at Phase 3 unless noted — verify the phase before downstream use.

**Distinctive:** the only modeled regime with a **statutory ban on behavioral tracking and targeted advertising directed at children** (§ 9) — this moves the A9 floor from convergent guidance to statute.

## A0 — Scope
Data Fiduciaries processing digital personal data. **§ 10 — Significant Data Fiduciaries:** Central Government may designate by volume, sensitivity, national-security implication — attracting additional obligations (periodic DPIA, audits, DPO). Extraterritorial reach: **s. 3(b)** (web-verified 2026-07-17) — processing outside India in connection with offering goods or services to Data Principals within India.

## A1 — Enforcement
Data Protection Board of India (**DPBI**). Penalties: up to **INR 250 Cr (~USD 30M) per breach per instance**, scaled by category. Private right of action: *not located*.

## A2 — Lawful Basis & Consent
`basis_model:` enumerated-bases (two-track): **§ 4** — consent, or enumerated "legitimate uses." Sensitive-category escalation: **none — the Act defines no special-category tier** `[UNVERIFIED — the Act's single-tier design (all "digital personal data") is its known structure but the absence is not stated in suite sources; confirm]`. Children (§ 9) are the escalation class instead. Tag: `PROCEDURAL`.

## A3 — Collection Limitation
`test_type:` necessity. **§ 8(3):** a Data Fiduciary shall ensure personal data collected is limited to what is necessary for the specified purpose. P-mapping: **P1**. Tag: `ARCH-DISSOLVES`.

## A4 — Purpose Limitation
**§ 6:** personal data processed only for the purposes for which it was collected ("§ 6(1) purpose limitation" per the source quick-select). P2. Tag: `PROCEDURAL` + `ARCH-SATISFIES`.

## A5 — Sensitive Categories
`sensitive_model:` **none** — single-tier by design (see A2) `[UNVERIFIED — DPDP Rules 2025 (notified Nov 14 2025) reported without sensitivity tiering; confirm against Rules text]`. The protective escalations run through § 9 (children) and § 10 (SDF designation) instead of data categories.

## A6 — Rights
**§§ 11–14** (web-verified 2026-07-17): access to a summary of data + processing activities (s. 11) · correction, completion, updating, erasure (s. 12) · grievance redressal (s. 13) · nomination (s. 14). Response clocks live in the DPDP Rules 2025 (Phase 3, May 13 2027). Tag: `PROCEDURAL`.

## A7 — Retention & Erasure
**§ 8(7):** personal data shall not be retained beyond the period necessary for the specified purpose; **delete upon purpose fulfillment or consent withdrawal** (subject to legal retention obligations). P4. Tag: `ARCH-SATISFIES` (TTL keyed to purpose + consent-state is direct performance).

## A8 — Breach Notification
**s. 8(6)** (web-verified 2026-07-17): **dual intimation — the Board and each affected Data Principal.** Clocks live in the DPDP Rules 2025 (notified Nov 14 2025; operative at Phase 3, May 13 2027) `[rule-level anchor UNVERIFIED — confirm]`. `clock_model:` pending Rules. Tag: duty `PROCEDURAL`.

## A9 — Children
**Under 18** (§ 9): verifiable parental/guardian consent; **statutory prohibition on behavioral tracking and targeted advertising directed at children**; same protections for persons with disabilities via guardians. Highest statutory threshold among modeled regimes (ties LGPD/POPIA) and the only statutory ad-tracking ban. Tag: consent mechanics `PROCEDURAL`; the tracking ban is `ARCH-SATISFIES` (no-tracking is an architecture property, not a policy).

## A10 — Cross-Border Transfer
**s. 16(1)** (web-verified 2026-07-17): **negative-list (blacklist) model** — transfer permitted to any country except those restricted by Central Government notification. `transfer_model:` open-unless-blacklisted.

## A11 — Security Safeguards
Reasonable security safeguards duty — **s. 8(5)** (web-verified 2026-07-17): reasonable safeguards to prevent personal data breach. **P7**. Tag: `ARCH-SATISFIES`.

## A12 — DPIA / PIA
`dpia_model:` mandatory-for-designated-entities — **§ 10:** Significant Data Fiduciaries must conduct **periodic DPIAs**, periodic audits, and appoint a DPO (sourced). Non-SDF fiduciaries: no DPIA duty in source. Tag: `PROCEDURAL`.
