# Record: Vietnam — PDPL (Law No. 91/2025/QH15)

| | |
|---|---|
| **Record** | `vn-pdpl` · **Status/Tier:** SCAFFOLD / Tier 3b · **Schema:** v1.0 · **Current as of:** 2026-07-05 (web-sourced) |
| **Instruments** | Law on Personal Data Protection No. 91/2025/QH15 (enacted June 26 2025, **effective January 1 2026**) + implementing Decree No. 356/2025/ND-CP (issued Dec 31 2025, effective Jan 1 2026) |
| **Sources** | **Web research 2026-07-05** (Tilleke & Gibbins; Rouse; FPF; luatvietnam — see reconciliation log). No suite grounding source exists for the new law; article-level anchors are `[UNVERIFIED]` unless stated. Predecessor regime: `regulatory-taxonomy--vn-pdpd.md` (historical) |
| **Transition** | Decree 13/2023 presumably ceases effect (formal repeal mechanism not stated in sources); consented processing under Decree 13 may continue without fresh consent |

## A0 — Scope
Controllers/processors of Vietnamese personal data. **Graduated application:** small/startup enterprises get a 5-year grace period (from Jan 1 2026) on DPIA and DPO duties; household/micro-enterprises exempt — carve-outs: entities providing data-processing services, directly processing sensitive data, or processing large subject volumes get no grace.

## A1 — Enforcement
**MPS — A05 department** (Cybersecurity and High-Tech Crime Prevention) receives dossiers and breach notices. Penalties (web-sourced): **illegal data trading — up to 10× revenue gained**; **cross-border violations — up to 5% of prior-year annual revenue** (min VND 3B); other violations — max VND 3B. Criminal tier: *not located in sources*.

## A2 — Lawful Basis & Consent
`basis_model:` consent-centric with enumerated exemptions (legitimate-rights defense, contractual necessity for service providers, other cases per law). **Art. 9 = consent:** voluntary, informed, explicit, granular across data types/purposes/controllers, easily revocable (per earlier PDPL check). Specifics delegated to Decree 356/2025. Tag: `PROCEDURAL`.

## A3 — Collection Limitation
Minimization within the consent-granularity model; dedicated statutory hook *not located* `[UNVERIFIED — the PDPL principles article; sources reviewed give no number]`. P-mapping: **P1**. Tag: `ARCH-DISSOLVES`.

## A4 — Purpose Limitation
Per-purpose granular consent binds processing (Art. 9 structure). P2. Tag: `PROCEDURAL`.

## A5 — Sensitive Categories
`sensitive_model:` two-tier (basic/sensitive) retained; **category lists delegated to the implementing decree** (Decree 356/2025) — sector safeguards named for health, financial, biometric, location data. Tag: `ARCH-DISSOLVES` where provable-not-disclosable; else `PROCEDURAL`.

## A6 — Rights
Rights retained from the Decree-13 regime with clarifications — **rights sit at Art. 4** (per PDPL check): informed, access, revoke consent, amend, erase, restrict, object. **Novel: statutory data-subject *obligations*** (self-protection, respecting others' data, accuracy) — unique among modeled regimes. Response clocks: *not located*. Tag: `PROCEDURAL`.

## A7 — Retention & Erasure
Erasure right at Art. 4; retention rules delegated to decree — *not located*. P4. Tag: `ARCH-SATISFIES`.

## A8 — Breach Notification
`clock_model:` fixed-clock — **72 hours from detection to A05** (revised from Decree 13's "from occurrence"); **individual notice for biometric-data incidents and financial-services incidents** (an incident-class trigger, unique among modeled regimes). Tag: duty `PROCEDURAL`.

## A9 — Children
Parental consent generally; **dual consent (child + parent) where data concerns private life/personal secrets and the child is 7+** — the only modeled regime with a child-co-consent mechanic. Tag: `PROCEDURAL`.

## A10 — Cross-Border Transfer
`transfer_model:` assessment-dossier (filing, not approval): **Data Processing Impact Assessment + Transfer Impact Assessment dossiers to A05**; 6-month update cycle on change; immediate update on restructuring/new provider/new business line. **No data-localization requirement appears in the PDPL text reviewed** — the Decree-13-era localization claim did not carry over `[UNVERIFIED — Vietnam's separate Cybersecurity Law 2018 / Decree 53/2022 localization regime may still apply to in-scope services; confirm before relying on the absence]`. Enforcement teeth: 5%-of-revenue penalty tier attaches here. Tag: `PROCEDURAL` (dossiers) + `ARCH-DISSOLVES` for non-personal-before-export.

## A11 — Security Safeguards
Delegated to decree; *not located*. **P7**. Tag: `ARCH-SATISFIES` pending anchor.

## A12 — DPIA / PIA
`dpia_model:` **mandatory-filing** — DPIA (and TIA) dossiers *submitted to the regulator*, not kept on file: the strictest assessment form among modeled regimes; 6-month update cadence. DPO-or-department (or external provider) mandatory, detail in decree; 5-year small-enterprise grace. Tag: `PROCEDURAL`.
