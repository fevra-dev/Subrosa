# Regex Patterns Reference

Canonical patterns for entity detection. Use as a reference during structured data or code redaction passes.

---

## Personal Identifiers

```
# Email (domain part must allow subdomains, or the match truncates
# at the first label and the redaction span is wrong)
[\w.+-]+@[\w-]+(\.[\w-]+)*\.[a-zA-Z]{2,}

# Phone (North American + international) — word-bounded, or any long
# digit run produces false partial matches
\b(\+?1[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}\b
\+\d{1,3}[\s-]?\d{1,4}[\s-]?\d{1,4}[\s-]?\d{1,9}

# SSN / SIN (Canada)
\b\d{3}[-\s]?\d{2}[-\s]?\d{4}\b   # SSN
\b\d{3}[-\s]?\d{3}[-\s]?\d{3}\b   # SIN

# IP Address (v4)
\b(?:\d{1,3}\.){3}\d{1,3}\b

# IP Address (v6) — full form
([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}
# IPv6 compressed (::) forms — the pattern above misses them, and most
# real-world IPv6 is written compressed. Heuristic (over-matches; score MEDIUM):
\b(?:[0-9a-fA-F]{1,4}:){1,7}:(?:[0-9a-fA-F]{1,4}(?::[0-9a-fA-F]{1,4}){0,6})?\b

# MAC Address
([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}
```

---

## Financial

```
# Credit card (Visa, MC, Amex, Discover)
\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12})\b
# With separators (16-digit 4-4-4-4 layout; Amex separates 4-6-5 — catch via
# the unseparated pattern or a dedicated \b\d{4}[-\s]\d{6}[-\s]\d{5}\b):
\b(?:\d{4}[-\s]?){3}\d{4}\b

# CVV
\b[0-9]{3,4}\b  # Only meaningful in context of card data

# IBAN (generic: 2-letter country + 2 check digits + 11-30 alphanumeric BBAN;
# BBAN structure is country-specific — validate per-country if precision matters)
\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b
```

---

## Credentials & Secrets

```
# Generic API key assignment (Python, JS, env)
(?i)(api_?key|api_?token|secret|access_?key|bearer|auth_?token)\s*[=:]\s*['"]?[\w\-\.]{16,}['"]?

# Common key prefixes (charset must include - and _ : Anthropic keys are
# sk-ant-api03-... — a hyphenless charset fails on them)
sk-[a-zA-Z0-9_-]{16,}        # OpenAI / Anthropic style
pk-[a-zA-Z0-9_-]{16,}
ghp_[a-zA-Z0-9]{36}          # GitHub PAT
xoxb-[0-9]+-[a-zA-Z0-9-]+    # Slack bot token
ya29\.[a-zA-Z0-9._-]{50,}    # Google OAuth

# PEM private key
-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----

# BIP39 mnemonic (12 or 24 words from wordlist — heuristic)
# Look for sequences of 12 or 24 lowercase dictionary words separated by spaces
```

---

## Crypto / Web3

See `crypto-patterns.md` for full detail.

```
# Ethereum address
0x[a-fA-F0-9]{40}

# Bitcoin P2PKH
[13][a-km-zA-HJ-NP-Z1-9]{25,34}

# Bitcoin Bech32
bc1[ac-hj-np-z02-9]{6,87}

# Solana (base58, 32–44 chars)
[1-9A-HJ-NP-Za-km-z]{32,44}
# Note: HIGH false-positive rate — always require contextual confirmation
```

---

## Notes on Confidence Scoring

- **HIGH**: Pattern matches AND surrounding context confirms (e.g., `email:`, `wallet:`, `Bearer `)
- **MEDIUM**: Pattern matches but context is ambiguous
- **LOW**: Heuristic match only — surface for user review, do not auto-redact
