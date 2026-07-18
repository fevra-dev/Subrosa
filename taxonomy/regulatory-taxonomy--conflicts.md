# Cross-Regime Conflict Register

**Derived 2026-07-04 from schema v1.0 records + suite prose.** Obligations that are mutually incompatible — or in structural tension — across regimes. Each entry: the colliding obligations, why they collide, the suite's recommended resolution, residual risk, and the enforcement-mode reading (which side architecture dissolves). Not legal advice.

---

## C1 — Erasure rights vs immutable storage
**Collides:** GDPR Art. 17 / Law 25 Art. 28 PPIPS / LGPD Art. 18(VI) / PIPL Art. 47 (erasure) / **KR PIPA Art. 21 (destruction must be *irreversible* — the sharpest form of the duty)** ↔ any append-only or public-chain design.
**Mechanism:** the statutes assume deletion is physically possible; a public ledger makes it impossible post-write. The suite's canonical collision between privacy-by-architecture and privacy-by-policy (`skills/privacy-suite/SKILL.md` §Blockchain Continuity).
**Resolution (sourced):** personal data fully off-chain; only content-addressed commitments on-chain; where on-chain payloads are unavoidable, encrypt-before-write and treat key destruction as practical erasure; the suite's blockchain caveat clause (`skills/consent-language/references/rights-language.md`) discloses the residue.
**Residual risk:** encryption-as-erasure is not settled law (EDPB Guidelines 05/2019 acknowledge without resolving); consult the competent DPA before relying on it in a regulated context.
**Arch reading:** `ARCH-DISSOLVES` — PII that never touches the chain never conflicts.

