# Record: United States (California) — CCPA/CPRA

| | |
|---|---|
| **Record** | `us-ca-ccpa` |
| **Instruments** | CCPA, Cal. Civ. Code §§ 1798.100–1798.199.100 (eff. Jan 1 2020) · CPRA, Prop. 24 (Nov 2020; substantive provisions eff. Jan 1 2023) · CPPA regs, Cal. Code Regs. tit. 11 — **ADMT / risk-assessment / cybersecurity-audit regs adopted Jul 24 2025, OAL-approved Sep 23 2025, eff. Jan 1 2026** |
| **Status / Tier** | FULL / Tier 1 |
| **Schema** | v1.0 |
| **Current as of** | 2026-07-17 (currency sweep, web-verified) |
| **Sources** | `skills/data-minimization/references/regulatory-reference.md` · `skills/data-minimization/references/pipeda-gdpr.md` · `skills/consent-language/SKILL.md` · `skills/consent-language/references/rights-language.md` · `skills/consent-language/references/breach-notification.md` · `skills/consent-language/references/cookie-consent.md` |
| **Related** | Other US state omnibus laws (CO, CT, VA, UT, TX, MT, OR, DE per `skills/consent-language/references/cookie-consent.md`) — long-tail candidates, not modeled here. Federal sectoral overlays (COPPA, HIPAA, GLBA, BIPA-IL) registered SECTORAL in master |
| **Companion statute** | **Delete Act (SB 362)** — see A6 note; data-broker registration + one-stop deletion (DROP), enforced by the same agency (CPPA/CalPrivacy) |

**Design rule (sourced):** CPRA aligned California materially with GDPR on minimization and purpose limitation — design to CPRA standard = materially GDPR-compatible for most data types.

---

## A0 — Scope & Applicability

- **Territorial:** businesses collecting PI of California residents ("consumers").
- **Thresholds (§ 1798.140(d), web-verified 2026-07-17):** for-profit businesses doing business in California meeting any of: >$25M annual gross revenue (CPI-adjusted to **$26.625M for 2026**, per CPPA adjustment); buys/sells/shares PI of 100,000+ consumers or households; ≥50% revenue from selling/sharing PI.
- Extraterritorial reach: follows the **consumer's California residency**, subject to the doing-business-in-California nexus (§ 1798.140(d) chapeau — web-verified 2026-07-17).

## A1 — Enforcement

- Authority: **CPPA** (rulemaking + enforcement transferred from AG, § 1798.199.40).
- Penalty ceiling (**§ 1798.155**, web-verified 2026-07-17): administrative fines up to **$2,500 per violation; $7,500 per intentional violation or violations involving PI of consumers known to be under 16** (amounts CPI-adjusted by the CPPA).
- **Private right of action: YES, breach-only** — § 1798.150 (reasonable security; statutory damages for breaches). No general private right of action.

## A2 — Lawful Basis & Consent Model

- `basis_model:` **notice-and-optout** — no lawful-basis concept. Processing is permitted subject to at-collection notice (§ 1798.100(b)) and consumer rights; the control point is *disclosure + opt-out*, not authorization.
- Default posture: **opt-out** for sale/sharing (§§ 1798.120, 1798.135); **GPC signal is a valid opt-out** and must be honored (Cal. Code Regs. tit. 11, § 7026).
- Sensitive escalation: not consent but a **right to limit use** of sensitive PI to what is necessary to perform the service (§ 1798.121), with special notice.
- Two request-submission methods minimum; 15 business days to process opt-outs (per `skills/consent-language/references/rights-language.md`).

Tag: `PROCEDURAL` (notice + signal plumbing); GPC honoring is `ARCH-SATISFIES` (a technical control implements the legal duty).

## A3 — Collection Limitation (minimization hook)

- `test_type:` **proportionality + necessity.**
- **§ 1798.100(c)** *(anchor corrected 2026-07-17 — previously miscited as (a)(3), which is the retention-disclosure/limitation provision)*: collection, use, retention, and sharing must be "reasonably necessary and proportionate" to the disclosed purpose. Proportionality is a second limb beyond necessity — a field may be necessary yet still fail as disproportionate.

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
| **ADMT** (significant decisions): pre-use notice, **opt-out**, access to logic/key parameters/effects | CPPA ADMT regs, eff. Jan 1 2026; compliance by **Jan 1 2027** (web-verified 2026-07-17). No GDPR-style restriction/objection rights |

