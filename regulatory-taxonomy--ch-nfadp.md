# Record: Switzerland — nFADP

| | |
|---|---|
| **Record** | `ch-nfadp` · **Status/Tier:** SCAFFOLD / Tier 3b · **Schema:** v1.0 · **Current as of:** 2026-07-04 |
| **Instrument** | Federal Act on Data Protection (DSG/nFADP), SR 235.1; in force Sept 1 2023 (replaces 1992 FADP) |
| **Sources** | `data-minimization--regulatory-reference.md` §nFADP (incl. GDPR-diff table) |

## A0 — Scope
Private persons and federal bodies; processing in Switzerland and processing with effects in Switzerland (extraterritorial, GDPR-like). **EU adequacy holds** — free EU↔CH flows (sourced).

## A1 — Enforcement
FDPIC. Penalties: criminal fines up to **CHF 250,000 against responsible individuals** — not entities (unusual; personal-liability regime). Tag note: shifts exposure analysis from corporate to officer level.

## A2 — Lawful Basis & Consent
`basis_model:` principles-based — processing permitted if proportionate to purpose; no GDPR-style enumerated bases (sourced diff table). High-risk profiling requires explicit consent or other justification. Sensitive PI requires justification. Tag: `PROCEDURAL`.

## A3 — Collection Limitation
`test_type:` proportionality. **Art. 6** — processing must be proportionate to the purpose; "effectively a data minimization requirement phrased as proportionality" (sourced). **Art. 7** privacy by design and by default (GDPR Art. 25 analog). P-mapping: **P1**. Tag: `ARCH-DISSOLVES`.

## A4 — Purpose Limitation
Within the Art. 6 proportionality principle (purpose-bound processing). P2. Tag: `PROCEDURAL` + `ARCH-SATISFIES`.

## A5 — Sensitive Categories
`sensitive_model:` prohibitive-list — **broader than GDPR Art. 9** (sourced): religious/ideological/political/trade-union views; health; intimate sphere; racial origin; **social-welfare measures**; **administrative and criminal proceedings/sanctions**; genetic data; biometric data uniquely identifying; **location data if revealing sensitive context**. Tag: `ARCH-DISSOLVES` where provable-not-disclosable; else `PROCEDURAL`.

## A6 — Rights
*Not located in suite sources* beyond the diff table `[UNVERIFIED — Arts. 25–29 access/rectification range; confirm]`. Response clock: *not located*. Tag: `PROCEDURAL`.

## A7 — Retention & Erasure
Implicit in Art. 6 proportionality + Art. 7 by-default; dedicated anchor *not located* `[UNVERIFIED]`. P4. Tag: `ARCH-SATISFIES`.

## A8 — Breach Notification
`clock_model:` promptness-standard — "as soon as possible" to FDPIC, **no fixed timeline** (sourced diff table). Tag: duty `PROCEDURAL`.

## A9 — Children
*Not located* — no Switzerland row in children's table; no age threshold in source.

## A10 — Cross-Border Transfer
Adequacy-based (mirrors GDPR model; CH itself holds EU adequacy). Dedicated anchor *not located* `[UNVERIFIED — Arts. 16–17; confirm]`. Tag: `PROCEDURAL`.

## A11 — Security Safeguards
Art. 7 technical/organisational measures + privacy-friendly defaults (sourced). **P7**. Tag: `ARCH-SATISFIES`.

## A12 — DPIA / PIA
`dpia_model:` mandatory-triggered — DPIA for high-risk processing (**Art. 22**, sourced diff table); DPO voluntary (FDPIC-recommended for large scale). High-risk-profiling notification to FDPIC if no DPO appointed — sourced as "Art. 12" `[VERIFY — Art. 12 canonically covers the register of processing activities; the high-residual-risk FDPIC consultation is Art. 23; confirm which anchor the notification duty actually carries]`. Tag: `PROCEDURAL`.
