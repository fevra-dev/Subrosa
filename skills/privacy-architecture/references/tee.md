# Trusted Execution Environments

> *"Trusted third parties are security holes."*
> — Nick Szabo (2001)

By Szabo's razor, a TEE is not an elimination of the trusted third party but its **minimization into silicon** — you still trust the chip vendor, the attestation chain, and the microcode. That makes TEEs the honest compromise of this suite: use one when the cryptographic primitives (ZKP, MPC, HE) can't meet the performance budget, and threat-model it as the TTP it is (side-channel history below). Hardware-enforced isolated execution: code and data inside the enclave are protected from the host OS, hypervisor, and physical memory attacks — even from the device owner in some configurations.

---

## TEE Taxonomy

| TEE | Manufacturer | Architecture | Use in this stack |
|---|---|---|---|
| Intel SGX | Intel | x86 (server/desktop) | Server-side private RAG, MPC nodes |
| AMD SEV/SEV-SNP | AMD | x86 (server) | Cloud confidential VMs |
| ARM TrustZone | ARM | ARMv8+ (mobile/embedded) | Mobile/embedded secure signing, Android |
| Apple Secure Enclave | Apple | ARM (Apple Silicon) | iOS key storage, Face ID |
| Solana Seed Vault | Solana/OSOM | ARM TrustZone subset | Solana mobile wallet (MWA 2.0) key isolation |
| AWS Nitro Enclaves | AWS | x86 (cloud) | Cloud-hosted private compute |
| Google Titan | Google | Custom ARM | Android StrongBox |

---

## Intel SGX

**What it is:** Software Guard Extensions. Creates encrypted "enclaves" in RAM — pages encrypted by the CPU memory controller. Even the OS, hypervisor, and privileged kernel code cannot read enclave memory.

**Architecture:**
```
┌────────────────────────────────────────┐
│ Normal world (OS, apps, hypervisor)   │  ← untrusted
├────────────────────────────────────────┤
│ SGX Enclave (encrypted RAM pages)     │  ← trusted by hardware
│  - Code + data encrypted at rest      │
│  - Decrypted only inside CPU          │
│  - Attestation proves enclave identity│
└────────────────────────────────────────┘
```

**Remote attestation:** A third party can verify:
1. The code running in the enclave is exactly what was expected (hash of enclave binary)
2. The enclave is running on genuine SGX hardware
3. The SGX platform is up-to-date (patched against known vulnerabilities)

**Attestation protocol (DCAP):**
- Enclave generates quote signed by platform key
- Quote verified against Intel Attestation Service (IAS) or local DCAP
- Result: cryptographic proof that specific code is running in SGX

**Production deployments:**
- Signal: private contact discovery using SGX (sealed sender, contact intersection)
- Microsoft Azure Confidential Computing: SGX-based VMs
- Fortanix: SGX-based key management
- Secret Network (Cosmos): SGX-based private smart contracts

**Libraries:**
- `Gramine` (Linux SGX shim) — run unmodified Linux applications in SGX
- `EGo` (Go SDK for SGX) — write Go code that runs in SGX
- `Teaclave` (Rust) — Apache incubating SGX framework
- `OpenEnclave` (C/C++) — cross-platform TEE abstraction (SGX + TrustZone)

### Known SGX Vulnerabilities

SGX has a documented history of side-channel attacks. These do not break the confidentiality model in most deployment scenarios but require awareness:

| Attack | Class | Impact | Mitigation |
|---|---|---|---|
| Spectre / Meltdown | Speculative execution | Information leakage via cache timing | Microcode patches; disable hyperthreading |
| Foreshadow (L1TF) | Cache side-channel | Read enclave memory via L1 cache | Microcode + OS patches |
| SGAxe | Attestation key extraction | Forge attestation quotes | Platform re-keying; keep SGX firmware updated |
| ÆPIC Leak | Architectural data sampling | Read stale enclave data from CPU APIC | Microcode patch (Jun 2022 Intel) |
| Plundervolt | Frequency/voltage fault | Corrupt enclave computation | Disable SGX overclocking interface |
| LVI | Load Value Injection | Inject values into enclave execution | Compiler mitigations (clang -mlvi-hardening) |

**Practical guidance:** For most privacy applications, SGX with current microcode patches and recommended mitigations is sufficient. Nation-state adversaries with physical access are the realistic concern for remaining attacks. Run SGX with hyperthreading disabled in high-security deployments.

---

## ARM TrustZone

**What it is:** Hardware security extension in ARM processors creating two execution worlds:
- **Normal World:** Standard OS (Android, Linux) — untrusted
- **Secure World (TEE OS):** Isolated trusted OS — protected from Normal World

**Mobile deployment:**
- Nearly all modern smartphones (Android and iPhone) include TrustZone
- Qualcomm Snapdragon: QSEE (Qualcomm Secure Execution Environment)
- MediaTek Dimensity: Trusted Platform Module + TrustZone TEE (**Seeker hardware**)
- Samsung Exynos: Samsung TEE

**What TrustZone protects on mobile:**
- Biometric templates (fingerprint, face)
- Cryptographic key material (hardware-backed Keystore)
- DRM license keys
- Payment credentials (SE/TEE cooperation)
- **Solana Seed Vault** (see below)

