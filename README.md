<p align="center">
  <img src="assets/subrosa-logo.png" alt="Subrosa — a geometric rose, hanging from its stem" width="300">
</p>

# Subrosa

*Sub rosa — "under the rose." The rose hung over a Roman council table meant: what is said here stays here. Confidentiality by mutual understanding; selective disclosure by architecture.*

Subrosa is a privacy engineering suite that takes both halves of the privacy problem seriously: the **cypherpunk half** (privacy must be structural — built from cryptographic primitives that make over-disclosure impossible) and the **regulatory half** (statute-precise compliance mapping across 27 jurisdictional and sectoral records). Its thesis, enforced rather than asserted:

> **Compliance is a floor. Selective disclosure is the ceiling.**

## What's here

```
skills/                          Nine Claude Code skills (SKILL.md + references/)
  privacy-suite/                 Router — diagnoses the need, sequences the others
  threat-model-privacy/          IC-methodology adversary profiling (7 archetypes)
  data-minimization/             Field-level schema audits, P1–P7, remediation vocabulary
  consent-language/              Notices, cookie consent, rights pages, breach letters
  privacy-impact-assessment/     DPIA/PIA workflow, regulator-ready output
  opsec-review/                  Inferential-leakage audit before anything ships
  redact/                        PII/credential/wallet scrubbing (regex + crypto patterns)
  metadata-hygiene/              EXIF/document/AV/archive/git metadata stripping
  privacy-architecture/          The build layer: ZKP, anonymous credentials, blind
                                 signatures, commitments, stealth addresses, PSI/MPC,
                                 DP, TEE, mixnets — with the Statutory Dissolution Map
taxonomy/                        The normalized regulatory layer
  regulatory-taxonomy.md         Frozen axis set (A0–A12) + sectoral profile (S0–S5)
  regulatory-taxonomy--*.md      27 jurisdiction/sectoral records, citation-backed
  --floor.md                     Strictest-regime-wins: build to this, comply everywhere
  --conflicts.md                 C1–C8: where regimes collide (incl. AML vs anonymity)
  --arch-rollup.md               Which obligations dissolve under selective disclosure
.fable/                          Methodology provenance: lessons, reconciliation log,
                                 dogfood tests, phase prompts
```

## The two-layer design

**The taxonomy layer** normalizes every regime — GDPR/UK, PIPEDA + Quebec Law 25, CCPA/CPRA, LGPD, POPIA, PIPL, the PDPA family, APPI, DPDPA, the APPs, nFADP, KR PIPA, and sectoral overlays (HIPAA, GLBA, COPPA, BIPA, FERPA, ePrivacy, NIS2, DORA, EU AI Act) — onto one frozen axis set. Every cell carries a statutory citation or an explicit `[UNVERIFIED]` flag, plus an enforcement-mode tag: **ARCH-DISSOLVES** (the duty never attaches to a well-designed system), **ARCH-SATISFIES** (a technical measure discharges it), **PROCEDURAL** (only paper satisfies it), or **ARCH-MANDATES** (the law demands the architecture itself — AU APP 2's anonymity option, BIPA § 15(c)'s profit ban, India's child-tracking prohibition).

**The architecture layer** builds what the tags promise. Its Statutory Dissolution Map (`skills/privacy-architecture/references/regulatory-dissolution.md`) runs the bridge in the other direction: pick a primitive, read off exactly which obligations it dissolves, with record citations — so an ADR's compliance claim is auditable, not vibes. Roll-up finding: **~60% of tagged obligations across all records dissolve or discharge architecturally; the procedural remainder is five workflows of paper.**

## Methodology (why this is trustworthy)

Every statutory claim was either traced to a grounding source or flagged — never guessed. The discipline caught real errors that a hand-authored reference had carried confidently: a folkloric "72-hour" Quebec breach clock (the statute says *promptly*), a section-shifted POPIA condition table, a duplicated LGPD rights anchor, a conflated Swiss provision, an uncorroborated UAE penalty figure — and one entire superseded statute (Vietnam's Decree 13 → PDPL 91/2025). All corrections are logged with sources in `.fable/reconciliation-log.md`; a Currency Protocol (quarterly sweeps, supersession banners) keeps the records from rotting. The repo enforces its own invariants in CI: `tools/validate.py` verifies every cross-reference resolves, every skill's frontmatter is well-formed, and every record carries a current `Current as of` date — and prints the `[UNVERIFIED]` census so flag-debt is visible per commit.

## The canonical texts

Subrosa's design principle — privacy must be structural, not procedural — has a fifty-year lineage. The suite quotes and builds on all of it:

| Text | Author | Year | Core contribution |
|---|---|---|---|
| "New Directions in Cryptography" | Diffie & Hellman | 1976 | Public key cryptography — made everything possible |
| "Untraceable Electronic Mail, Return Addresses, and Digital Pseudonyms" | David Chaum | 1981 | Mix networks — metadata unlinkability; ancestor of every mixnet |
| "Blind Signatures for Untraceable Payments" | David Chaum | 1982 | Anonymous digital cash — first working implementation |
| "Security without Identification" | David Chaum | 1985 | Full philosophical and technical statement of privacy-by-architecture |
| "The Knowledge Complexity of Interactive Proof Systems" | Goldwasser, Micali & Rackoff | 1985 | Zero-knowledge formalized — proof without disclosure |
| "The Crypto Anarchist Manifesto" | Timothy C. May | 1988 | Political framework; crypto anarchy program |
| "Why I Wrote PGP" | Philip Zimmermann | 1991 | Cryptography as civil disobedience |
| "A Cypherpunk's Manifesto" | Eric Hughes | 1993 | Privacy as selective disclosure; transaction necessity |
| "The Cyphernomicon" | Timothy C. May | 1994 | 370-page FAQ; comprehensive philosophical reference |
| "A Declaration of the Independence of Cyberspace" | John Perry Barlow | 1996 | Maximalist position; architecture over law |
| "b-money" | Wei Dai | 1998 | Anonymous distributed electronic cash |
| "Code and Other Laws of Cyberspace" | Lawrence Lessig | 1999 | Code is law; architectural regulation |
| "Trusted Third Parties are Security Holes" | Nick Szabo | 2001 | Architectural principle for trust minimization |
| "Bitcoin: A Peer-to-Peer Electronic Cash System" | Satoshi Nakamoto | 2008 | Implementation of the cypherpunk program |

Full text-by-text mapping — each canonical work tied to the cryptographic primitive it authorizes and its place in the suite — is `skills/privacy-architecture/references/lineage.md`. Narrative exposition: `skills/privacy-suite/SKILL.md` §The Intellectual Lineage. Per-primitive epigraphs anchor each architecture reference (Chaum 1982 → blind signatures; GMR 1985 / May 1988 → ZKPs; Nakamoto 2008 §10 → Web3 privacy; Szabo 2001 → the TEE-as-minimized-TTP framing; Diffie–Hellman 1976 → everything).

## Using the skills

Each `skills/<name>/SKILL.md` is a Claude Code skill (frontmatter `name`/`description`, references loaded on demand). Install by copying into `~/.claude/skills/` or registering the repo as a plugin; start with `privacy-suite`, which routes to the rest.

---

**Not legal advice.** The taxonomy is an engineering reference for schema design, disclosure drafting, and architecture decisions. Verify effective dates and pending rulemakings against primary sources before advising in a regulated context — the Currency Protocol tells you how stale any record is.

*Hughes, 1993: "Cypherpunks write code." This repo is that code, with citations.*
