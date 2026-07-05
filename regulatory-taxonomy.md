---
name: regulatory-taxonomy
description: Normalized cross-jurisdiction regulatory mapping layer for the Guise privacy suite. One frozen axis set; one record file per jurisdiction. Use when answering any cross-jurisdiction compliance question ("who has a 72-hour breach clock", "which regimes treat geolocation as sensitive", "what age is a child in Brazil"), when adding a new jurisdiction to the suite, or when a downstream skill (consent-language, data-minimization, privacy-impact-assessment) needs a statutory citation. Records are the single source of truth; prose skills cite records.
---

# Regulatory Taxonomy — Master

**Schema: v1.1 — omnibus axes A0–A12 FROZEN 2026-07-04 (unchanged); sectoral overlay profile S0–S5 added 2026-07-05 (operator-approved).** Any change to A0–A12 requires a version bump, a change note here, and re-validation of every FULL record; the S-profile extends the schema without touching them.

**Regulatory status:** Records carry their own "current as of" date. This layer is for schema design, audit, and disclosure drafting — not legal advice. Verify effective dates and pending rulemakings against primary sources before advising in a regulated context.

---

## Design Contract

1. **One record per regime.** Each jurisdiction record is a standalone file (`regulatory-taxonomy--<iso>-<statute>.md`) populated against the axes below. Closely-coupled instruments share a record with a divergence block (EU GDPR + UK GDPR; PIPEDA + Quebec Law 25).
2. **Records are source of truth.** Downstream skills (consent-language, data-minimization, privacy-impact-assessment) cite records; they do not restate statutory facts. (Wiring of downstream skills is Phase 2 — until then the prose files remain authoritative where they conflict, and conflicts get logged, not silently resolved.)
3. **Citation floor.** Every cell is backed by a statutory citation verifiable against the suite's reference files, or carries `[UNVERIFIED — confirm against primary source]`. An empty cell marked *not located* is correct; a fabricated citation is a defect. Cells where the suite's own sources are suspected wrong carry `[VERIFY — <reason>]` and keep the sourced value.
4. **Omnibus scope + sectoral overlays.** Axes A0–A12 model omnibus data-protection regimes. Sectoral/single-purpose laws do not fit them without distortion — they use the **Sectoral Overlay Profile** below (v1.1, operator-approved 2026-07-05). Do not force a sectoral law into the omnibus template.

---

## Sectoral Overlay Profile (S0–S5) — v1.1

Sectoral laws are modeled as *modifiers on the omnibus baseline*, not parallel regimes. When a record's S0 trigger fires, its S3 overlay rewrites the affected omnibus-axis floors for that data/entity scope — which keeps the floor matrix and conflict register composable.

| Field | Content |
|---|---|
| S0 | **Scope trigger** — data type × entity class that pulls a system into the law |
| S1 | **Enforcement** — authority, penalties, private right of action |
| S2 | **Obligation spine** — the law's own core structure, in its own shape |
| S3 | **Overlay map** — which A-axes it hardens or overrides when triggered ("A8 → 60-day clock") |
| S4 | **Interactions** — preemption, carve-outs, layering with other laws |
| S5 | **Defined lists** — identifier/category lists the law itself defines (18 PHI, NPI, biometric identifiers) |

Enforcement-mode tags apply to S-cells exactly as to A-cells.

---

## The Axes (A0–A12)

Every record populates all thirteen axes. Each axis row carries: normalized value(s) → citation(s) → P-mapping (P1–P7 per `data-minimization.md`) → enforcement-mode tag.

