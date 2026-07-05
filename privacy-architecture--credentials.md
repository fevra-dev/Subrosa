# Anonymous Credentials & Blind Signatures

> *"When I purchase a magazine at a store and hand cash to the clerk, there is no need to know who I am."*
> — Eric Hughes (1993)

Chaum's 1982 blind signature scheme was the first cryptographic implementation of this principle. Forty years of refinement has produced practical anonymous credential systems deployable today.

---

## Blind Signatures (Chaum 1982)

**What it does:** A signer signs a message without seeing its content. The resulting signature is valid and unlinkable to the signing interaction.

**The envelope analogy (Chaum):** Place a document and carbon paper in an envelope. The signer signs the outside of the envelope (making an imprint through the carbon paper), then returns it. You open the envelope and have a signed document — the signer never saw the content and cannot link the signature to the signing event.

**Protocol (RSA blind signature):**
```
1. User picks message m, random blinding factor r
2. User computes blinded message: m' = m × r^e mod n
3. User sends m' to signer
4. Signer signs: s' = (m')^d mod n
5. User unblinds: s = s' × r^(-1) mod n = m^d mod n
6. (m, s) is a valid RSA signature — signer never saw m
```

**Properties:**
- Signer cannot link the issued credential to a later presentation
- Issuer cannot track usage
- User cannot forge credentials (standard signature security)

**Production implementations:**
- RSA blind signatures (original Chaum — used in DigiCash)
- Schnorr blind signatures (more efficient, used in privacy coins)
- Blind BLS signatures (aggregate-friendly)

**Use cases:** Anonymous authentication tokens, e-cash schemes, anonymous voting, anonymous access credentials.

**Chaum's DigiCash (1989-1998):** First deployment of blind signatures for electronic cash. Failed commercially but proved the concept. Bitcoin's anonymous transaction model is the spiritual successor.

---

## BBS+ Signatures (Boneh-Boyen-Shacham)

**What it does:** Sign a vector of messages. The holder can later prove possession of a valid signature over a *subset* of messages without revealing the others, and without the verifier being able to link two presentations of the same credential.

**Why BBS+ is critical:**
- **Selective disclosure:** Prove "I am over 18" from a credential containing {name, DOB, address, nationality} without revealing any other field
- **Unlinkability:** Two presentations of the same BBS+ credential produce unlinkable proofs — the verifier cannot determine they came from the same credential
- **Holder binding:** Optional — can bind the credential to a holder key so only the legitimate holder can present it

**Protocol sketch:**
```
Issuance:
  Issuer signs (m1, m2, ..., mk) with BBS+ key
  → single signature σ over all k messages

Presentation:
  Holder selects disclosed attributes D ⊆ {m1...mk}
  Holder generates zero-knowledge proof π that:
    - σ is a valid BBS+ signature
    - The undisclosed attributes exist but are hidden
    - Any required predicates over attributes are satisfied
  → Verifier receives (D, π) — not σ, not undisclosed attributes
```

**Unlinkability property:** Each presentation proof uses fresh randomness. Two presentations of the same credential are computationally indistinguishable from presentations of different credentials.

**Production implementations:**
- `mattrglobal/bbs-signatures` (TypeScript) — IETF draft implementation
- `hyperledger/anoncreds-rs` (Rust) — Hyperledger AnonCreds, production-grade
- `jsonld-signatures-bbs` — JSON-LD + BBS+ for W3C VC ecosystem

**IETF Draft:** draft-irtf-cfrg-bbs-signatures (active, 2024) — on track for RFC status.

---

## W3C Verifiable Credentials + DIDs

**W3C Verifiable Credentials Data Model 2.0** (CR 2023): Standard data model for cryptographically verifiable claims.

**Components:**
- **Issuer:** Signs the credential (university, government, employer, protocol)
- **Holder:** Receives and stores the credential; generates presentations
- **Verifier:** Checks presentations without contacting the issuer
- **DID (Decentralized Identifier):** Self-sovereign identifier for issuer and/or holder

**VC + BBS+ selective disclosure stack:**
```
Credential (from issuer):
{
  "@context": ["https://www.w3.org/2018/credentials/v1"],
  "type": ["VerifiableCredential", "AgeCredential"],
  "issuer": "did:key:z6Mk...",
  "credentialSubject": {
    "id": "did:key:z6Mk...",  // holder DID — optional
    "dateOfBirth": "1990-03-15",
    "nationality": "CA",
    "name": "Alice Smith"
  },
  "proof": { "type": "BbsBlsSignature2020", ... }
}

Presentation (to verifier — selective disclosure):
{
  "@context": [...],
  "type": "VerifiablePresentation",
  "verifiableCredential": [{
    "credentialSubject": {
      "isOver18": true  // derived predicate — DOB not disclosed
    },
    "proof": { "type": "BbsBlsSignatureProof2020", ... }  // ZK proof
  }]
}
```

