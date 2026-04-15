# System Architecture

## Overview

The system follows a **4-layer architecture** with a strict separation of concerns.
Security controls are applied at every layer.

---

## Layer Diagram

```
┌──────────────────────────────────────────────────────────┐
│  LAYER 1 — Mobile Client (Flutter)                       │
│                                                          │
│  • Cross-platform: Android + iOS                         │
│  • Camera capture → client-side validation               │
│  • JWT token storage (secure local storage)              │
│  • Image compression (<300KB before upload)              │
│  • Result display: disease name, confidence, treatment   │
└───────────────────────┬──────────────────────────────────┘
                        │ HTTPS / TLS 1.3 + JWT Bearer Token
┌───────────────────────▼──────────────────────────────────┐
│  LAYER 2 — API Gateway (FastAPI)                         │
│                                                          │
│  • JWT authentication middleware                         │
│  • Magic Byte file validation                            │
│  • Payload size enforcement (max 5MB)                    │
│  • Rate limiting (100 req/60s per IP)                    │
│  • Request/response logging                              │
│  • OpenAPI / Swagger UI auto-documentation               │
└───────────────────────┬──────────────────────────────────┘
                        │ Validated, authenticated requests
┌───────────────────────▼──────────────────────────────────┐
│  LAYER 3 — Service Layer                                 │
│                                                          │
│  ┌──────────────────┐    ┌──────────────────────────┐   │
│  │ Inference Service │    │ Remediation Engine       │   │
│  │                  │    │                          │   │
│  │ • Image resize   │    │ • Disease → Treatment    │   │
│  │   (224×224)      │    │   lookup (deterministic) │   │
│  │ • Normalize      │    │ • FAO-verified protocols │   │
│  │ • DeiT-Tiny      │    │ • No AI generation       │   │
│  │   forward pass   │    │   (no hallucination risk)│   │
│  │ • Softmax        │    │                          │   │
│  │   confidence     │    └──────────────────────────┘   │
│  └──────────────────┘                                   │
└───────────────────────┬──────────────────────────────────┘
                        │
┌───────────────────────▼──────────────────────────────────┐
│  LAYER 4 — Data Layer                                    │
│                                                          │
│  • PostgreSQL: treatment_protocols table                 │
│  • PostgreSQL: users table (hashed passwords)            │
│  • PostgreSQL: diagnosis_history table                   │
│  • DeiT-Tiny model weights (.pth file)                   │
└──────────────────────────────────────────────────────────┘
```

---

## 7-Stage Diagnosis Pipeline

| Stage | Where | Action |
|-------|-------|--------|
| 1. CAPTURE | Mobile (Flutter) | Farmer photographs diseased leaf with camera |
| 2. VALIDATE | Mobile (Flutter) | Check file format, image brightness, size |
| 3. TRANSMIT | Transport | TLS 1.3 encrypted HTTPS POST with JWT Bearer token |
| 4. CHECK | Backend (FastAPI) | Magic Byte validation + payload size limit |
| 5. INFERENCE | Backend (Service) | Resize to 224×224 → DeiT-Tiny forward pass → softmax |
| 6. REMEDIATE | Backend (Service) | Query PostgreSQL with disease class → expert treatment |
| 7. RESPOND | Backend → Mobile | JSON response: disease name, confidence %, treatment |

---

## Key Design Decisions

### Why DeiT-Tiny over standard ViT?
Standard Vision Transformers require ~14M training images (full ImageNet).
PlantVillage has only 54,306 images. DeiT uses knowledge distillation from
ResNet-50 to achieve transformer-grade accuracy on small datasets.

### Why Deterministic Rule Engine over AI generation?
AI-generated treatment recommendations (like Plantix) risk hallucinated or
agronomically unsafe advice. Our rule engine maps each classified disease to
expert-verified FAO treatment protocols — deterministic, auditable, safe.

### Why cloud-based inference over edge/on-device?
- Allows instant model updates without app store resubmission
- Keeps mobile app lightweight
- Consistent hardware for reproducible latency measurements
- Easier to enforce security controls server-side

---

## Technology Justification Summary

| Technology | Alternative Considered | Why We Chose It |
|-----------|----------------------|-----------------|
| DeiT-Tiny | ResNet-50, EfficientNet | Knowledge distillation — transformer accuracy on small dataset |
| FastAPI | Flask, Django | 2-3× faster throughput, async, auto OpenAPI docs |
| Flutter | React Native, Native | Single codebase Android + iOS, ~50% dev time saving |
| PostgreSQL | MySQL, MongoDB | ACID compliance critical for treatment data integrity |
| JWT | Session-based auth | Stateless, mobile-friendly, no server-side session storage |
| TLS 1.3 | TLS 1.2 | Faster handshake, stronger cipher suites, no legacy algorithms |
