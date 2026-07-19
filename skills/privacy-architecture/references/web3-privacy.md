# Web3 / Blockchain Privacy

> *"What is needed is an electronic payment system based on cryptographic proof instead of trust... The privacy model works by breaking the flow of information in another place: by keeping public keys anonymous."*
> — Satoshi Nakamoto, Bitcoin: A Peer-to-Peer Electronic Cash System (2008), Sections 1 & 10

Nakamoto's 2008 whitepaper is a direct implementation of Hughes' 1993 program. Section 10 describes a privacy model built on pseudonymous public keys — the minimal-disclosure transaction system Hughes called for. This reference covers what has been built since.

---

## The Blockchain Privacy Paradox

Public blockchains are permanent, global, pseudonymous ledgers. Every transaction is visible to every participant forever.

**What Nakamoto's privacy model guarantees:** Unlinkability between public key and real identity — IF the public key is used only once and its ownership is never disclosed.

**What it does not guarantee:** Unlinkability between transactions from the same key. Address reuse, exchange deposits/withdrawals, and on-chain analytics shatter pseudonymity for most users in practice.

**The gap:** Blockchain analytics firms (Chainalysis, Elliptic, TRM Labs, Nansen) maintain databases linking wallet addresses to real identities via:
- KYC data from exchanges (depositing to/withdrawing from a known exchange links wallet to identity)
- ENS/SNS names (user-chosen, often real name or known handle)
- Behavioral clustering (heuristics linking wallets that transact together)
- OSINT correlation (social media posts mentioning wallet addresses)
- IP logging at RPC nodes (transaction submission leaks IP)

The privacy primitives below address this gap.

---

## Stealth Addresses

**What it does:** Receiver publishes a single stealth meta-address. Senders generate a one-time address per payment. Only the receiver can identify and spend from these addresses.

**Ethereum standard:** ERC-5564 (stealth address standard), ERC-6538 (stealth address registry). In production on EVM.

**Solana status:** No native standard. Custom program implementation required. Research area.

**Protocol (simplified DLEQ-based):**
```
Receiver setup:
  - Spending key: (s, S=s·G)
  - Viewing key:  (v, V=v·G)
  - Meta-address: (S, V) — published publicly

Per-payment (sender):
  1. Generate ephemeral key r, R=r·G
  2. Compute shared secret: ss = H(r·V) = H(v·R)  [ECDH]
  3. Compute stealth address: P = H(ss)·G + S
  4. Send to P; publish R on-chain (in tx metadata)

Receiver scanning:
  1. For each published R: compute ss = H(v·R)
  2. Check if H(ss)·G + S matches any UTXO/account
  3. If match found: spending key = H(ss) + s

Result: Sender cannot link P to the receiver's identity.
        Third party observing chain cannot link P to S or V.
        Only receiver (with viewing key) can identify their payments.
```

**Solana implementation path:**
- Custom Solana program for stealth address registry
- Off-chain scanning service (or client-side with viewing key)
- Account creation: PDA derived from stealth address

**Privacy properties:**
- Sender: learns receiver's stealth address (one-time); cannot link to other payments
- Receiver: learns sender's ephemeral key R (public); can scan for payments
- Chain observer: sees the one-time address P and R; cannot link to receiver identity

---

## Ring Signatures

**What it does:** Sign on behalf of a group ("ring") without revealing which member signed.

**Monero implementation:** Monero has used ring signatures (with key images for double-spend prevention) since 2014. Every Monero transaction mixes the real input with n-1 decoy inputs — a verifier sees n possible signers but cannot determine which one signed.

**Key image:** A deterministic function of the private key — `I = x·H(P)`. Prevents double-spending: signing the same key twice produces the same key image, which the network rejects.

**Current status in Monero:** Ring CT (Confidential Transactions) + RingCT signatures + Bulletproofs for range proofs. Ring size fixed at 16 (15 decoys + the real input) since 2022.

**Limitations:**
- Ring size provides probabilistic, not perfect, privacy
- Chain analysis can reduce the effective anonymity set
- Not natively available on Solana — custom implementation required

