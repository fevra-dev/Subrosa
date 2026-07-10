---
name: privacy-architecture
description: Selects and applies cryptographic primitives for privacy-by-design — systems where selective disclosure is structural, not procedural. Use when user says "build this with privacy built in", "how do I avoid collecting identity", "zero-knowledge proof for this", "anonymous credential", "can I prove X without revealing Y", "stealth address", "blind signature", "private transaction", "MPC", "homomorphic encryption", "differential privacy for analytics", "TEE", "can I verify without seeing the data", or when designing a new system, protocol, or product and wants privacy to be architectural rather than a policy layer added afterward. The Cypherpunk layer of the privacy suite — implements Eric Hughes' (1993) selective disclosure principle and Timothy May's (1988) anonymous transaction system program using contemporary cryptographic primitives. Distinct from all other privacy skills: those audit and repair; this one builds.
---

# Privacy Architecture

> *"Privacy in an open society requires anonymous transaction systems... An anonymous system empowers individuals to reveal their identity when desired and only when desired; this is the essence of privacy."*
> — Eric Hughes, A Cypherpunk's Manifesto (1993)

> *"The methods are based upon public-key encryption, zero-knowledge interactive proof systems, and various software protocols for interaction, authentication, and verification."*
> — Timothy C. May, The Crypto Anarchist Manifesto (1988)

Cryptographic primitive selection and implementation guidance for systems where privacy is structural. The goal is selective disclosure: users prove exactly what is necessary, reveal nothing more, and retain control.

**Composable with:**
- `threat-model-privacy` — run first to establish what must be protected and from whom; guides primitive selection
- `data-minimization` — verify the minimized schema matches the architecture
- `privacy-impact-assessment` — document architectural choices in a DPIA; ZK-based designs shrink the residual-risk register toward nil, but the assessment duty itself is procedural and remains (GDPR Art. 35 / Law 25 Art. 63.5 — see `regulatory-taxonomy--arch-rollup.md`, axis A12)
- `regulatory-taxonomy` — the statutory payoff of every primitive here is mapped in `references/regulatory-dissolution.md` (primitive-first) and `regulatory-taxonomy--arch-rollup.md` (axis-first); cite records, not vibes

---

## Primitive Selection Guide

Quick routing from use case to primitive. Load the relevant reference section for implementation detail.

| Use case | Primitive | Reference |
|---|---|---|
| Prove you meet a requirement without revealing the underlying data | Zero-Knowledge Proof | `references/zkp.md` |
| Present a credential without linking uses to each other | Anonymous Credential / BBS+ | `references/credentials.md` |
| Let a signer sign data without seeing it | Blind Signature | `references/credentials.md` |
| Commit to a value now, reveal it later | Commitment Scheme | `references/primitives.md` |
| Receive funds without linking to sending address | Stealth Address | `references/web3-privacy.md` |
| Sign on behalf of a group without revealing which member | Ring Signature | `references/web3-privacy.md` |
| Two parties find common elements without revealing non-overlapping data | Private Set Intersection | `references/primitives.md` |
| Compute on encrypted data without decrypting it | Homomorphic Encryption | `references/primitives.md` |
| Multiple parties compute a function without revealing their inputs | Secure Multi-Party Computation | `references/primitives.md` |
| Add calibrated noise so individual data is protected but statistics are accurate | Differential Privacy | `references/primitives.md` |
| Execute code in a hardware-isolated trusted environment | Trusted Execution Environment | `references/tee.md` |
| Route communications so origin is unlinkable | Mixnet / Onion Routing | `references/comms.md` |
| AI agent infers patterns without seeing individual records | Federated Learning + DP | `references/primitives.md` |

**Statutory payoff per primitive** — which obligations each one dissolves, discharges, or is outright mandated by (APP 2, BIPA § 15(c), DPDPA § 9, KR PIPA, HIPAA Safe Harbor): `references/regulatory-dissolution.md`.

---

## Design Workflow

### Step 1 — Establish the disclosure requirement

The central question is always: **what must be proven, and what must remain hidden?**

For each interaction in the system, answer:

