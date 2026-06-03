#!/bin/bash

set -e

echo "🛑 Stopping gen-ai-automation services..."

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT"

docker compose down

echo "✅ Services stopped"