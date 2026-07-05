# Record: China — PIPL

| | |
|---|---|
| **Record** | `cn-pipl` · **Status/Tier:** SCAFFOLD / Tier 2 · **Schema:** v1.0 · **Current as of:** 2026-07-04 |
| **Instrument** | Personal Information Protection Law of the PRC, promulgated Aug 20 2021, effective Nov 1 2021 |
| **Sources** | `data-minimization--regulatory-reference.md` §PIPL · `consent-language--breach-notification.md` · `consent-language--childrens-consent.md` · `consent-language--rights-language.md` · `privacy-impact-assessment--dpia-triggers.md` §PIPL Art. 55 · `data-minimization.md` Step 2b(5) |

**Headline (sourced):** the most restrictive cross-border transfer regime of any major framework; Art. 6's excessive-collection prohibition is stricter than GDPR and reaches derived outputs, not just inputs.

## A0 — Scope
Extraterritorial (Art. 3), three limbs: processing within China; processing abroad to (a) provide products/services to individuals in China, (b) analyze/assess behavior of individuals in China, or (c) as otherwise required by law.

## A1 — Enforcement
CAC (primary) + MPS, SAMR, sector regulators. Penalties: up to RMB 50M or 5% of prior-year revenue; responsible individuals up to RMB 1M; business-license suspension/revocation for serious violations. Private right of action: *not located*.

## A2 — Lawful Basis & Consent
`basis_model:` enumerated-bases — Art. 13: consent; contract performance; legal obligation; public-health emergency; public interest; reasonable scope of already-disclosed PI; other bases per law. **No legitimate-interests basis** in the sourced list — a structural divergence from GDPR/LGPD/Thai PDPA. Sensitive escalation: **separate consent** + specific purpose + sufficient necessity (Arts. 28–32). Minors under 14: guardian consent + dedicated processing rules (Art. 31). Transparency duties: Art. 17 (identity, purpose, categories, retention period, rights). Tag: `PROCEDURAL`.

## A3 — Collection Limitation
`test_type:` minimum-necessary + explicit excessive-collection prohibition. **Art. 6** (Chinese text sourced in reference file): clear and reasonable purpose; directly related to purpose; method with least impact on personal rights; collection limited to minimum scope; **excessive collection (过度收集) prohibited** — enforcement has cited apps collecting location/contacts beyond stated function. Extends to derived fields: generating behavioral profiles beyond stated purpose violates Art. 6 even with minimized inputs (`data-minimization.md` Step 2b rule 5). P-mapping: **P1** (stricter than GDPR, per source). Tag: `ARCH-DISSOLVES`.

## A4 — Purpose Limitation
Art. 6 "directly related to the processing purpose" + least-impact-method requirement. P2. Tag: `PROCEDURAL` + `ARCH-SATISFIES`.

## A5 — Sensitive Categories
`sensitive_model:` prohibitive-list (heightened-requirements form): biometric characteristics; religious beliefs; medical/health; financial accounts; whereabouts/location tracking; PI of minors under 14 (Arts. 28–32). Trigger: specific purpose + sufficient necessity + **separate consent** (distinct consent act, not bundled). Tag: `ARCH-DISSOLVES` where attribute provable-without-disclosure; else `PROCEDURAL`.

## A6 — Rights
Access Art. 45 · rectification Art. 46 · erasure Art. 47 · objection Art. 44 · portability Art. 45 · ADM Art. 24 (per suite rights matrix). Response clock: *not located*. Guardian exercise on behalf of minors under 14 (per childrens-consent file). Tag: `PROCEDURAL`.

## A7 — Retention & Erasure
Retention-period disclosure duty (Art. 17); erasure right (Art. 47). Dedicated storage-limitation article: *not located* `[UNVERIFIED — Art. 19 shortest-time-necessary rule; confirm]`. P4. Tag: `ARCH-SATISFIES`.

## A8 — Breach Notification
`clock_model:` promptness-standard (immediacy). "Immediately" to both regulator and individuals; threshold: any breach of personal information (per `consent-language--breach-notification.md`). Statutory anchor `[UNVERIFIED — Art. 57; not cited in suite sources]`. Tag: duty `PROCEDURAL`.

## A9 — Children
**Under 14** — minor PI is *sensitive* by definition (Art. 31): guardian consent, dedicated processing rules, disclosure directly to guardians, guardian identity verification (per childrens-consent file). Tag: `PROCEDURAL`.

## A10 — Cross-Border Transfer
`transfer_model:` approval-based (strictest globally, sourced). Arts. 38–43 — one of: **CAC security assessment** (mandatory for CII operators; processors of 1M+ individuals' PI; or 100k+ individuals / 10k+ sensitive-PI individuals in the preceding year); CAC-recognized certification; **CAC Standard Contract** (eff. June 1 2023); other CAC-prescribed conditions. Art. 43 reciprocal countermeasures. **Sourced schema rule: if you cannot lawfully transfer it, don't collect it** — transfer feasibility constrains collection from day one. Tag: `PROCEDURAL` (mechanism) + `ARCH-DISSOLVES` where processing stays in-country or data is non-personal pre-export — the strongest business case in any regime for local-only/PSI/MPC designs (`privacy-architecture.md`).

## A11 — Security Safeguards
*Not located as a dedicated axis in suite sources* `[UNVERIFIED — Art. 51 technical measures; confirm]`; safeguard adequacy is assessed inside the Art. 55/56 PIA (measures "lawful, effective, appropriate to risk"). **P7**. Tag: `ARCH-SATISFIES`.

## A12 — DPIA / PIA
`dpia_model:` mandatory-triggered. **Art. 55** — PIA required *before*: processing sensitive PI; automated decision-making; entrusting processing / sharing / disclosure; providing PI overseas; other processing with major influence on individuals. **Art. 56** content: lawfulness/legitimacy/necessity of purpose and means; impact on rights + security risk; whether protection measures are lawful, effective, proportionate. **Records retained ≥ 3 years.** Tag: `PROCEDURAL`.
