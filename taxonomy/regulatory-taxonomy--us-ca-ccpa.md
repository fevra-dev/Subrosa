# Record: United States (California) — CCPA/CPRA

| | |
|---|---|
| **Record** | `us-ca-ccpa` |
| **Instruments** | CCPA, Cal. Civ. Code §§ 1798.100–1798.199.100 (eff. Jan 1 2020) · CPRA, Prop. 24 (Nov 2020; substantive provisions eff. Jan 1 2023) · CPPA regs, Cal. Code Regs. tit. 11 |
| **Status / Tier** | FULL / Tier 1 |
| **Schema** | v1.0 |
| **Current as of** | 2026-07-04 (content dated June 2026 in sources) |
| **Sources** | `skills/data-minimization/references/regulatory-reference.md` · `skills/data-minimization/references/pipeda-gdpr.md` · `skills/consent-language/SKILL.md` · `skills/consent-language/references/rights-language.md` · `skills/consent-language/references/breach-notification.md` · `skills/consent-language/references/cookie-consent.md` |
| **Related** | Other US state omnibus laws (CO, CT, VA, UT, TX, MT, OR, DE per `skills/consent-language/references/cookie-consent.md`) — long-tail candidates, not modeled here. Federal sectoral overlays (COPPA, HIPAA, GLBA, BIPA-IL) registered SECTORAL in master |

**Design rule (sourced):** CPRA aligned California materially with GDPR on minimization and purpose limitation — design to CPRA standard = materially GDPR-compatible for most data types.

---

## A0 — Scope & Applicability

- **Territorial:** businesses collecting PI of California residents ("consumers").
- **Thresholds:** for-profit businesses meeting any of: >$25M annual gross revenue; buys/sells/shares PI of 100,000+ consumers or households; ≥50% revenue from selling/sharing PI. `[UNVERIFIED — thresholds not in suite sources; confirm § 1798.140(d) against primary source]`
- Extraterritorial reach: follows residency of the consumer, not location of the business `[UNVERIFIED]`.

## A1 — Enforcement

- Authority: **CPPA** (rulemaking + enforcement transferred from AG, § 1798.199.40).
- Penalty ceiling: not stated in suite sources — *not located*. `[UNVERIFIED — administrative fines per violation under § 1798.155; confirm amounts]`
- **Private right of action: YES, breach-only** — § 1798.150 (reasonable security; statutory damages for breaches). No general private right of action.

## A2 — Lawful Basis & Consent Model

- `basis_model:` **notice-and-optout** — no lawful-basis concept. Processing is permitted subject to at-collection notice (§ 1798.100(b)) and consumer rights; the control point is *disclosure + opt-out*, not authorization.
- Default posture: **opt-out** for sale/sharing (§§ 1798.120, 1798.135); **GPC signal is a valid opt-out** and must be honored (Cal. Code Regs. tit. 11, § 7026).
- Sensitive escalation: not consent but a **right to limit use** of sensitive PI to what is necessary to perform the service (§ 1798.121), with special notice.
- Two request-submission methods minimum; 15 business days to process opt-outs (per `skills/consent-language/references/rights-language.md`).

Tag: `PROCEDURAL` (notice + signal plumbing); GPC honoring is `ARCH-SATISFIES` (a technical control implements the legal duty).

## A3 — Collection Limitation (minimization hook)

- `test_type:` **proportionality + necessity.**
- **§ 1798.100(a)(3):** collection, use, retention, and sharing must be "reasonably necessary and proportionate" to the disclosed purpose. Proportionality is a second limb beyond necessity — a field may be necessary yet still fail as disproportionate.

P-mapping: **P1**. Tag: `ARCH-DISSOLVES` — same construction-satisfies logic as GDPR Art. 25 / PIPEDA 4.4.

## A4 — Purpose Limitation

- **§ 1798.100(a)(4):** no use incompatible with purposes disclosed at collection.

P-mapping: P2. Tag: `PROCEDURAL` (disclosure) + `ARCH-SATISFIES` via separation/scoped identifiers.

## A5 — Sensitive Categories

- `sensitive_model:` **rights-based-list.** § 1798.140(ae): SSN/passport/DL numbers; financial account + credentials; **precise geolocation (within 1,850 ft / ~565 m)**; racial/ethnic origin; religious beliefs; union membership; contents of mail/email/texts; genetic data; biometric data; health/medical; sexual orientation or gender identity. Always CRITICAL tier (sourced).
- Trigger: right to limit use (§ 1798.121) + special notice — not a processing prohibition.

