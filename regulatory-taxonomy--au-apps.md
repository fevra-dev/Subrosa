# Record: Australia — Privacy Act 1988 + APPs

| | |
|---|---|
| **Record** | `au-apps` · **Status/Tier:** FULL / Tier 3a · **Schema:** v1.0 · **Current as of:** 2026-07-04 |
| **Instruments** | Privacy Act 1988 (Cth) + Australian Privacy Principles (Schedule 1, as amended 2012); penalty amendments: Privacy and Other Legislation Amendment Act 2024 (s. 13G) |
| **Sources** | `data-minimization--regulatory-reference.md` §APPs · `consent-language--breach-notification.md` · `consent-language--childrens-consent.md` |
| **Reform watch** | Small-business exemption narrowing under reform proposals (sourced) |

**Distinctive:** the only modeled regime that statutorily mandates *offering* anonymity (APP 2) — see A2 and the arch roll-up.

## A0 — Scope
APP entities. **Small-business exemption:** annual turnover ≤ AUD 3M generally exempt (s. 6C) — narrowing under reform. Extraterritorial reach: *not located* in suite sources `[UNVERIFIED — s. 5B "Australian link" test; confirm]`.

## A1 — Enforcement
OAIC. Penalties (2024 amendment, s. 13G): up to **AUD 50M, or 3× benefit obtained, or 30% of adjusted turnover** — for serious or repeated interferences. Private right of action: *not located* `[UNVERIFIED — a direct right of action was part of the reform agenda; confirm status]`.

## A2 — Lawful Basis & Consent
`basis_model:` consent-centric hybrid — collection of ordinary PI is necessity-based with notice (APP 3 + APP 5), no consent required; **sensitive information requires consent in addition to the necessity test** (APP 3.3 / s. 6). **APP 2 — anonymity and pseudonymity:** entities must offer individuals the option to interact anonymously or pseudonymously where lawful and practicable — a statutory selective-disclosure mandate. P-mapping: P5 (APP 2, per source), P1/P2 (APP 3/5). Tag: APP 2 is the rare **ARCH-MANDATES** case — the statute requires what the architecture provides; consent/notice mechanics `PROCEDURAL`.

## A3 — Collection Limitation
`test_type:` necessity (reasonableness-qualified). **APP 3:** collect only if reasonably necessary for (or directly related to) the entity's functions or activities; APP 3.3 for sensitive adds consent. Third-party collection only where direct collection not reasonable/practicable. P-mapping: **P1**. Tag: `ARCH-DISSOLVES`.

## A4 — Purpose Limitation
APP 6: use/disclose only for the primary purpose of collection, or a secondary purpose with consent or an exception. APP 5 notification fixes the purpose set. P2. Tag: `PROCEDURAL` + `ARCH-SATISFIES` via separation.

## A5 — Sensitive Categories
`sensitive_model:` prohibitive-list (consent-escalation form). s. 6: racial/ethnic origin; political opinions; membership of political association; religious beliefs/affiliations; **philosophical beliefs**; membership of professional/trade association; trade union membership; sexual orientation or practices; **criminal record**; health; genetic; biometric information. Consent required for collection on top of the APP 3 necessity test. Tag: `ARCH-DISSOLVES` where provable-not-disclosable; else `PROCEDURAL`.

## A6 — Rights
Access — APP 12 · correction — APP 13. No erasure *right* (see A7's entity-side duty), no restriction/portability/objection/ADM in suite sources — *not located*. Response clock: *not located* `[UNVERIFIED — "reasonable period"/30-day conventions; confirm]`. Complaint: OAIC. Tag: `PROCEDURAL`.

## A7 — Retention & Erasure
**APP 11.2:** take reasonable steps to **destroy or de-identify** PI no longer needed for any permitted purpose — the APP analog of GDPR Art. 5(1)(e)/PIPEDA 4.5.3 (sourced), framed as an entity duty rather than a data-subject right. P4. Tag: `ARCH-SATISFIES` (TTL/de-identification pipelines are direct performance); de-identify option makes this friendlier to aggregate-retention designs than erasure-only regimes.

## A8 — Breach Notification
`clock_model:` promptness-standard. NDB scheme: notify OAIC and individuals **ASAP** where breach is **likely to result in serious harm** (per `consent-language--breach-notification.md`). Statutory anchor `[UNVERIFIED — Part IIIC ss. 26WE–26WR; not in suite sources]`. Tag: duty `PROCEDURAL`; serious-harm threshold is holdings-dependent.

## A9 — Children
**Under 15** — OAIC guidance, not statutory (per `consent-language--childrens-consent.md`); parental consent. Tag: `PROCEDURAL`.

## A10 — Cross-Border Transfer
*Not located in suite sources* `[UNVERIFIED — APP 8 + s. 16C accountability model (transferor remains liable) is the canonical anchor; confirm]`. `transfer_model:` accountability pending confirmation. Tag: `PROCEDURAL`.

## A11 — Security Safeguards
**APP 11:** reasonable steps to protect PI from misuse, interference, loss, unauthorised access/modification/disclosure. Principles-based. **P7**. Tag: `ARCH-SATISFIES`.

## A12 — DPIA / PIA
`dpia_model:` none in suite sources for the private sector — *not located* `[UNVERIFIED — PIAs mandatory for Australian Government agencies under the Privacy (Australian Government Agencies — Governance) APP Code; confirm private-sector status]`.
