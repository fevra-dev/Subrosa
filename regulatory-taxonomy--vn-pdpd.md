# Record: Vietnam — PDPD

| | |
|---|---|
| **Record** | `vn-pdpd` · **Status/Tier:** SCAFFOLD / Tier 3b · **Schema:** v1.0 · **Current as of:** 2026-07-04 |
| **Instrument** | Decree 13/2023/ND-CP on Personal Data Protection; effective July 1 2023 |
| **Sources** | `data-minimization--regulatory-reference.md` §Vietnam (brief entry + quick-select row "Art. 9 (minimization)") |
| **Reform watch** | A full PDP *Law* elevating the Decree has been in Vietnam's legislative pipeline `[UNVERIFIED — confirm status; would supersede this record]` |

## A0 — Scope
Personal data of Vietnamese citizens; processing in Vietnam and by foreign entities processing Vietnamese citizens' data `[UNVERIFIED — Art. 1 scope; the brief entry doesn't detail reach]`.

## A1 — Enforcement
Ministry of Public Security (**MPS**) — a security ministry, not a data authority; factor into threat-model Archetype 6 analysis. Penalties: administrative fines up to VND 5B (~USD 200K); criminal liability for serious violations (sourced).

## A2 — Lawful Basis & Consent
`basis_model:` consent-centric (strict form) — **explicit, voluntary, informed consent for each specific purpose** (sourced); per-purpose granularity is the strictest consent wording among modeled regimes alongside PIPL's separate-consent. Sensitive escalation: explicit consent (sourced two-tier structure). Tag: `PROCEDURAL`.

## A3 — Collection Limitation
`test_type:` necessity. Minimization hook: **Art. 9** per the quick-select row `[UNVERIFIED — the brief entry gives no article text; confirm]`. P-mapping: **P1**. Tag: `ARCH-DISSOLVES`.

## A4 — Purpose Limitation
Per-purpose consent binds processing to declared purposes (sourced consent structure). P2. Tag: `PROCEDURAL`.

## A5 — Sensitive Categories
`sensitive_model:` prohibitive-list (two-tier: "basic" vs "sensitive"). Sourced sensitive list: political views; religion; health; sexual orientation; criminal records; genetic data; biometric data; **financial data**; **geolocation**. Explicit consent required. Tag: `ARCH-DISSOLVES` where provable-not-disclosable; else `PROCEDURAL`.

## A6 — Rights
*Not located in suite sources* `[UNVERIFIED — Art. 9 of the Decree enumerates data-subject rights (consent withdrawal, deletion, restriction); note the quick-select's "Art. 9 (minimization)" may collide with this — confirm which Art. 9 is which against primary]`. Tag: `PROCEDURAL`.

## A7 — Retention & Erasure
*Not located* `[UNVERIFIED]`. P4.

## A8 — Breach Notification
*Not located in suite sources* `[UNVERIFIED — Art. 23: notify MPS within 72 hours; confirm]`. `clock_model:` pending confirmation.

## A9 — Children
*Not located in suite sources* `[UNVERIFIED — Art. 20: processing children's (under-16) data requires consent of child (7+) and parent/guardian; confirm]`.

## A10 — Cross-Border Transfer
`transfer_model:` **localization + approval** — **Art. 26: personal data of Vietnamese citizens collected/exploited/used in Vietnam must be stored in Vietnam**; cross-border transfer requires MPS approval or a transfer impact self-assessment dossier (sourced). Joins PIPL as a party to conflict **C3**. Tag: `PROCEDURAL` (dossier) + `ARCH-DISSOLVES` for local-only processing.

## A11 — Security Safeguards
*Not located* `[UNVERIFIED]`. **P7**. Tag: `ARCH-SATISFIES` pending anchor.

## A12 — DPIA / PIA
*Not located in suite sources* `[UNVERIFIED — Arts. 24–25: processing impact assessment dossier filed with MPS within 60 days of processing start; transfer dossier likewise; confirm — if so, Vietnam is a mandatory-filing regime, stricter in form than Law 25's keep-on-file]`.