```
Interaction: [e.g. "user pays for a service"]
What the counterparty legitimately needs to know:
  - [e.g. "payment is authorized", "user is over 18"]
What the counterparty does NOT need to know:
  - [e.g. "user's identity", "exact wallet balance", "which accounts they hold"]
What must be verified:
  - [e.g. "payment amount >= fee", "credential was issued by trusted authority"]
What must remain private:
  - [e.g. "all other financial details", "other credentials held"]
```

This is Hughes' transaction necessity test applied as a design specification. Every field in the counterparty's knowledge set that isn't strictly necessary for the transaction is a privacy failure.

### Step 2 — Classify the disclosure type

Three categories of what needs to be proven:

**Membership proof** — "I am a member of set S" without revealing which member.
→ Ring signatures, group signatures, anonymous credentials, zk-membership proofs

**Range/threshold proof** — "My value V satisfies condition C (V > x, V ∈ [a,b])" without revealing V.
→ Bulletproofs (range proofs), ZK-SNARKs with range constraints, Pedersen commitments + range proof

**Predicate proof** — "Statement P is true about my data" without revealing the data.
→ General ZK-SNARKs/STARKs, ZK-EVMs, Noir circuits, Circom circuits

**Identity proof** — "I am the holder of credential C issued by authority A" without revealing C or linkable identity.
→ BBS+ signatures, CL credentials, W3C Verifiable Credentials with selective disclosure, zk-DID

### Step 3 — Select primitive tier

Three tiers by implementation cost vs. privacy guarantee:

**Tier 1 — Practical today (production-ready)**
- Commitment schemes + hash functions
- Blind signatures (Chaum 1982; production: RSA blind sig, Schnorr blind sig)
- BBS+ signatures / W3C Verifiable Credentials selective disclosure
- Stealth addresses (ERC-5564 on EVM; implementation exists for Solana)
- Ring signatures (used in Monero since 2014)
- Differential privacy (Apple, Google deployments; OpenDP library)
- TEEs (Intel SGX, ARM TrustZone; Solana: Seed Vault)

**Tier 2 — Mature but specialist (requires cryptography expertise)**
- ZK-SNARKs (Groth16, PLONK) — proving time seconds-minutes; verification ~milliseconds
- Bulletproofs (range proofs) — no trusted setup; larger proof size
- Private Set Intersection — production deployments at Google, Apple for private contact discovery
- Threshold signatures / MPC signing — production: tBTC, Lightning Network, custody systems

**Tier 3 — Emerging / high cost (use with caution in production)**
- ZK-STARKs — post-quantum secure, no trusted setup; larger proofs, high prover cost
- Fully Homomorphic Encryption (FHE) — 100x-10,000x computation overhead; improving rapidly (TFHE-rs, Zama)
- General-purpose MPC — high communication overhead; practical for specific use cases
- Recursive SNARKs / proof aggregation — production on Mina, StarkNet

### Step 4 — Specify the circuit or protocol

For ZKP-based designs, the privacy guarantee lives in the circuit — the set of constraints the prover must satisfy. Specify the circuit before choosing a proving system:

```
CIRCUIT SPECIFICATION
Name: [e.g. "delegation_risk_score"]
Public inputs:  [what the verifier sees — e.g. "risk_score_bucket: LOW/MED/HIGH"]
Private inputs: [what only the prover knows — e.g. "delegation_count, wallet_address, 
                 token_amounts, counterparty_addresses"]
Constraints:
  1. risk_score = f(delegation_count, token_amounts, counterparty_risk)
  2. risk_score ∈ {LOW: 0-33, MED: 34-66, HIGH: 67-100}
  3. public output = bucket(risk_score)
  4. [hash commitment to inputs for auditability if required]

Proving system: [Groth16 / PLONK / Noir / STARK]
Trusted setup:  [required for Groth16/PLONK; not required for STARK/Bulletproof]
Prover:         [who runs the proof — user device, server, TEE]
Verifier:       [on-chain program / smart contract / off-chain verifier]
```

### Step 5 — Threat model the architecture

A cryptographic primitive guarantees privacy only within its formal security model. Outside that model, implementation and deployment vulnerabilities dominate. After selecting primitives:

