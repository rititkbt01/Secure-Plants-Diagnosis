# Security Architecture — Defense-in-Depth

## Overview

This system implements a **defense-in-depth** security strategy.
Multiple independent security controls are applied at each architectural layer,
so that if one control fails, others remain effective.

---

## Security Layers

```
LAYER 1 — Mobile Client (Flutter)
├── Client-side image validation (format, size, brightness)
├── JWT token stored in secure local storage
├── Image compressed to <300KB before upload
└── HTTPS enforced (no plain HTTP)

LAYER 2 — Transport
└── TLS 1.3 encryption (all traffic encrypted in transit)
    • Stronger cipher suites than TLS 1.2
    • 0-RTT reduced round trips (faster + secure)
    • Removes legacy vulnerable algorithms (RC4, 3DES, MD5)

LAYER 3 — API Gateway (FastAPI)
├── JWT authentication on every protected endpoint
├── Magic Byte validation (byte-level file signature check)
├── Payload size enforcement (max 5MB)
├── Rate limiting (100 requests / 60 seconds per IP)
├── MIME type verification
└── Request/response audit logging

LAYER 4 — Service Layer
├── SQLAlchemy ORM (parameterized queries — prevents SQL injection)
├── No user input passed directly to shell commands
└── Model inference isolated from database operations

LAYER 5 — Data Layer
├── Passwords hashed with bcrypt (cost factor 12)
├── Sensitive env vars stored in .env (never in code)
├── Images never stored (only SHA-256 hash for audit)
└── PostgreSQL: role-based access (app user ≠ admin user)
```

---

## Magic Byte Validation

File extensions can be spoofed (e.g., renaming `malware.exe` to `leaf.jpg`).
Magic Byte validation reads the actual first bytes of the file:

| Format | Magic Bytes (Hex) | Description |
|--------|--------------------|-------------|
| JPEG | `FF D8 FF` | All JPEG/JPG files start with these bytes |
| PNG | `89 50 4E 47 0D 0A 1A 0A` | PNG signature |

Any file that does not match these signatures is **rejected with HTTP 400**,
regardless of its file extension or MIME type header.

---

## JWT Implementation

```
Access Token:
  - Algorithm: HS256
  - Expiry: 30 minutes
  - Payload: { sub: user_id, exp: timestamp, iat: timestamp }

Refresh Token:
  - Algorithm: HS256
  - Expiry: 7 days
  - Used only to obtain new access tokens

Secret Key:
  - Minimum 32 characters
  - Stored in .env (never hardcoded)
  - Different keys for access and refresh tokens recommended
```

---

## Rate Limiting

Applied at the API middleware level:
- **100 requests per 60-second window** per client IP
- Exceeding the limit returns **HTTP 429 Too Many Requests**
- Protects against: credential stuffing, DoS, brute-force attacks

---

## OWASP Top 10 Mapping

| OWASP Risk | Our Mitigation |
|-----------|---------------|
| A01 Broken Access Control | JWT required on all non-public endpoints |
| A02 Cryptographic Failures | TLS 1.3 in transit, bcrypt for passwords, strong JWT secret |
| A03 Injection | SQLAlchemy ORM (parameterized queries), no raw SQL with user input |
| A04 Insecure Design | Defense-in-depth, threat modeling in proposal |
| A05 Security Misconfiguration | `.env` for secrets, debug=False in production, no default passwords |
| A07 Auth Failures | JWT with expiry, bcrypt password hashing |
| A08 Software & Data Integrity | Magic Byte validation prevents malicious file uploads |

---

## Known Limitations (Academic Prototype)

- No HTTPS certificate in local dev (TLS handled at reverse proxy in production)
- No federated learning (data privacy tradeoff documented in proposal)
- No advanced anomaly detection (flagged as future work)
- No WAF (Web Application Firewall) — out of capstone scope
