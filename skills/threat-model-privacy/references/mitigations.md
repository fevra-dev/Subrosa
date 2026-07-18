# Mitigation Library

Full control library for Phase 4 of the threat model workflow. Organized by attack vector category. Each control tagged with tier (M1/M2/M3), effort (LOW/MED/HIGH), and impact (LOW/MED/HIGH).

This file expands on the asset-taxonomy.md mitigation section with deeper implementation guidance and additional controls.

---

## Credential & Account Security

| ID | Control | Tier | Effort | Impact | Notes |
|---|---|---|---|---|---|
| C-01 | Unique password per service via password manager | M1 | LOW | HIGH | KeePassXC (local-first) or Bitwarden (cloud sync) |
| C-02 | Hardware MFA (YubiKey 5 series) for T1/T2 accounts | M1 | MED | HIGH | Eliminates SIM swap + phishing-based MFA bypass entirely |
| C-03 | TOTP MFA (Aegis on Android, Ente Auth or 2FAS on iOS) | M1 | LOW | HIGH | Not SMS — TOTP resists SIM swap. (Raivo is no longer recommendable post-2023 acquisition) |
| C-04 | Remove phone number from all accounts where optional | M1 | LOW | HIGH | Eliminates SIM swap surface entirely |
| C-05 | Email alias system (SimpleLogin, AnonAddy) | M1 | MED | HIGH | One alias per service; breach isolation; enumeration prevention |
| C-06 | Passkeys where available (FIDO2/WebAuthn) | M1 | LOW | HIGH | Phishing-resistant by cryptographic design |
| C-07 | Account recovery codes stored offline (printed, locked) | M3 | LOW | HIGH | Last-resort recovery without digital exposure |
| C-08 | HaveIBeenPwned monitoring for all email addresses | M2 | LOW | MED | Early warning of breach; trigger password rotation |
| C-09 | Credit freeze at all three bureaus (Equifax, Experian, TransUnion) | M1 | LOW | HIGH | Blocks new credit without unfreeze; financial identity theft prevention |
| C-10 | Separate email account for high-sensitivity contexts | M1 | MED | MED | Proton Mail or Tuta (formerly Tutanota); encrypted at rest; zero-knowledge |

---

## Device & Endpoint Security

| ID | Control | Tier | Effort | Impact | Notes |
|---|---|---|---|---|---|
| D-01 | Full-disk encryption (FileVault/macOS, BitLocker/Win, LUKS/Linux) | M1 | LOW | HIGH | Protects against physical device access |
| D-02 | Strong PIN/passphrase (not biometric alone) | M1 | LOW | HIGH | Biometric can be compelled; PIN cannot in many jurisdictions |
| D-03 | Automatic screen lock (≤2 min timeout) | M1 | LOW | MED | Physical access window minimization |
| D-04 | Firmware password / Secure Boot | M1 | LOW | MED | Prevents boot from external media |
| D-05 | OS and software current (patched) | M1 | LOW | HIGH | Closes known CVEs; highest-ROI security action |
| D-06 | No unknown USB devices | M1 | LOW | HIGH | USB HID attacks (Rubber Ducky, OMG Cable, O.MG) |
| D-07 | Browser extension audit (quarterly) | M1 | LOW | MED | Extensions have broad read/write access to all pages |
| D-08 | Separate browser profiles per identity context | M1 | LOW | MED | Prevents cross-context fingerprinting and cookie sharing |
| D-09 | Periodic stalkerware check (if insider threat relevant) | M2 | MED | HIGH | Tools: Certo (iOS), Malwarebytes, manual review of installed apps |
| D-10 | Travel device (clean device for border crossings) | M1 | HIGH | HIGH | Restore from encrypted backup after crossing |
| D-11 | Remote wipe capability enabled | M3 | LOW | MED | Last resort if device stolen; minimize before crossing borders |

---

## Communications Security

| ID | Control | Tier | Effort | Impact | Notes |
|---|---|---|---|---|---|
| CM-01 | Signal for sensitive communications (disappearing messages on) | M1 | LOW | HIGH | E2E + forward secrecy + disappearing; best consumer option |
| CM-02 | Disappearing messages as default in all Signal conversations | M1 | LOW | MED | Limits historical exposure if device compromised |
| CM-03 | Avoid SMS for any sensitive content or MFA | M1 | LOW | HIGH | SMS: unencrypted, SIM-swappable, carrier-accessible |
| CM-04 | VPN on untrusted networks (Mullvad, ProtonVPN — no-log providers) | M1 | LOW | MED | ISP-level traffic analysis prevention; choose audited no-log provider |
| CM-05 | Tor Browser for high-sensitivity web browsing | M1 | LOW | HIGH | IP address anonymization; resist fingerprinting; higher latency |
| CM-06 | PGP/GPG for sensitive email (when Signal not possible) | M1 | MED | MED | E2E for email; metadata (to/from/subject) still visible |
| CM-07 | Separate phone number (Google Voice, MySudo) for non-sensitive use | M1 | MED | MED | Reduces exposure of primary number |
| CM-08 | Secure email (Proton Mail) for sensitive correspondence | M1 | LOW | MED | Zero-knowledge; encrypted at rest; Swiss jurisdiction |
| CM-09 | Verify Signal Safety Numbers on first contact | M1 | LOW | HIGH | Prevents MITM; takes 30 seconds |

