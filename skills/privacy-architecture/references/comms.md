# Communications Privacy

> *"Privacy in an open society also requires cryptography. If I say something, I want it heard only by those for whom I intend it."*
> — Eric Hughes, A Cypherpunk's Manifesto (1993)

> *"Cypherpunks are actively engaged in making the networks safer for privacy. We are defending our privacy with cryptography, with anonymous mail forwarding systems, with digital signatures, and with electronic money."*
> — Hughes (1993)

---

## Threat Model for Communications

Before selecting a protocol, establish what must be hidden:

| Property | What it hides | Protocol layer |
|---|---|---|
| **Confidentiality** | Message content | Encryption (AES, ChaCha20) |
| **Integrity** | Message tampering | MAC (HMAC, Poly1305) |
| **Authentication** | Sender identity | Digital signature (Ed25519) |
| **Forward secrecy** | Past messages if key compromised | Ephemeral key exchange (X3DH, DH ratchet) |
| **Break-in recovery** | Future messages if key compromised | Double Ratchet algorithm |
| **Sender anonymity** | Who sent the message | Mixnets, onion routing |
| **Receiver anonymity** | Who received the message | Anonymous routing, PIR |
| **Message existence** | That a message was sent at all | Cover traffic, steganography |
| **Timing** | When the message was sent | Batching, delays, cover traffic |
| **Volume** | How much was communicated | Fixed-length padding |

Most protocols provide the first three. Forward secrecy is table stakes for modern security. The lower properties (sender/receiver anonymity, message existence) require architectural solutions beyond encryption.

---

## Signal Protocol

The gold standard for end-to-end encrypted messaging. Used in Signal, WhatsApp, Google Messages (RCS), Facebook Messenger (secret mode), Wire.

**Components:**

### X3DH (Extended Triple Diffie-Hellman) — Session Establishment
```
Keys per user:
  IK: Identity key (long-term signing key)
  SPK: Signed prekey (medium-term; rotated ~weekly)
  OPK: One-time prekey (single-use; batch published)

Session key establishment:
  DH1 = DH(IK_Alice, SPK_Bob)
  DH2 = DH(EK_Alice, IK_Bob)        [EK = ephemeral key]
  DH3 = DH(EK_Alice, SPK_Bob)
  DH4 = DH(EK_Alice, OPK_Bob)       [if OPK available]
  SK  = KDF(DH1 || DH2 || DH3 || DH4)
```
**Properties:** Mutual authentication; forward secrecy; deniability (neither party can prove the other sent anything).

### Double Ratchet — Ongoing Messaging
Two ratchets chained:
- **Diffie-Hellman ratchet:** New DH exchange per message direction change → new chain key
- **Symmetric-key ratchet:** New message key per message from current chain key

**Properties:**
- **Forward secrecy:** Old message keys deleted after use — past messages safe if current key compromised
- **Break-in recovery (post-compromise security):** After a compromise, the next DH ratchet step heals the session — future messages are safe
- **Out-of-order delivery:** Each message has an independent key; can decrypt out of sequence

**Implementation:**
```rust
// Using libsignal-protocol-rust
use libsignal_protocol::*;

// Session store, identity store, prekey store needed
let session_cipher = SessionCipher::new(
    &mut session_store,
    &mut identity_store,
    &address,
    &mut csprng
);

let ciphertext = session_cipher.encrypt(&message).await?;
let plaintext = session_cipher.decrypt(&ciphertext).await?;
```

**Libraries:**
- `libsignal-client` (Rust/Java/TypeScript) — Signal's official cross-platform library
- `signal-protocol` (JavaScript) — web implementation

---

## Onion Routing / Tor

**Architecture:** Messages are wrapped in layers of encryption and routed through a circuit of relay nodes. Each node decrypts one layer and forwards to the next — no single node sees both source and destination.

```
Alice → [Encrypt for Exit] → [Encrypt for Middle] → [Encrypt for Guard]
                                                              ↓
                                                    Guard node (knows Alice, not destination)
                                                              ↓
                                                    Middle node (knows neither)
                                                              ↓
                                                    Exit node (knows destination, not Alice)
                                                              ↓
                                                         Destination
```

