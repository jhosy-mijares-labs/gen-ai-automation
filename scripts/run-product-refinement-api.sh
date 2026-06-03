#!/bin/bash

set -e

echo "🚀 Starting GenAI Automation API..."

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT"

./venv/bin/python3 -m uvicorn apps.api.main:app --reload