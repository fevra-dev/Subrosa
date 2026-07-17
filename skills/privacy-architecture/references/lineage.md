# The Cypherpunk Lineage — texts → primitives

> *"Cypherpunks write code. We know that someone has to write software to defend privacy, and... we're going to write it."*
> — Eric Hughes, A Cypherpunk's Manifesto (1993)

Subrosa's thesis — **privacy must be structural, not procedural** — is not an opinion; it is the conclusion of a fifty-year argument. This file is the argument, each text mapped to the primitive it authorizes and the place in this suite where that primitive is built. Read it as the intellectual provenance of every `ARCH-DISSOLVES` tag in the taxonomy.

The through-line: each text removes one more **trusted third party** from the critical path of a transaction (Szabo's frame), until Nakamoto removes the last one. Compliance regulates the intermediary's behavior; architecture removes the intermediary. That is the whole difference between the floor and the ceiling.

---

| # | Text | Author · Year | Contribution | Where it lives in Subrosa |
|---|---|---|---|---|
| 1 | **New Directions in Cryptography** | Diffie & Hellman · 1976 | Public-key cryptography: two strangers derive a shared secret without meeting — the intermediary becomes *optional* | `references/primitives.md` epigraph; the precondition for every asymmetric primitive in the suite |
| 2 | **Untraceable Electronic Mail, Return Addresses, and Digital Pseudonyms** | Chaum · 1981 | Mix networks: batch, layer-encrypt, shuffle — even a global observer cannot link sender to recipient. Metadata unlinkability as an architectural property; digital pseudonyms | `references/comms.md` §Mixnets (Nym, Loopix/Sphinx, Katzenpost all descend from this paper); the answer to every metadata-retention duty the content layer can't touch |
| 3 | **Blind Signatures for Untraceable Payments** | Chaum · 1982 | The first *working* privacy-by-architecture: a signer signs what it cannot see. Anonymous e-cash (DigiCash) | `references/credentials.md` — blind signatures; the C5 children's-verification pattern's ancestor |
| 4 | **The Knowledge Complexity of Interactive Proof Systems** | Goldwasser, Micali & Rackoff · 1985 | Zero-knowledge formalized: completeness, soundness, zero-knowledge — proof that verification need not transfer knowledge | `references/zkp.md` (the GMR properties open the file); the formal foundation May names in 1988 |
| 5 | **Security without Identification** | Chaum · 1985 | The full statement: transaction systems where *even the operator* cannot correlate identities. "Big Brother obsolete" | The taxonomy's whole `ARCH-DISSOLVES` column; quoted atop `taxonomy/regulatory-taxonomy--arch-rollup.md` and `regulatory-dissolution.md` |
| 6 | **The Crypto Anarchist Manifesto** | May · 1988 | The political program; names ZK interactive proofs as the technical basis before they were practical | `references/zkp.md` epigraph; `threat-model-privacy` Archetypes 6–7 (institutional adversary as *structural*, not incidental) |
| 7 | **Why I Wrote PGP** | Zimmermann · 1991 | Cryptography as civil disobedience; "the only way to be sure is to have the source code reviewed" — auditability as a privacy property | `references/comms.md` (PGP/GPG, metadata caveat); the reason every primitive here names its library and its *limitations*, not just its guarantees |
| 8 | **A Cypherpunk's Manifesto** | Hughes · 1993 | Privacy = *selective disclosure*; the transaction-necessity test ("no need to know who I am to buy a magazine") | The design workflow's Step 1 (`SKILL.md`); identical in force to every A3 minimization hook (GDPR 5(1)(c), PIPEDA 4.4.1) |
| 9 | **The Cyphernomicon** | May · 1994 | The 370-page encyclopedia of the movement; the exhaustive FAQ that turned manifesto into engineering discipline | The reference-density model for this suite itself: a claim without its caveat is not finished |
| 10 | **A Declaration of the Independence of Cyberspace** | Barlow · 1996 | The maximalist boundary condition: build systems privacy-preserving *regardless of what laws pass* | The stance behind "compliance is a floor": the architecture must hold even where the statute is absent or hostile (`skills/privacy-suite/SKILL.md` §Institutional Adversaries) |
| 11 | **b-money** | Wei Dai · 1998 | Anonymous distributed electronic cash; pseudonymous participants, collective ledger — the design Bitcoin cites | `references/web3-privacy.md` — the pre-Bitcoin lineage of pseudonymous-ledger privacy and its limits |
| 12 | **Code and Other Laws of Cyberspace** | Lessig · 1999 | "Code is law": software regulates as directly as statute; writing privacy-preserving code *is* privacy legislation | Why the taxonomy tags obligations `ARCH-MANDATES` — the point where the two regulators (code, law) demand the same thing |
| 13 | **Trusted Third Parties are Security Holes** | Szabo · 2001 | Every intermediary is a point of subpoena, compromise, or compulsion; minimize them out of the critical path | `references/tee.md` — the TEE reframed as a TTP *minimized into silicon*, not eliminated; the C3/C4 localization resolutions |
| 14 | **Bitcoin: A Peer-to-Peer Electronic Cash System** | Nakamoto · 2008 | The implementation: the last trusted third party (the payment processor) removed. §10 is the privacy model — pseudonymous keys | `references/web3-privacy.md` epigraph; the C1 erasure-vs-immutability conflict is this text meeting GDPR head-on |

---

## The single principle

Diffie–Hellman made the intermediary optional (1976). Chaum made the *channel* unlinkable (1981), then made anonymity constructive (1982) and total (1985); Goldwasser, Micali, and Rackoff proved the same year that verification need not transfer knowledge. May and Hughes gave it politics and a design test (1988, 1993). Zimmermann made it civil disobedience and demanded auditability (1991). Barlow set the boundary condition (1996); Lessig explained why code is the effective law (1999); Szabo named the enemy — the trusted third party (2001). Wei Dai (1998) and finally Nakamoto (2008) removed the last one.

Every regime in `taxonomy/` arrived at a fragment of the same conclusion decades later, and phrased it as *procedure*: minimize collection, limit purpose, honor erasure, restrict transfer. The architecture layer discharges those duties *structurally* — and in the `ARCH-MANDATES` cases (AU APP 2, DPDPA §9, BIPA §15(c), KR PIPA, GDPR Art. 25) the law has caught up and now demands the architecture by name.

Hughes, 1993: *"We must defend our own privacy if we expect to have any. We must come together and create systems which allow anonymous transactions to take place."* The rest of this skill is those systems. The taxonomy is the proof they are also compliant.
