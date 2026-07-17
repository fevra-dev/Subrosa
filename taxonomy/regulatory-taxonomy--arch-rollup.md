# Architecture-vs-Policy Roll-Up (the cypherpunk payoff)

**Derived 2026-07-04 from the enforcement-mode tags across all nine schema-v1.0 records; extended same day to seventeen records after the Tier-3 merge.** This is the operational form of the suite thesis: *compliance is a floor, selective disclosure is the ceiling* (`skills/privacy-suite/SKILL.md`). It answers: which obligations **dissolve** under a selective-disclosure architecture, which are **discharged** by technical measures, and which are **irreducibly procedural** — the paper that remains when the architecture has done everything architecture can do.

Baseline rule (master, tagging rule 1): data never collected creates no duty under any regime — Hughes' transaction-necessity principle and every A3 minimization hook are the *same statement*. The roll-up below is about the data a system does hold.

---

## Per-axis dominant mode (across all 9 records)

| Axis | Dominant mode | Consistency across regimes | Dissolving/discharging primitive (`skills/privacy-architecture/SKILL.md`) |
|---|---|---|---|
| A3 collection limitation | **ARCH-DISSOLVES** | 9/9 — every regime's minimization hook is satisfied by construction | The architecture itself: selective disclosure ≡ the statutory test |
| A5 sensitive categories | **ARCH-DISSOLVES** (where provable-not-disclosable) | 7/9 tagged dissolvable | ZKP predicate proofs, anonymous credentials (BBS+, CL) — prove the attribute, never hold it |
| A8 breach — *trigger surface* | **ARCH-DISSOLVES / ARCH-SATISFIES** | universal — every threshold (RROSH, serious-injury, significant-harm, 500-person) is a function of holdings; encryption safe-harbors defeat individual-notice triggers | Minimized holdings, commitments, encryption-at-rest |
| A7 retention/erasure | **ARCH-SATISFIES** (dissolves for commitment-only holdings) | 9/9 | Automated TTL, crypto-erasure/key destruction, off-chain PII + on-chain commitments |
| A10 cross-border | **ARCH-DISSOLVES** (partial) | 5/9 explicitly | Local-only processing, PSI/MPC/HE (compute crosses, data doesn't), DP aggregation pre-export |
| A11 safeguards | **ARCH-SATISFIES** | 9/9 | Encryption, tokenization, HMAC (P7) |
| A4 purpose limitation | split: PROCEDURAL (declaration) + ARCH-SATISFIES (binding) | 9/9 split the same way | Separation (P6) + scoped identifiers (P5) make cross-purpose reuse *impossible*, not just forbidden |
| A2 consent/basis | **PROCEDURAL** | 9/9 | — (though selective disclosure shrinks what consent must cover) |
| A6 rights workflow | **PROCEDURAL** | 9/9 (scope shrinks with holdings) | — |
| A9 children | **PROCEDURAL** (AADC defaults are ARCH-SATISFIES) | 8/9 | ZKP age proofs are the C5 end-state, not yet regulator-approved |
| A12 DPIA/PIA | **PROCEDURAL** | all regimes that have one | — (architecture shrinks the risk register the paper documents) |
| A1/A0 | — (exposure/scope, not obligations) | — | — |

Approximate cell count across the seventeen records: **~60% of tagged obligation-cells dissolve or are discharged architecturally; ~40% are procedural** — and the procedural cells cluster into five workflows (below), not forty obligations. The Tier-3 merge *strengthened* the dissolves column (next section).

---

## Statutory recognition of the architecture (Tier-3 finding)

The long-tail regimes turned out to contain the strongest pro-architecture statutes in the whole set — four places where the *law itself* names the architectural move:

| Statute | Provision | What it recognizes |
|---|---|---|
| 🇦🇺 APP 2 | Offer anonymous/pseudonymous interaction where lawful and practicable | The only modeled statute that **mandates offering** selective disclosure — an `ARCH-MANDATES` case beyond our three-tag vocabulary; the option itself is the legal duty |
| 🇯🇵 APPI 2022 | 仮名加工情報 / 匿名加工情報 categories | A **statutory reward ladder** for the suite's remediation vocabulary: TOKENIZE earns the pseudonymized tier's lighter obligations, full anonymization exits core scope |
| 🇰🇷 PIPA Art. 3(7), Art. 21, Art. 23 | Process anonymously where possible; irreversible destruction; segregated sensitive storage | Statutory forms of P5 (anonymity preference), crypto-erasure fit (irreversibility is what key destruction provides), and P6 (separation as law) |
| 🇮🇳 DPDPA § 9 | Ban on behavioral tracking/targeted ads at children | A **no-tracking mandate** — satisfiable only by not building the tracking; policy cannot comply, only architecture can *(not in force as of June 2026)* |

This inverts the usual compliance posture: in these four regimes, the selective-disclosure design isn't just the cheapest way to comply — parts of it are the *compliance target itself*. Hughes wrote code because law wouldn't; these provisions are law catching up to the code.

---

## The irreducible procedural core

What remains for a system built to the suite's design target (selective disclosure by construction):

1. **Transparency paper** — notices at collection, purpose declarations, transfer disclosures (GDPR Arts. 13/14, CCPA § 1798.100(b), PIPL Art. 17, PIPEDA Cl. 4.8). Honest framing: this is the one obligation class that *grows* slightly under exotic architecture — you must explain ZKPs in Grade-8 language.
2. **Rights-request workflow** — receive, verify, respond on the 30-day floor (15-day if Brazil). Selective disclosure shrinks every response ("we hold: a commitment and a proof") but the workflow must exist.
3. **Assessment paper** — PIA before risky projects (Law 25 Art. 63.5 floor), EDPB screening, records kept ≥3 years (PIPL floor). Architecture shrinks the risk register; it cannot write the document.
4. **Breach duty once triggered** — the 72h pipeline must exist even if minimization makes firing it unlikely.
5. **Consent/verification mechanics** — sensitive-data opt-in UX, children's gates, GPC plumbing (the plumbing itself is ARCH-SATISFIES; the *duty to offer it* is procedural).
6. *(v1.1 gap, logged)* **Governance roles** — DPO/representative/RoPA. Pure paper; will land in axis A1 when unfrozen.

---

## The theorem, operationally

**Failure Mode 1** (`skills/privacy-suite/SKILL.md`) — policy without architecture — is a system living entirely in the procedural column, holding everything and promising restraint. Its compliance surface is all 13 axes, forever, in every jurisdiction it touches.

**Failure Mode 2** — compliance without privacy — passes audits while forcing disclosure structurally. The roll-up exposes it: its A3/A5/A10 cells never dissolve; it pays the full procedural bill *and* the full breach/transfer exposure.

**The design target** collapses the surface: build selective disclosure and eight of thirteen axes are satisfied by the same controls that constitute the product — what's left is five workflows of paper. Architecture is not an alternative to compliance; it is the cheapest compliance program that exists. Chaum (1985) said this first; the matrix above is the statutory proof.

**Primitive → obligation map** (bridge to `skills/privacy-architecture/SKILL.md`):
ZKP/anonymous credentials → A5, A9 (C5) · commitments + off-chain storage → A7, C1 · local-only/PSI/MPC/HE → A10, C3/C4 · DP/aggregation → A3, A8-scope · encryption/key-destruction → A7, A8 safe-harbor, A11 · tokenization/HMAC → A11, C6 · separation (P6) → A4, C7.
