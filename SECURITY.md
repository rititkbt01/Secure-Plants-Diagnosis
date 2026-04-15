# Security Policy

## Project Context

This is an **academic capstone project** (BCS Honours, Taylor's University, Group 31).
The security implementations are designed as a proof-of-concept demonstrating
defense-in-depth principles in agricultural AI applications.

## Security Architecture

This project implements the following security layers:

### 1. Transport Security
- **TLS 1.3** encryption for all client-server communication
- Prevents Man-in-the-Middle (MitM) attacks on image data in transit
- Removes legacy cryptographic algorithms present in TLS 1.2

### 2. Authentication
- **JWT (JSON Web Tokens)** — RFC 7519 compliant
- Stateless tokens with configurable expiration (default: 30 minutes access)
- Refresh token mechanism (default: 7 days)
- All API endpoints (except `/health`) require valid JWT

### 3. Input Validation
- **Magic Byte Validation** — verifies file signatures at byte level (not just extension)
- **Payload Size Limit** — maximum 5MB per image upload
- **MIME type verification** — only JPEG and PNG accepted
- Prevents malicious file uploads and injection attacks

### 4. Rate Limiting
- 100 requests per 60-second window per IP
- Protects against Denial-of-Service (DoS) abuse
- Applied at the API gateway middleware layer

### 5. OWASP Top 10 Compliance
The backend is designed with awareness of:
- A01: Broken Access Control → JWT on all endpoints
- A02: Cryptographic Failures → TLS 1.3, strong JWT secrets
- A03: Injection → Parameterized queries (SQLAlchemy ORM)
- A04: Insecure Design → Defense-in-depth architecture
- A05: Security Misconfiguration → `.env` secrets, no debug in production

## Reporting Vulnerabilities (Academic Context)

Since this is an academic project, please report any security concerns to:

**Project Leader:** Ritik Budhathoki  
**Email:** ritik2080-0072@iimscollege.edu.np  
**Supervisor:** Mr. Rabin Thapa — rabin@iimscollege.edu.np

## Important Notes

- This is a **prototype** and is not intended for production agricultural deployment without further security hardening
- **Do not commit** `.env` files, model weights, or dataset files to Git
- All secrets must remain in `.env` (listed in `.gitignore`)
