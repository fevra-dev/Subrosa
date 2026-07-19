# Foundational Cryptographic Primitives

> *"We stand today on the brink of a revolution in cryptography... Public key cryptosystems... may permit... transactions to be carried out with neither party seeing the other's true name or number."*
> — Whitfield Diffie & Martin Hellman, "New Directions in Cryptography" (1976)

Everything below descends from that 1976 revolution: two strangers on a network establishing secrets without meeting made the intermediary optional, and Chaum (1985) turned it into a program. Commitment schemes, PSI, homomorphic encryption, MPC, differential privacy, and ORAM — the building blocks beneath ZKPs and credentials.

---

## Commitment Schemes

**What it does:** Commit to a value now; reveal it later. The commitment is binding (cannot change the value) and hiding (reveals nothing about the value until opening).

**Two properties:**
- **Binding:** Cannot open the commitment to a different value than was committed
- **Hiding:** The commitment reveals nothing about the committed value

### Hash Commitment (Simple, no setup)
```
Commit: C = H(value || randomness)
Open:   Reveal (value, randomness) → verifier checks H(value || randomness) == C
```
**Binding:** Collision resistance of hash function  
**Hiding:** Preimage resistance  
**Caveat:** Not homomorphic — cannot compute on committed values

### Pedersen Commitment (Homomorphic)
```
Setup: Public parameters (G, H) — two generators, discrete log unknown
Commit: C = r·G + v·H  (r = random blinding, v = value)
Open: Reveal (r, v) → verifier checks r·G + v·H == C
```
**Binding:** Discrete log hardness (if log_G(H) is unknown, cannot cheat)  
**Hiding:** Perfect (statistically hiding — even computationally unbounded adversary learns nothing)  
**Homomorphic:** C(v1) + C(v2) = C(v1 + v2) — can add committed values  
**Use cases:** Range proofs (Bulletproofs use Pedersen), confidential transactions (Monero, Grin), ZKP input commitments

### KZG Commitment (Polynomial)
```
Commit to polynomial f(x) as C = f(τ)·G (τ is trusted setup secret)
Prove f(z) = y without revealing f
```
**Use cases:** ZK-SNARKs (PLONK), Ethereum danksharding, proof aggregation  
**Requires trusted setup** (the τ must be destroyed)

---

## Private Set Intersection (PSI)

**What it does:** Two parties (Alice with set A, Bob with set B) learn |A ∩ B| or the elements of A ∩ B — without revealing elements NOT in the intersection.

**Example:** Alice has a contact list; Bob has a contact list. They want to find mutual contacts without revealing their full lists.

**Production deployments:**
- Apple iMessage "Find Friends" — PSI for contact discovery
- Google/Apple COVID exposure notification — PSI for proximity matching
- Meta Messenger end-to-end encrypted contact upload — PSI variant

**Protocols:**

**ECDH-based PSI (efficient, semi-honest):**
```
1. Alice hashes and blinds each element: H(a_i)^r_A
2. Bob blinds Alice's elements: (H(a_i)^r_A)^r_B
3. Bob sends his own elements blinded: H(b_j)^r_B
4. Alice unblinds Bob's elements: H(b_j)^r_B → H(b_j)^r_A^r_B ... wait
   Actually: Alice computes H(b_j)^r_A from Bob's H(b_j)^r_B? No.
   
Correct protocol:
1. Alice: a'_i = H(a_i)^r_A for all a_i; send {a'_i}
2. Bob: b'_j = H(b_j)^r_B for all b_j; 
        a''_i = (a'_i)^r_B = H(a_i)^(r_A·r_B); send {b'_j}, {a''_i}
3. Alice: computes (b'_j)^r_A = H(b_j)^(r_A·r_B)
          intersection = {b_j : H(b_j)^(r_A·r_B) ∈ {a''_i}}
```

**Libraries:**
- `OpenMined/PSI` (C++/Python/JavaScript) — ECDH + OT-based PSI
- `Microsoft APSI` (C++) — asymmetric PSI for large/small set intersection
- `Secretflow` (Python) — privacy-preserving ML framework including PSI

**Use cases for privacy suite:**
- Agent memory privacy: check if two agents' memory sets overlap without full disclosure
- Delegate Scout: check if wallet appears in a risk list without revealing the list
- Exchange.Art: match buyer/seller interests without revealing preference lists

---

## Homomorphic Encryption

**What it does:** Compute on encrypted data without decrypting it. The server processes ciphertexts; the result decrypts to the correct computation output.

### Partially Homomorphic (PHE)
Supports ONE operation type:
- **Paillier:** Additive homomorphism — `E(a) + E(b) = E(a+b)`. Production-ready. Used in MPC.
- **RSA:** Multiplicative homomorphism. Not used for HE in practice.
- **ElGamal:** Multiplicative homomorphism over elliptic curves.