Tag: `ARCH-DISSOLVES` where the sensitive attribute is never held in usable form (geolocation truncation defeats the 1,850-ft precision definition — a TRUNCATE remediation moves the field *out of the sensitive class by statutory definition*); otherwise `PROCEDURAL`.

## A6 — Data-Subject Rights

| Right | Basis |
|---|---|
| Know / access (categories + specific pieces, sources, purposes, third parties) | § 1798.100 |
| Delete (no soft-delete) | § 1798.105 |
| Correct | § 1798.106 (CPRA) |
| Portability (portable, readily usable format) | § 1798.100 |
| **Opt out of sale/sharing** | §§ 1798.120, 1798.135 |
| **Limit use of sensitive PI** | § 1798.121 |
| Non-discrimination for exercising rights | § 1798.125 |
| Restriction / objection / ADM | — (no GDPR-style equivalents in suite sources; CPPA ADM rulemaking `[UNVERIFIED — confirm current reg status]`) |

- **Response clock:** 45 days + 45-day extension (notify within first 45) — per `skills/consent-language/references/rights-language.md`. Opt-outs: 15 business days.
- Complaint route: cppa.ca.gov.

Tag: `PROCEDURAL`.

## A7 — Retention & Erasure

- Deletion on verifiable request (§ 1798.105) — **no soft-delete** (sourced).
- Retention disclosure: retention periods or criteria must be disclosed at collection `[UNVERIFIED — § 1798.100(a)(3) retention limb sourced; the at-collection retention-disclosure duty under § 1798.100(b) not detailed in suite sources]`.

P-mapping: P4, P6. Tag: `ARCH-SATISFIES` (hard-delete paths, TTL); `ARCH-DISSOLVES` for never-collected/aggregate-only holdings.

## A8 — Breach Notification

- `clock_model:` **none** — CCPA has no regulator-notification duty; § 1798.150 creates breach *liability* (private right of action for unauthorized access resulting from failure to maintain reasonable security). Per `skills/consent-language/references/breach-notification.md`: "N/A (civil action only)."
- California's separate general breach-notification statute (Civ. Code § 1798.82) is out of scope of the suite sources — *not located* `[UNVERIFIED]`.

Tag: the exposure is economic, not procedural — `ARCH-SATISFIES`/`ARCH-DISSOLVES` dominate: reasonable security defeats § 1798.150 liability, and minimized holdings shrink the class.

## A9 — Children

- CCPA/CPRA layer: affirmative authorization (opt-in) required for sale/sharing of PI of consumers under 16; parental consent under 13 `[UNVERIFIED — § 1798.120(c) not in suite sources; confirm]`.
- Federal overlay: **COPPA** (under 13, verifiable parental consent) — registered SECTORAL; full mechanics in `skills/consent-language/references/childrens-consent.md`.

Tag: `PROCEDURAL`.

## A10 — Cross-Border Transfer

- `transfer_model:` **none-specific** — no transfer regime in suite sources; obligations follow the data via contract (service-provider terms) rather than geography — *not located* / `[UNVERIFIED]`.

Tag: —.

## A11 — Security Safeguards

- § 1798.150: duty to implement and maintain **reasonable security procedures** — enforced through the breach private right of action. Specificity: principles-based.

P-mapping: P7. Tag: `ARCH-SATISFIES`.

## A12 — DPIA / PIA

- `dpia_model:` **none** in the statute as sourced. CPPA rulemaking on risk assessments / cybersecurity audits for high-risk processing: `[UNVERIFIED — confirm current status of CPPA regs before advising]`.

Tag: — (pending rulemaking).

---

## Divergence Notes — vs the other Tier-1 records

- Only Tier-1 regime with **no lawful-basis concept**, **no regulator breach clock**, and a **breach-only private right of action**.
- Only regime whose sensitive-data protection is a *consumer right* (limit-use) rather than a processing prohibition (GDPR Art. 9) or consent escalation (Law 25 Art. 12).
- Proportionality limb (§ 1798.100(a)(3)) is the strictest *wording* of the minimization test among Tier-1 — a necessity-passing field can still fail.
- GPC: the only Tier-1 regime where a browser signal is a legally binding opt-out (tit. 11 § 7026); EU treats GPC as withdrawal-only (EDPB Op. 8/2024); UK as legitimate signal (ICO draft).
