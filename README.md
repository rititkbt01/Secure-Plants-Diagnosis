<div align="center">

# 🌿 Secure-Plants_Diagnosis

### Secure Mobile Application for Real-Time Plant Disease Diagnosis
### Leveraging Vision Transformers and a Deterministic Remedial Engine

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104%2B-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Flutter](https://img.shields.io/badge/Flutter-3.x-02569B?logo=flutter)](https://flutter.dev/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-EE4C2C?logo=pytorch)](https://pytorch.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?logo=postgresql)](https://www.postgresql.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Taylor's University | School of Computer Science | BCS (Honours) | Group 31 | February 2026**

</div>

---

## 📖 Overview

Plant diseases cause **20–40% annual crop yield losses** globally, amounting to **USD 220 billion** in economic damage (FAO, 2019). This project builds a **secure, mobile-first diagnosis system** that:

- 📸 Captures a leaf image via smartphone camera
- 🔐 Securely transmits it over **TLS 1.3** with **JWT authentication**
- 🧠 Classifies the disease using **DeiT-Tiny** trained via **Knowledge Distillation** from ResNet-50
- 💊 Retrieves expert-verified treatment from a **deterministic rule-based engine**
- ⚡ Returns results in **< 3 seconds**

### Supported Crops
| Crop | Classes |
|------|---------|
| 🍅 Tomato | 10 disease/healthy classes |
| 🥔 Potato | 3 disease/healthy classes |
| 🫑 Bell Pepper | 2 disease/healthy classes |

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 1: Mobile Client (Flutter)                               │
│  Camera → Client Validation → Encrypted Transmission           │
└───────────────────────────┬─────────────────────────────────────┘
                            │ TLS 1.3 + JWT
┌───────────────────────────▼─────────────────────────────────────┐
│  LAYER 2: API Gateway (FastAPI)                                 │
│  JWT Auth → Magic Byte Check → Payload Limit → Rate Limiting    │
└───────────────────────────┬─────────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│  LAYER 3: Service Layer                                         │
│  DeiT-Tiny Inference  +  Deterministic Rule Engine             │
└───────────────────────────┬─────────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│  LAYER 4: Data Layer                                            │
│  PostgreSQL (Treatment DB)  +  Model Weights (.pth)            │
└─────────────────────────────────────────────────────────────────┘
```

### 7-Stage Diagnosis Pipeline
```
1. CAPTURE    → Farmer photographs diseased leaf
2. VALIDATE   → Client-side format & size check (Flutter)
3. TRANSMIT   → TLS 1.3 encrypted + JWT token
4. CHECK      → Magic Byte validation + payload size limit
5. INFERENCE  → DeiT-Tiny classifies disease (224×224 px)
6. REMEDIATE  → Rule engine queries PostgreSQL for treatment
7. RESPOND    → JSON: { disease, confidence, treatment }
```

---

## 🛠️ Tech Stack

| Layer | Technology | Justification |
|-------|-----------|---------------|
| Mobile | Flutter (Dart) | Single codebase for Android & iOS |
| Backend | FastAPI (Python) | Async, 2-3× faster than Flask/Django |
| AI Model | DeiT-Tiny + timm | Data-efficient transformer via distillation |
| Teacher Model | ResNet-50 (PyTorch) | CNN teacher for knowledge distillation |
| Database | PostgreSQL 15 | ACID compliance for treatment data integrity |
| Auth | JWT (RFC 7519) | Stateless, mobile-friendly authentication |
| Encryption | TLS 1.3 | Latest standard, faster handshake |
| CI/CD | GitHub Actions | Automated lint + test on push/PR |

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/Secure-Plants_Diagnosis.git
cd Secure-Plants_Diagnosis

# 2. Backend
cd backend && cp ../.env.example .env
pip install -r requirements.txt
uvicorn app.main:app --reload

# 3. Mobile
cd mobile && flutter pub get && flutter run

# 4. Docker (Backend + PostgreSQL)
docker-compose up --build
```

> **Full setup guides:** See [`docs/setup/`](docs/setup/)

---

## 📚 Documentation

| Doc | Link |
|-----|------|
| System Architecture | [docs/architecture/system-architecture.md](docs/architecture/system-architecture.md) |
| API Design | [docs/architecture/api-design.md](docs/architecture/api-design.md) |
| Database Schema | [docs/architecture/database-schema.md](docs/architecture/database-schema.md) |
| Security Architecture | [docs/architecture/security-architecture.md](docs/architecture/security-architecture.md) |
| Development Setup | [docs/setup/development-setup.md](docs/setup/development-setup.md) |
| Model Training (Kaggle) | [docs/setup/model-training-setup.md](docs/setup/model-training-setup.md) |
| Literature Review | [docs/research/literature-summary.md](docs/research/literature-summary.md) |
| Dataset Analysis | [docs/research/dataset-analysis.md](docs/research/dataset-analysis.md) |

---

## 👥 Team — Group 31

| Member | Role | Domain |
|--------|------|--------|
| **Ritik Budhathoki** 👑 | Security Lead / Backend / Project Leader | `backend/` |
| **Yashraj Shrestha** | AI Lead | `ml/` — DeiT + Distillation |
| **Rishi Kumar Kushwaha** | Data Engineering Lead | `ml/src/data/` |
| **Jeshik Neupane** | App Development Lead | `mobile/` |
| **Rishav Dhakal** | Model Optimization Lead | `ml/src/evaluation/` |

**Supervisor:** Mr. Rabin Thapa | `rabin@iimscollege.edu.np`

---

## 📊 Performance Targets

| Metric | Target |
|--------|--------|
| Classification Accuracy | ≥ 85% |
| Precision (per class avg) | ≥ 0.85 |
| Recall (per class avg) | ≥ 0.85 |
| F1-Score | ≥ 0.88 |
| End-to-End Latency | < 3 seconds |

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">
Made with ❤️ by Group 31 | Taylor's University | School of Computer Science | 2026
</div>