**Use case for PHE (Paillier):** Privacy-preserving sum/average without revealing individual values. E.g.: aggregate sensor readings, private voting tallies, confidential payroll.

### Somewhat/Leveled Homomorphic (SHE/LHE)
Supports a limited number of multiplications before noise overwhelms ciphertext. BGV, BFV schemes.

**Use case:** Fixed-depth ML inference on encrypted data (small neural networks).

### Fully Homomorphic Encryption (FHE)
Supports arbitrary computation on encrypted data. Bootstrapping periodically "refreshes" ciphertexts to allow unbounded computation.

**Current performance (2024):**
- Simple operations: ~1000x overhead vs. plaintext
- AES evaluation: seconds per block
- Small neural network inference: minutes
- Improving rapidly — TFHE-rs (Zama) shows 10x speedup vs. 2022

**Libraries:**
- `TFHE-rs` (Rust, Zama) — fast FHE over booleans; GPU acceleration
- `OpenFHE` (C++) — supports BGV, BFV, CKKS; most comprehensive
- `Microsoft SEAL` (C++) — BGV, BFV, CKKS; well-documented
- `Concrete` (Python, Zama) — Python API over TFHE-rs; compile Python to FHE

**When FHE is practical today:**
- Simple operations on small data (comparison, equality, small range)
- Offline batch processing where latency is not critical
- High-value use cases that justify infrastructure cost (medical, financial)

**When to wait:**
- Real-time interactive applications — overhead too high
- Large neural network inference — impractical without GPU cluster
- Mobile devices — prover cost prohibitive for current FHE schemes

**Relevant to OpenClaw:** FHE-based private memory retrieval is theoretically appealing but practically impractical in 2024. Watch TFHE-rs GPU benchmarks — this may be viable on server-side within 2-3 years.

---

## Secure Multi-Party Computation (MPC)

**What it does:** Multiple parties jointly compute a function over their private inputs, with each party learning only the output — not others' inputs.

**Foundational result (Yao 1986, Ben-Or et al. 1988):** Any function computable by a single party can be computed by multiple parties without any party learning more than the output.

### Secret Sharing (Shamir, 1979)
Split a secret into n shares; any t shares reconstruct the secret; t-1 shares reveal nothing.

```python
# Shamir (t,n) secret sharing over prime field
# Secret s split into n shares, any t reconstruct
shares = shamir_split(secret=s, threshold=t, num_shares=n)
# Each party holds one share
reconstructed = shamir_combine(shares[:t])  # any t shares suffice
```

**Applications:** Threshold signatures (t-of-n signing without any one party holding the full key), distributed key generation, private key custody.

### Garbled Circuits (Yao 1986)
One party "garbles" a Boolean circuit; the other evaluates it obliviously using Oblivious Transfer. Two-party, semi-honest, constant number of rounds.

**Performance:** ~10 ns per AND gate (AES-based garbling). Practical for circuits with millions of gates.

### GMW / SPDZ Protocols
Multi-party (>2), various adversarial models.

**SPDZ (Damgaard et al., 2012):** Preprocessing model — generate correlated randomness offline; efficient online phase. Production-grade for high-value use cases.

**Libraries:**
- `MP-SPDZ` (C++) — most performant; supports many MPC protocols; research + production
- `SCALE-MAMBA` (C++) — SPDZ successor; production-focused
- `ABY` (C++) — efficient two-party computation; garbled circuits + secret sharing
- `tf-encrypted` (Python) — TensorFlow on top of MPC for privacy-preserving ML
- `CrypTen` (Python) — PyTorch on top of MPC (Facebook Research)

**MPC for Solana / Web3:**
- **Threshold ECDSA/EdDSA:** t-of-n signing without a single key holder. Used in: tBTC bridge (Threshold Network), Lightning Network watchtowers, institutional custody (Fireblocks MPC).
- **Mobile wallet key management:** MPC-based (threshold) signing splits a wallet key across devices without a single point of failure — applicable to Seed Vault-backed mobile wallets.

**Performance rule of thumb:**
- LAN MPC: practical for circuits up to ~10^8 gates
- WAN MPC: practical for circuits up to ~10^6 gates
- Mobile: practical only for very small circuits (threshold signing, key generation)

---

## Differential Privacy

> *"Differential privacy offers a mathematically rigorous guarantee of privacy... it limits what any adversary can infer about an individual from the output of a computation, regardless of what other information the adversary has."*
> — Cynthia Dwork, The Algorithmic Foundations of Differential Privacy (2014)

**What it does:** Add calibrated statistical noise to query outputs so that no individual's data has more than a bounded effect on the result. An adversary cannot determine whether any specific individual was in the dataset.

