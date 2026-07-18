# LINDDUN Crosswalk — locating Subrosa in the standard vocabulary

> **Why this file exists.** LINDDUN (KU Leuven; referenced by the NIST Privacy Framework) is the most established *privacy* threat-modeling taxonomy — the privacy counterpart to STRIDE. A privacy engineer arriving at this suite will already think in LINDDUN's seven categories. This crosswalk lets them locate Subrosa's home-grown vocabulary (adversary archetypes, the P1–P7 minimization principles, the A0–A12 taxonomy axes, and the architecture primitives) inside the framework they already use — and vice versa. It is a translation layer, not a replacement: Subrosa keeps its own vocabulary because it is tuned to individual/OPSEC and Web3 contexts LINDDUN treats generically.

LINDDUN is a mnemonic for seven privacy threat categories (the current formulation): **L**inking, **I**dentifying, **N**on-repudiation, **D**etecting, **D**ata disclosure, **U**nawareness & unintervenability, **N**on-compliance.

## The crosswalk

| LINDDUN threat | What it means | Subrosa archetype(s) | Minimization principle | Taxonomy axis | Dissolving/discharging primitive |
|---|---|---|---|---|---|
| **Linking** | Associating two+ data items or actions to the same subject/group without necessarily naming them | A2 OSINT Aggregator; A3 Crypto-Targeted (wallet clustering) | **P5** Identifier Minimality · **P6** Separation | A5 (sensitive inference), A10 (cross-context) | Stealth addresses, ring signatures, unlinkable credentials (BBS+); mixnets for the metadata layer |
| **Identifying** | Learning the actual identity behind data or a pseudonym | A2 Dossier Builder; A6 Institutional/Legal; A7 Nation-State | **P5** Identifier Minimality · **P3** Precision minimality | A0 scope, A5 | ZKP predicate proofs (prove attribute, not identity); anonymous credentials; k-anonymity/DP for release |
| **Non-repudiation** | The subject *cannot deny* an action — permanent attributable records where deniability was wanted | A5 Insider; A6 Legal (compelled evidence) | **P4** Storage Limitation · **P6** Separation | A7 retention, A8 breach exposure | Deniable messaging (Signal double ratchet / OTR); crypto-erasure; off-chain PII (C1) |
| **Detecting** | Inferring that a subject/record *exists* from observable side-effects, even without content | A3 Crypto-Targeted; A7 Nation-State (traffic analysis) | **P1** Collection Limitation · **P7** Crypto Minimization | A11 safeguards | Mixnets + cover traffic (the residual ZKPs don't cover — an interaction still *happened*); PSI |
| **Data disclosure** | Collecting/storing/processing/sharing more than necessary; leakage of the content itself | every archetype; A8 Supply-Chain/MCP | **P1** Collection · **P2** Purpose Binding · **P7** | A3 minimization, A4 purpose, A11 | The whole `data-minimization` skill; HE/MPC (compute without disclosing); TEE (discharge, not dissolve) |
| **Unawareness & unintervenability** | The subject is under-informed or cannot exercise control (access, correction, erasure, objection) | A6 Institutional (opaque processing) | (transparency/rights, not a P-principle) | A6 rights, A12 DPIA | Mostly `PROCEDURAL` — consent-language + PIA skills; the honest boundary where architecture doesn't dissolve the duty |
| **Non-compliance** | The system violates policy/regulation (the meta-threat) | A6 Institutional/Legal | all P1–P7 as controls | the entire taxonomy + `taxonomy/regulatory-taxonomy--floor.md` + `taxonomy/regulatory-taxonomy--conflicts.md` | The `skills/privacy-architecture/references/regulatory-dissolution.md` map is the answer to this row: which duties architecture discharges vs the procedural remainder |

## How the two models differ (and why Subrosa keeps its own)

- **LINDDUN is system/data-flow-centric** (threats per DFD element). **Subrosa's archetypes are adversary-centric** (who wants the data, with what capability — ICD 203 confidence framing). They compose: run LINDDUN to enumerate *threat types* against a data-flow, then Subrosa archetypes to weight *which adversary* makes each threat real for this subject. See `references/adversary-profiles.md`.
- **LINDDUN's Non-compliance is one box.** In Subrosa it is the entire taxonomy layer — because "compliant" is not binary but 27 records × 13 axes, and the interesting question (which the dissolution map answers) is *which* obligations architecture removes rather than merely satisfies.
- **Unawareness/unintervenability is where Subrosa is honest about its ceiling.** These are the `PROCEDURAL` duties architecture does not dissolve — the arch-rollup's "five workflows of paper." A crosswalk that pretended a primitive fixed this row would be the exact overclaim the suite's methodology rejects.

## Using it

- **Inbound (you think in LINDDUN):** find your threat category in column 1 → jump to the archetype, the minimization principle, and the primitive that addresses it.
- **Outbound (you're writing a Subrosa threat model):** tag each finding with its LINDDUN letter so a reviewer using the standard framework can audit coverage. A threat model that touches all seven has structural completeness in the vocabulary NIST points to.

*LINDDUN © KU Leuven (linddun.org); used here as an interoperability reference, not redistributed. Subrosa maps to it; it does not vendor it.*
