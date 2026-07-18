# Sectoral Record: UK — Online Safety Act (age assurance)

| | |
|---|---|
| **Record** | `uk-osa` · **Status:** SECTORAL-OVERLAY (S-profile v1.1) · **Current as of:** 2026-07-17 (web-verified) |
| **Instruments** | Online Safety Act 2023 (c. 50); Ofcom codes + guidance. **Highly-effective age assurance (HEAA) enforceable from 25 July 2025** (Part 3 user-to-user/search "primary priority content"; Part 5 services publishing their own pornography) |
| **Sources** | **Web research 2026-07-17** (Ofcom age-assurance guidance; Ofcom Part 3/Part 5 enforcement programme; GOV.UK OSA explainer). No prior suite grounding source — a new coverage area |
| **Companion** | Conflict **C5** (`regulatory-taxonomy--conflicts.md`) — the age-verification/minimization paradox; US parallel below |

**Why this record exists:** the suite modeled children's *consent* (COPPA VPC, GDPR Art. 8) but not the 2025 **age-assurance wave** — the first regime to *mandate* the exact problem the dissolution map already answers with ZK age predicates. It is the strongest real-world case that privacy-preserving age proof is not academic: regulators now require age gates on pain of revenue-percentage fines, and the naive implementation (collect government ID from every visitor) is a mass-surveillance honeypot. This record is where the C5 architecture meets a live enforcement deadline.

## S0 — Scope Trigger
Services with UK users that provide (a) **pornographic content they publish themselves** (Part 5), or (b) user-to-user / search services where children can encounter **"primary priority content"** — pornography, and content encouraging suicide, self-harm, or eating disorders (Part 3). Extraterritorial: applies by UK-user linkage, not establishment.

## S1 — Enforcement
**Ofcom.** Penalties: up to **£18M or 10% of qualifying worldwide revenue, whichever is greater**; business-disruption measures and, for senior managers, potential criminal liability for non-compliance with information notices. Active enforcement programme opened against Part 3 and Part 5 services from July 2025.

## S2 — Obligation Spine
- **Highly-effective age assurance (HEAA):** age checks must be *technically accurate, robust, reliable, and fair.* **Passive self-declaration (tick-box "I am 18", self-certification) is explicitly no longer permissible.** Accepted methods include facial age estimation, ID-document + liveness checks, open-banking/credit-card checks, mobile-network-operator age flags, and digital identity wallets.
- **Data-protection duty runs alongside:** the age-assurance process is itself personal-data processing under UK GDPR — the check must be data-minimizing (verify age, do not build an identity record), which is exactly the tension C5 names.
- **Children's Access Assessment + risk assessment** duties feed the HEAA obligation.

## S3 — Overlay Map (when S0 fires)
| Axis | Override |
|---|---|
| A9 | age *assurance* (prove the age band) becomes a hard gate, distinct from age *consent*; the floor moves from "reasonable efforts" (GDPR Art. 8(2)) to "highly effective" |
| A3 | minimization applies *to the age check itself* — the statutory-quality demand ("fair", data-protection-compliant) forbids retaining verification documents; verify-and-discard is the compliant pattern |
| A5 | verification data (face scan, ID image) is biometric/special-category the instant it is collected — escalates to CRITICAL, which is the argument *against* retention-based methods |
| A12 | Children's Access Assessment is a mandatory risk-assessment class (procedural) |

## S4 — Interactions
Sits alongside UK GDPR (age assurance is processing; UK ICO + Ofcom joint statement on age assurance and data protection). Parallels the **US age-verification wave**: in ***Free Speech Coalition v. Paxton*, 606 U.S. 461 (June 27 2025)**, the Supreme Court (6–3) upheld Texas HB 1181's age-verification mandate for sites one-third-or-more "sexual material harmful to minors" under intermediate scrutiny — with ~two dozen states holding similar laws. The dissent and EFF's critique both turn on the *privacy* cost of ID-based verification, which is precisely the cost a ZK age predicate removes. Also parallels the **EU AADC-style** age-appropriate-design expectations and **COPPA** (record `us-coppa`).

## S5 — Defined Lists
"Primary priority content" and "priority content" categories (OSA + Ofcom); the HEAA accepted-methods and rejected-methods (self-declaration) lists.

**Tags:** the age gate itself `PROCEDURAL` (a duty to check) — but the *method* is where architecture decides the privacy outcome: **retention-based ID checks are a surveillance honeypot; ZK age/attribute proofs `ARCH-SATISFIES` the "highly effective" bar while dissolving the data-retention exposure** (`skills/privacy-architecture/references/zkp.md` predicate proofs; `skills/privacy-architecture/references/credentials.md` anonymous credentials — the C5 end-state). Verify-and-discard is the interim `ARCH-SATISFIES` control. This is the record where "compliance is a floor, selective disclosure is the ceiling" is most concretely demonstrable: two implementations of the *same* legal duty, one a honeypot and one a proof.