**Formal definition (ε-DP):** A randomized mechanism M satisfies ε-differential privacy if for all datasets D1, D2 differing in one individual's data, and all outputs S:
```
Pr[M(D1) ∈ S] ≤ e^ε × Pr[M(D2) ∈ S]
```

**ε (epsilon) — privacy budget:**
- ε → 0: stronger privacy (more noise, less utility)
- ε = 0.1: very strong (Apple/Google crash report standard)
- ε = 1.0: strong (Apple differential privacy for emoji/word usage)
- ε = 10: weak (meaningful but not strong privacy)

**Sensitivity (Δf):** Maximum change in output when one individual's data changes. Determines noise magnitude.

**Mechanisms:**
- **Laplace mechanism:** Add Laplace(0, Δf/ε) noise. For numeric queries.
- **Gaussian mechanism:** Add N(0, (Δf·σ/ε)²) noise. For (ε, δ)-DP. Lower noise than Laplace for multi-dimensional output.
- **Exponential mechanism:** For categorical outputs. Sample from distribution weighted by score × ε/(2Δu).
- **Randomized response:** For local DP (noise added at data source, not aggregator).

**Composition:**
- **Sequential composition:** k queries each with ε_i use total budget ε = Σ ε_i
- **Advanced composition (Rényi DP):** Tighter bound for many queries — use RDP accountant in practice
- **Zero-concentrated DP (zCDP):** Even tighter for Gaussian mechanism; preferred for ML training (DP-SGD)

**Local vs. Central DP:**
- **Central DP:** Noise added to aggregate; data collected in plaintext. Curator must be trusted.
- **Local DP:** Noise added by each user before submission. No trusted curator needed. Higher noise (√n× worse than central for same ε).

**Libraries:**
- `OpenDP` (Python/Rust) — academic standard; most rigorous implementation
- `Google Differential Privacy` (C++/Go/Java) — production-grade; used in Google products
- `Apple Differential Privacy` — framework described in WWDC; not open source
- `Diffprivlib` (Python, IBM) — scikit-learn compatible DP ML

**Production deployments:**
- Apple: DP for emoji/word usage, health data aggregation (ε ≈ 1.0-8.0 per feature)
- Google: RAPPOR for Chrome browser statistics, DP in Google Analytics
- US Census Bureau: 2020 Decennial Census used DP (TopDown algorithm) — highly controversial, useful case study

**Relevant to privacy suite:**
- Agent behavioral analytics (Section 3.5 of portfolio paper) — ε-DP on query embeddings
- Delegate Scout aggregated risk statistics — DP sum/count queries over delegation data
- Exchange.Art trading pattern analytics — DP on purchase behavior

---

## Oblivious RAM (ORAM)

**What it does:** Access a data store such that the access pattern — which records were read/written and when — reveals nothing to an observer.

**Why needed:** Even encrypted databases leak access patterns. If an adversary observes that record 42 is accessed after every login, they can infer that record 42 is the user's session credential — even without decrypting it.

**Construction:** Every ORAM access involves shuffling data in a way that hides which record was truly accessed.

**Performance cost:** O(log²N) overhead per access (Circuit ORAM, best practical). For N=10^6 records: ~20x overhead vs. direct access.

**Practical threshold:** ORAM is practical for small-to-medium datasets (~10^5 records) with moderate access frequency. For large-scale production databases: too expensive.

**Libraries:**
- `Obliv-C` (C) — ORAM primitives for two-party computation
- `Path ORAM` reference implementation (multiple languages)
- Running Qdrant in TEE is a pragmatic alternative for moderate threat models

**Relevant to:** Private RAG retrieval for OpenClaw (see SKILL.md pattern); Delegate Scout private scanner queries.

---

## References

- Shamir, A. (1979). "How to share a secret." *Communications of the ACM 22(11).*
- Yao, A.C. (1986). "How to generate and exchange secrets." *FOCS 1986.* (Garbled circuits)
- Ben-Or, M., Goldwasser, S. & Wigderson, A. (1988). "Completeness theorems for non-cryptographic fault-tolerant distributed computation." *STOC 1988.*
- Goldreich, O., Micali, S. & Wigderson, A. (1987). "How to play any mental game." *STOC 1987.* (MPC foundations)
- Dwork, C. (2006). "Differential privacy." *ICALP 2006.*
- Dwork, C. & Roth, A. (2014). "The algorithmic foundations of differential privacy." *Foundations and Trends in TCS.*
- Damgaard, I., et al. (2012). "Multiparty computation from somewhat homomorphic encryption." *CRYPTO 2012.* (SPDZ)
- Gentry, C. (2009). "A fully homomorphic encryption scheme." *PhD Thesis, Stanford.*
- Pagh, R. & Mironov, I. (2022). "TFHE deep-dive." Zama blog.
