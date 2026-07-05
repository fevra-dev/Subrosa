# Regex Patterns Reference

Canonical patterns for entity detection. Use as a reference during structured data or code redaction passes.

---

## Personal Identifiers

```
# Email
[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}

# Phone (North American + international)
(\+?1[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}
\+\d{1,3}[\s-]?\d{1,4}[\s-]?\d{1,4}[\s-]?\d{1,9}

# SSN / SIN (Canada)
\b\d{3}[-\s]?\d{2}[-\s]?\d{4}\b   # SSN
\b\d{3}[-\s]?\d{3}[-\s]?\d{3}\b   # SIN

# IP Address (v4)
\b(?:\d{1,3}\.){3}\d{1,3}\b

# IP Address (v6)
([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}

# MAC Address
([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}
```

---

## Financial

```
# Credit card (Visa, MC, Amex, Discover)
\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12})\b
# With separators:
\b(?:\d{4}[-\s]?){3}\d{4}\b

# CVV
\b[0-9]{3,4}\b  # Only meaningful in context of card data

# IBAN
[A-Z]{2}\d{2}[A-Z0-9]{4}\d{7}([A-Z0-9]?){0,16}
```

---

## Credentials & Secrets

```
# Generic API key assignment (Python, JS, env)
(?i)(api_?key|api_?token|secret|access_?key|bearer|auth_?token)\s*[=:]\s*['"]?[\w\-\.]{16,}['"]?

# Common key prefixes
sk-[a-zA-Z0-9]{20,}          # OpenAI / Anthropic style
pk-[a-zA-Z0-9]{20,}
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
