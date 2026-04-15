#!/bin/bash
# Run all tests (backend + ML + Flutter)
cd "$(dirname "$0")/.."
echo "================================================"
echo " Running All Tests"
echo "================================================"

echo ""
echo "→ Backend tests..."
cd backend
pytest tests/ -v --tb=short
cd ..

echo ""
echo "→ ML tests..."
cd ml
pytest tests/ -v --tb=short
cd ..

echo ""
echo "→ Flutter tests..."
cd mobile
flutter test
cd ..

echo ""
echo "================================================"
echo " ✅ All tests complete"
echo "================================================"