## C2 — Mandated security logging vs storage limitation
**Collides:** EU AI Act Art. 12 (high-risk AI operation logs) / NIS2 Arts. 21, 23 / DORA Arts. 10, 17 / GLBA audit-trail duties ↔ GDPR Art. 5(1)(e) / PIPEDA Cl. 4.5.3 (don't retain).
**Mechanism:** one regime mandates retention the other mandates minimizing — both apply to the same log line.
**Resolution (sourced):** tiered retention (hot/warm/cold) with sensitivity-graded TTLs on log *fields*, pseudonymized identity fields in logs, and a documented MINIMIZATION EXCEPTION RECORD per retained high-fidelity field (`skills/data-minimization/references/regulatory-reference.md` template).
**Residual risk:** TTL choices are judgment calls a regulator can second-guess; the exception record is the defense.
**Arch reading:** `ARCH-SATISFIES` — the conflict is dissolved at field granularity, not log granularity.

## C3 — Localization regimes vs global service architecture and portability
**Collides:** PIPL Arts. 38–43 (CAC assessment/contract/certification; Art. 43 reciprocity) + **VN PDPL 91/2025 (DPIA + Transfer Impact Assessment dossiers filed with A05; 5%-of-revenue penalty tier — note: the PDPL text reviewed carries no localization mandate; Vietnam's separate Cybersecurity Law/Decree 53 regime may still, `[UNVERIFIED]`)** ↔ GDPR Art. 20 portability, global processing topologies, Law 25 Art. 17 outbound assessments.
**Mechanism:** data that lawfully cannot leave the territory cannot be ported, replicated, or centrally processed; PIPL volume thresholds (1M+ individuals; 100k+/10k+ sensitive) trip mandatory CAC assessment; Vietnam adds a hard storage-location mandate.
**Resolution:** regional data residency; collect-locally-process-locally; and the sourced design rule — *if you cannot lawfully transfer it, don't collect it*.
**Residual risk:** CAC discretion and reciprocity countermeasures are policy-driven and can shift without statutory change.
**Arch reading:** `ARCH-DISSOLVES` under local-only/edge processing; PSI/MPC/HE let global functions run without the data crossing (`skills/privacy-architecture/SKILL.md`).

## C4 — Quebec outbound-communication assessment vs cloud defaults
**Collides:** Law 25 Art. 17 PPIPS (adequate-protection assessment before PI leaves Quebec) ↔ default SaaS/cloud topologies that replicate freely.
**Resolution:** flow inventory + per-provider assessment + contractual safeguards + minimization of what flows; regional hosting where feasible.
**Residual risk:** the assessment standard is judgment-based; CAI expectations are still forming.
**Arch reading:** `ARCH-DISSOLVES` for data that never leaves or is non-personal before it does.

## C5 — Children's verification paradox: VPC vs minimization
**Collides:** COPPA 16 CFR § 312.5(b) verifiable-parental-consent methods (government ID check, credit card, face-match) ↔ P1/collection-limitation in every regime — *verifying the parent requires collecting more data than the service itself*.
**Resolution (sourced + architectural):** ephemeral verification — the sourced VPC method is "check photo ID **+ delete afterward**"; verify, don't retain. Architectural end-state: ZKP age/guardianship predicate proofs (`skills/privacy-architecture/SKILL.md`) — prove "parent of user, over 18" with zero documents retained.
**Residual risk:** ZKP-based VPC is not yet an FTC-approved method (the 2023 face-match proposal shows the direction); until then, deletion discipline is the control.
**Arch reading:** the flagship `ARCH-DISSOLVES` use case for anonymous credentials.
**2025–26 age-assurance escalation (sourced, web-verified 2026-07-17):** the paradox is no longer hypothetical — it is a mandate with revenue-percentage fines. The **UK Online Safety Act's highly-effective age assurance** became enforceable **25 July 2025** (record `regulatory-taxonomy--uk-osa.md`; Ofcom; passive self-declaration now *prohibited*), and in the US ***Free Speech Coalition v. Paxton*, 606 U.S. 461 (June 27 2025)** upheld Texas HB 1181's age-verification mandate (6–3), with ~two dozen states holding similar laws. Both regimes force the C5 collision at scale: the compliant *gate* is required, but the naive *method* (collect and retain government ID / face scans from every visitor) manufactures exactly the special-category honeypot minimization forbids. The architecture split is now the whole ballgame — **retention-based ID checks vs ZK age/attribute predicates that prove "over 18" and discard everything else.** This is the suite's most concrete "floor vs ceiling" demonstration: one legal duty, two implementations, opposite privacy outcomes.

## C6 — Detection fidelity vs minimization
**Collides:** fraud/intrusion detection needing full-fidelity identifiers (full IP, device IDs) ↔ P1/P3 minimization hooks in every regime (GDPR 5(1)(c), PIPEDA 4.4.1, CCPA 100(a)(3)).
**Resolution (sourced):** documented, justified exception with compensating controls — the suite's MINIMIZATION EXCEPTION RECORD (role-scoped access, no analytics replication, hard TTL, encryption, pseudonymized reporting). Undocumented exceptions are violations; documented ones are defensible.
**Residual risk:** the retained identifier remains a breach asset for its TTL window.
**Arch reading:** partial — HMAC/tokenized equality checks (`P7`) shrink the retained surface where detection needs matching, not raw values.

## C7 — Erasure rights vs statutory retention duties *(resolved-by-design exemplar)*
**Collides:** GDPR Art. 17 / CCPA § 1798.105 (delete on request) ↔ financial/tax/AML record-keeping mandates.
**Resolution:** already built into the statutes — Art. 17(3)(b) exception, CCPA deletion exceptions; restrict processing to what the exception permits and disclose the exception in the notice (`skills/consent-language/references/rights-language.md` retention-exceptions clause).
**Residual risk:** minimal in one jurisdiction; edge cases where jurisdiction A mandates retention of what jurisdiction B orders erased — segregate holdings per legal basis so the conflict never shares a record.
**Arch reading:** `SEPARATE` (P6) is the control: retention-mandated data lives apart from erasable data.

## C8 — Identification mandates vs anonymous transaction systems *(the open-combat entry)*
**Collides:** the AML/CFT financial-surveillance stack — **FATF Recommendation 16 (the "Travel Rule": originator + beneficiary identity attached to every VASP-to-VASP virtual-asset transfer above USD/EUR 1,000)**; **EU Transfer of Funds Regulation (EU) 2023/1113** (fully applicable **Dec 30 2024**, aligned with MiCA — *zero threshold* for CASPs, i.e. stricter than FATF, plus a self-hosted-wallet ownership-verification duty above EUR 1,000); US **31 U.S.C. § 5330 / 18 U.S.C. § 1960** unlicensed-money-transmitter liability ↔ the suite's foundational primitive: **anonymous transaction systems** (Chaum 1985; Nakamoto 2008 §10) and the mixers/shielded pools that implement them.
**Mechanism — why this one is different from C1–C7.** Every prior conflict is architecture-vs-*policy* where the architecture *dissolves the duty* (data not collected needs no consent, PII off-chain can't be un-erased). C8 is the case the thesis does **not** simply win: the law does not regulate what you *hold*, it criminalizes the *act of building unlinkability itself* when it moves others' value. This is a genuine collision, not a stricter floor — and pretending otherwise would be exactly the "vibes, not citations" failure the suite exists to prevent.
**The enforcement arc (web-verified 2026-07-17 — this is live law, not hypothesis):**
- **Tornado Cash:** OFAC-sanctioned Aug 2022 → ***Van Loon v. Treasury* (5th Cir., Nov 26 2024)** held immutable smart contracts are not "property" OFAC can sanction → **OFAC delisted the contracts Mar 21 2025** (developer Roman Semenov remains SDN-listed). Contributor **Roman Storm convicted Aug 6 2025** of conspiracy to run an unlicensed money-transmitting business (jury deadlocked on the money-laundering and sanctions counts; DOJ seeking retrial). Dutch developer **Alexey Pertsev** convicted of money laundering (64 months; on appeal).
- **Samourai Wallet:** founders Keonne Rodriguez and William Hill **pleaded guilty Jul 30 2025** to conspiring to operate an unlicensed money transmitter; Rodriguez **sentenced to 5 years (Nov 2025)**.
- **The takeaway that survives:** *publishing privacy code* and *operating a value-transmitting service* are being drawn as different legal acts — a distinction that is architectural, and one the suite can help a builder stay on the correct side of.
**Resolution (the pragmatic-privacy equilibrium — sourced).** The answer that emerged from the crypto community is not "give up privacy" and not "ignore the law" — it is **selective disclosure applied to compliance itself**: prove your funds are *not* associated with illicit deposits without revealing your identity or full history. **Privacy Pools** (Buterin, Illum, Nadler, Schär, Soleimani 2023, *"Blockchain Privacy and Regulatory Compliance: Towards a Practical Equilibrium"*; deployed on Ethereum by 0xbow, 2025) is the canonical construction: a ZK **proof of membership in an "association set" of honest deposits** (a *proof of innocence*), the exact inverse of Tornado Cash's undifferentiated anonymity. This is Hughes' selective-disclosure principle turned on the regulator's own question — the ceiling, expressed as a compliance argument.
**Residual risk (do not soft-pedal):** association-set governance recreates a trusted third party (who curates the set?) — Szabo's warning applies to the ASP itself; the *proof of innocence* framing may not satisfy every regulator or the money-transmitter analysis (which turns on *control of funds*, not privacy of ledger); and none of this cures the developer-liability exposure the Storm/Samourai cases established. **This is design-informing context, not a compliance guarantee — and least of all legal advice.**
**Arch reading:** `ARCH-SATISFIES` at the frontier (a ZK proof discharges the "show the funds are clean" demand without identity disclosure) but **explicitly not `ARCH-DISSOLVES`** — the identification mandate does not evaporate under good architecture the way an erasure duty does; it is *answered differently*. C8 is the register's one entry where the honest tag is a qualified yes.

---

**Register rule:** new records must be checked against C1–C8 and may add entries; a new regime that moves a floor in `regulatory-taxonomy--floor.md` is also a conflict-register review trigger.

**Tier-3 scan (2026-07-04):** eight regimes checked (AU, JP, IN, CH, KR, AE, NG, VN). No new *mutual incompatibilities* found; two entries gained parties — C1 (+KR Art. 21 irreversible destruction) and C3 (+VN Art. 26 localization). Honest note: the scan added obligations that are *stricter*, not *conflicting* — strictness moves the floor, not the register.

**C8 added 2026-07-17.** The first register entry that is architecture-vs-law *combat* rather than architecture-vs-policy *dissolution* — added because a privacy suite authored by a blockchain developer that omitted the Travel Rule / mixer-prosecution collision would be conspicuously incomplete. Sourced from primary enforcement actions and the Privacy Pools paper; every claim web-verified 2026-07-17 (see `.fable/reconciliation-log.md`).