**TrustZone vs. SGX:**
- TrustZone: coarser isolation; Secure World shares CPU with Normal World
- SGX: per-enclave isolation; multiple enclaves can coexist with mutual isolation
- TrustZone: lower overhead, simpler programming model
- SGX: stronger isolation guarantees, richer attestation

**TrustZone development:**
- `OP-TEE` (Open Portable TEE) — open-source TEE OS for TrustZone; reference implementation
- `Trusty TEE` (Google) — Android's TrustZone TEE OS; used in most Android devices
- Trusted Applications (TAs): small programs running in Secure World; communicate with Normal World via SMC (Secure Monitor Call)

---

## Solana Seed Vault

**What it is:** Solana Mobile's hardware key management system. Uses the device's TrustZone-backed secure hardware to store seed phrases and private keys, isolated from the main Android OS.

**Security model:**
```
Android App (Normal World)
  ↓ MWA 2.0 intent
Solana dApp Store Wallet (Normal World mediator)
  ↓ Binder IPC
Seed Vault Service (Normal World)
  ↓ SMC / TrustZone gateway
Seed Vault TA (Secure World)
  → Signs transaction with key material that never leaves Secure World
  → Returns signature only
```

**What Seed Vault protects:**
- Private key material never enters Normal World
- Transaction signing occurs entirely in Secure World
- Seed phrase encrypted with hardware key; decryptable only by Seed Vault TA
- Screen confirmation (TrustZone-backed UI) required before signing

**Seed Vault limitations:**
- Root access to Android can potentially extract Seed Vault data via Secure World exploits (rare; requires sophisticated attack)
- Device must have Android Keystore hardware backing (virtually all modern Android devices)
- Backup: seed-phrase backup (e.g. via steganographic encoding) is an app-level backup path

**API:**
```kotlin
// MWA 2.0 + Seed Vault signing
val result = MobileWalletAdapter().transact(activityResultSender) {
    val authorizationResult = authorize(
        identityUri = Uri.parse("https://example.com"),
        iconUri = Uri.parse("favicon.ico"),
        identityName = "MyWallet"
    )
    // Request signing — happens in Seed Vault (Secure World)
    val signResult = signTransactions(
        transactions = arrayOf(serializedTransaction)
    )
    signResult.signedPayloads[0] // Signature returned; key never leaves Secure World
}
```

---

## Apple Secure Enclave

**What it is:** A dedicated secure processor (T2/Apple Silicon) with its own encrypted memory, isolated from the Application Processor.

**Properties:**
- Unique Device ID (UID) fused into silicon at manufacture — Apple cannot read it
- Biometric template storage (Face ID, Touch ID) — templates never leave SEP
- AES engine hardware-accelerated
- `SecureEnclave.Key` API in CryptoKit (iOS 13+)

```swift
// Generate key in Secure Enclave — never extractable
let key = try SecureEnclave.P256.Signing.PrivateKey()
let signature = try key.signature(for: data)  // Signing in SE
```

**Attestation:** Apple's DeviceCheck and AppAttest APIs allow apps to attest that code is running on a genuine Apple device with a specific app identity. Not equivalent to SGX remote attestation — Apple is the attestation root of trust.

---

## AWS Nitro Enclaves

**What it is:** EC2 feature creating isolated, hardened VMs with no persistent storage, no external network, and no interactive access — not even by the instance owner or AWS.

**Architecture:**
- Parent EC2 instance passes data to enclave via local VSOCK only
- Enclave has no SSH, no internet, no storage
- Cryptographic attestation document proves enclave identity
- AWS KMS can be configured to decrypt only for specific attested enclaves

**Use cases:** Server-side private compute, key management, private ML inference, private database queries.

**Tools:** AWS Nitro CLI, enclave SDK (C, Rust, Python, Java).

**Relevant to OpenClaw:** Privacy-preserving agent memory retrieval on AWS infrastructure — run Qdrant inside a Nitro Enclave; only attested enclave code can query the memory store.

---

## Side-Channel Taxonomy for TEEs

All TEEs share a common class of residual vulnerabilities: **side channels**. The isolation is hardware-enforced against direct memory access but does not prevent information leakage via observable physical effects.

| Channel | Mechanism | Relevance |
|---|---|---|
| Cache timing | Shared L1/L2/L3 cache — attacker measures access time | SGX, TrustZone (if sharing CPU) |
| Branch prediction | Spectre-class — speculative execution leaks data | All modern CPUs |
| Power analysis | Measure CPU power draw correlated with data | Physical access scenarios |
| EM emissions | Electromagnetic emissions correlated with computation | Physical access, close proximity |
| Acoustic | CPU/coil whine correlated with computation | Physical access |
| Memory bus | DRAM access patterns visible to DRAM controller | SGX pre-DIMM-encryption |

---

## References

- Costan, V. & Devadas, S. (2016). "Intel SGX explained." *IACR ePrint 2016/086.*
- Van Bulck, J., et al. (2018). "Foreshadow: Extracting the keys to the Intel SGX kingdom." *USENIX Security 2018.*
- ARM Limited. (2022). "ARM Security Technology: Building a Secure System using TrustZone Technology." *ARM whitepaper.*
- Solana Mobile. (2023). "Seed Vault specification." *github.com/solana-mobile/seed-vault-sdk.*
- Apple. (2023). "Apple Platform Security: Secure Enclave." *apple.com/privacy/docs.*
- AWS. (2023). "AWS Nitro Enclaves documentation." *docs.aws.amazon.com.*
