# API Design — REST Endpoints

Base URL: `https://your-domain.com/api/v1`  
Documentation (auto-generated): `http://localhost:8000/docs` (Swagger UI)

---

## Authentication

All endpoints except `/health` and `/auth/login` require:
```
Authorization: Bearer <JWT_ACCESS_TOKEN>
```

---

## Endpoints

### 🔐 Authentication

#### POST `/auth/register`
Register a new user account.

**Request Body:**
```json
{
  "username": "farmer_john",
  "email": "john@example.com",
  "password": "securePassword123"
}
```
**Response `201`:**
```json
{
  "message": "User registered successfully",
  "user_id": "uuid-here"
}
```

---

#### POST `/auth/login`
Authenticate and receive JWT tokens.

**Request Body:**
```json
{
  "username": "farmer_john",
  "password": "securePassword123"
}
```
**Response `200`:**
```json
{
  "access_token": "eyJhbGci...",
  "refresh_token": "eyJhbGci...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

---

#### POST `/auth/refresh`
Get new access token using refresh token.

**Request Body:**
```json
{
  "refresh_token": "eyJhbGci..."
}
```
**Response `200`:**
```json
{
  "access_token": "eyJhbGci...",
  "token_type": "bearer"
}
```

---

### 🌿 Diagnosis

#### POST `/diagnose`
Upload a leaf image for disease diagnosis.

**Headers:** `Authorization: Bearer <token>`  
**Content-Type:** `multipart/form-data`

**Request:**
```
file: <image file — JPEG or PNG, max 5MB>
```

**Security Checks (server-side):**
1. JWT token validation
2. Magic Byte verification (JPEG: `FF D8 FF`, PNG: `89 50 4E 47`)
3. Payload size check (≤ 5MB)
4. Rate limit check (100 req/60s)

**Response `200`:**
```json
{
  "disease_name": "Tomato Early Blight",
  "confidence": 0.923,
  "crop": "Tomato",
  "disease_class": "early_blight",
  "is_healthy": false,
  "treatment": {
    "chemical_control": "Apply chlorothalonil fungicide (2g/L) every 7-10 days",
    "cultural_control": "Remove infected leaves, improve air circulation",
    "preventive_measures": "Crop rotation, avoid overhead irrigation",
    "safety_note": "Wear protective gear when applying fungicides. Follow FAO safety guidelines.",
    "source": "FAO Plant Production and Protection Guidelines, 2019"
  },
  "inference_time_ms": 847,
  "timestamp": "2026-04-15T10:30:00Z"
}
```

**Error Responses:**
| Code | Reason |
|------|--------|
| `400` | Invalid file type / Magic Byte mismatch |
| `401` | Missing or invalid JWT |
| `413` | Payload too large (>5MB) |
| `422` | Unprocessable entity |
| `429` | Rate limit exceeded |
| `500` | Inference error |

---

### 💊 Treatment

#### GET `/treatment/{disease_class}`
Get treatment for a specific disease (without inference).

**Response `200`:**
```json
{
  "disease_class": "potato_late_blight",
  "disease_name": "Potato Late Blight",
  "treatment": { ... }
}
```

---

### ❤️ Health

#### GET `/health`
Check if the API is running. No authentication required.

**Response `200`:**
```json
{
  "status": "healthy",
  "version": "0.1.0",
  "model_loaded": true,
  "database_connected": true,
  "timestamp": "2026-04-15T10:30:00Z"
}
```

---

## Disease Classes

| ID | Class | Crop |
|----|-------|------|
| 0 | `tomato_bacterial_spot` | Tomato |
| 1 | `tomato_early_blight` | Tomato |
| 2 | `tomato_late_blight` | Tomato |
| 3 | `tomato_leaf_mold` | Tomato |
| 4 | `tomato_septoria_leaf_spot` | Tomato |
| 5 | `tomato_spider_mites` | Tomato |
| 6 | `tomato_target_spot` | Tomato |
| 7 | `tomato_yellow_leaf_curl_virus` | Tomato |
| 8 | `tomato_mosaic_virus` | Tomato |
| 9 | `tomato_healthy` | Tomato |
| 10 | `potato_early_blight` | Potato |
| 11 | `potato_late_blight` | Potato |
| 12 | `potato_healthy` | Potato |
| 13 | `pepper_bacterial_spot` | Bell Pepper |
| 14 | `pepper_healthy` | Bell Pepper |
