# Crypto Address Patterns Reference

Detailed format specs for Web3 address detection and confidence scoring.

---

## Solana

| Type | Format | Length | Charset | Confidence signal |
|---|---|---|---|---|
| Wallet address | Base58 | 32–44 chars | `[1-9A-HJ-NP-Za-km-z]` | Context: `pubkey`, `wallet`, `from`, `to`, `mint`, `owner` |
| Transaction hash | Base58 | 86–88 chars (base58 of a 64-byte signature) | Same | Context: `txid`, `signature`, `tx`, `hash` |
| Program ID | Base58 | 32–44 chars | Same | Context: `programId`, `program` |
| Token mint | Base58 | 32–44 chars | Same | Context: `mint`, `token`, `SPL` |

**Key risk:** Solana base58 strings collide with random alphanumeric. Always require at least ONE contextual word nearby before flagging MEDIUM+. Flag all matches as LOW without context.

Exclude known public program IDs from redaction:
- `TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA` (SPL Token)
- `11111111111111111111111111111111` (System Program)
- `metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s` (Metaplex)

---

## Ethereum

| Type | Format | Example pattern |
|---|---|---|
| Wallet / contract address | `0x` + 40 hex chars | `0x742d35Cc6634...` |
| Transaction hash | `0x` + 64 hex chars | `0xabc123...` (66 chars total) |
| EIP-55 checksummed | Mixed case hex | Same regex, mixed case |

**Confidence:** `0x` prefix is a strong signal. HIGH confidence with any context.

---

## Bitcoin

| Type | Format | Notes |
|---|---|---|
| P2PKH (Legacy) | Starts with `1`, 25–34 chars base58 | Most common legacy |
| P2SH (Script) | Starts with `3`, 25–34 chars base58 | |
| Bech32 (SegWit) | `bc1` prefix, 14–74 chars, lowercase alphanumeric | Native SegWit |
| Bech32m (Taproot) | `bc1p` prefix | |

---

## Other Chains

| Chain | Format hint |
|---|---|
| Litecoin | `L` or `M` prefix, base58 |
| Dogecoin | `D` prefix, base58 |
| Cardano | `addr1` prefix (Bech32) |
| Polkadot | SS58 format, 47–48 chars |
| Cosmos | `cosmos1` prefix, bech32 |

Flag any of the above as MEDIUM if detected; surface for user confirmation.

---

## Seed Phrases / Mnemonics

BIP39 uses a wordlist of 2048 words. A 12-word or 24-word sequence of lowercase BIP39 words separated by spaces is extremely high sensitivity.

**Do not attempt regex match** — too many false positives. Instead:
- If user pastes text and mentions "seed", "mnemonic", "recovery phrase", "backup words" — treat the entire block as HIGH sensitivity and redact fully.
- Offer to replace with `[SEED_PHRASE_REDACTED]`.

---

## Private Keys

| Type | Format |
|---|---|
| Solana keypair file | JSON **array of 64 integers (0–255)** — e.g. `[12,84,...]`; the base58 *export* of the same secret key is an 86–88 char base58 string |
| Ethereum private key | 64 hex chars (32 bytes), often with `0x` prefix |
| PEM format | `-----BEGIN PRIVATE KEY-----` block |
| WIF (Bitcoin) | `5`, `K`, or `L` prefix, 51–52 chars base58 |

**All private key matches are AUTO-REDACT regardless of confidence.** These are never safe to share.