**DID methods relevant to Web3 context:**

| DID method | Resolution | Privacy |
|---|---|---|
| `did:key` | Local (no registry) | High — no on-chain footprint |
| `did:web` | HTTPS resolution | Medium — domain is visible |
| `did:ion` | Bitcoin (Sidetree) | Medium — anchored on Bitcoin |
| `did:sol` | Solana | Medium — on-chain, pseudonymous |
| `did:pkh` | Blockchain address | Low — directly links to wallet |

**For pseudonymous contexts:** `did:key` generates a DID from a key pair locally — no registry, no on-chain footprint. Ideal for Kyma's Morse fist biometric DID concept.

**Tools:**
- `Veramo` (TypeScript/Node.js) — full DID + VC stack, multi-method
- `SpruceID DIDKit` (Rust + FFI) — cross-platform, mobile-ready
- `walt.id` — managed VC/DID infrastructure
- `Hyperledger AnonCreds` — enterprise anonymous credential system

---

## Camenisch-Lysyanskaya (CL) Credentials

**What it is:** The foundational anonymous credential scheme (Camenisch & Lysyanskaya, 2001/2002/2004). Precedes BBS+ in the literature. Used in Idemix (IBM), Hyperledger Fabric, and Microsoft U-Prove.

**Key properties over BBS+:**
- Supports predicate proofs directly (prove age > 18 without revealing age)
- Supports credential updates without re-issuance
- Supports accumulator-based revocation with privacy (verifier learns credential is unrevoked, not which credential)

**When to prefer CL over BBS+:**
- Need predicate proofs (range proofs over attributes) natively
- Need credential revocation with privacy
- Enterprise / government context where Idemix/Hyperledger ecosystem is relevant

**When to prefer BBS+:**
- Web3 / Solana context (better tooling, lighter verification)
- IETF standards alignment
- Mobile-first (BBS+ implementations more portable)

---

## Accumulator-Based Revocation

Both BBS+ and CL credentials support revocation without a revocation list that leaks which credentials have been checked.

**Cryptographic accumulator:** A compact commitment to a set of values. A holder proves their credential value is in the accumulator (i.e., is not revoked) without revealing which value they hold.

```
Accumulator value A = g^(∏ v_i) mod n
  where v_i are the values of all valid credentials

Proof: "My credential value v is in the accumulator"
       without revealing v
       
Revocation: Issuer updates accumulator by removing v_revoked
            Holders with valid credentials update their witness
            Verifier checks proof against current accumulator
```

**Tools:** `anoncreds-rs` accumulator revocation; Hyperledger Indy revocation registry.

---

## Implementation Decision Tree

```
Need to prove a claim about identity/credential?
│
├─ Simple membership / possession proof
│  └─ BBS+ Verifiable Credential (IETF draft, Veramo)
│
├─ Range proof over credential attribute (age >= 18, balance >= X)
│  ├─ BBS+ + Bulletproof range proof (combined)
│  └─ CL credential with predicate proof (Idemix)
│
├─ Unlinkable multi-use token (prove membership repeatedly)
│  └─ BBS+ (unlinkability property) or CL with randomized pseudonym
│
├─ Anonymous e-cash / token
│  └─ Blind signatures (Chaum) or ZK-based token (Zcash/Tornado pattern)
│
├─ One-time anonymous authentication (no re-use)
│  └─ Hash-based token: H(secret || nonce); nullifier prevents reuse
│
└─ Privacy-preserving KYC attestation on Solana
   └─ ZK proof of BBS+ credential (Noir circuit verifying BBS+ proof)
      → on-chain verifier checks ZK proof, not credential
```

---

## References

- Chaum, D. (1982). "Blind signatures for untraceable payments." *Advances in Cryptology — CRYPTO 1982.*
- Chaum, D. (1985). "Security without identification: Transaction systems to make Big Brother obsolete." *Communications of the ACM 28(10).*
- Camenisch, J. & Lysyanskaya, A. (2001). "An efficient system for non-transferable anonymous credentials with optional anonymity revocation." *EUROCRYPT 2001.*
- Camenisch, J. & Lysyanskaya, A. (2002). "A signature scheme with efficient protocols." *SCN 2002.*
- Boneh, D., Boyen, X. & Shacham, H. (2004). "Short group signatures." *CRYPTO 2004.* (BBS foundation)
- Lodder, M. & Looker, T. (2024). "The BBS Signature Scheme." *IETF draft-irtf-cfrg-bbs-signatures.*
- W3C. (2023). "Verifiable Credentials Data Model 2.0." *W3C Candidate Recommendation.*
