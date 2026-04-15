.PHONY: help setup run-backend run-mobile test lint clean docker-up docker-down

# ═══════════════════════════════════════════════════════════
#  Secure-Plants_Diagnosis — Makefile
#  Quick commands for development tasks
#  Usage: make <command>
# ═══════════════════════════════════════════════════════════

help:  ## Show this help message
	@echo ""
	@echo "Secure-Plants_Diagnosis — Available Commands"
	@echo "============================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-25s\033[0m %s\n", $$1, $$2}'
	@echo ""

# ── Setup ─────────────────────────────────────────────────────
setup:  ## Install all dependencies (backend + ML)
	@echo "Setting up backend..."
	cd backend && pip install -r requirements.txt
	@echo "Setting up ML..."
	cd ml && pip install -r requirements.txt
	@echo "Copying .env.example to .env (if not exists)..."
	cp -n .env.example .env || true
	@echo "✅ Setup complete. Edit .env with your credentials."

setup-mobile:  ## Install Flutter dependencies
	cd mobile && flutter pub get
	@echo "✅ Flutter dependencies installed."

# ── Run ───────────────────────────────────────────────────────
run-backend:  ## Start FastAPI backend (dev mode)
	cd backend && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

run-mobile:  ## Run Flutter app on connected device
	cd mobile && flutter run

run-mobile-web:  ## Run Flutter app in browser
	cd mobile && flutter run -d chrome

# ── Testing ───────────────────────────────────────────────────
test:  ## Run all tests (backend + ML)
	@echo "Running backend tests..."
	cd backend && pytest tests/ -v --tb=short
	@echo "Running ML tests..."
	cd ml && pytest tests/ -v --tb=short

test-backend:  ## Run backend tests only
	cd backend && pytest tests/ -v

test-ml:  ## Run ML tests only
	cd ml && pytest tests/ -v

test-mobile:  ## Run Flutter widget tests
	cd mobile && flutter test

# ── Linting ───────────────────────────────────────────────────
lint:  ## Lint Python code (flake8) + Dart (flutter analyze)
	@echo "Linting Python..."
	flake8 backend/app/ ml/src/ --max-line-length=88
	@echo "Linting Dart..."
	cd mobile && flutter analyze

lint-python:  ## Lint Python only
	flake8 backend/app/ ml/src/ --max-line-length=88

lint-dart:  ## Lint Dart only
	cd mobile && flutter analyze

# ── Docker ────────────────────────────────────────────────────
docker-up:  ## Start all services with Docker Compose
	docker-compose up --build

docker-down:  ## Stop all Docker services
	docker-compose down

docker-logs:  ## View backend logs
	docker-compose logs -f backend

# ── ML Training ───────────────────────────────────────────────
train-teacher:  ## Train ResNet-50 teacher model
	cd ml && python scripts/train_teacher.py

train-student:  ## Train DeiT-Tiny student (knowledge distillation)
	cd ml && python scripts/train_student.py

evaluate:  ## Evaluate model on test set
	cd ml && python scripts/evaluate.py

# ── Clean ─────────────────────────────────────────────────────
clean:  ## Remove Python cache files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@echo "✅ Cache cleaned."
