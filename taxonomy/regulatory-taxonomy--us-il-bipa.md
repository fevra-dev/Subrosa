# Sectoral Record: United States (Illinois) — BIPA

| | |
|---|---|
| **Record** | `us-il-bipa` · **Status:** SECTORAL-OVERLAY (S-profile v1.1) · **Current as of:** 2026-07-05 |
| **Instrument** | Biometric Information Privacy Act, 740 ILCS 14/1 et seq. (2008) |
| **Sources** | `skills/data-minimization/references/regulatory-reference.md` §BIPA |

## S0 — Scope Trigger
**Biometric identifiers/information × private entity × Illinois nexus.** Covered (§ 10): retina/iris scan, fingerprint, voiceprint, hand/face geometry scan, other biometric identifiers. **Not covered:** photographs, signatures, physical descriptions, demographics.

## S1 — Enforcement
**Private right of action — the defining feature.** $1,000 per negligent violation, $5,000 per intentional/reckless; fees and costs; **no aggregate cap, no proof of actual harm required**; 5-year SOL; **per-collection accrual** (500 employees scanned daily ≈ hundreds of thousands of violations). Most-litigated US privacy law: Meta $650M, BNSF $228M verdict, Google $100M, TikTok $92M. Class-action exposure is existential (sourced).

## S2 — Obligation Spine
- **§ 15(a)** — written, **public** retention-and-destruction policy **before any collection** (destroy at purpose satisfaction or within 3 years of last interaction). Companies lose cases on this alone (sourced).
- **§ 15(b)** — informed **written release** before collection: purpose + duration disclosed, signed. (Consent language template in source.)
- **§ 15(c)** — **no selling, leasing, trading, or profiting** from biometric data. Absolute.
- **§ 15(d)** — no disclosure absent consent / legal requirement / warrant.
- **§ 15(e)** — store/transmit at ≥ the standard for other confidential data, industry standard of care.

## S3 — Overlay Map (when S0 fires)
| Axis | Override |
|---|---|
| A5 | biometrics auto-CRITICAL with a **written-release** trigger — stricter consent form than any omnibus regime |
| A7 | § 15(a): **statutory TTL** — a mandatory public retention schedule, the only US law requiring one pre-collection |
| A2 | written consent only; no implied/deemed path; no opt-out alternative |
| A1 | exposure model inverts: per-violation PRA damages dwarf regulator fines — controls should be sized against class-action math, not penalty ceilings |
| A11 | § 15(e) comparative security standard |

## S4 — Interactions
CCPA treats biometric data as sensitive PI (limit-use right) — BIPA's written-release + PRA is strictly harder where both apply. Variants (sourced): TX CUBI (AG-only), WA My Health My Data, NYC LL 894 — registered in stubs.

## S5 — Defined Lists
§ 10 covered/excluded identifier lists (above, S0).

**Tags:** § 15(c) profit ban `ARCH-MANDATES` (only a design that cannot monetize biometrics complies absolutely) · **the dominant dissolution: don't collect biometrics if PIN/password works** — sourced P1 mapping; on-device matching (templates never leave the device / TEE per `skills/privacy-architecture/SKILL.md`) collapses the entire exposure · § 15(a)/(b) paper `PROCEDURAL` · § 15(e) `ARCH-SATISFIES`.