**Properties:**
- Guard node knows sender, not destination
- Exit node knows destination, not sender
- Middle node knows neither
- End-to-end encryption hides content from exit node (when destination uses HTTPS/TLS)

**Limitations:**
- **Traffic analysis:** Global adversary observing both Alice's ISP and the destination can correlate timing to deanonymize
- **Exit node attacks:** Exit node sees plaintext if destination doesn't use TLS
- **Timing correlation:** High-bandwidth flows are easier to correlate
- **Bridge enumeration:** Tor bridges (unlisted entry nodes) help against censorship; don't help against global adversaries

**Use for privacy suite:**
- RPC call privacy for Solana: `torsocks solana transfer ...`
- API requests from autonomous agents when anonymity matters
- Git repository access without revealing IP

**Onion services (.onion):** Both sender and receiver are anonymous. Used for: hidden services, SecureDrop (journalism), privacy-preserving APIs.

---

## Mixnets

> *"A technique based on public key cryptography is presented that allows an electronic mail system to hide who a participant communicates with as well as the content of the communication — in spite of an unsecured underlying telecommunication system."*
> — David Chaum, "Untraceable Electronic Mail, Return Addresses, and Digital Pseudonyms" (1981), *Communications of the ACM 24(2)*

**Concept (Chaum, 1981):** Messages are batched, encrypted in layers, and shuffled. Even a global adversary observing all traffic cannot link input messages to output messages.

**Chaum Mixnet:**
```
Alice  ──→┐                      ┌──→ Bob
           │  Mix (batch+shuffle) │
Carol ──→┤  (Re-encrypt all)    ├──→ Dave
           │  Output in random    │
Eve   ──→┘  order               └──→ Frank
```

**vs. Tor:**
- Mixnet: stronger anonymity (batch + delay defeats traffic analysis); higher latency
- Tor: lower latency (streaming); vulnerable to traffic analysis by global adversary

**Production mixnets:**
- `Nym` (NymTech): production mixnet with nym tokens; application SDK available
- `Loopix` / `Sphinx`: academic state-of-the-art mixnet protocol
- `Katzenpost`: Panoramix successor; research-grade

**Relevant to:** High-sensitivity agent communications (inter-agent messaging in multi-agent fleets); low-bandwidth channel metadata hiding (cover traffic + mixnet for the submission layer).

---

## Forward Secrecy Reference

**Why it matters:** If an attacker records encrypted traffic today and obtains your long-term key later, they can decrypt all past traffic — unless forward secrecy is used.

**Ephemeral key exchange:** Generate a fresh DH key pair per session. Session key derived from ephemeral × peer key. Delete ephemeral key immediately after use — past session keys cannot be derived from long-term keys.

**Implementations:**
```
TLS 1.3:    Mandatory ephemeral DH (ECDHE) — forward secrecy by default
TLS 1.2:    Forward secrecy only with ECDHE or DHE cipher suites
            (NOT RSA key exchange — static RSA doesn't provide FS)
Signal:     X3DH + Double Ratchet → per-message forward secrecy
OTR:        Per-session FS; predecessor to Signal Protocol
Noise Protocol Framework: General-purpose protocol framework with FS patterns
```
---

## References

- Chaum, D. (1981). "Untraceable electronic mail, return addresses, and digital pseudonyms." *Communications of the ACM 24(2).*
- Chaum, D. (1985). "Security without identification." *Communications of the ACM 28(10).*
- Goldberg, I. (2000). "Privacy-enhancing technologies for the Internet." *PhD Thesis, UC Berkeley.*
- Marlinspike, M. & Perrin, T. (2016). "The Double Ratchet algorithm." *signal.org/docs/specifications/doubleratchet.*
- Marlinspike, M. & Perrin, T. (2016). "The X3DH key agreement protocol." *signal.org/docs/specifications/x3dh.*
- Dingledine, R., Mathewson, N. & Syverson, P. (2004). "Tor: The second-generation onion router." *USENIX Security 2004.*
- Piotrowska, A., et al. (2017). "The Loopix anonymity system." *USENIX Security 2017.*

---

## Noise Protocol Framework

**Specification:** Trevor Perrin, "The Noise Protocol Framework" (2018). *noiseprotocol.org/noise.html*

