# Database Schema — PostgreSQL

## Overview

PostgreSQL 15 is used for:
1. **User management** (authentication)
2. **Treatment protocols** (deterministic rule engine data)
3. **Diagnosis history** (audit trail per user)

---

## Tables

### `users`
Stores registered users with hashed passwords.

```sql
CREATE TABLE users (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username      VARCHAR(50)  UNIQUE NOT NULL,
    email         VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,          -- bcrypt hashed
    is_active     BOOLEAN DEFAULT TRUE,
    created_at    TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at    TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

---

### `treatment_protocols`
Pre-populated table of expert-verified treatments (FAO-based).
This is the core of the deterministic rule engine — READ ONLY at runtime.

```sql
CREATE TABLE treatment_protocols (
    id                  SERIAL PRIMARY KEY,
    disease_class       VARCHAR(100) UNIQUE NOT NULL,  -- e.g. 'tomato_early_blight'
    disease_name        VARCHAR(200) NOT NULL,
    crop                VARCHAR(50)  NOT NULL,          -- Tomato | Potato | Bell Pepper
    is_healthy          BOOLEAN DEFAULT FALSE,
    chemical_control    TEXT,
    cultural_control    TEXT,
    preventive_measures TEXT,
    safety_note         TEXT,
    source              VARCHAR(500),
    created_at          TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

---

### `diagnosis_history`
Audit trail of all diagnoses performed by each user.

```sql
CREATE TABLE diagnosis_history (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id         UUID REFERENCES users(id) ON DELETE CASCADE,
    disease_class   VARCHAR(100),
    disease_name    VARCHAR(200),
    confidence      FLOAT,
    image_hash      VARCHAR(64),    -- SHA-256 of uploaded image (not the image itself)
    inference_ms    INTEGER,
    created_at      TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

---

## ER Diagram (Text)

```
users                   diagnosis_history           treatment_protocols
──────────────          ──────────────────          ───────────────────
id (PK)         1──∞    id (PK)                     id (PK)
username                user_id (FK → users.id)     disease_class (UNIQUE)
email                   disease_class ──────────∞── disease_name
password_hash           confidence                  crop
is_active               image_hash                  chemical_control
created_at              inference_ms                cultural_control
                        created_at                  preventive_measures
                                                    safety_note
                                                    source
```

---

## Seeding Treatment Data

The `treatment_protocols` table is pre-populated from:
`backend/app/database/seed_data/treatment_protocols.json`

Run seed script during first deployment:
```bash
cd backend
python -m app.database.seed
```

---

## Indexing Strategy

```sql
-- Fast lookup by disease class (used by rule engine on every diagnosis)
CREATE INDEX idx_treatment_disease_class ON treatment_protocols(disease_class);

-- Fast user history lookup
CREATE INDEX idx_diagnosis_user_id ON diagnosis_history(user_id);
CREATE INDEX idx_diagnosis_created_at ON diagnosis_history(created_at);
```
