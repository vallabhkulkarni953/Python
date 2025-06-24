#!/bin/bash

echo "🛠️  Starting build process for SupermarketApp..."

# Activate your virtual environment (optional, if you use one)
# source venv/bin/activate

# Clean previous builds
echo "🧹 Cleaning old builds..."
rm -rf build/ dist/ __pycache__/ *.spec

# Generate new spec file (optional step if you want to rebuild from scratch)
# pyinstaller main.py --name SupermarketApp --icon=assets/app_icon.ico --onefile

# Use existing custom spec file
echo "📦 Building using SupermarketApp.spec..."
pyinstaller SupermarketApp.spec

# Check if build succeeded
if [ -f "dist/SupermarketApp.exe" ]; then
    echo "✅ Build complete! Find your .exe in dist/SupermarketApp.exe"
else
    echo "❌ Build failed. Check error logs above."
fi
