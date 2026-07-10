# Asset Taxonomy & Mitigation Library

---

## Asset Taxonomy

### T1 — CRITICAL (Irreversible harm on exposure)

| Asset | Why T1 |
|---|---|
| Private keys / seed phrases | Permanent loss of controlled assets |
| Real identity behind pseudonym (if separation is critical) | Once linked, cannot be unlinked |
| Home address (stalking/harassment context) | Physical safety risk |
| Biometric data | Cannot be changed; permanent authentication bypass |
| Unpublished zero-day research | Loss of leverage; enables adversary |
| Client data under NDA/legal duty | Legal liability + relationship destruction |
| Master password / password manager vault | All other credentials cascade |

### T2 — HIGH (Significant harm, recoverable)

| Asset | Why T2 |
|---|---|
| Email account access | Gateway to account recovery on all services |
| Primary financial account access | Financial loss, recoverable via dispute |
| Professional reputation | Damaged but rebuildable |
| Source code / IP (pre-release) | Competitive harm, first-mover advantage lost |
| Social graph / relationship data | Enables social engineering of contacts |
| Phone number | SIM swap vector; MFA bypass |

### T3 — MEDIUM (Meaningful harm, manageable)

| Asset | Why T3 |
|---|---|
| Secondary email addresses | Phishing surface, account correlation |
| Platform account access (non-primary) | Disruption, impersonation risk |
| Internal tool knowledge | Useful to adversary but limited standalone value |
| Work location / employer | Social engineering vector |
| Pseudonymous reputation (non-critical context) | Reputational harm to alt identity |

### T4 — LOW

| Asset | Why T4 |
|---|---|
| General city of residence (already semi-public) | Low precision, limited targeting utility |
| Professional role / title | Often public anyway |
| Platform posting history (non-sensitive) | Correlation value only |

### T5 — INFO (Essentially public)

| Asset | Why T5 |
|---|---|
| Name (if not pseudonymous) | Public by default in most contexts |
| Public GitHub repos | Intentionally public |
| Published work | Intentionally public |

---

## Mitigation Library

Organized by attack vector. Each control tagged with: `[M1/M2/M3]` tier, effort `[LOW/MED/HIGH]`, impact `[LOW/MED/HIGH]`.

---

### Credential & Account Security

| Control | Tier | Effort | Impact | Notes |
|---|---|---|---|---|
| Unique password per service | M1 | LOW | HIGH | Password manager eliminates friction |
| Password manager (Bitwarden, 1Password, KeePassXC) | M1 | LOW | HIGH | Local-first preferred (KeePassXC) |
| Hardware MFA (YubiKey) for T1/T2 accounts | M1 | MED | HIGH | Eliminates SIM swap and phishing-based MFA bypass |
| TOTP (not SMS) MFA on all accounts | M1 | LOW | HIGH | Aegis (Android), Ente Auth or 2FAS (iOS) |
| Remove phone number from accounts where optional | M1 | LOW | MED | Eliminates SIM swap surface |
| Email alias system (SimpleLogin, AnonAddy) | M1 | MED | HIGH | Prevents email enumeration and breach correlation |
| Passkeys where available | M1 | LOW | HIGH | Phishing-resistant by design |
| Monitor HaveIBeenPwned for email addresses | M2 | LOW | MED | Early warning of breach exposure |
| Account recovery codes stored offline | M3 | LOW | HIGH | Offline = not exfiltrable remotely |

---

### Device & Endpoint Security

| Control | Tier | Effort | Impact | Notes |
|---|---|---|---|---|
| Full-disk encryption enabled (FileVault, BitLocker, LUKS) | M1 | LOW | HIGH | Protects against physical access |
| Strong device passcode / PIN (not biometric only) | M1 | LOW | HIGH | Biometric can be compelled; PIN cannot (in many jurisdictions) |
| Automatic screen lock (short timeout) | M1 | LOW | MED | |
| Firmware password (Mac) | M1 | LOW | MED | Prevents boot from external media |
| Keep OS and software updated | M1 | LOW | HIGH | Patches known CVEs |
| Avoid unknown USB devices | M1 | LOW | HIGH | USB HID/BadUSB attacks |
| Review installed browser extensions periodically | M1 | LOW | MED | Extensions have broad access |
| Separate browser profiles for different identity contexts | M1 | LOW | MED | Prevents cross-context fingerprinting |
| Periodic check for stalkerware (if insider threat relevant) | M2 | MED | HIGH | Use trusted tools, not ones suggested by suspected adversary |

