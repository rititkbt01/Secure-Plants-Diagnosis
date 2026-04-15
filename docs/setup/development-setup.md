# Development Environment Setup

Complete guide to set up the full development environment for all team members.

---

## Prerequisites

Install the following tools before starting:

| Tool | Version | Download |
|------|---------|----------|
| Python | 3.10+ | https://www.python.org/downloads/ |
| Flutter SDK | 3.x (stable) | https://docs.flutter.dev/get-started/install |
| Git | Latest | https://git-scm.com/ |
| Docker Desktop | Latest | https://www.docker.com/products/docker-desktop/ |
| VS Code | Latest | https://code.visualstudio.com/ |
| PostgreSQL | 15 | https://www.postgresql.org/download/ (or use Docker) |

### VS Code Extensions (Recommended)
- **Python** (Microsoft)
- **Pylance**
- **Flutter**
- **Dart**
- **Docker**
- **GitLens**
- **Prettier**
- **SQLTools + SQLTools PostgreSQL Driver**

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Secure-Plants_Diagnosis.git
cd Secure-Plants_Diagnosis
```

---

## Step 2: Configure Environment Variables

```bash
cp .env.example .env
```

Open `.env` and fill in:
- Database credentials (`DB_USER`, `DB_PASSWORD`, `DB_NAME`)
- JWT secret key (`JWT_SECRET_KEY` — minimum 32 characters)
- Leave other values as default for local development

⚠️ **Never commit your `.env` file**

---

## Step 3: Backend Setup

```bash
cd backend

# Create Python virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run backend server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

✅ Backend running at: http://localhost:8000  
✅ Swagger UI at: http://localhost:8000/docs  
✅ ReDoc at: http://localhost:8000/redoc

---

## Step 4: Database Setup

### Option A — Docker (Recommended)
```bash
# From the project root:
docker-compose up db -d
```

### Option B — Local PostgreSQL
```bash
# Create database
psql -U postgres
CREATE DATABASE plant_diagnosis_db;
CREATE USER plant_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE plant_diagnosis_db TO plant_user;
\q
```

---

## Step 5: Mobile (Flutter) Setup

```bash
cd mobile

# Get Flutter packages
flutter pub get

# Check Flutter setup
flutter doctor

# Run on connected Android device or emulator
flutter run

# Run on iOS simulator (macOS only)
flutter run -d ios

# Run on Chrome (web, for UI development)
flutter run -d chrome
```

---

## Step 6: ML Environment Setup

```bash
cd ml

# Create separate virtual environment for ML
python -m venv ml_venv
source ml_venv/bin/activate   # or ml_venv\Scripts\activate on Windows

# Install ML dependencies
pip install -r requirements.txt
```

For model training, see: [model-training-setup.md](model-training-setup.md)

---

## Step 7: Run Tests

```bash
# Backend tests
cd backend && pytest tests/ -v

# ML tests
cd ml && pytest tests/ -v

# Flutter tests
cd mobile && flutter test
```

---

## Git Workflow Reminder

```bash
# Always start from latest develop
git checkout develop
git pull origin develop

# Create your feature branch
git checkout -b feature/your-task-name

# After work is done
git add .
git commit -m "feat(backend): add magic byte validation"
git push origin feature/your-task-name
# Then open a PR on GitHub → develop
```

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for full branching guide.
