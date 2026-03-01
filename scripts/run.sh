#!/bin/bash
# ============================================
# CCR3 - Chinese Chess Robot
# Run Script - Khởi chạy hệ thống
# ============================================

set -e

echo "========================================"
echo "  CCR3 - Chinese Chess Robot"
echo "  Starting system..."
echo "========================================"

# Activate virtual environment
if [ -d ".venv" ]; then
    source .venv/bin/activate
else
    echo "Virtual environment not found. Run ./scripts/setup.sh first!"
    exit 1
fi

# Run main application
echo "Starting Game Manager..."
python3 software/game_manager/main.py "$@"
