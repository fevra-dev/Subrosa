# Naming decision — **Subrosa** (retained record)

> **Settled 2026-07-05: the suite is Subrosa.** This file is kept as the decision record — the shortlist, the criteria, and the reasoning that produced the name. "Guise" below is the original working name that Subrosa replaced; it is preserved here only as the rejected candidate the analysis argues against.

**Why the working name "Guise" was rejected:** a *guise* is an outward appearance that conceals the real — it connotes **deception**. The suite's thesis is the opposite: *honest selective disclosure* — reveal exactly what's necessary, truthfully, and nothing more (Hughes 1993). The name argued against the product. It was also phonetically ambiguous (guise/guys/geese) and hard to search.

**Criteria** (Rams: less, but better):
1. Encodes *selective* disclosure — not hiding, not masking: **calibrated revealing**
2. Carries cypherpunk or legal-privacy lineage a reader can discover
3. One word, spellable on hearing, works as CLI verb / repo / skill prefix
4. No collision in the privacy/crypto space (availability below is **unchecked** — verify GitHub org, npm/crates, USPTO/CIPO, domain before committing)

---

## Finalists

### 1. **Sub Rosa** (`subrosa`) — recommended
"Under the rose" — the Roman/medieval symbol of confidentiality; a rose hung over the council table meant *what is said here stays here*. Legal English still uses *sub rosa* for "in strict confidence." Elegant, discoverable lineage, zero deception connotation — confidentiality by *mutual understanding*, which is exactly consent-based selective disclosure. Risks: two words (fine as `subrosa`); a small indie game and scattered brand uses exist — likely clear in this class, verify.

### 2. **Scrim**
Theater fabric that is opaque or transparent **depending on how it's lit** — visibility controlled by the operator, not the audience. The best pure metaphor for selective disclosure on the list; short, unixy, verb-able ("scrim the schema"). Risks: obscure to non-theater people (a feature for a portfolio piece — it invites the explanation); minor JS-library namespace noise.

### 3. **Aperture**
A calibrated opening — admits exactly as much light as the operator chooses. Photography metaphor maps one-to-one onto disclosure control (stop down = minimize). Risks: heavy cultural load (Portal's Aperture Science — affectionate but loud), crowded namespace in photo tooling.

---

## Worth considering

| Name | Case for | Case against |
|---|---|---|
| **Penumbra** | The killer double meaning: partial shadow (selective light) AND *Griswold v. Connecticut*'s "penumbras" — the doctrinal origin of the US constitutional privacy right. Perfect thesis fit | **Same-space collision: Penumbra Labs is the Cosmos privacy chain.** Likely disqualifying for a privacy-crypto portfolio piece |
| **Lattice** | Garden lattice = a screen you deliberately see *through*; lattice cryptography = the post-quantum future. Double crypto meaning | Lattice (HR platform) is a large trademark neighbor; noisy |
| **Membrane** | Semipermeable — biology's selective disclosure; passes what should pass | Clinical tone; long |
| **In Camera** (`incamera`) | Legal term for proceedings held in private chambers — judicial-grade confidentiality | Reads as photography app; two words |
| **Nym** | Direct cypherpunk lineage (pseudonym culture, nym servers) | **Taken: Nym Technologies (mixnet company)** — disqualified |
| **Sieve** | Selective passing as function | The idiom runs the wrong way ("leaks like a sieve") — disqualified, listed as a warning about metaphor direction |
| **Palimpsest** | Erasure-and-rewrite resonance (Art. 17 energy) | On inspection it's anti-privacy: a palimpsest is famous because the erased layer *remains recoverable* — a trap name |

## The case for keeping **Guise**
Defensible reading: a guise is *chosen self-presentation* — Hughes' "power to selectively reveal oneself" is literally the power to choose one's guise, and `skills/privacy-suite/SKILL.md` already frames pseudonymity as first-class. Short, available (you hold the repo), and renaming has real cost (links, memory, momentum). If the deception connotation doesn't bother you in a portfolio context, keeping it is not a mistake — but Sub Rosa says *confidence*, Guise says *cover*.

---

**Recommendation:** `subrosa` first, `scrim` second. Decide after an availability sweep (GitHub org / npm / crates / TM databases / domains) — happy to run it.

---

## ✅ DECISION (2026-07-05): **Subrosa**

Operator-selected. Repo: `github.com/fevra-dev/Subrosa`. The suite is **Subrosa** — under the rose: confidentiality by mutual understanding, selective disclosure by architecture. This file is retained as the decision record.
