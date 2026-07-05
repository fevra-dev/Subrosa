# Zero-Knowledge Proof Reference

> *"The methods are based upon public-key encryption, zero-knowledge interactive proof systems, and various software protocols for interaction, authentication, and verification."*
> — Timothy C. May, The Crypto Anarchist Manifesto (1988)

ZKPs were formalized by Goldwasser, Micali, and Rackoff (1985). May cited them in 1988 as the technical basis for the Cypherpunk program. Thirty-five years of research has made them practical.

---

## What a ZKP Is

A ZKP allows a **prover** to convince a **verifier** that a statement is true without revealing any information beyond the truth of the statement.

Three properties (GMR 1985):
- **Completeness:** If the statement is true, an honest prover can convince an honest verifier
- **Soundness:** If the statement is false, no cheating prover can convince an honest verifier (except with negligible probability)
- **Zero-knowledge:** The verifier learns nothing beyond the fact that the statement is true

**Non-interactive ZKPs (NIZKs):** The prover generates a single proof string; the verifier checks it. No back-and-forth. All modern production ZKPs are non-interactive via the Fiat-Shamir heuristic (in the random oracle model) or a structured reference string (trusted setup).

---

## Proving System Comparison

| System | Setup | Proof size | Prover time | Verifier time | Post-quantum | Best for |
|---|---|---|---|---|---|---|
| **Groth16** | Trusted (per-circuit) | ~200 bytes | Fast | ~1ms | No | On-chain verification; smallest proofs |
| **PLONK** | Trusted (universal) | ~1-2KB | Moderate | ~5ms | No | Flexible; one setup for many circuits |
| **Marlin** | Trusted (universal) | ~1KB | Moderate | ~3ms | No | Similar to PLONK |
| **Bulletproofs** | None | ~1-2KB (range), grows with circuit | Slow | Slow | No | Range proofs; no trusted setup |
| **STARK** | None | ~40-200KB | Very slow | Fast | Yes | High security; no trusted setup; post-quantum |
| **Plonky2** | None | ~100KB | Fast | Fast | No | Recursive proofs; Polygon ecosystem |
| **Nova/SuperNova** | None | Constant | Incremental | Fast | No | Recursive / folding; IVC |

**Trusted setup note:** Groth16 requires a circuit-specific ceremony. PLONK requires a universal ceremony (usable for any circuit up to a size). STARKs and Bulletproofs require no setup — the security relies on hash functions only. For new systems: prefer PLONK-family (one ceremony, reusable) or STARKs (no ceremony) over Groth16 unless proof size is critical.

---

## Tooling

### Noir (Recommended for new projects)
**Language:** Rust-like DSL, compiles to ACIR (Abstract Circuit Intermediate Representation)  
**Backends:** Barretenberg (PLONK/UltraPLONK, Aztec), Marlin, STARK (via transpilation)  
**Platform:** Browser (WASM), Node.js, native Rust  
**Mobile:** WASM proving viable on modern mobile hardware — benchmark for Seeker (Dimensity 7300)  
**Strengths:** Best developer experience; growing ecosystem; Aztec mainnet target  
**Weaknesses:** Ecosystem younger than Circom; some backend limitations

```noir
// Example: Prove age >= 18 without revealing exact age
fn main(age: u32, threshold: pub u32) {
    assert(age >= threshold);
}
// Public input: threshold (18)
// Private input: age (hidden from verifier)
// Proof: "I know an age value >= 18"
```

### Circom + SnarkJS
**Language:** Circom DSL (constraint system definition)  
**Backends:** Groth16, PLONK via snarkjs  
**Platform:** JavaScript/Node.js; WASM in browser  
**Strengths:** Most mature ecosystem; extensive tooling; battle-tested  
**Weaknesses:** Verbose; more footgun-prone; Groth16 requires per-circuit setup

```circom
// Range proof: prove value is in [0, 2^32)
template RangeCheck(n) {
    signal input value;
    signal bits[n];
    var sum = 0;
    for (var i = 0; i < n; i++) {
        bits[i] <-- (value >> i) & 1;
        bits[i] * (1 - bits[i]) === 0;  // bit constraint
        sum += bits[i] * (2 ** i);
    }
    sum === value;
}
```

### Arkworks (Rust)
**Language:** Rust  
**Backends:** Groth16, PLONK, Marlin, IPA  
**Strengths:** Most flexible; production-grade Rust; used in Zcash, Aleo  
**Weaknesses:** Steepest learning curve; verbose circuit authoring

### RISC Zero
**Approach:** ZK-STARK proving of arbitrary Rust code execution  
**Strengths:** Write normal Rust; the proving system handles the circuit  
**Weaknesses:** Large proof size; high prover cost; not suitable for on-chain verification without recursion  
**Use case:** Off-chain computation proofs; proving program execution results

### SP1 (Succinct Labs)
**Approach:** ZK-STARK proving of RISC-V execution (Rust/C/Go programs)  
**Strengths:** Compile existing Rust code to provable execution; rapidly maturing  
**Weaknesses:** Still maturing; recursion overhead  
**Use case:** Similar to RISC Zero; alternative with different performance tradeoffs