A framework for building cryptographic protocols from composable patterns. Underlies WireGuard, the Signal Protocol's transport layer (Noise_XX), and is increasingly used for IoT and embedded systems.

### Why Noise for constrained / low-bandwidth channels

A common pattern for a constrained channel is a static AES-256-GCM key with a durable nonce pool: confidentiality and replay prevention, but no forward secrecy — if the static key is compromised, all past traffic is decryptable. An ad-hoc ephemeral X25519 handshake is the usual first fix.

The Noise Protocol Framework provides the correctly-specified, battle-hardened version of that fix. A Noise handshake fits into 1-3 short frames (32-96 bytes depending on pattern) and provides mutual authentication, forward secrecy, and break-in recovery — well suited to low-bandwidth or embedded transports.

### Noise Handshake Patterns

Patterns are named by the keys used. Each character represents a message:

```
XX pattern (mutual authentication, both parties unknown):
  → e              (initiator sends ephemeral key)
  ← e, ee, s, es   (responder sends ephemeral + static, mixes DHs)
  → s, se           (initiator sends static, mixes DH)
  [Transport phase: both parties have authenticated session key]
```

**Example — a constrained transport:**

```
Recommended: Noise_XX_25519_AESGCM_SHA256

Rationale:
  - XX: mutual authentication (sender and receiver authenticate each other)
  - 25519: X25519 for all DH operations
  - AESGCM: transport encryption (compatible with existing AES-256-GCM layer)
  - SHA256: hash function

Handshake size: 3 messages
  Message 1: 32 bytes (initiator ephemeral key)
  Message 2: 96 bytes (responder ephemeral + static + auth tag)
  Message 3: 64 bytes (initiator static + auth tag)
  Total: 192 bytes — small enough for constrained / low-bandwidth transports

Post-handshake: transport keys derived; AES-256-GCM for all subsequent frames
Forward secrecy: yes — ephemeral keys deleted after handshake
Break-in recovery: yes — new handshake restores security after compromise
```

**NNpsk0 pattern (pre-shared key, simpler):**
```
NNpsk0:
  → psk, e         (initiator sends ephemeral, applies PSK)
  ← e, ee           (responder sends ephemeral, completes DH)
  [Transport phase]

Use when: both parties share a pre-distributed key (a pre-shared-key / one-way delivery mode).
Simpler than XX; does not provide mutual authentication.
Size: 2 messages, ~64 bytes total — fits in a single short frame.
```

### Noise vs. Ad-hoc X25519

| Property | Ad-hoc X25519 | Noise_XX |
|---|---|---|
| Forward secrecy | Yes | Yes |
| Mutual authentication | No | Yes |
| Break-in recovery | No | Yes |
| Protocol specification | Custom | IETF-reviewed |
| Implementation | Custom code | libnoise-c, snow (Rust), noise-protocol (Go) |
| Handshake overhead | ~64 bytes | ~192 bytes |
| Auditability | Low | High |

**Recommendation:** Noise_XX for standard session mode (mutual authentication); Noise_NNpsk0 for a pre-shared-key / anonymous-sender mode.

### Libraries

- `snow` (Rust) — Noise protocol; production-grade; no_std support for embedded
- `noise-protocol` (Go) — Full Noise framework
- `libnoise-c` (C) — Reference C implementation
- `noise-java` (Java/Android)

### Noise for agent / fleet communications

For inter-agent communication in a multi-agent fleet, Noise_IK (initiator knows responder's static key) provides efficient authenticated sessions:

```
IK pattern:
  → e, es, s, ss    (single round-trip — initiator knows responder static key)
  ← e, ee, se       (responder completes)

Advantage: 1 round-trip vs. 2 for XX.
Use case: agents with known, pre-registered identities (fleet members).
```

This gives each agent a verifiable, stable identity (static key registered at fleet initialization) while providing per-session forward secrecy.

### References

- Perrin, T. (2018). "The Noise Protocol Framework, Revision 34." *noiseprotocol.org.*
- Donenfeld, J. (2017). "WireGuard: Next generation kernel network tunnel." *NDSS 2017.* (Noise_IKpsk2 deployment)
- Marlinspike, M. (2016). "Signal Protocol." Uses Noise as transport layer.
