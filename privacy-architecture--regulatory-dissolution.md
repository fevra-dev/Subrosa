# The Statutory Dissolution Map

> *"It is possible to construct a system... in such a way that it would be impossible for outsiders, and even for the system operator, to determine the correspondence between the identities."*
> — David Chaum, "Security without Identification" (1985)

Chaum's claim, forty years on, is now checkable against statute. This file is the bridge between the suite's two layers, read **primitive-first**: for each cryptographic primitive, which legal obligations it *dissolves* (the duty never attaches), which it *discharges* (the duty attaches and the primitive satisfies it), and where the law *mandates* it outright. The inverse view (axis-first) is `regulatory-taxonomy--arch-rollup.md`; citations resolve to the 26 `regulatory-taxonomy--*.md` records (axes A0–A12, sectoral S-records).

**How to use:** pick primitives in the design workflow (`privacy-architecture.md` Steps 1–3), then pull each primitive's row here into the ADR's Regulatory Mapping block — the compliance argument writes itself from record citations instead of freetext.

---

## Primitive → Statute Map

| Primitive (lineage) | DISSOLVES — duty never attaches | DISCHARGES — duty satisfied | Law that mandates or names it |
|---|---|---|---|
| **ZKP predicate/range proofs** (GMR 1985; May 1988 named ZKIPs as the program's basis) | A5 sensitive-category regimes when the attribute is proven, not disclosed: GDPR Art. 9, CCPA § 1798.121/140(ae), PIPL Arts. 28–32, LGPD Art. 11 — no special-category data held → no special-category regime | Minimization tests (A3) by construction: GDPR 5(1)(c), CCPA 100(a)(3), PIPL Art. 6, PIPEDA 4.4.1 | GDPR Art. 25(1) makes implementing-the-principles-technically a *duty* — ZKP is direct performance |
| **Anonymous credentials / BBS+** (Chaum 1985 → CL → BBS+) | Identity-linkage duties across presentations; the verifier's whole data-subject file (nothing identifiable retained → A6 rights workload ≈ nil) | Children's age assurance without document retention — the C5 resolution (COPPA VPC paradox); GDPR Art. 8(2) "reasonable efforts" verification | UK AADC age-assurance expectations; COPPA's delete-after-verify VPC methods point here |
| **Blind signatures** (Chaum 1982 — the first working implementation of Hughes' cash principle) | Issuer-side usage tracking: the issuer *cannot* build the profile, so profile-derived duties (ADM rights, A6 access to inferences) never arise | Purpose-binding (A4): unlinkability enforces single-purpose use cryptographically | — |
| **Commitments + off-chain PII** (Pedersen; hash) | On-chain erasure conflict **C1** entirely: GDPR Art. 17, Law 25 Art. 28, LGPD 18(VI), PIPL 47, KR PIPA Art. 21 (irreversible destruction) — nothing personal on the immutable layer | Blockchain-caveat disclosure obligations shrink to a footnote (`consent-language--rights-language.md` clause) | — |
| **Crypto-erasure / key destruction** | — | A7 deletion duties where physical erasure is impractical (backups, append-only): KR Art. 21's *irreversibility* requirement is the best statutory fit; GDPR Art. 17 acceptance unsettled (EDPB 05/2019 — see C1 residual) | APPI 仮名加工/匿名加工 ladder statutorily rewards the transform tier |
| **Stealth addresses / ring signatures** (Nakamoto 2008 §10's pseudonymity, hardened) | Cross-context identity linkage (P5) that quasi-identifier analysis would otherwise flag; wallet-as-persistent-correlation-key findings | A6/A10 exposure scope: what analytics firms can't cluster, subpoenas can't compel from you | — |
| **PSI / MPC** (Yao 1982-era lineage `[UNVERIFIED — not in suite sources]`) | Cross-border transfer regimes (A10) when computation crosses but data doesn't: PIPL Arts. 38–43, VN Art. 26, Law 25 Art. 17 — the **C3** architectural exit | Clean-room analytics without either party processing the other's PI (GDPR: aggregate outputs outside personal-data scope) | — |
| **Differential privacy / aggregation** | Breach-notification triggers (A8) for released statistics — RROSH, serious-harm, 500/1,000-person thresholds are functions of identifiable holdings; ε-DP aggregates hold none | EU AI Act Art. 10(3) training-data minimization; GDPR Recital 26 anonymous-data exit (bar is high — membership-inference caveat in `data-minimization--regulatory-reference.md` §Synthetic Data) | — |
| **On-device processing / local matching** | **The BIPA collapse:** biometric templates that never leave the device defeat § 15's collection trigger — the entire class-action exposure model (per-scan accrual, no damages cap) rests on *collection*; also CCPA precise-geolocation class via truncation-before-storage | KR Art. 23 segregated-storage; AADC defaults (geolocation off, profiling off) | DPDPA § 9's child-tracking ban is satisfiable only this way — no policy complies |
| **TEE** (Szabo 2001 lens: a trusted third party *minimized into silicon* — a compromise, not an elimination) | — (side-channels mean nothing dissolves; see `references/tee.md`) | Safeguards mandates (A11) at the prescriptive end: HIPAA § 164.312, GLBA § 314.4(c)(5)-adjacent; PIPL PIA "effective measures" (Art. 56) | — |
| **Mixnets / cover traffic** (Chaum 1981 untraceable mail `[UNVERIFIED — 1981 paper not in suite sources]`) | Traffic-metadata profiling duties: ePrivacy Art. 6 traffic-data restrictions are moot for traffic that reveals nothing | Metadata-leakage residual of every other primitive (ZKPs don't hide that an interaction happened) | — |
| **Tokenization / HMAC** (P7 workhorse) | — | A11 everywhere; the **C6** detection-fidelity resolution (equality checks without raw values); APPI pseudonymized-tier qualification; GDPR Recital 78 names pseudonymization explicitly | KR Art. 28-2 pseudonymization safe harbor |

---

## Where the Law Demands the Architecture (`ARCH-MANDATES`)

The strongest portfolio claim in the suite, found during Tier-3 normalization: in these provisions, selective disclosure isn't the cheap way to comply — it is the compliance target. Policy cannot satisfy them; only the design can.

| Provision | The mandated property |
|---|---|
| 🇦🇺 **APP 2** | Must *offer* anonymous/pseudonymous interaction where lawful and practicable — the anonymity option is itself the legal duty |
| 🇮🇳 **DPDPA § 9** | No behavioral tracking or targeted advertising directed at children — only not-building-the-tracking complies *(not in force as of June 2026)* |
| 🇺🇸-IL **BIPA § 15(c)** | Absolute ban on profiting from biometric data — only a design that cannot monetize it complies absolutely |
| 🇰🇷 **PIPA Art. 3(7) · 21 · 23** | Process anonymously where possible; destroy irreversibly; store sensitive PI segregated — P5, crypto-erasure, and P6 written as statute |
| 🇯🇵 **APPI 2022 categories** | 仮名加工情報/匿名加工情報 — a statutory reward ladder for TOKENIZE/anonymize transforms |
| 🇺🇸 **HIPAA § 164.514(b)(2)** | Safe Harbor: the law hands you the exact 18-field DROP list that exits its scope — dissolution with a statutory recipe |
| 🇪🇺 **GDPR Art. 25(1)–(2)** | Privacy by design and by default as enforceable duty (upper-tier-fine adjacent via Art. 5) — the general form all the above specialize |

Hughes: *"Cypherpunks write code."* These provisions are the law arriving at the same conclusion.

---

## Conflict Resolutions (C1–C7 → primitive)

From `regulatory-taxonomy--conflicts.md`; each residual-risk note applies.

| Conflict | Architectural resolution |
|---|---|
| C1 erasure vs immutability | Commitments on-chain, PII off-chain; crypto-erasure (unsettled — flag) |
| C2 mandated logging vs storage limitation | Field-level tokenization inside logs; tiered TTLs (see `privacy-architecture.md` §Privacy-Preserving Audit Logs; ZK compliance attestation at the frontier) |
| C3 localization vs global architecture | Local-only processing; PSI/MPC — compute crosses, data doesn't |
| C4 Quebec outbound assessment vs cloud | Regional residency + non-personal-before-export |
| C5 child-verification paradox | Ephemeral verification today; ZKP age/guardianship predicates as end-state |
| C6 detection fidelity vs minimization | HMAC equality-matching; documented exception record for the irreducible remainder |
| C7 erasure vs retention mandates | SEPARATE (P6): segregate retention-mandated holdings so the conflict never shares a record |

---

## Worked Example — Age Verification ADR (the C5 pattern)

```
ADR-X: BBS+ age predicate for under-18 gating
Context:   Must prove: user ≥ threshold age per market (13 US / 13–16 EU / 18 BR-ZA-IN).
           Must stay hidden: DOB, identity document, everything else.
           Threat model: verifier compromise; issuer-verifier collusion.
Decision:  BBS+ credential from ID-verification issuer; derived proof "isOverT: true".
Regulatory mapping (from records — not freetext):
  DISSOLVES  A5/A9 document retention: no DOB or ID document ever held by verifier
             → COPPA § 312.10 retention duty attaches to nothing (us-coppa S3);
             → GDPR Art. 9 never triggered (eu-gdpr-uk A5).
  DISCHARGES GDPR Art. 8(2) reasonable-efforts verification (eu-gdpr-uk A9);
             COPPA VPC delete-after-verify made structural (C5);
             AADC data-minimisation standard (eu-gdpr-uk divergence block).
  RESIDUAL   PROCEDURAL: parental-consent UX for under-threshold users;
             VPC method approval — ZKP not yet an FTC-listed method (C5 residual).
  FLOOR      regulatory-taxonomy--floor.md A9 row satisfied for all listed markets.
```

This is the template: every ADR's Regulatory Mapping block cites records, floor rows, and conflict entries — auditable compliance claims, not vibes.
