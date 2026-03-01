#!/bin/bash
# ============================================
# CCR3 - Chinese Chess Robot
# Setup Script - Cài đặt dependencies
# ============================================

set -e

echo "========================================"
echo "  CCR3 - Chinese Chess Robot Setup"
echo "========================================"

# Check Python version
echo "[1/5] Checking Python version..."
python3 --version || { echo "Python 3 is required!"; exit 1; }

# Create virtual environment
echo "[2/5] Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

# Install Python dependencies
echo "[3/5] Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt 2>/dev/null || echo "requirements.txt not found, skipping..."

# Install PlatformIO (for firmware)
echo "[4/5] Installing PlatformIO..."
pip install platformio

# Download Pikafish (if not exists)
echo "[5/5] Checking chess engine..."
if [ ! -f "software/chess_engine/pikafish" ]; then
    echo "Please download Pikafish manually from: https://github.com/official-pikafish/Pikafish"
    echo "Place the binary at: software/chess_engine/pikafish"
fi

echo ""
echo "========================================"
echo "  Setup complete! Run: ./scripts/run.sh"
echo "========================================"
