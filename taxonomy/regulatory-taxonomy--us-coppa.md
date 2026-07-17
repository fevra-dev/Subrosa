# Sectoral Record: United States — COPPA

| | |
|---|---|
| **Record** | `us-coppa` · **Status:** SECTORAL-OVERLAY (S-profile v1.1) · **Current as of:** 2026-07-05 |
| **Instruments** | COPPA, 15 U.S.C. §§ 6501–6506 · FTC COPPA Rule, 16 CFR Part 312 (amended 2013; 2023 amendments proposed — verify status) |
| **Sources** | `skills/data-minimization/references/regulatory-reference.md` §COPPA · `skills/consent-language/references/childrens-consent.md` |

## S0 — Scope Trigger
**Child-under-13 PI × (child-directed service ∪ actual knowledge).** "Directed to children" factors: § 312.2 (subject matter, visuals, characters, ads, models). Mixed-audience services: COPPA attaches per-user on actual knowledge. Applies regardless of operator location if directed at US children.

## S1 — Enforcement
FTC; state AGs under § 6504(b). Civil penalties to **$51,744 per violation per day** (2023-adjusted). No private right of action.

## S2 — Obligation Spine
- **Verifiable parental consent before collection** (§ 6502(b)(1)(A); § 312.5) — approved methods per § 312.5(b): email-plus, print-and-send, video conference, government-ID check (+ delete afterward), credit card, KBA; face-match proposed 2023. Email-only is not verifiable.
- **Notice** (§ 312.5(a) + § 312.4 `[UNVERIFIED — § 312.4 not in suite sources; substance is standard COPPA but confirm against 16 CFR]`): home page and every collection point; direct notice to parents.
- **No conditioning** (§ 6502(b)(1)(D) via § 312.7): participation may not be conditioned on more PI than reasonably necessary.
- **Retention/deletion** (§ 312.10): keep only as long as reasonably necessary; protected deletion.
- **Neutral age screening**: no PI collection after an under-13 signal; no re-ask; no bypassable gates ("actual knowledge" accrues on circumventable screens).
- **Parental rights**: review, delete, refuse further collection, revoke.

## S3 — Overlay Map (when S0 fires)
| Axis | Override |
|---|---|
| A9 | full override: the under-13 regime *is* COPPA — VPC methods, notice mechanics, parental rights replace omnibus children's provisions for US children |
| A3 | § 312.7 conditioning ban — a statutory minimization test keyed to service necessity |
| A5 | **persistent identifiers (cookie, IP, device ID, advertising ID) are PI** when associated with a child — quasi-identifiers get promoted to PI by statute |
| A7 | § 312.10 purpose-bounded retention + protected deletion |
| A2 | consent model becomes parent-mediated opt-in; no deemed/implied consent path |

## S4 — Interactions
Layers under CCPA's minor provisions (13–16 opt-in, § 1798.120(c) `[UNVERIFIED]`) and parallels UK AADC's broader under-18 design duties. **Conflict C5** (`regulatory-taxonomy--conflicts.md`): VPC's verification-data paradox — resolution: ephemeral verification, delete-after-check; architectural end-state: ZKP age/guardianship proofs.

## S5 — Defined Lists
**COPPA PI** (§ 312.2): name; address; email; phone; SSN; persistent identifiers; photo/video/audio of the child; geolocation; anything permitting contact.

**Tags:** age-gate-without-PI + no-tracking design `ARCH-MANDATES`-adjacent (the compliant gate is an architecture property) · ephemeral verification `ARCH-SATISFIES` · VPC mechanics, notices, parental-rights workflow `PROCEDURAL`.
