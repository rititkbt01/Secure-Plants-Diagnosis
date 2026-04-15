# Backend — FastAPI

**Owner:** Ritik Budhathoki (Security Lead / Backend)

This folder contains the FastAPI backend for the Secure-Plants_Diagnosis system.

## Responsibilities
- REST API with JWT authentication
- Magic Byte file validation + payload enforcement
- Rate limiting middleware
- DeiT-Tiny model inference service
- Deterministic rule-based treatment engine
- PostgreSQL database integration

## Quick Start
```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

API Docs: http://localhost:8000/docs

## Full Setup Guide
See: [docs/setup/backend-setup.md](../docs/setup/backend-setup.md)
