# Record: Brazil — LGPD

| | |
|---|---|
| **Record** | `br-lgpd` · **Status/Tier:** SCAFFOLD / Tier 2 · **Schema:** v1.0 · **Current as of:** 2026-07-04 |
| **Instrument** | Lei Geral de Proteção de Dados, Law No. 13,709/2018 (as amended by Law 13,853/2019); in force Aug 2020, penalties Aug 2021 |
| **Sources** | `data-minimization--regulatory-reference.md` §LGPD · `consent-language--breach-notification.md` · `consent-language--childrens-consent.md` · `consent-language--rights-language.md` |

## A0 — Scope
Extraterritorial (Art. 3): any processing of data of individuals in Brazil regardless of processor location — mirrors GDPR Art. 3. Thresholds/exemptions: *not located*.

## A1 — Enforcement
ANPD. Penalties: up to BRL 50M per violation or 2% of Brazil revenue (capped BRL 50M per infraction). Private right of action: *not located*.

## A2 — Lawful Basis & Consent
`basis_model:` enumerated-bases — the full Art. 7 basis list is not in suite sources `[UNVERIFIED — confirm Art. 7 against primary source]`. Sensitive escalation: specific legal basis required — explicit consent or an Art. 11(II) ground. Children: specific consent from parent/guardian (Art. 14). Tag: `PROCEDURAL`.

## A3 — Collection Limitation
`test_type:` necessity. **Art. 6(III)** — "limitação ao mínimo necessário para a realização de suas finalidades" (limitation to the minimum necessary for the purposes). Primary minimization hook; GDPR Art. 5(1)(c) analog. P-mapping: **P1**. Tag: `ARCH-DISSOLVES`.

## A4 — Purpose Limitation
Art. 6(I) purpose (legitimate, explicit, informed) + Art. 6(II) adequacy (compatible with disclosed purposes). P2. Tag: `PROCEDURAL` + `ARCH-SATISFIES` via separation/scoped identifiers.

## A5 — Sensitive Categories
`sensitive_model:` prohibitive-list. Art. 5(II) + Art. 11: racial/ethnic origin; religious beliefs; political opinions; union membership; health / sexual life / sexual orientation; genetic/biometric data. CRITICAL tier always (sourced). Trigger: specific basis (explicit consent or Art. 11(II)). Tag: `ARCH-DISSOLVES` where attribute is proven not disclosed (ZKP/anonymous credentials); else `PROCEDURAL`.

## A6 — Rights
Access Art. 18(II) · rectification Art. 18(III) · anonymization/blocking/**deletion of unnecessary or excessive data** Art. 18(IV) (a minimization *right* — unique among modeled regimes) · erasure of consented data Art. 18(VI) · portability Art. 18(V) · **objection Art. 18 § 2** *(primary-source corrected 2026-07-05 — the suite rights matrix had duplicated Art. 18(II); § 2 grants opposition to processing on non-consent bases in case of noncompliance)* · ADM review Art. 20 · free access principle Art. 6(IV). Response clock: **15 days**, no extension listed (per rights matrix). Complaint: gov.br/anpd. Restriction / opt-out-of-sale / limit-sensitive / de-indexing: —. Tag: `PROCEDURAL`.

## A7 — Retention & Erasure
Deletion right Art. 18(VI); prevention principle Art. 6(VIII). A dedicated storage-limitation article is *not located* in suite sources `[UNVERIFIED — Arts. 15–16 govern termination/retention; confirm]`. P4. Tag: `ARCH-SATISFIES` (TTL/crypto-erasure).

## A8 — Breach Notification
`clock_model:` fixed-clock. Art. 48 + ANPD Resolution CD/ANPD No. 15/2023: **3 business days to ANPD; 5 business days to data subjects** (high-risk incidents). Threshold: significant risk to data subjects. Tag: duty `PROCEDURAL`; trigger surface shrinks with minimized holdings.

## A9 — Children
**Under 18** (Art. 14) — highest age threshold among modeled regimes. Specific parental/guardian consent; processing must serve the child's best interests; collecting data unnecessary to the service is prohibited. Operational rules: ANPD Resolution CD/ANPD No. 4/2023. Tag: `PROCEDURAL`.

## A10 — Cross-Border Transfer
`transfer_model:` adequacy+mechanisms. Art. 33: adequate-protection countries, or safeguards — SCCs (Art. 33(V)), BCRs (Art. 33(VII)). ANPD adequacy list: verify current as of use date (sourced instruction). Tag: `PROCEDURAL` + `ARCH-DISSOLVES` for data rendered non-personal pre-export.

## A11 — Security Safeguards
Art. 46: technical and administrative measures against unauthorized access and accidental/unlawful destruction, loss, alteration, disclosure. Art. 6(VII) security principle. Principles-based. **P7**. Tag: `ARCH-SATISFIES`.

## A12 — DPIA / PIA
`dpia_model:` discretionary — **Art. 38**: ANPD may require DPIAs (RIPD); voluntary otherwise but expected (sourced: `privacy-impact-assessment.md` regime table — upgraded from [UNVERIFIED] 2026-07-04, see reconciliation log). No mandatory-trigger list; trigger conditions `[UNVERIFIED — confirm Art. 38 scope against primary source]`.