| Axis | Name | Normalized field(s) |
|---|---|---|
| A0 | Scope & applicability | Territorial trigger · extraterritorial reach · covered entities · thresholds/exemptions |
| A1 | Enforcement | Authority · penalty ceiling · private right of action (Y/N) |
| A2 | Lawful basis & consent model | `basis_model:` enumerated-bases / consent-centric / notice-and-optout · default posture (opt-in/opt-out) · sensitive-data escalation |
| A3 | Collection limitation (minimization hook) | `test_type:` necessity / proportionality+necessity / reasonableness / minimum-necessary · operative statutory text |
| A4 | Purpose limitation | Binding rule · compatible-use standard |
| A5 | Sensitive categories | `sensitive_model:` prohibitive-list / contextual / rights-based-list · category list · processing trigger |
| A6 | Data-subject rights | Rights vector (access · rectification · erasure · restriction · portability · objection · ADM/profiling · opt-out-of-sale · limit-sensitive · de-indexing) · response clock + extension |
| A7 | Retention & erasure | Storage-limitation rule · deletion duty · immutability conflict note |
| A8 | Breach notification | `clock_model:` fixed-clock / promptness-standard / none · authority deadline · individual deadline · threshold |
| A9 | Children | Age threshold (statutory vs guidance) · consent mechanism |
| A10 | Cross-border transfer | `transfer_model:` adequacy+mechanisms / accountability / approval-based / localization · mechanisms |
| A11 | Security safeguards | Standard · specificity (principles vs prescriptive) |
| A12 | DPIA / PIA | `dpia_model:` mandatory-triggered / none / risk-analysis-equivalent · triggers · prior-consultation duty |

**P-mappings** use the suite's seven minimization principles exactly as defined in `data-minimization.md`: P1 Collection Limitation · P2 Purpose Specification & Binding · P3 Accuracy & Minimality of Precision · P4 Storage Limitation · P5 Identifier Minimality · P6 Separation of Concerns · P7 Cryptographic Minimization. Where an existing suite file already maps a provision to principles, that mapping is preserved verbatim.

---

## Enforcement-Mode Tags (the cypherpunk layer)

Each obligation is tagged for whether architecture or only process can satisfy it — this operationalizes the suite thesis (*compliance is a floor, selective disclosure is the ceiling*, `privacy-suite.md`) and bridges to `privacy-architecture.md`.

| Tag | Meaning | Example |
|---|---|---|
| `ARCH-DISSOLVES` | A selective-disclosure architecture renders the obligation moot for the data in question — the duty never attaches because identifiable data never exists in the relevant form | Breach notification for data held only as commitments; erasure via crypto-erasure/off-chain design |
| `ARCH-SATISFIES` | The duty attaches, but a technical measure discharges it | Encryption for safeguards mandates; automated TTL for retention limits; pseudonymization for minimization |
| `PROCEDURAL` | Irreducibly process/paper — only organizational action satisfies it | Notices, DPO designation, records of processing, regulator consultation, consent UX, board reporting |
| `ARCH-MANDATES` *(v1.1)* | The statute requires the architectural property itself — policy cannot comply, only the design can | AU APP 2 (must *offer* anonymity); DPDPA § 9 tracking ban; BIPA § 15(c) profit prohibition |

