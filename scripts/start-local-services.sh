#!/bin/bash

set -e

echo "🚀 Starting gen-ai-automation project..."

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT"

echo "📁 Project path: $PROJECT_ROOT"

if [ ! -d "venv" ]; then
  echo "🐍 Creating Python virtual environment..."
  python3 -m venv venv
else
  echo "🐍 Virtual environment already exists"
fi

echo "📦 Installing/updating Python dependencies..."
./venv/bin/python3 -m pip install --upgrade pip
./venv/bin/python3 -m pip install -r requirements.txt

echo "🎭 Installing Playwright browsers..."
./venv/bin/python3 -m playwright install

echo "🐳 Starting Docker services..."
docker compose up -d

echo "✅ Project is ready!"
echo "🌐 n8n: http://localhost:5678"