---

### Communications Security

| Control | Tier | Effort | Impact | Notes |
|---|---|---|---|---|
| Signal for sensitive communications | M1 | LOW | HIGH | E2E + disappearing messages |
| Disappearing messages enabled by default | M1 | LOW | MED | Limits historical exposure if device compromised |
| Separate email account for sensitive contexts | M1 | MED | MED | Proton Mail, Tuta (formerly Tutanota) for higher sensitivity |
| Avoid SMS for MFA or sensitive content | M1 | LOW | HIGH | SMS is not encrypted and SIM-swappable |
| VPN for untrusted networks | M1 | LOW | MED | Prevents ISP-level traffic analysis; choose carefully |
| Email alias per service/context | M1 | MED | HIGH | Breach isolation + identity separation |
| Audit who has your phone number | M1 | LOW | MED | Reduce SIM swap surface |

---

### Identity & Pseudonym Separation

| Control | Tier | Effort | Impact | Notes |
|---|---|---|---|---|
| Separate devices for separate identities (ideal) | M1 | HIGH | HIGH | Eliminates device fingerprint correlation |
| Separate browser profiles with separate extensions | M1 | LOW | HIGH | Prevents fingerprint bleed |
| Never log into real and pseudonymous accounts simultaneously | M1 | LOW | HIGH | Session / IP correlation |
| Separate email infrastructure per identity | M1 | MED | HIGH | |
| Pseudonym-specific writing style discipline | M1 | MED | HIGH | Avoid vocabulary/phrasing from real-identity writing |
| Pseudonym payment isolation (crypto, privacy-preserving) | M1 | HIGH | HIGH | Payment records break pseudonym separation |
| Audit temporal posting patterns | M1 | LOW | MED | Don't post as pseudonym only during real-identity work hours |
| No shared profile images across identities | M1 | LOW | HIGH | Reverse image search trivially links them |
| Review mutual follower/connection overlap periodically | M2 | LOW | MED | Social graph correlation surface |

---

### Physical Security

| Control | Tier | Effort | Impact | Notes |
|---|---|---|---|---|
| Private home address (avoid on public records) | M1 | MED | HIGH | Use PO box or registered agent for business |
| Remove address from data broker listings | M1 | MED | MED | Tedious but effective; services like DeleteMe automate |
| Vary physical routines | M1 | LOW | MED | Predictable patterns enable physical surveillance |
| Device encryption + wipe capability before border crossings | M1 | MED | HIGH | Travel with clean device; restore from encrypted backup after |
| Be aware of background in photos/videos | M1 | LOW | MED | Identifiable locations, office decor, whiteboard content |
| EXIF stripping before publishing photos | M1 | LOW | HIGH | GPS metadata, device model, timestamp |

---

### Data Minimization

| Control | Tier | Effort | Impact | Notes |
|---|---|---|---|---|
| Audit what data third parties hold about you | M1 | MED | HIGH | You can't be compelled to produce what you don't have; neither can providers |
| Use throwaway emails for low-value signups | M1 | LOW | MED | Reduces breach correlation surface |
| Minimize personal data in public repos / docs | M1 | LOW | HIGH | Invoke `opsec-review` skill before publishing |
| Periodic account audit — delete unused accounts | M1 | MED | MED | Stale accounts = breach surface with no value |
| Local-first storage preference | M1 | MED | HIGH | Cloud storage is subpoenable; local is not (without physical access) |
| Minimize logging in own infrastructure | M1 | MED | MED | You can't produce logs you didn't keep |

---

### Detection & Response

| Control | Tier | Effort | Impact | Notes |
|---|---|---|---|---|
| Login notification alerts on T1/T2 accounts | M2 | LOW | HIGH | Email/push on new login |
| Google Alerts for your name / handles | M2 | LOW | MED | Early warning of doxxing or impersonation |
| Periodic breach check (HaveIBeenPwned) | M2 | LOW | MED | |
| Credit monitoring / freeze (financial adversary context) | M2 | LOW | HIGH | Credit freeze is M1 if financial identity theft is a risk |
| Documented incident response plan | M3 | MED | HIGH | Know what to do before you need to do it |
| Account recovery backup codes stored securely offline | M3 | LOW | HIGH | |
| Pre-designated trusted contact for incident response | M3 | LOW | MED | Someone who can help if you're locked out or incapacitated |
| Regular encrypted backups of critical data | M3 | MED | HIGH | Ransomware and device loss resilience |
