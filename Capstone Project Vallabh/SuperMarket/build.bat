@echo off
echo -------------------------------
echo 🛠️ Building SupermarketApp.exe
echo -------------------------------

REM Optional: Activate virtual environment (uncomment if needed)
REM call venv\Scripts\activate.bat

REM Clean old builds
echo 🧹 Cleaning previous build folders...
rmdir /S /Q build
rmdir /S /Q dist
del /Q *.spec

REM Build using custom spec file
echo 📦 Building using SupermarketApp.spec...
pyinstaller SupermarketApp.spec

REM Check if build succeeded
IF EXIST dist\SupermarketApp.exe (
    echo ✅ Build successful!
    echo Output file: dist\SupermarketApp.exe
) ELSE (
    echo ❌ Build failed. Please check for errors.
)

pause
