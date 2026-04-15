# Backend Setup Guide (FastAPI)

**Owner:** Ritik Budhathoki (Security Lead / Backend)

---

## Project Structure

```
backend/
├── app/
│   ├── main.py              ← FastAPI entry point
│   ├── config.py            ← App settings from .env
│   ├── api/
│   │   ├── routes/          ← Endpoint handlers
│   │   ├── dependencies.py  ← Shared dependencies (DB, auth)
│   │   └── middleware.py    ← Rate limiting, logging
│   ├── core/
│   │   ├── security.py      ← JWT creation/verification
│   │   └── validation.py    ← Magic Byte + payload checks
│   ├── models/
│   │   ├── database.py      ← SQLAlchemy ORM models
│   │   └── schemas.py       ← Pydantic request/response schemas
│   ├── services/
│   │   ├── inference_service.py    ← DeiT model loading + inference
│   │   ├── remediation_engine.py   ← Treatment lookup
│   │   └── image_processing.py     ← Image preprocessing
│   └── database/
│       ├── connection.py    ← DB session management
│       └── seed_data/       ← Treatment protocols JSON
└── tests/                   ← pytest test suite
```

---

## Installation

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Running the API

```bash
# Development (auto-reload on file changes)
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Production
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

---

## API Documentation

Once running, visit:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc
- **OpenAPI JSON:** http://localhost:8000/openapi.json

---

## Running Tests

```bash
cd backend
pytest tests/ -v --tb=short
pytest tests/ -v --cov=app    # With coverage report
```

---

## Environment Variables Required

See `.env.example` for full list. Minimum required:
```
DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
JWT_SECRET_KEY
MODEL_PATH
```
