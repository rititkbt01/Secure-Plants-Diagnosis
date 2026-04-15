#!/bin/bash
# Start FastAPI backend server
cd "$(dirname "$0")/.."
echo "Starting FastAPI backend on http://localhost:8000..."
echo "API docs: http://localhost:8000/docs"
cd backend
source venv/bin/activate || source venv/Scripts/activate 2>/dev/null || true
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
