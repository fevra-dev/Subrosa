---
name: privacy-suite
description: Master privacy skill — diagnoses need and routes to the right specialist skill. Use when: user says "privacy", "OPSEC", "anonymity", "am I safe to share this", "what are my risks", "help me stay private", "secure this", "check this before I post/push/send", or "what could someone learn about me"; when the request spans multiple privacy concerns at once; when starting a new project, identity, or pseudonym and unsure where to begin; when something was accidentally exposed and damage control is needed; when preparing any artifact, schema, file, or communication for external use. Routes to: threat-model-privacy (who wants my data and why, risk baseline, adversary profiles), data-minimization (schema/API/OCSF field audits, what to drop/hash/encrypt, GDPR/PIPEDA compliance), opsec-review (inferential leakage audit before sharing — what an adversary can infer, not just what's explicit), redact (strip PII/credentials/wallet addresses from text and code), metadata-hygiene (clean EXIF/document properties/git history from files before sharing). Sequences multiple skills for complex requests: pre-publication = redact → metadata-hygiene → opsec-review; new project = threat-model-privacy → data-minimization → metadata-hygiene; incident response = triage → rotate credentials → redact/metadata-hygiene → threat-model-privacy reassessment.
---

# Privacy Suite — **Subrosa**

*Sub rosa: under the rose — the Roman symbol hung over council tables meaning "what is said here stays here." Confidentiality by mutual understanding; selective disclosure by architecture.*

Master routing skill for the Subrosa privacy toolkit. Diagnoses the user's privacy need and dispatches to the appropriate specialist skill — or composes multiple skills in sequence.

---

## Philosophical Foundation

> *"Privacy is not secrecy. A private matter is something one doesn't want the whole world to know, but a secret matter is something one doesn't want anybody to know. Privacy is the power to selectively reveal oneself to the world."*
> — Eric Hughes, A Cypherpunk's Manifesto (1993)

> *"We must ensure that each party to a transaction have knowledge only of that which is directly necessary for that transaction."*
> — Hughes (1993)

> *"We cannot expect governments, corporations, or other large, faceless organizations to grant us privacy out of their beneficence."*
> — Hughes (1993)

> *"Computer technology is on the verge of providing the ability for individuals and groups to communicate and interact with each other in a totally anonymous manner... Reputations will be of central importance, far more important in dealings than even the credit ratings of today."*
> — Timothy C. May, The Crypto Anarchist Manifesto (1988)

> *"What is needed is an electronic payment system based on cryptographic proof instead of trust, allowing any two willing parties to transact directly with each other without the need for a trusted third party."*
> — Satoshi Nakamoto, Bitcoin: A Peer-to-Peer Electronic Cash System (2008)

> *"The solution we propose begins with a timestamp server... The privacy model... works by breaking the flow of information in another place: by keeping public keys anonymous."*
> — Nakamoto (2008), Section 10: Privacy

These texts share a single design principle that predates every privacy regulation in the suite's regulatory reference: **privacy must be structural, not procedural**. A system that forces identity disclosure by its underlying mechanism has no privacy regardless of its policy. A system architected for selective disclosure has privacy regardless of whether it complies with GDPR.

### The Two Failure Modes

**Failure Mode 1 — Policy without architecture:** A system collects everything, retains everything, and promises via policy not to misuse it. This is the default posture of most digital products. Hughes identifies exactly why it fails: "We cannot expect governments, corporations, or other large, faceless organizations to grant us privacy out of their beneficence." Policy without architecture is trust without cryptography — and trust is not a security primitive.

**Failure Mode 2 — Compliance without privacy:** A system passes every regulatory audit, satisfies every DPIA, and produces beautiful data handling policies — but its underlying mechanism still forces unnecessary identity disclosure at every transaction. GDPR Art. 5(1)(c) (data minimisation) and Hughes' transaction necessity principle (1993) say the same thing, but compliance alone doesn't build the anonymous transaction systems Hughes describes.

### The Design Target

The goal of this suite is not regulatory compliance. Compliance is a floor, not a ceiling. The design target is **selective disclosure** — systems where users reveal exactly what is necessary, to exactly the parties who need it, and nothing more. By design, not by policy.

- **`threat-model-privacy`** — maps the adversarial landscape: who wants your data, why, and how
- **`data-minimization`** + **`privacy-impact-assessment`** — enforces transaction necessity: collect only what the transaction requires
- **`opsec-review`** + **`redact`** + **`metadata-hygiene`** — removes what was over-disclosed: damage control for existing systems
- **`privacy-architecture`** — the Cypherpunk layer: cryptographic primitives for selective disclosure by design

The first four skills audit and repair. The last one builds. Hughes wrote in 1993: *"Cypherpunks write code."* This suite is that code.

### On Institutional Adversaries

May's Crypto Anarchist Manifesto (1988) and Hughes (1993) are explicit that institutional actors — governments, corporations — are structural adversaries, not benign parties who happen to occasionally misuse data. This is not a political position; it is a threat model. The `threat-model-privacy` skill encodes this in Archetype 6 (Institutional/Legal Adversary) and Archetype 7 (Nation-State/APT). Regulatory compliance addresses these adversaries only partially — it constrains their behavior contractually; it does not prevent capability. Architecture is the only defense that doesn't depend on the adversary's good faith.

### The Intellectual Lineage

Privacy by architecture did not begin with Hughes in 1993. It began with public key cryptography.

> *"We stand today on the brink of a revolution in cryptography... Public key cryptosystems... may permit... transactions to be carried out with neither party seeing the other's true name or number."*
> — Whitfield Diffie & Martin Hellman, "New Directions in Cryptography" (1976)

Diffie and Hellman's 1976 paper made the entire Cypherpunk program technically possible. Before it, secure communication required a pre-shared secret — which meant a meeting, a courier, or a trusted third party. After it, two strangers on a network could establish a shared secret without ever having met. The intermediary became optional. The trusted third party became a choice, not a necessity.

> *"It is possible to construct a system for carrying out transactions... in such a way that it would be impossible for outsiders, and even for the system operator, to determine the correspondence between the identities... The solution is to use an anonymous transaction system... making Big Brother obsolete."*
> — David Chaum, "Security without Identification: Transaction Systems to Make Big Brother Obsolete" (1985), *Communications of the ACM 28(10)*

Chaum's 1985 paper is the direct predecessor of the cypherpunk program. Hughes and May were building on Chaum. Every anonymous credential scheme, every blind signature, every zero-knowledge proof used in this suite descends from this paper. Chaum saw in 1985 that the digitization of commerce would create an unprecedented surveillance infrastructure — and that the only defense was architectural, not legal.

> *"If you want privacy... you'll have to use cryptography. But how do you know the encryption software you use is trustworthy? What if it has bugs, or intentional trapdoors? How do you know PGP doesn't have a back door for the NSA?... The only way to be sure is to have the source code reviewed."*
> — Philip Zimmermann, "Why I Wrote PGP" (1991)

Zimmermann wrote PGP as an act of civil disobedience. The US State Department prosecuted him for "munitions export" — encryption was literally classified as a weapon. The case was eventually dropped, but the principle it established endures: cryptographic tools are political acts. The `privacy-architecture` skill is in this tradition. Every ZKP circuit, every anonymous credential, every stealth address is a deployed political argument about the proper relationship between individuals and institutions.

> *"Trusted third parties are security holes."*
> — Nick Szabo, "Trusted Third Parties are Security Holes" (2001)

Szabo's most quoted sentence is also his most architectural. Every time a system introduces an intermediary — a payment processor, an authentication provider, an identity verifier — it introduces a point of compromise, subpoena, compulsion, or failure. The Cypherpunk design program is the systematic elimination of trusted third parties from the critical path of any transaction. Kyma's acoustic channel, Delegate Scout's on-chain attestations, and every ZK proof in this suite are implementations of Szabo's principle.

> *"The State will of course try to slow or halt the spread of this technology, citing national security concerns, use of the technology by drug dealers and tax evaders... Many of these concerns will be valid; crypto anarchy will allow national secrets to be traded freely and will allow illicit and stolen materials to be traded... But this will not halt the spread of crypto anarchy."*
> — Timothy C. May, "The Crypto Anarchist Manifesto" (1988)

May's 1988 manifesto, distributed at a hacker conference on a single sheet of paper, predicted the internet's effect on privacy, commerce, and state power with striking accuracy. The Cyphernomicon (1994) — his 370-page FAQ document — is the comprehensive philosophical encyclopedia of the movement. May was uncompromising: privacy technology would be used for things governments disapprove of, and that was not a reason to build weaker technology. It was a reason to build stronger institutions.

> *"Governments of the Industrial World, you weary giants of flesh and steel, I come from Cyberspace, the new home of Mind... You have no sovereignty where we gather."*
> — John Perry Barlow, "A Declaration of the Independence of Cyberspace" (1996)

Barlow's maximalist position — written the day the US Communications Decency Act was signed — is the boundary condition of the cypherpunk program. The position that cyberspace is beyond governmental sovereignty was wrong as a legal matter (courts have consistently disagreed) but right as an architectural aspiration: the goal is to build systems that are privacy-preserving regardless of what laws are passed. Architecture beats policy. Code is law.

> *"In real space, we recognize how laws regulate — through constitutions, statutes, and other legal codes. In cyberspace we must understand how code regulates — how the software and hardware that make cyberspace what it is regulate cyberspace as it is... The code is the law."*
> — Lawrence Lessig, "Code and Other Laws of Cyberspace" (1999)

Lessig's contribution completes the circle. If code is law, then writing privacy-preserving code is the most direct form of privacy legislation available. Lobbying for stronger privacy laws is asking the powerful to constrain themselves. Building privacy-preserving systems makes the constraint architectural and unavoidable. Hughes said "Cypherpunks write code." Lessig explains why that matters: the code is the law that actually governs.

### The Blockchain Continuity

Nakamoto's 2008 whitepaper is a direct implementation of Hughes' 1993 program — and Chaum's 1985 program, and Diffie and Hellman's 1976 program. Thirty years of cypherpunk development: Chaum's blind signatures (1982) → DigiCash (1989) → Szabo's smart contracts (1994) → b-money (Wei Dai, 1998) → Hashcash (Adam Back, 2002) → Bit Gold (Szabo, 2005) → Bitcoin (2008). Each step eliminated another trusted third party from the transaction stack. The Solana ecosystem this suite partially serves (Delegate Scout, Kyma, Exchange.Art) is the next generation of that lineage.

The tension between on-chain immutability and GDPR Art. 17 right to erasure is not a regulatory oversight — it is the collision between two philosophically incompatible privacy models: Nakamoto's cryptographic privacy-by-architecture and the EU's procedural privacy-by-policy. Neither fully wins. The `privacy-architecture` skill provides the bridge: zero-knowledge proofs, stealth addresses, and commitment schemes that satisfy both the cypherpunk selective disclosure principle and regulatory erasure requirements simultaneously.

### Canonical Texts

| Text | Author | Year | Core contribution |
|---|---|---|---|
| "New Directions in Cryptography" | Diffie & Hellman | 1976 | Public key cryptography — made everything possible |
| "Blind Signatures for Untraceable Payments" | David Chaum | 1982 | Anonymous digital cash — first working implementation |
| "Security without Identification" | David Chaum | 1985 | Full philosophical and technical statement of privacy-by-architecture |
| "Why I Wrote PGP" | Philip Zimmermann | 1991 | Cryptography as civil disobedience |
| "The Crypto Anarchist Manifesto" | Timothy C. May | 1988 | Political framework; crypto anarchy program |
| "A Cypherpunk's Manifesto" | Eric Hughes | 1993 | Privacy as selective disclosure; transaction necessity |
| "The Cyphernomicon" | Timothy C. May | 1994 | 370-page FAQ; comprehensive philosophical reference |
| "A Declaration of the Independence of Cyberspace" | John Perry Barlow | 1996 | Maximalist position; architecture over law |
| "b-money" | Wei Dai | 1998 | Anonymous distributed electronic cash |
| "Code and Other Laws of Cyberspace" | Lawrence Lessig | 1999 | Code is law; architectural regulation |
| "Trusted Third Parties are Security Holes" | Nick Szabo | 2001 | Architectural principle for trust minimization |
| "Bitcoin: A Peer-to-Peer Electronic Cash System" | Satoshi Nakamoto | 2008 | Implementation of the cypherpunk program |

---

## The Nine Skills

```
┌──────────────────────────────────────────────────────────────────┐
│                        PRIVACY SUITE                             │
│                                                                  │
│  UNDERSTAND          DESIGN              AUDIT                   │
│                                                                  │
│  threat-model   →   data-minimization   →   opsec-review        │
│  ─────────────       ────────────────       ──────────────       │
│  Who wants my        What should my         Is this safe         │
│  data and why?       schema collect?        to share?            │
│                                                                  │
│  privacy-impact-assessment     consent-language                  │
│  ─────────────────────────     ────────────────                  │
│  DPIA mandatory? Document       Write compliant notices,         │
│  risks formally                 cookie banners, rights pages     │
│                                                                  │
│  CLEAN                                   BUILD                   │
│                                                                  │
│  redact  +  metadata-hygiene      privacy-architecture           │
│  ───────────────────────────      ───────────────────            │
│  Strip PII from text/files        Cryptographic selective        │
│                                   disclosure by design           │
└──────────────────────────────────────────────────────────────────┘

Compliance is a floor. Selective disclosure is the ceiling.
Cypherpunks write code. This suite is that code.
```

---

## Routing Logic

### Route to `regulatory-taxonomy` (the normalized mapping layer) when:
- Any cross-jurisdiction statutory question — "who has a 72-hour breach clock", "what age is a child in Brazil", "which regimes treat geolocation as sensitive" → the records (axes A0–A12) are the source of truth; prose skills cite them
- Designing to one global standard → `taxonomy/regulatory-taxonomy--floor.md` (strictest-regime-wins)
- Obligations collide across regimes (erasure vs immutability, logging vs storage limitation) → `taxonomy/regulatory-taxonomy--conflicts.md`
- Arguing architecture over policy → `taxonomy/regulatory-taxonomy--arch-rollup.md` (which obligations dissolve under selective disclosure)

### Route to `consent-language` when:
- User needs a privacy notice, privacy policy, or cookie banner
- User says "write a privacy policy", "GDPR consent flow", "cookie consent", "data subject rights page", "at-collection notice", "COPPA notice", "children's consent", "breach notification letter"
- Product is launching and needs compliant disclosure language
- User asks what must be disclosed under GDPR, CCPA, PIPEDA, COPPA, or any other regime
- User needs consent UI copy, opt-out language, or rights exercise mechanism copy
- `data-minimization` or `privacy-impact-assessment` has identified a legal basis that now needs corresponding disclosure language

**Run `data-minimization` first when possible** — consent language is most accurate when the field inventory is known. You cannot write a complete privacy notice without knowing what data is collected.

### Route to `privacy-architecture` when:

Read the user's request and route based on the primary need. Multiple skills may be needed — sequence matters.

### Route to `threat-model-privacy` when:
- User wants to understand their overall risk posture
- User is starting a new project, identity, or operational context
- User asks "who would target me", "what should I protect", "am I at risk"
- No specific artifact or schema is present — pure planning mode
- User wants to assess a new threat they've become aware of

**Always run threat model first when there's no existing baseline.** All other skills operate more effectively with a threat model in place.

### Route to `data-minimization` when:
- User shares a schema, data model, API payload, or event structure
- User asks about GDPR/PIPEDA compliance for a data structure
- User asks what fields to drop, hash, or encrypt
- User is designing a new schema and wants privacy-by-design
- User asks about OCSF mapping, SIEM schema, or on-chain data structure
- Code review where the primary concern is what data is being stored

**Load `data-minimization` before `opsec-review` when both apply** — minimize first, then audit the minimized artifact.

### Route to `opsec-review` when:
- User is about to share, publish, post, or push something
- User asks "is this safe to share", "OPSEC check", "review before I post"
- User has a specific artifact: README, code, social post, commit, PR, paste
- User wants to know what an adversary could infer from an artifact
- No file binary involved — purely text/code content

**opsec-review is inference-focused.** It catches what `redact` and `metadata-hygiene` miss: what the content *implies* rather than what it explicitly states.

### Route to `redact` when:
- User has text, code, or a document containing explicit PII
- User asks to "scrub", "anonymize", "remove personal info", "sanitize"
- User is preparing content for external APIs, bug reports, or log sharing
- User wants explicit identifiers (names, emails, wallets, keys) removed

**redact handles explicit identifiers in text.** Pair with `metadata-hygiene` for files that also have embedded binary metadata.

### Route to `metadata-hygiene` when:
- User has a file (image, document, video, audio, archive, binary)
- User asks to "strip EXIF", "remove metadata", "clean this file"
- User is sharing photos, documents, or compiled code
- User is pushing a git repository with identity concerns
- `opsec-review` flagged a metadata finding that needs execution

**metadata-hygiene handles embedded binary and structured metadata.** It's the execution layer for metadata findings from `opsec-review`.

---

## Composition Patterns

### Pattern 1: New Project OPSEC Setup
**Trigger:** Starting a new repo, product, or identity

```
1. threat-model-privacy   → establish adversary profiles and asset tiers
2. data-minimization      → design schemas with minimization from day one
3. opsec-review           → audit README and initial docs before first push
4. metadata-hygiene       → configure git identity before first commit
```

### Pattern 2: Pre-Publication Artifact Review
**Trigger:** "I'm about to share/post/publish this"

```
1. redact                 → strip any explicit PII from text content
2. metadata-hygiene       → strip embedded metadata from files
3. opsec-review           → red-team the cleaned artifact for inferential leakage
```

Always in this order: strip first, then infer — avoids auditing content that will be removed anyway.

### Pattern 3: Schema / API Privacy Review
**Trigger:** Sharing a data model or schema for review

```
1. data-minimization      → field-level audit with remediation
2. threat-model-privacy   → (if no baseline exists) contextualize residual risk
```

### Pattern 4: Incident Response — Accidental Exposure
**Trigger:** "I accidentally shared / committed / posted something"

```
1. Triage:                → what was exposed? (text PII, file metadata, secret, schema?)
2. redact                 → if PII was in text that can be edited
3. metadata-hygiene       → if file metadata was exposed; git history rewrite if needed
4. threat-model-privacy   → reassess: does this change adversary capability?
```

**For credential exposure specifically:** Rotate the credential immediately — this takes priority over all skill invocations.

### Pattern 5: Pseudonym Launch
**Trigger:** Establishing a new pseudonymous identity

```
1. threat-model-privacy   → model deanonymization adversaries specifically
2. metadata-hygiene       → configure git identity, establish clean file workflow
3. opsec-review           → audit all content with pseudonymous persona mode active
```

### Pattern 6: Regulatory Compliance Documentation
**Trigger:** "I need a DPIA", "regulator asked for a privacy assessment", "client requires compliance docs"

```
1. data-minimization      → schema audit produces field inventory and findings
2. privacy-impact-assessment → import findings; produce regulator-ready DPIA document
3. threat-model-privacy   → Phase 3 risk register feeds into PIA risk register
```

### Pattern 7: Privacy-by-Architecture Design
**Trigger:** "Build this with privacy built in", "how do I avoid collecting identity", "ZK proof for this use case", "anonymous credential for this flow", new product design from scratch

```
1. threat-model-privacy   → establish what must be protected and from whom
2. privacy-architecture   → select cryptographic primitives for selective disclosure
3. data-minimization      → verify schema matches the minimized architecture
4. privacy-impact-assessment → document the design choices in a DPIA
```

This is the Cypherpunk pattern — building systems where privacy is structural, not procedural.

---

## Triage Questions

When the user's need is ambiguous, ask one clarifying question — pick the most discriminating:

**"Do you have a specific artifact (file, schema, text, code) or is this more of a planning/design question?"**

- Artifact present → lean toward `redact`, `metadata-hygiene`, `opsec-review`, `data-minimization`
- Planning mode → lean toward `threat-model-privacy` or `privacy-impact-assessment`
- Design mode → lean toward `privacy-architecture`

If artifact present: **"Is it a file with embedded metadata (image, document, video) or is it text/code content?"**

- File with metadata → `metadata-hygiene` (+ `opsec-review` for content)
- Text/code → `redact` and/or `opsec-review`

Never ask more than one clarifying question before beginning. Infer from context where possible.

---

## Skill Summaries

### `threat-model-privacy`
Four-phase IC-methodology threat modeling. Asset inventory → adversary profiling (seven archetypes with ICD 203 confidence framing, including institutional and nation-state adversaries) → attack surface map with kill chains and pre-mortem → tiered mitigation plan. Special contexts: pseudonymous identity, coercive control, legal/regulatory adversary.

### `data-minimization`
Field-level privacy audit for schemas, APIs, event logs, OCSF structures, on-chain data. Seven minimization principles (P1–P7). Ten remediation actions (DROP, HASH, HMAC, ENCRYPT, TOKENIZE, TRUNCATE, AGGREGATE, SEPARATE, ADD TTL, SCOPE-REDUCE). Global regulatory mapping at statutory precision: HIPAA 18 PHI identifiers, PIPEDA, GDPR, CCPA/CPRA, COPPA, LGPD, PIPL, APPs, APPI, DPDPA, POPIA, GLBA, Singapore PDPA, ePrivacy Directive, EU AI Act. Quasi-identifier cluster detection. Policy mode produces regulator-ready written data handling policy. On-chain immutability escalation.

### `privacy-impact-assessment`
Seven-phase DPIA/PIA workflow producing regulator-ready documentation. Mandatory trigger detection (GDPR Art. 35, Quebec Law 25 Art. 63.5, HIPAA § 164.308, PIPL Art. 55, EU AI Act Art. 9). Processing description with data flow map and field inventory. Risk register (12 risk categories) → mitigation register → Art. 36 prior consultation trigger. Rights assessment with immutability conflict documentation. Full DPIA document output with sign-off record and review log.

### `opsec-review`
Adversarial inference audit for artifacts before external exposure. Three adversary profiles (Public/Targeted/Insider). Seven signal categories: infrastructure fingerprinting, org structure, timing, tradecraft, supply chain, geolocation, identity correlation. CRITICAL→INFO severity tiers. Code-specific and doc/social-specific signal libraries. Pseudonymous persona escalation mode.

### `redact`
Multi-pass PII detection and sanitization. Five modes: REDACT, PSEUDONYMIZE (default), TOKENIZE, HIPAA_SAFE_HARBOR (18-identifier de-identification), GDPR_ANONYMIZE (k-anonymity/l-diversity). Entity categories: personal identifiers (including all 18 HIPAA PHI), health/medical, financial, credentials/secrets, crypto/Web3, organizational. Typed pseudonymization labels with consistent intra-document mapping. Redaction manifest with confidence tiers. Special handling: code, logs, JSON/YAML, markdown.

### `metadata-hygiene`
Embedded binary and structured metadata cleaning for files before sharing. Five metadata risk tiers (location → identity → device → temporal → organizational). Coverage: images (EXIF/IPTC/XMP), documents (PDF/Office — track changes, speaker notes, company fields), audio/video (GPS in iPhone video, iTunes Apple ID in M4A, BWF broadcast wave chunks), archives (TAR uname string, ZIP Unix extra field, macOS AppleDouble files), git repositories, compiled binaries. ExifTool/mat2/git-filter-repo command reference. Verification steps. Residual risk statement.

### `consent-language`
Generates legally compliant privacy notices, cookie consent banners, data subject rights disclosures, children's consent flows, and breach notification letters. Covers GDPR Arts. 13/14, PIPEDA Clause 4.8, CCPA § 1798.100, Quebec Law 25, COPPA (16 CFR Part 312), ePrivacy Directive Art. 5(3), PIPL Art. 17, and LGPD Art. 18. Outputs: full privacy notice (multi-jurisdiction), short/layered at-collection notice, CCPA at-collection notice, legitimate interests notice, compliant cookie banner (three tiers), granular preference panel, data subject rights language (all rights, all jurisdictions), COPPA verifiable parental consent mechanisms, GDPR Art. 8 age verification, breach notifications for GDPR/PIPEDA/HIPAA/LGPD. Anti-pattern refusal list (cookie walls, pre-ticked boxes, "by continuing" constructs). GPC signal handling.

### `privacy-architecture`
The Cypherpunk layer. Cryptographic primitives for selective disclosure by design: zero-knowledge proofs (ZK-SNARKs/STARKs, Groth16, PLONK, Noir), anonymous credentials (BBS+, Camenisch-Lysyanskaya, W3C Verifiable Credentials), blind signatures (Chaum 1982), commitment schemes (Pedersen, hash), stealth addresses, ring signatures, private set intersection, homomorphic encryption, secure multi-party computation, trusted execution environments, differential privacy. Production tool selection and implementation guidance. Design patterns for Solana/Web3, AI agent, and communications privacy contexts.

### `regulatory-taxonomy`
The normalized mapping layer beneath the suite. One frozen axis set (A0–A12: scope, enforcement, basis/consent, minimization test, purpose, sensitive categories, rights, retention, breach, children, transfer, safeguards, DPIA) × one record per jurisdiction, each cell citation-backed and tagged ARCH-DISSOLVES / ARCH-SATISFIES / PROCEDURAL. Derived artifacts: strictest-regime-wins design floor, cross-regime conflict register, architecture-vs-policy roll-up. Downstream skills (`consent-language`, `data-minimization`, `privacy-impact-assessment`) cite records instead of restating statutes; reconciliations log to `.fable/reconciliation-log.md`.

---

## Canonical Tool Chain

| Task | Primary tool | Skill |
|---|---|---|
| Strip image/doc metadata | ExifTool, mat2 | `metadata-hygiene` |
| Rewrite git history | git-filter-repo | `metadata-hygiene` |
| PII detection in text | Claude (skill) | `redact` |
| Schema field audit | Claude (skill) | `data-minimization` |
| Artifact inference audit | Claude (skill) | `opsec-review` |
| Threat model | Claude (skill) | `threat-model-privacy` |
| DPIA document | Claude (skill) | `privacy-impact-assessment` |
| ZK circuit authoring | Noir, Circom | `privacy-architecture` |
| Anonymous credentials | BBS+, VC libraries | `privacy-architecture` |
| Differential privacy | OpenDP | `privacy-architecture` |
| Blind signatures | libsodium, MIRACL | `privacy-architecture` |
| MPC | MP-SPDZ, SCALE-MAMBA | `privacy-architecture` |