1. **Trusted setup risk**: Groth16 and PLONK require a trusted setup ceremony. If the setup is compromised, proofs can be forged. Use a large multi-party ceremony (Hermez, Ethereum's Powers of Tau) or use setup-free systems (STARKs, Bulletproofs).

2. **Side-channel leakage**: TEEs (SGX, TrustZone) have documented side-channel attacks — cache timing, power analysis, Spectre/Meltdown variants. Kyma's Seed Vault TEE integration is relevant here. Don't treat TEE isolation as absolute.

3. **Metadata leakage**: ZKPs prove statements about data; they don't hide the existence of the interaction, its timing, size, or frequency. Combine with mixnets or cover traffic if interaction metadata is sensitive.

4. **Implementation bugs**: ZKP circuits are code. Under-constrained circuits are a critical vulnerability class — they allow provers to satisfy the verifier without actually satisfying the intended constraint. Reference: Circom/SnarkJS vulnerability history; Tornado Cash circuit bugs.

5. **Key management**: Anonymous credentials and blind signatures require key material. Key compromise breaks all unlinkability guarantees retroactively or prospectively depending on scheme.

6. **Prover cost vs. mobile**: ZK-SNARKs require significant computation to generate proofs. On mobile (Seeker hardware, Android 15), proving time must be benchmarked for your circuit size. Noir is currently the most practical for mobile proving.

### Step 6 — Produce the architecture decision record

For each privacy-architectural decision, document it as an ADR:

```
ADR-[N]: [Primitive name] for [Use case]
Date: [date]
Status: [Proposed / Accepted / Deprecated]

Context:
  What must be proven: [disclosure requirement from Step 1]
  What must remain hidden: [privacy requirement]
  Threat model: [relevant adversary from threat-model-privacy]

Decision:
  Primitive: [chosen primitive]
  Proving system: [if applicable]
  Implementation: [library / tool]
  
Consequences:
  Privacy guarantee: [formal guarantee — what the primitive provably hides]
  Assumptions: [what the guarantee depends on — trusted setup, 
                computational hardness assumption, honest majority, etc.]
  Limitations: [what the primitive does NOT hide]
  Performance: [proving time, proof size, verification cost]
  
Regulatory mapping (cite taxonomy records, not freetext — worked example in
references/regulatory-dissolution.md):
  DISSOLVES:  [obligations that never attach — record + axis, e.g.
               "GDPR Art. 9 never triggered (eu-gdpr-uk A5)"]
  DISCHARGES: [duties satisfied by the primitive — record + axis]
  RESIDUAL:   [what stays PROCEDURAL — notices, rights workflow, assessment paper]
  FLOOR:      [which regulatory-taxonomy--floor.md rows this satisfies]
  CONFLICTS:  [any C1–C7 entry this design resolves, with its residual-risk note]
```

---

## Patterns by Domain

### Solana / Web3 Privacy

**Pattern: On-chain credential verification without identity disclosure**
Use case: Prove wallet meets a criterion (delegation risk score, KYC status, token holding) without revealing wallet address or underlying data.

```
Design:
  1. Trusted issuer signs a credential (BBS+ or Groth16)
  2. User generates a ZK proof of valid credential + satisfied predicate
  3. On-chain verifier checks the proof, not the credential
  4. No wallet address or credential content appears on-chain
  
Tools: Noir (circuit), Solana Program Library (verifier), 
       BBS+ (credential issuance)
Relevant to: Delegate Scout risk attestation, KYC compliance 
             without identity disclosure
```

**Pattern: Stealth address payments**
Use case: Receive payments on Solana without linking transactions to a public identity.

```
Design:
  1. Recipient publishes a stealth meta-address (spend key + view key)
  2. Sender generates a one-time stealth address per payment
  3. Recipient scans chain with view key to find their payments
  4. Recipient spends with spend key
  
Note: Native stealth address support on Solana is nascent — 
      implementation requires custom program. ERC-5564 exists 
      on EVM; port is the open research question.
Relevant to: Kyma payment privacy, Exchange.Art anonymous purchasing
```

**Pattern: Private NFT ownership attestation**
Use case: Prove you own an NFT from collection X without revealing which specific NFT or your wallet address.

```
Design:
  1. Merkle tree of collection ownership (or Bubblegum cNFT tree)
  2. ZK proof of Merkle inclusion (you own a leaf)
  3. Verifier checks proof against public Merkle root
  4. Your specific NFT and wallet remain private
  
Tools: Circom (Merkle proof circuit), Solana (cNFT tree),
       Groth16 or PLONK (proving system)
```

### AI Agent / LLM Privacy

**Pattern: Private RAG — retrieve without revealing query**
Use case: Agent retrieves from a sensitive knowledge base without the retrieval service learning what was queried.

```
Design:
  Private Information Retrieval (PIR) — mathematically hides 
  which record was retrieved from a database
  
  Practical: Oblivious RAM (ORAM) over encrypted vector store
  Deployment: Run vector store in TEE (SGX/TrustZone)
  
Tools: Oblivious ORAM library (Go/Rust), Gramine (SGX), 
       Qdrant-in-TEE (experimental)
Note: PIR has high computational overhead (~100x vs. plain retrieval).
      For most threat models, namespace-scoped retrieval (Control RS-1 
      from agent memory taxonomy) is the practical alternative.
Relevant to: OpenClaw memory privacy, MINJA mitigation
```

**Pattern: Differentially private analytics over agent interactions**
Use case: Derive statistics about agent usage patterns without exposing individual user behavior.

```
Design:
  Apply ε-differential privacy at the query layer:
  1. Clip individual user contributions to sensitivity bound
  2. Add calibrated Laplace or Gaussian noise to aggregate query
  3. Enforce privacy budget (ε) across all queries over time
  
  ε guidance: ε = 0.1 → strong privacy, low utility
              ε = 1.0 → balanced (Apple/Google production standard)
              ε = 10  → weak privacy, high utility
              
Tools: OpenDP (Python), Google DP library (C++/Go), 
       Apple's Differential Privacy WWDC resources
Relevant to: OpenClaw fleet behavioral analytics, 
             agent memory temporal correlation mitigation
```

**Pattern: MPC model inference — compute on private inputs**
Use case: User inputs private data; model produces output; neither party sees the other's full information.

```
Design:
  Garbled circuits or secret-sharing MPC:
  1. User secret-shares their input
  2. MPC parties jointly evaluate the model
  3. Output is revealed; inputs remain hidden from all parties
  
Tools: MP-SPDZ (most performant MPC framework), 
       SCALE-MAMBA, Rosetta (TensorFlow MPC)
Cost: Significant communication overhead — practical for 
      small models or high-sensitivity use cases
Relevant to: Privacy-preserving ML inference on sensitive data
```

### Identity and Communications

**Pattern: Pseudonymous DID with selective disclosure**
Use case: Establish a decentralized identity that can prove claims (age, credential, membership) without revealing the underlying identity or linking uses.

```
Design:
  W3C DID + Verifiable Credentials + BBS+ selective disclosure:
  1. DID generated locally — no central registry required
  2. Credentials issued by trusted authorities to DID
  3. User generates BBS+ derived proof: proves specific attributes 
     without revealing full credential or linking to DID
  4. Verifier confirms attribute without learning DID
  
  BBS+ property: k presentations of the same credential produce 
  k unlinkable proofs — unlike standard JWT VCs
  
Tools: DIF BBS+ spec (ietf-bbs-signatures), 
       Veramo (DID framework, Node.js),
       Spruce DIDKit (cross-platform)
Relevant to: Kyma Morse fist DID, fevra-dev identity architecture,
             Exchange.Art artist verification
```

**Pattern: Acoustic channel metadata minimization (Kyma-specific)**
Use case: ggwave acoustic transmission reveals timing, frequency, and acoustic fingerprint — minimize what can be inferred from the side channel.

```
Design:
  1. Cover traffic — transmit dummy acoustic bursts at fixed intervals
     to prevent timing correlation attacks
  2. Frequency hopping — vary carrier frequency within 15-19.5kHz 
     range to prevent device fingerprinting via acoustic signature
  3. Fixed-length padding — pad all payloads to a fixed acoustic 
     burst length to prevent length-based content inference
  4. Replay prevention — AES-256-GCM nonce + durable nonce pool 
     already implemented; verify nonce uniqueness is enforced
     
Note: This is acoustic traffic analysis resistance, not encryption —
      the AES-256-GCM layer handles confidentiality; this layer 
      handles metadata privacy of the channel itself
```

---

## Reference Files

- `references/zkp.md` — Zero-knowledge proof primer: ZK-SNARKs (Groth16, PLONK), ZK-STARKs, Bulletproofs, Noir, Circom, circuit vulnerability taxonomy, trusted setup guide
- `references/credentials.md` — Anonymous credentials: BBS+ signatures, Camenisch-Lysyanskaya (CL) credentials, W3C DID + Verifiable Credentials, blind signatures (Chaum 1982), selective disclosure implementations
- `references/primitives.md` — Foundational primitives: commitment schemes (Pedersen, hash), private set intersection, homomorphic encryption (FHE/PHE), secure MPC, differential privacy, oblivious RAM
- `references/web3-privacy.md` — Web3 / blockchain privacy: stealth addresses, ring signatures, confidential transactions, ZK rollups, Tornado Cash architecture analysis, Solana-specific privacy tooling
- `references/tee.md` — Trusted execution environments: Intel SGX, ARM TrustZone, Apple Secure Enclave, Solana Seed Vault, known side-channel vulnerabilities, attestation protocols
- `references/comms.md` — Communications privacy: Tor/onion routing, mixnets, Signal Protocol, forward secrecy, acoustic channel privacy (Kyma context)
- `references/regulatory-dissolution.md` — The Statutory Dissolution Map: primitive → obligations dissolved/discharged across the 26-record taxonomy; the ARCH-MANDATES statutes; C1–C7 resolutions; the record-cited ADR pattern
- `references/lineage.md` — The Cypherpunk Lineage: all twelve canonical texts (Diffie–Hellman 1976 → Nakamoto 2008) mapped to the primitive each authorizes and its place in this suite

---

## Privacy-Preserving Audit Logs

**The compliance paradox:** GDPR Art. 30 (Records of Processing Activities), HIPAA § 164.312(b) (Audit Controls), GLBA § 314.4(c)(2) (Data Inventory and Logs), and GDPR Art. 5(2) (Accountability) all mandate audit trails. But audit trails containing personal data create their own minimization problem under Art. 5(1)(c). You must log to comply; logging may itself be non-compliant.

**The standard resolution:** Tiered retention — log everything for 30 days (operational); retain anonymized aggregates for 12 months (audit); retain compliance attestations indefinitely. Functional but imperfect — the 30-day operational logs contain full PII.

**The cryptographic resolution (research frontier):** ZK-proofs for compliance attestation — prove that a log entry exists, is authentic, and satisfies a compliance predicate, without revealing the log entry's content.

### Architecture: ZK Compliance Attestation

```
Standard audit log entry (contains PII):
{
  timestamp: "2024-01-15T14:32:11Z",
  user_id: "u_abc123",
  action: "read",
  resource: "patient_record_789",
  ip_address: "192.168.1.45"
}

ZK compliance attestation model:
  1. Store log entry encrypted: E_k(entry)
  2. Compute commitment: C = H(entry || randomness)
  3. Generate ZK proof π that:
     - Entry exists (matches commitment)
     - Entry is authentic (signed by logging system)
     - Entry satisfies compliance predicate P
       (e.g., "access was by an authorized user"
              "no PHI was accessed outside business hours"
              "all accesses had a documented purpose")
  4. Publish: (C, π, timestamp) — no PII in public record
  5. Auditor verifies: π against C — learns compliance status, not content
  6. On subpoena: produce E_k(entry) + decryption key
     (full entry revealed only under legal compulsion)
```

**Compliance predicates (examples):**

```
P1: ∃ authorization_record such that
    access.user_id ∈ authorized_users(access.resource, access.timestamp)
    [Prove access was authorized without revealing who accessed what]

P2: access.timestamp ∈ business_hours(access.user.location)
    [Prove access occurred during permitted hours without revealing time/location]

P3: count(access | access.user_id = U, access.day = D) ≤ MAX_DAILY_ACCESS
    [Prove access frequency policy was followed without revealing access count]
```

**Implementation path (2024):**
- Circuit: Noir or Circom
- Proving system: Groth16 (smallest proof for on-chain verification) or PLONK
- Commitment scheme: Pedersen or Poseidon hash (ZK-friendly)
- Encryption: AES-256-GCM with hardware-backed key (TEE or HSM)
- Nullifier: prevent double-counting same log entry across compliance reports

**Current state:** Prototype-feasible. No production deployment known as of 2024. Active research area. Proving time for a single log entry audit predicate: ~1-5 seconds on server hardware (Groth16). For high-volume systems, batch proving across multiple log entries in a single proof is required.

**Relevance to Delegate Scout:** On-chain security event logging with GDPR compliance. Prove that Delegate Scout logged a security event and that the log entry satisfies OCSF class requirements — without revealing the wallet addresses, transaction details, or user identifiers in the log.

**Relevance to OpenClaw:** Agent tool call audit trail. Prove that agent actions were within policy bounds — without revealing the content of tool calls to third-party auditors.

### Simpler Near-Term Alternative

For systems not ready for ZK audit logs:

```
Tiered audit log architecture:
  Tier 1 (0-30 days):  Full fidelity, encrypted at rest, access-controlled
  Tier 2 (30-365 days): Pseudonymized — user_id → HMAC(user_id, domain_key)
                         Resources pseudonymized similarly
                         Timestamps retained (day precision only, not second)
  Tier 3 (1-7 years):  Aggregated only — counts, not individual records
                        "47 PHI accesses in January 2024" not individual entries
  On legal hold:        Tier 1 full fidelity retained past 30 days for affected records
```

This satisfies GDPR Art. 5(2) accountability, HIPAA § 164.312(b), and GLBA § 314.4(c)(2) while minimizing PII retention per Art. 5(1)(e).

---

## Data Clean Rooms

**What it is:** A privacy-controlled environment where two or more parties can run analytics and queries on combined data without either party seeing the other's raw data. The clean room mediates all queries and returns only aggregate results that pass a privacy threshold.

**The advertising use case (canonical):** A retailer has purchase data; an advertiser has impression data. They want to measure ad effectiveness (did people who saw the ad buy more?). Neither can share raw customer lists. A clean room lets them compute the overlap and attribution without either seeing the other's data.

**Production deployments:**
- **AWS Clean Rooms** — row-level security, query restrictions, aggregation controls
- **Google Ads Data Hub** — BigQuery-based; query results must aggregate ≥50 users
- **Meta Advanced Analytics** — similar model
- **Habu, Infosum, LiveRamp Safe Haven** — third-party clean room infrastructure
- **IQVIA** — pharmaceutical-specific clean room for health data

**Privacy mechanisms inside clean rooms:**

```
Query controls:
  - Minimum group size (k-anonymity): results suppressed if <k rows
  - Column restrictions: certain columns unavailable to query
  - Aggregation-only: no row-level results ever returned
  - Rate limiting: limits on queries per day per analyst

Cryptographic options (more advanced):
  - Secure multi-party computation (MPC): neither party sees raw data
  - Private set intersection (PSI): compute overlap without sharing sets
  - Federated analytics: compute runs at data source, only aggregates shared
  - Homomorphic encryption: query computed on encrypted data
```

**GDPR compliance pattern for clean rooms:**
```
Data controller A (retailer) ──→ Clean room ←── Data controller B (advertiser)
                                      │
                               Query: "conversion rate for users
                                       who saw campaign X"
                                      │
                               Response: "4.2% (n=12,847)"
                                      ─ no individual records exposed
                                      ─ minimum group size: 50
                                      ─ purpose limited to agreed campaign analysis
                                      ─ neither party receives the other's PI
```

**Legal basis:** Typically legitimate interests (Art. 6(1)(f)) for analytics use cases, where the aggregate output cannot identify individuals and minimum group size controls prevent re-identification.

**Regulatory status:**
- GDPR: aggregate outputs meeting k-anonymity thresholds are outside personal data scope — no individual data is processed by either party
- CCPA: clean room outputs that don't identify individuals are not PI — not subject to opt-out requirements
- Google's mandated clean room model: Privacy Sandbox initiative is effectively requiring advertiser migration to clean rooms as third-party cookies are phased out

**Build vs. buy decision:**
- **Buy (AWS/Google):** Faster; regulatory track record; auditable controls. Limitation: data must leave your infrastructure.
- **Build with MPC/PSI:** Data never leaves either party. Higher engineering cost. Stronger privacy guarantee. Relevant when data is too sensitive for cloud infrastructure.

**Relevant to the suite:**
- `data-minimization` → clean room as a SYNTHESIZE-equivalent for multi-party analytics
- `privacy-architecture/primitives.md` → PSI and MPC are the cryptographic foundations
- Delegate Scout: clean room pattern for sharing risk signals with exchanges without revealing raw wallet data