**Solana path:** Implement as a custom program using Ristretto255 (Solana's native curve supports this). Computationally expensive on-chain — off-chain proof + on-chain verification is the practical architecture.

---

## Confidential Transactions

**What it does:** Hides transaction amounts while proving they are valid (non-negative, sum correctly).

**Pedersen commitment + Bulletproof:**
```
Amount commitment: C = v·H + r·G  (Pedersen)
  - v = amount (hidden)
  - r = blinding factor (hidden)
  - C is publicly verifiable

Range proof: Bulletproof proving 0 ≤ v < 2^64
  - No trusted setup
  - ~670 byte proof for 64-bit range
  
Balance proof: C_input = C_output + C_fee
  - Homomorphic property: commitments add correctly
  - Verifier checks balance without learning amounts
```

**Deployments:** Monero (RingCT), Grin, Beam, Liquid Network (Bitcoin sidechain), Aztec (Ethereum).

**Solana path:** Solana's ZK Token program (experimental, mainnet-beta) implements confidential transfers for SPL tokens using ElGamal encryption + ZK proofs. This is directly relevant to Solana confidential-transfer designs.

**`spl-token-2022` Confidential Transfers:**
- Extension to SPL Token-2022 standard
- ElGamal encryption for balances
- ZK range proofs for validity
- Auditor key support (optional disclosure to regulator)
- Status: Deployed on mainnet-beta; production-ready for SPL Token-2022 tokens

---

## ZK Rollups and Privacy

**ZK Rollup (general):** Batch many transactions off-chain; post a single ZK proof on-chain proving all transactions were valid. Scales L1 throughput without sacrificing L1 security.

**Privacy ZK Rollups:** Aztec Network (Ethereum L2) — combines ZK scaling with confidential transactions. Users can shield assets and execute private transactions inside the rollup.

**Tornado Cash (Ethereum) — architectural analysis:**
- Deposit: User deposits ETH/ERC-20 and receives a secret note
- Withdraw: User generates ZK proof that they know a secret corresponding to a deposit, without revealing which deposit
- Nullifier: Prevents double-spending (like ring signature key image)
- **Regulatory arc (the cautionary spine of conflict C8):** OFAC-sanctioned Aug 2022 → ***Van Loon v. Treasury* (5th Cir., Nov 2024)** held immutable smart contracts aren't sanctionable "property" → **OFAC delisted the contracts Mar 2025**. But contributor **Roman Storm was convicted (Aug 2025)** of conspiracy to run an unlicensed money transmitter, and **Samourai Wallet's founders pleaded guilty (Jul 2025)**. The lesson is no longer just "design with censorship vectors in mind" — it is that *undifferentiated* anonymity (a pool that cannot distinguish clean from illicit funds) is now the shape of privacy infrastructure regulators and prosecutors target. The architectural answer is below.

**Zcash — the production ZK privacy system:**
- Shielded pool: ZK-SNARK-based private transactions since 2016
- Sapling (Groth16): current production proving system
- Orchard (Halo2): next-generation, no trusted setup
- Privacy model: sender, receiver, and amount all hidden in shielded transactions
- Transparent pool also exists — most users transact transparently (privacy opt-in, not default)

**Lesson from Zcash:** Privacy-by-default produces better privacy outcomes than opt-in. If most transactions are transparent, shielded transactions stand out. Design systems where the private path is the default.

---

## Regulatory-Compliant Privacy — the pragmatic equilibrium

> *"All users with 'good' assets have strong incentives and the ability to prove their membership in a 'good'-only association set."*
> — Buterin, Illum, Nadler, Schär & Soleimani, *Blockchain Privacy and Regulatory Compliance: Towards a Practical Equilibrium* (2023)

The Tornado Cash and Samourai prosecutions (conflict **C8** in `taxonomy/regulatory-taxonomy--conflicts.md`) drew a line: a mixer that pools *all* deposits indiscriminately — clean and illicit alike — is the architecture the AML/CFT regime (FATF R16 Travel Rule; EU TFR 2023/1113) treats as a value-transmitting service, not a privacy tool. The cypherpunk reply is not weaker privacy; it is **selective disclosure aimed at the compliance question itself.**

**Privacy Pools (the construction):**
- On withdrawal, the user proves in zero-knowledge that their deposit belongs to an **association set** of known-honest deposits — a **proof of innocence** — without revealing *which* deposit is theirs or their identity.
- An **Association Set Provider (ASP)** curates the set (excluding sanctioned/illicit deposits). Honest users prove membership in the clean set; illicit funds cannot.
- This is the **exact inverse of Tornado Cash's undifferentiated anonymity**: same ZK unlinkability, plus a cryptographic answer to "are these funds clean?"
- Deployed on Ethereum by **0xbow (2025)**; Vitalik Buterin was among the first depositors.

**The honest caveats (do not design without them):**
- **The ASP is a re-introduced trusted third party** — Szabo's warning (`references/tee.md` framing) applies directly: who controls the set controls who is included. Decentralizing the ASP is an open problem.
- **Money-transmitter liability turns on control of funds, not ledger privacy** — Privacy Pools' non-custodial design helps, but the Storm/Samourai theory (operating an unlicensed transmitter) is not automatically cured by adding a proof of innocence.
- **`ARCH-SATISFIES`, never `ARCH-DISSOLVES`** — the AML identification duty is *answered differently*, not made to disappear. Treat this section as design-informing context, **not legal advice**; a builder in this space needs counsel, not a taxonomy.

**Relevant to Solana:** the association-set pattern is chain-agnostic. A Solana confidential-transfer or ZK-account design (below) that needs to survive the C8 collision should build the proof-of-innocence affordance in from day one rather than bolt compliance on after a subpoena.

---

## Solana-Specific Privacy Tooling

### spl-token-2022 Confidential Transfers
```rust
// Mint with confidential transfer extension
let mint = Mint {
    extensions: vec![
        ExtensionType::ConfidentialTransferMint,
        ExtensionType::ConfidentialTransferFeeConfig,
    ],
    ...
};

// Transfer with confidential amounts
confidential_transfer::process_transfer(
    &program_id,
    accounts,
    &TransferData {
        new_source_decryptable_available_balance: ...,
        proof_instruction_offset: ..., // ZK proof
    }
)
```

### Solana ZK ElGamal Proof Program
Solana's native program (`ZkTokenProof1111...`) verifies:
- Zero-balance proofs
- Range proofs
- Ciphertext validity proofs
- Transfer validity proofs

Used by spl-token-2022 confidential transfers. Verification is cheap on-chain (~15,000 compute units for a range proof).

### Light Protocol (Compressed ZK Accounts)
State compression + ZK proofs for private on-chain state. Active development. Combines Bubblegum-style compression with ZK privacy.

### Elusiv Protocol *(historical — sunset 2024)*
Privacy protocol for Solana — ZK-based private transfers with a selective-disclosure compliance layer (auditor reveal). Reached mainnet, then shut down in 2024; retained here as the reference design for compliance-compatible privacy on Solana. Do not build on it.

---

## RPC Privacy

**Problem:** When a Solana wallet submits a transaction, the RPC node logs the originating IP address. Transaction content + IP = linkable identity even with perfect on-chain privacy.

**Mitigations:**

1. **Tor / VPN over RPC:** Route RPC calls through Tor or a trusted VPN. Cheap, practical, imperfect (Tor exit nodes can be malicious).

2. **Private RPC providers:** Helius, Triton, QuickNode — may have better privacy practices than public RPCs, but still log IPs. Review their data handling.

3. **Self-hosted RPC:** Run your own Solana RPC node. No third-party logging. High cost (~$500/month minimum for archive node).

4. **Jito MEV bundles:** Submit transactions via Jito block engine — bundles obfuscate which RPC submitted which transaction. Not primarily a privacy feature but has privacy side effects.

5. **ZK-compressed transaction submission:** Research area — submit proofs rather than transactions directly to reduce metadata linkage.

**Out-of-band submission consideration:** Transactions submitted via any out-of-band channel ultimately hit an RPC somewhere. The channel may provide payload privacy (encrypted content), but the submitting device's IP still reaches the RPC. Put a VPN or Tor on the submitting device.

---

## Privacy Coin Threat Model

Understanding why privacy coins work (and don't work) informs better Solana privacy design:

| Coin | Technique | Default private? | Weakness |
|---|---|---|---|
| Monero | RingCT + stealth + Dandelion++ (Kovri was abandoned) | Yes (mandatory) | Ring analysis; decoy-selection heuristics |
| Zcash | Groth16 ZK-SNARK | No (opt-in) | Transparent pool dominates usage |
| Grin | MimbleWimble + Bulletproof | Yes | Graph-cut linkability; no scripting |
| Dash | CoinJoin (PrivateSend) | No (opt-in) | Not cryptographically private |
| Bitcoin | None natively | No | Address reuse; chain analytics |

**Design lesson:** Privacy defaults matter more than privacy capabilities. Build private-by-default and allow opt-out rather than the reverse.

---

## References

- Nakamoto, S. (2008). "Bitcoin: A peer-to-peer electronic cash system." *bitcoin.org/bitcoin.pdf.*
- Dai, W. (1998). "b-money." *weidai.com/bmoney.txt.* (Anonymous distributed e-cash)
- Szabo, N. (2005). "Bit gold." *unenumerated.blogspot.com.* (Proof-of-work predecessor)
- Back, A. (2002). "Hashcash — a denial of service counter-measure." *hashcash.org/papers/hashcash.pdf.*
- Noether, S. (2015). "Ring signature confidential transactions for Monero." *IACR ePrint 2015/1098.*
- Bünz, B., et al. (2018). "Bulletproofs: Short proofs for confidential transactions." *IEEE S&P 2018.*
- Ben-Sasson, E., et al. (2014). "Zerocash: Decentralized anonymous payments from Bitcoin." *IEEE S&P 2014.*
- Buterin, V., Illum, J., Nadler, M., Schär, F., & Soleimani, A. (2023). "Blockchain Privacy and Regulatory Compliance: Towards a Practical Equilibrium." *SSRN 4563364.* (Privacy Pools / proof of innocence)
- van Saberhagen, N. (2013). "CryptoNote v2.0." (Ring signatures + stealth addresses; the Monero design)
- Perrin, T. & Marlinspike, M. (2016). "The Double Ratchet Algorithm." *signal.org/docs.*
- EIP-5564. (2022). "Stealth addresses." *eips.ethereum.org/EIPS/eip-5564.*
- Solana Labs. (2023). "SPL Token-2022 confidential transfers." *spl.solana.com.*