---

## Circuit Vulnerability Taxonomy

Under-constrained circuits are the dominant ZKP security bug class. The verifier accepts invalid proofs because the circuit doesn't fully encode the intended statement.

### UC-1 — Missing range constraint
```circom
// VULNERABLE: doesn't constrain x to [0, 2^n)
template BadRange() {
    signal input x;
    signal output y;
    y <== x;  // x could be negative or > max in field arithmetic
}

// FIXED: add Num2Bits range check
component rangeCheck = Num2Bits(32);
rangeCheck.in <== x;
```

### UC-2 — Non-deterministic intermediate signals
```circom
// VULNERABLE: intermediate computed outside constraints
signal intermediate;
intermediate <-- a / b;  // <-- is assignment, not constraint
// MUST add: intermediate * b === a;
```

### UC-3 — Field arithmetic overflow
ZKP circuits operate in a finite field (typically prime order ~2^254). Values wrap around. An "age" field with value 0 is indistinguishable from field_prime — both satisfy `age >= 0`. Always constrain value ranges explicitly.

### UC-4 — Trusted setup toxic waste reuse
If the random secret ("toxic waste") from a Groth16 ceremony is not destroyed and is later compromised, anyone possessing it can forge proofs for that circuit. Use large multi-party ceremonies: the secret is safe as long as at least one participant destroys their contribution.

**Auditing resource:** Trail of Bits "Audit Techniques for Zero-Knowledge Circuits" (2023) — the definitive vulnerability taxonomy for Circom/Noir circuits.

---

## Proving System Selection by Use Case

**On-chain Solana verification:**  
→ Groth16 (smallest proof, cheapest on-chain verification cost)  
→ Use `solana-zk-token-proof` as reference for on-chain verifier pattern  
→ Alternatively: PLONK with the Aztec Barretenberg verifier  

**Mobile proving (Kyma / Seeker):**  
→ Noir + Barretenberg WASM — benchmark first  
→ Alternatively: PLONK with small circuit sizes  
→ Groth16 for smallest proof transmission (acoustic channel bandwidth is limited)  
→ STARKs are too large for acoustic transmission  

**Post-quantum requirement:**  
→ STARKs only — all SNARK systems rely on elliptic curve discrete log (not post-quantum)  

**No trusted setup requirement:**  
→ STARKs, Bulletproofs, or Halo2 (IPA-based, no trusted setup)  

**Recursive proofs (proof aggregation):**  
→ Plonky2, Nova/SuperNova, Halo2 recursive  
→ Use case: batch-verify many proofs into one; ZK rollup compression  

---

## Trusted Setup Ceremonies

If using Groth16 or PLONK, a trusted setup is required. Two phases:

**Phase 1 (Powers of Tau):** Universal; reusable across all circuits. Use Ethereum's perpetual powers of tau ceremony (hermez.io/downloads/hez2_final.zkey). Already complete — download and use.

**Phase 2 (Circuit-specific):** Required for Groth16; one ceremony per circuit. Run your own or participate in a project ceremony. For PLONK: Phase 2 is the universal SRS — Ethereum's KZG ceremony output is usable.

**Minimum ceremony:** For internal/low-stakes use, a single-participant ceremony is technically valid but defeats the security model. For production: use at least 6-10 independent participants, each contributing and destroying their randomness, with a public transcript.

---

## Key Academic References

- Goldwasser, Micali, Rackoff (1985) — "The Knowledge Complexity of Interactive Proof Systems." Seminal ZKP definition.
- Groth (2016) — "On the Size of Pairing-Based Non-Interactive Arguments." Groth16.
- Ben-Sasson et al. (2018) — "Scalable, transparent, and post-quantum secure computational integrity." zk-STARKs.
- Bünz et al. (2018) — "Bulletproofs: Short Proofs for Confidential Transactions and More." Range proofs without trusted setup.
- Gabizon, Williamson, Ciobotaru (2019) — "PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive arguments of Knowledge."
- Boneh et al. (2020) — "Recursive Proof Composition without a Trusted Setup." Halo.
- Trail of Bits (2023) — "Audit Techniques for Zero-Knowledge Circuits." Vulnerability taxonomy.

---

## Post-Quantum Cryptography (PQC)

> *"Harvest Now, Decrypt Later" (HNDL): Nation-state adversaries are recording encrypted traffic today with the intention of decrypting it when quantum computers become capable. For data with 10+ year sensitivity, this is a present-day threat.*

All ZKP systems documented above rely on elliptic curve discrete logarithm hardness (ECDL) or integer factorisation — both broken by Shor's algorithm on a sufficiently powerful quantum computer. STARKs are the exception: hash-function security only, post-quantum by construction.

### NIST PQC Standards (Finalized 2024)

NIST finalized three post-quantum cryptographic standards in August 2024:

| Standard | Algorithm | Type | Security basis | Use case |
|---|---|---|---|---|
| **FIPS 203** | ML-KEM (Kyber) | Key encapsulation mechanism (KEM) | Module lattice / LWE | Key exchange, session establishment |
| **FIPS 204** | ML-DSA (Dilithium) | Digital signature | Module lattice / SIS | Signatures, authentication |
| **FIPS 205** | SLH-DSA (SPHINCS+) | Digital signature | Hash functions only | High-security signatures, no lattice assumption |

