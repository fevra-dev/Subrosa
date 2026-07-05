# Record: Thailand — PDPA

| | |
|---|---|
| **Record** | `th-pdpa` · **Status/Tier:** SCAFFOLD / Tier 2 · **Schema:** v1.0 · **Current as of:** 2026-07-04 |
| **Instrument** | Personal Data Protection Act B.E. 2562 (2019); full force June 1 2022 |
| **Sources** | `data-minimization--regulatory-reference.md` §Thailand (brief entry) + quick-select row ("Sec. 22 (minimization)"). No Thailand rows exist in the breach/children/rights sub-files — sourcing for this record is a single paragraph plus one table row; cells beyond it are flagged accordingly. |

**Sourced characterization:** closely modeled on GDPR.

## A0 — Scope
Processing of personal data of individuals in Thailand. Extraterritorial reach `[UNVERIFIED — s. 5 extends to overseas controllers offering goods/services to or monitoring data subjects in Thailand; not in suite sources]`.

## A1 — Enforcement
Personal Data Protection Committee (**PDPC**). Penalties (sourced): up to THB 5M civil; up to THB 1M + 1 year imprisonment criminal. Administrative-fine tier `[UNVERIFIED — the Act also carries administrative penalties; suite lists only civil/criminal]`. Private right of action: *not located*.

## A2 — Lawful Basis & Consent
`basis_model:` enumerated-bases — **six lawful bases including consent and legitimate interests** (sourced). Statutory anchor `[UNVERIFIED — s. 24; suite states the count, not the section]`. Sensitive escalation: explicit consent or specific exemption (sourced). Tag: `PROCEDURAL`.

## A3 — Collection Limitation
`test_type:` necessity (GDPR-modeled, sourced). Minimization hook: **Sec. 22** per the suite quick-select row — collection limited to what is necessary for the informed purpose. P-mapping: **P1**. Tag: `ARCH-DISSOLVES`.

## A4 — Purpose Limitation
GDPR-modeled purpose binding (sourced characterization). Statutory anchor `[UNVERIFIED — s. 21; not in suite sources]`. P2. Tag: `PROCEDURAL`.

## A5 — Sensitive Categories
`sensitive_model:` prohibitive-list. Sourced list: health, racial origin, religion, political opinion, criminal records, biometrics, genetic data, sexual orientation, **disability** (a category most regimes omit). Trigger: explicit consent or specific exemption. Statutory anchor `[UNVERIFIED — s. 26; suite gives the list, not the section]`. Tag: `ARCH-DISSOLVES` where provable-not-disclosable; else `PROCEDURAL`.

## A6 — Rights
Sourced vector: access · rectification · deletion · restriction · portability · objection — the full GDPR-shaped set (the only Tier-2 regime sourced with *restriction*). Section anchors and response clocks `[UNVERIFIED — ss. 30–36 range, 30-day clock commonly cited; none in suite sources]`. ADM: *not located*. Tag: `PROCEDURAL`.

## A7 — Retention & Erasure
Deletion right sourced (see A6). Storage-limitation provision: *not located* `[UNVERIFIED — retention notice duty under s. 23; confirm]`. P4. Tag: `ARCH-SATISFIES`.

## A8 — Breach Notification
`clock_model:` fixed-clock. **72-hour notification to PDPC** (sourced). Individual-notification duty and high-risk threshold `[UNVERIFIED — s. 37(4): individuals notified without delay where high risk; not in suite sources]`. Tag: duty `PROCEDURAL`.

## A9 — Children
*Not located in suite sources* `[UNVERIFIED — the Act ties child consent to the Civil and Commercial Code's capacity rules (guardian consent below specified ages, incl. under-10 rule); confirm before use — do not assume a single GDPR-style age]`. Tag: `PROCEDURAL`.

## A10 — Cross-Border Transfer
*Not located in suite sources* `[UNVERIFIED — ss. 28–29: adequate-protection destination or safeguards (BCR-like, consent, contract necessity); confirm]`. `transfer_model:` adequacy+mechanisms pending confirmation. Tag: `PROCEDURAL`.

## A11 — Security Safeguards
GDPR-modeled security duty `[UNVERIFIED — s. 37(1) appropriate security measures per PDPC minimum standards; not in suite sources]`. **P7**. Tag: `ARCH-SATISFIES`.

## A12 — DPIA / PIA
`dpia_model:` *not located* — no Thai DPIA regime in suite sources `[UNVERIFIED — the Act itself mandates no general DPIA; PDPC sub-regulations address risk assessment for some contexts; confirm]`.