---

## Identity & Pseudonym Separation

| ID | Control | Tier | Effort | Impact | Notes |
|---|---|---|---|---|---|
| I-01 | Separate devices per identity (ideal) | M1 | HIGH | HIGH | Eliminates device fingerprint correlation entirely |
| I-02 | Separate browser profiles with separate extensions + fingerprint | M1 | LOW | HIGH | Firefox Multi-Account Containers; Brave per-profile isolation |
| I-03 | Never log into real + pseudonymous accounts simultaneously | M1 | LOW | HIGH | Session / IP correlation via advertising networks |
| I-04 | Separate email infrastructure per identity | M1 | MED | HIGH | Proton Mail aliases or separate accounts |
| I-05 | Deliberate writing style variation (see opsec-review stylometry) | M1 | MED | HIGH | Function word frequencies; punctuation habits; sentence length |
| I-06 | Payment isolation (crypto, privacy-preserving methods) | M1 | HIGH | HIGH | Payment records break pseudonym separation definitively |
| I-07 | Post timing variation (not at same time as real-identity posting) | M1 | LOW | MED | Temporal correlation attack mitigation |
| I-08 | No shared profile images across identities | M1 | LOW | HIGH | Reverse image search trivially links them |
| I-09 | Separate git config per repository (per-repo override) | M1 | LOW | HIGH | `git config user.email pseudonym@proton.me` before first commit |
| I-10 | Separate GPG/SSH keys per identity | M1 | MED | HIGH | Key reuse links identities cryptographically |
| I-11 | Mutual follower/connection audit (quarterly) | M2 | LOW | MED | Social graph overlap is a deanonymization vector |
| I-12 | `did:key` DID for cryptographic identity (no registry footprint) | M1 | MED | HIGH | Selective disclosure without linkable identity |

---

## Physical Security

| ID | Control | Tier | Effort | Impact | Notes |
|---|---|---|---|---|---|
| P-01 | Private home address (PO box or registered agent for business) | M1 | MED | HIGH | Remove from public records; data broker opt-outs |
| P-02 | Data broker removal — **California: use DROP** (one-stop statutory deletion, live Jan 1 2026; brokers must honor from Aug 1 2026); elsewhere DeleteMe/Kanary or manual | M1 | LOW–MED | MED–HIGH | DROP reaches all *registered* CA data brokers in one request — a statutory upgrade over per-broker opt-outs (Spokeo, WhitePages, BeenVerified, Radaris). Non-CA residents still need per-broker removal |
| P-03 | Vary physical routines (commute, gym, coffee) | M1 | LOW | MED | Predictable patterns enable physical surveillance |
| P-04 | EXIF stripping before publishing any photo | M1 | LOW | HIGH | GPS coordinates, device model, timestamp — all in EXIF |
| P-05 | Background audit in video/photos before publishing | M1 | LOW | MED | Whiteboards, screens, office decor, skyline — all identifiable |
| P-06 | Border crossing: use travel device or full wipe | M1 | MED | HIGH | CBP has broad authority to search devices at US border |
| P-07 | Biometric refusal at border (where legally possible) | M1 | LOW | MED | US citizens can refuse device search (5th Amendment debate ongoing) |
| P-08 | Conference badge awareness | M1 | LOW | MED | Badge photos post online; lanyard details; badge scanner logs |
| P-09 | Event photography opt-out | M1 | LOW | LOW | Request removal from event photos; attend without badge where possible |

---

## Data Minimization & Retention

| ID | Control | Tier | Effort | Impact | Notes |
|---|---|---|---|---|---|
| DM-01 | Cloud storage minimization (local-first preference) | M1 | MED | HIGH | Cloud = subpoenable; local = requires physical access |
| DM-02 | Throwaway emails for low-value signups | M1 | LOW | MED | SimpleLogin aliases; reduces breach correlation surface |
| DM-03 | Periodic account audit and deletion (annually) | M1 | MED | MED | Stale accounts = breach surface with no active value |
| DM-04 | Pre-publish OPSEC review (invoke opsec-review skill) | M1 | LOW | HIGH | Inferential leakage audit before any external publication |
| DM-05 | Pre-publish PII redaction (invoke redact skill) | M1 | LOW | HIGH | Strip explicit identifiers before sharing documents/code |
| DM-06 | Pre-publish metadata hygiene (invoke metadata-hygiene skill) | M1 | LOW | HIGH | Strip EXIF, document properties, git identity |
| DM-07 | Encrypted backup of critical data (offline copy) | M3 | MED | HIGH | Protects against ransomware and device loss |
| DM-08 | Minimize PI in public repos (invoke data-minimization skill) | M1 | LOW | HIGH | Schema audit before committing data models |