**Tagging rules:**
1. **The universal dissolution is assumed, not tagged.** Data never collected creates no duty under any regime (Hughes' transaction-necessity principle = P1). Tags describe obligations *for the data a system does hold* — otherwise every cell would read ARCH-DISSOLVES and the tag would carry no information.
2. **Split where the statute splits.** An axis can carry different tags per sub-obligation (e.g., A8: the notification *duty* is PROCEDURAL once triggered, but encryption safe-harbors make the *trigger* ARCH-SATISFIES).
3. Where a tag references a primitive, use the `privacy-architecture.md` vocabulary (ZKP, anonymous credentials, blind signatures, commitments, stealth addresses, PSI, HE, MPC, TEE, differential privacy).

---

## Record Statuses & Depth Definitions

| Status | Definition |
|---|---|
| `FULL` | All axes populated with normalized values, citations, P-mappings, and enforcement-mode tags; reconciled against every suite file that mentions the regime; divergence blocks complete |
| `SCAFFOLD` | All axes present; each has at minimum a normalized value + primary citation (or `[UNVERIFIED]`); tags applied; detail tables abbreviated |
| `STUB` | Record header + empty axes marked *not populated*, with pointers to any existing suite content |
| `SECTORAL` | Registered but not modeled on these axes; needs the sectoral variant profile (later phase) |

---

## Registry

| Record | File | Tier | Status |
|---|---|---|---|
| 🇨🇦 PIPEDA + Quebec Law 25 | `regulatory-taxonomy--ca-pipeda-law25.md` | 1 | FULL |
| 🇪🇺 GDPR + 🇬🇧 UK GDPR | `regulatory-taxonomy--eu-gdpr-uk.md` | 1 | FULL |
| 🇺🇸 CCPA/CPRA (California) | `regulatory-taxonomy--us-ca-ccpa.md` | 1 | FULL |
| 🇧🇷 LGPD | `regulatory-taxonomy--br-lgpd.md` | 2 | SCAFFOLD |
| 🇿🇦 POPIA | `regulatory-taxonomy--za-popia.md` | 2 | SCAFFOLD |
| 🇨🇳 PIPL | `regulatory-taxonomy--cn-pipl.md` | 2 | SCAFFOLD |
| 🇸🇬 PDPA (Singapore) | `regulatory-taxonomy--sg-pdpa.md` | 2 | SCAFFOLD |
| 🇲🇾 PDPA (Malaysia) | `regulatory-taxonomy--my-pdpa.md` | 2 | SCAFFOLD |
| 🇹🇭 PDPA (Thailand) | `regulatory-taxonomy--th-pdpa.md` | 2 | SCAFFOLD |
| 🇦🇺 Privacy Act 1988 + APPs | `regulatory-taxonomy--au-apps.md` | 3a | FULL |
| 🇯🇵 APPI | `regulatory-taxonomy--jp-appi.md` | 3a | FULL |
| 🇮🇳 DPDPA (not in force) | `regulatory-taxonomy--in-dpdpa.md` | 3a | FULL |
| 🇨🇭 nFADP | `regulatory-taxonomy--ch-nfadp.md` | 3b | SCAFFOLD |
| 🇰🇷 PIPA | `regulatory-taxonomy--kr-pipa.md` | 3b | SCAFFOLD |
| 🇦🇪 PDPL (federal; DIFC/ADGM separate) | `regulatory-taxonomy--ae-pdpl.md` | 3b | SCAFFOLD |
| 🇳🇬 NDPA | `regulatory-taxonomy--ng-ndpa.md` | 3b | SCAFFOLD |
| 🇻🇳 PDPD → **superseded by PDPL 91/2025/QH15, eff. 2026-01-01** | `regulatory-taxonomy--vn-pdpd.md` | 3b | SCAFFOLD (SUPERSEDED — re-author) |
| Long tail (AR 25.326, NZ Privacy Act, US states, SA/KE/ID — no suite source) | `regulatory-taxonomy--stubs.md` | 3c | STUB |
| 🇺🇸 HIPAA (health) | `regulatory-taxonomy--us-hipaa.md` | S | SECTORAL-OVERLAY |
| 🇺🇸 GLBA / FTC Safeguards (financial) | `regulatory-taxonomy--us-glba.md` | S | SECTORAL-OVERLAY |
| 🇺🇸 COPPA (children) | `regulatory-taxonomy--us-coppa.md` | S | SECTORAL-OVERLAY |
| 🇺🇸 BIPA (Illinois biometrics) | `regulatory-taxonomy--us-il-bipa.md` | S | SECTORAL-OVERLAY |
| 🇺🇸 FERPA (education) | `regulatory-taxonomy--us-ferpa.md` | S | SECTORAL-OVERLAY |
| 🇪🇺 ePrivacy Directive | `regulatory-taxonomy--eu-eprivacy.md` | S | SECTORAL-OVERLAY |
| 🇪🇺 NIS2 | `regulatory-taxonomy--eu-nis2.md` | S | SECTORAL-OVERLAY |
| 🇪🇺 DORA | `regulatory-taxonomy--eu-dora.md` | S | SECTORAL-OVERLAY |
| 🇪🇺 AI Act | `regulatory-taxonomy--eu-ai-act.md` | S | SECTORAL-OVERLAY |

**Derived artifacts** (regenerate on any record change): `regulatory-taxonomy--floor.md` — strictest-regime-wins design floor · `regulatory-taxonomy--conflicts.md` — cross-regime conflict register C1–C7 · `regulatory-taxonomy--arch-rollup.md` — architecture-vs-policy roll-up. Derived 2026-07-04 from Tier-1 + suite prose.

---

## Cross-Jurisdiction Quick Index (Phase-2 seed)

Compact answers to the motivating queries. Full strictest-wins derivation happens in Phase 2; this index is regenerated whenever a record changes.

**Breach clocks (regulator):** GDPR/UK 72h fixed · Quebec Law 25 **promptly** *(primary-source corrected 2026-07-05 — suite's prior 72h claim was wrong)* · LGPD 3 business days (ANPD Res. 15/2023) · Singapore PDPA 3 calendar days · Thailand PDPA 72h · PIPL "immediately" · PIPEDA "as soon as feasible" (RROSH) · POPIA "as soon as reasonably possible" · CCPA none (civil action only). Source: `consent-language--breach-notification.md` + reconciliation log.

**Children's ages:** US 13 (COPPA) · EU 16 default, member-state floor 13 · UK 13 (+AADC to 18) · Canada 13 (OPC guidance, non-statutory) · Brazil 18 · China 14 · South Africa 18 · Australia 15 (guidance). Source: `consent-language--childrens-consent.md`.

**Sensitive-data consent posture:** opt-in/explicit — GDPR Art. 9, Law 25 Art. 12 PPIPS, PIPL Arts. 28–32 (separate consent), LGPD Art. 11, APPI Art. 17(2) · rights-based limit — CCPA § 1798.121 · contextual, no closed list — PIPEDA (sensitivity scales safeguards, Cl. 4.7.1).

**Minimization test wording:** necessity (3-limb) — GDPR Art. 5(1)(c) · necessity + non-indiscriminate — PIPEDA Cl. 4.4.1 · reasonably-necessary-and-proportionate — CCPA § 1798.100(a)(3) · minimum-necessary + excessive-collection prohibition — PIPL Art. 6 · reasonable-person — Singapore PDPA s. 18.

**DPIA mandatory:** GDPR Art. 35(3) triggers + EDPB 09/2022 two-of-nine · Quebec Law 25 Art. 63.5 (any risky tech project, before implementation) · PIPL Art. 55 (sensitive PI, ADM, entrustment/sharing, export) · CCPA: CPPA risk-assessment rulemaking `[UNVERIFIED — confirm current reg status]`. Source: `privacy-impact-assessment--dpia-triggers.md`.

---

## Freeze Record — v1.0

Frozen 2026-07-04 after the axis set survived three structurally distinct regime types without special-casing:

| Stress | Regime | What it forced |
|---|---|---|
| Civil-law enumerated-basis necessity regime | GDPR | A2 `enumerated-bases`; A5 `prohibitive-list`; A8 `fixed-clock`; A12 `mandatory-triggered` |
| Common-law consent-centric reasonableness regime | PIPEDA (+ Law 25 overlay) | A2 `consent-centric` with no enumerated basis list; A5 `contextual` with **no closed category list**; A8 `promptness-standard`; A9 guidance-age (non-statutory); overlay mechanism for sub-national divergence |
| US notice-and-opt-out proportionality regime | CCPA/CPRA | A2 `notice-and-optout` with **no lawful-basis concept at all**; A5 `rights-based-list`; A6 rights that exist nowhere else (opt-out-of-sale, limit-sensitive); A8 `clock_model: none` |

Every axis accommodates all three via its enumerated field values; no axis is null for any of the three; no regime required a bespoke axis. The overlay/divergence-block mechanism handles sub-national and post-Brexit forks without new axes.

**Change control:** post-freeze changes append here (date · change · reason · records re-validated). The sectoral variant profile, when authored, extends this file without altering A0–A12.

- **2026-07-04 — v1.0 review (no schema change).** Axes re-validated against all nine populated records: no nulls, no bespoke axes, enums absorbed all three structural outliers. Gaps logged for **v1.1**: (1) governance-roles field under A1 — DPO/representative/records-of-processing/registration (Law 25 privacy officer, MY 2024 DPO; GDPR Arts. 30/37 and PIPL Art. 52 `[UNVERIFIED — not in suite sources]`); (2) direct-marketing sub-field under A2 (POPIA § 69, SG PDPA Part IX DNC; ePrivacy Art. 13 is sectoral). Neither blocks the derived artifacts — both are pure-PROCEDURAL classes; bundle with the sectoral variant profile.