A fourth standard — **FIPS 206 (ML-DSA-Ed / Falcon)** — was under final review as of mid-2024. Monitor NIST for status.

**Security levels (NIST categories):**
- Level 1: equivalent to AES-128
- Level 3: equivalent to AES-192
- Level 5: equivalent to AES-256

Most production deployments targeting Level 3 (Kyber-768 / Dilithium3) or Level 5 for critical systems.

### ML-KEM / Kyber (FIPS 203)

Replaces ECDH and RSA for key encapsulation. Drop-in replacement for X25519 in most protocols.

**Performance vs. X25519:**
- Public key: 1184 bytes (vs. 32 bytes X25519) — ~37x larger
- Ciphertext: 1088 bytes (vs. 32 bytes X25519)
- Operations: comparable speed to X25519 on modern hardware
- Memory: higher — relevant for embedded/mobile (Seeker hardware)

**Hybrid mode (recommended for now):**
Combine classical and PQC in the same handshake:
`shared_secret = X25519_output || Kyber_output`
Then derive session key: `HKDF(X25519_output || Kyber_output)`

This is secure if either algorithm is secure — provides PQC protection without abandoning classical security during transition.

**Libraries:**
- `liboqs` (Open Quantum Safe) — C, with Python/Rust/Go wrappers; Kyber, Dilithium, SPHINCS+
- `pqcrypto` crate (Rust) — Kyber, Dilithium
- `kyber-k2so` (pure Go) — Kyber only
- `bouncycastle` (Java) — Kyber, Dilithium (v1.73+)

### ML-DSA / Dilithium (FIPS 204)

Replaces ECDSA and Ed25519 for signatures.

**Performance vs. Ed25519:**
- Public key: 1312 bytes (vs. 32 bytes)
- Signature: 2420 bytes (vs. 64 bytes) at Level 3
- Signing: ~3x slower than Ed25519
- Verification: comparable

**For Solana context:** Solana uses Ed25519. Full PQC migration of Solana transaction signatures requires a protocol-level change — not addressable by individual developers today. Watch Solana Foundation for PQC roadmap. For application-layer signing (attestations, credentials, off-chain proofs): migrate to Dilithium now.

### SLH-DSA / SPHINCS+ (FIPS 205)

Hash-function-based signatures. No lattice assumption — maximum security conservatism.

**Trade-offs:**
- Signature size: 7856–49856 bytes depending on parameter set (very large)
- Signing: slow (~10-100ms)
- Verification: fast
- **No state required** — unlike XMSS/LMS (stateful hash-based signatures), SPHINCS+ is stateless

**Use when:** Long-term signatures (code signing, certificate authorities, legal documents) where lattice assumption risk is unacceptable and large signature size is tolerable.

### HNDL Threat Model Entry

Add to `threat-model-privacy` Archetype 7 (Nation-State) when long-term sensitive data is involved:

```
HNDL Attack Vector:
  Adversary records encrypted traffic in transit today.
  When quantum capability is achieved (~10-15 years, estimates vary):
  Adversary decrypts all previously recorded sessions.
  
Data at risk: Any data encrypted with classical algorithms
  (TLS 1.3 with ECDHE, Signal Protocol X3DH, PGP/RSA)
  that is sensitive for 10+ years.
  
High HNDL sensitivity: Medical records, legal privilege,
  government classified, long-term financial secrets,
  cryptographic key material, intelligence sources.
  
Mitigation: Deploy hybrid classical+PQC key exchange NOW
  for high-sensitivity long-term data.
  TLS 1.3 hybrid: X25519Kyber768 (supported in Chrome 116+,
  BoringSSL, Go 1.23+ experimental)
```

### PQC Migration Checklist

For any system with data sensitivity > 5 years:

- [ ] Identify all key exchange mechanisms (TLS, Signal, custom protocols)
- [ ] Identify all signature schemes (ECDSA, Ed25519, RSA)
- [ ] Assess data sensitivity horizon (how long must this data remain private?)
- [ ] Implement hybrid key exchange for new sessions (X25519 + Kyber)
- [ ] Plan signature migration timeline (Dilithium for new deployments)
- [ ] Re-encrypt archived sensitive data under PQC-protected keys before quantum capability
- [ ] Monitor NIST PQC standards page for FIPS 206 (Falcon) finalization
- [ ] Monitor Solana Foundation for Ed25519 → PQC migration roadmap

### References

- NIST. (2024). "FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard." *csrc.nist.gov.*
- NIST. (2024). "FIPS 204: Module-Lattice-Based Digital Signature Standard." *csrc.nist.gov.*
- NIST. (2024). "FIPS 205: Stateless Hash-Based Digital Signature Standard." *csrc.nist.gov.*
- Shor, P. (1994). "Algorithms for quantum computation: discrete logarithms and factoring." *FOCS 1994.*
- Open Quantum Safe Project. *openquantumsafe.org.*