---

## Detection & Monitoring

| ID | Control | Tier | Effort | Impact | Notes |
|---|---|---|---|---|---|
| DT-01 | Login notification alerts on all T1/T2 accounts | M2 | LOW | HIGH | Email or push on new device / new location login |
| DT-02 | Google Alerts for name, handles, and company | M2 | LOW | MED | Early warning of doxxing, impersonation, breach mention |
| DT-03 | Periodic HaveIBeenPwned check | M2 | LOW | MED | Both email and phone number |
| DT-04 | Credit monitoring (Experian, CreditKarma) | M2 | LOW | MED | Catch new credit applications under your name |
| DT-05 | Dark web monitoring (Identity Guard, Aura) | M2 | LOW | MED | Monitors dark web marketplaces for credential sale |
| DT-06 | DNS monitoring (your domains) | M2 | LOW | MED | Alert on domain hijacking or DNS changes |
| DT-07 | Social media impersonation scan (quarterly) | M2 | LOW | MED | Search for accounts impersonating you on each platform |

---

## Incident Response

| ID | Control | Tier | Effort | Impact | Notes |
|---|---|---|---|---|---|
| IR-01 | Documented incident response plan | M3 | MED | HIGH | Know what to do before you need to do it |
| IR-02 | Pre-designated trusted contact for incident response | M3 | LOW | MED | Someone who can act on your behalf if you're unavailable |
| IR-03 | Offline copy of account recovery codes | M3 | LOW | HIGH | Fireproof safe; encrypted USB |
| IR-04 | Credential rotation plan (know which accounts use which passwords) | M3 | LOW | HIGH | Password manager makes this feasible |
| IR-05 | Legal contacts (lawyer, privacy advocate) pre-established | M3 | LOW | MED | Don't find a lawyer during an incident |
| IR-06 | Platform-specific escalation contacts | M3 | LOW | LOW | Twitter Trust & Safety, Facebook law enforcement portal, etc. |

---

## Supply Chain & MCP Security (Archetype 8 specific)

| ID | Control | Tier | Effort | Impact | Notes |
|---|---|---|---|---|---|
| SC-01 | MCP server vetting before integration | M1 | MED | HIGH | Treat as data processor; require documented data handling |
| SC-02 | Dependency version pinning + lockfile | M1 | LOW | HIGH | `npm ci` not `npm install`; `cargo.lock` committed |
| SC-03 | Dependency checksum verification | M1 | LOW | HIGH | `npm audit`; `pip-audit`; Dependabot alerts |
| SC-04 | Tool call parameter minimization | M1 | LOW | MED | Pass only what the tool requires; not full context |
| SC-05 | MCP server network egress monitoring | M2 | MED | HIGH | Flag unexpected outbound connections from tool processes |
| SC-06 | Separate agent identity for tool calls | M1 | MED | MED | Tool-call identity ≠ user-facing agent identity |
| SC-07 | Never pass credentials in tool call parameters | M1 | LOW | HIGH | Use server-side credential injection; vault integration |
| SC-08 | Memory provenance tagging (source of each entry) | M1 | HIGH | HIGH | Tag: user / system / environmental; restrict cross-context retrieval |

---

## Nation-State / PQC-Specific Controls

| ID | Control | Tier | Effort | Impact | Notes |
|---|---|---|---|---|---|
| NS-01 | Hybrid key exchange (X25519 + Kyber) for long-term sensitive data | M1 | HIGH | HIGH | HNDL threat mitigation; NIST FIPS 203 (ML-KEM) |
| NS-02 | Air-gapped device for highest-sensitivity key material | M1 | HIGH | HIGH | Never networked; physically isolated; manual data transfer |
| NS-03 | TAILS OS for high-risk sessions (journalist, activist, researcher) | M1 | LOW | HIGH | Amnesiac OS; leaves no trace; routes all traffic through Tor |
| NS-04 | Faraday bag for device transport in high-threat environments | M1 | LOW | MED | Prevents remote activation; useful at hostile conferences |
| NS-05 | Physical security key for device unlock (not PIN) | M1 | MED | HIGH | YubiKey for device login; no PIN interception possible |
