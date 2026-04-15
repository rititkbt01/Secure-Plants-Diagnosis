#!/bin/bash
# ═══════════════════════════════════════════════════════════
# Secure-Plants_Diagnosis — One-Command Dev Setup
# Usage: bash scripts/setup_dev.sh
# ═══════════════════════════════════════════════════════════

set -e  # Exit on error

echo "================================================"
echo " Secure-Plants_Diagnosis — Dev Setup"
echo "================================================"

# Copy .env if not exists
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✅ Created .env from .env.example"
    echo "⚠️  Please fill in your credentials in .env"
else
    echo "✅ .env already exists"
fi

# Backend setup
echo ""
echo "→ Setting up Backend..."
cd backend
python -m venv venv
source venv/bin/activate || source venv/Scripts/activate
pip install -r requirements.txt
echo "✅ Backend dependencies installed"
cd ..

# ML setup
echo ""
echo "→ Setting up ML environment..."
cd ml
python -m venv ml_venv
source ml_venv/bin/activate || source ml_venv/Scripts/activate
pip install -r requirements.txt
echo "✅ ML dependencies installed"
cd ..

echo ""
echo "================================================"
echo " ✅ Setup complete!"
echo " Next steps:"
echo "   1. Edit .env with your DB credentials and JWT secret"
echo "   2. Run: make run-backend"
echo "   3. Run: cd mobile && flutter pub get && flutter run"
echo "   4. See docs/setup/development-setup.md for details"
echo "================================================"
