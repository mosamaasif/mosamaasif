#!/bin/bash
# Quick start script for setting up the terminal-styled GitHub profile

set -e

echo "🚀 Terminal-Styled GitHub Profile - Quick Start"
echo "================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.11+ first."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✓ Python version: $PYTHON_VERSION"

# Check if CONFIG.yaml exists
if [ ! -f "CONFIG.yaml" ]; then
    echo "❌ CONFIG.yaml not found. Please create it first."
    echo "   See SETUP.md for instructions."
    exit 1
fi

echo "✓ CONFIG.yaml found"

# Check if portrait exists
if [ ! -f "assets/portrait.png" ]; then
    echo "⚠️  Portrait image not found at assets/portrait.png"
    read -p "Create a placeholder portrait? (y/N): " CREATE_PLACEHOLDER

    if [ "$CREATE_PLACEHOLDER" = "y" ] || [ "$CREATE_PLACEHOLDER" = "Y" ]; then
        echo "📸 Creating placeholder portrait..."
        python3 create_placeholder.py
    else
        echo "ℹ️  Add your portrait to assets/portrait.png before generating SVGs"
    fi
else
    echo "✓ Portrait image found"
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo ""
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "📦 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo "✓ Dependencies installed"

# Generate SVG files
echo ""
echo "🎨 Generating SVG files..."
cd scripts
python3 generate_svg.py
cd ..

# Check if SVG files were created
if [ -f "assets/dark_mode.svg" ] && [ -f "assets/light_mode.svg" ]; then
    echo ""
    echo "✨ Success! SVG files generated:"
    echo "   - assets/dark_mode.svg"
    echo "   - assets/light_mode.svg"
    echo ""
    echo "📖 Next steps:"
    echo "   1. Open the SVG files in a browser to preview"
    echo "   2. Push to GitHub: git add . && git commit -m 'Initial commit' && git push"
    echo "   3. Set up GitHub Actions (see SETUP.md)"
    echo ""
    echo "💡 To update: run this script again or use 'cd scripts && python3 generate_svg.py'"
else
    echo ""
    echo "❌ SVG generation failed. Check the error messages above."
    exit 1
fi

# Deactivate virtual environment
deactivate