- **Response clock:** 45 days + 45-day extension (notify within first 45) — per `skills/consent-language/references/rights-language.md`. Opt-outs: 15 business days.
- Complaint route: cppa.ca.gov.
- **Delete Act (SB 362) — universal broker deletion (web-verified 2026-07-17):** a *statutory* one-stop erasure mechanism distinct from the per-business § 1798.105 right. **DROP** (Delete Request & Opt-out Platform) went **live for consumers Jan 1 2026**; registered **data brokers must process DROP requests from Aug 1 2026** (retrieve ≥ every 45 days, delete within 90 days absent an exception). CalPrivacy issued broker-registration enforcement decisions within a week of launch (Jan 8 2026). This is the current state of "data-broker removal" — supersedes the manual/DeleteMe-era mitigation in `skills/threat-model-privacy/references/mitigations.md`.

Tag: `PROCEDURAL` (broker-side processing duty) + `ARCH-DISSOLVES` for holdings the broker never collected — DROP only reaches registered data brokers.

## A7 — Retention & Erasure

- Deletion on verifiable request (§ 1798.105) — **no soft-delete** (sourced).
- Retention disclosure (**§ 1798.100(a)(3)**, web-verified 2026-07-17): the at-collection notice must state the intended **retention period per category, or the criteria** used to determine it — and PI may not be retained longer than reasonably necessary for the disclosed purpose.

P-mapping: P4, P6. Tag: `ARCH-SATISFIES` (hard-delete paths, TTL); `ARCH-DISSOLVES` for never-collected/aggregate-only holdings.

## A8 — Breach Notification

- `clock_model:` **none** — CCPA has no regulator-notification duty; § 1798.150 creates breach *liability* (private right of action for unauthorized access resulting from failure to maintain reasonable security). Per `skills/consent-language/references/breach-notification.md`: "N/A (civil action only)."
- California's separate general breach-notification statute (Civ. Code § 1798.82) is out of scope of the suite sources — *not located* `[UNVERIFIED]`.

Tag: the exposure is economic, not procedural — `ARCH-SATISFIES`/`ARCH-DISSOLVES` dominate: reasonable security defeats § 1798.150 liability, and minimized holdings shrink the class.

## A9 — Children

- CCPA/CPRA layer (**§ 1798.120(c)**, web-verified 2026-07-17): no sale/sharing with actual knowledge the consumer is under 16 unless **13–16 affirmatively authorize it themselves; under-13 requires parent/guardian authorization**; willful disregard of age = actual knowledge.
- Federal overlay: **COPPA** (under 13, verifiable parental consent) — registered SECTORAL; full mechanics in `skills/consent-language/references/childrens-consent.md`.

Tag: `PROCEDURAL`.

## A10 — Cross-Border Transfer

- `transfer_model:` **none-specific** — no transfer regime in suite sources; obligations follow the data via contract (service-provider terms) rather than geography — *not located* / `[UNVERIFIED]`.

Tag: —.

## A11 — Security Safeguards

- § 1798.150: duty to implement and maintain **reasonable security procedures** — enforced through the breach private right of action. Specificity: principles-based.

P-mapping: P7. Tag: `ARCH-SATISFIES`.

## A12 — DPIA / PIA

- `dpia_model:` **regulatory risk-assessment** — none in the statute; the CPPA regs (eff. Jan 1 2026, web-verified 2026-07-17) require documented **risk assessments before significant-risk processing**: selling/sharing PI, processing sensitive PI, ADMT for significant decisions, training ADMT on PI. Ongoing pre-2026 activities: assess by **Dec 31 2027**; first filing to the CPPA (attestation + summary) **Apr 1 2028**.
- **Annual cybersecurity audits** for businesses deriving ≥50% revenue from selling/sharing PI, or meeting the revenue threshold plus 250k+ consumers / 50k+ sensitive-PI consumers; submissions phased **Apr 1 2028 / 2029 / 2030** by revenue tier.

Tag: `PROCEDURAL` (assessment + filing duties).

---

## Divergence Notes — vs the other Tier-1 records

- Only Tier-1 regime with **no lawful-basis concept**, **no regulator breach clock**, and a **breach-only private right of action**.
- Only regime whose sensitive-data protection is a *consumer right* (limit-use) rather than a processing prohibition (GDPR Art. 9) or consent escalation (Law 25 Art. 12).
- Proportionality limb (§ 1798.100(c)) is the strictest *wording* of the minimization test among Tier-1 — a necessity-passing field can still fail.
- GPC: the only Tier-1 regime where a browser signal is a legally binding opt-out (tit. 11 § 7026); EU treats GPC as withdrawal-only (EDPB Op. 8/2024); UK as legitimate signal (ICO draft).
