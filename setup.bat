@echo off
REM Jarvis Setup Script - Automated installation and configuration (Windows)

setlocal enabledelayedexpansion

cls
echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║         Jarvis AI Assistant - Setup Script (Windows)        ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Check if Python is installed
echo 📋 Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo    Download from: https://www.python.org/downloads/
    echo    Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✓ Python %PYTHON_VERSION% found
echo.

REM Get project directory
set "PROJECT_DIR=%cd%"
echo 📁 Working directory: %PROJECT_DIR%
echo.

REM Step 1: Create virtual environment
echo 📦 Step 1: Creating virtual environment...
if not exist "venv" (
    python -m venv venv
    echo ✓ Virtual environment created
) else (
    echo ✓ Virtual environment already exists
)
echo.

REM Step 2: Activate virtual environment
echo 📦 Step 2: Activating virtual environment...
call venv\Scripts\activate.bat
echo ✓ Virtual environment activated
echo.

REM Step 3: Upgrade pip
echo 📦 Step 3: Upgrading pip...
python -m pip install --upgrade pip setuptools wheel >nul 2>&1
echo ✓ pip upgraded
echo.

REM Step 4: Install dependencies
echo 📦 Step 4: Installing dependencies...
pip install -r requirements.txt
echo ✓ Dependencies installed
echo.

REM Step 5: Setup .env file
echo 📦 Step 5: Setting up configuration...
if not exist ".env" (
    copy .env.example .env
    echo ✓ .env file created from template
    echo    ⚠️  Edit .env file with your API keys
) else (
    echo ✓ .env file already exists
)
echo.

REM Step 6: Create necessary directories
echo 📦 Step 6: Creating directories...
if not exist "logs" mkdir logs
if not exist "data" mkdir data
if not exist "cache" mkdir cache
echo ✓ Directories created
echo.

cls
echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║              ✅ Setup Complete!                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.
echo 📝 NEXT STEPS:
echo.
echo 1. CONFIGURE API KEYS (Optional but recommended):
echo    - Open .env file with Notepad
echo    - Add your API keys for OpenAI, Google, etc.
echo.
echo 2. RUN JARVIS:
echo    - Run: python main.py
echo.
echo 3. TRY THESE COMMANDS:
echo    - 'help' - Show all commands
echo    - 'search for python tutorials'
echo    - 'generate a function that sorts a list'
echo    - 'schedule a task for tomorrow'
echo.
echo Virtual environment is already activated!
echo.
pause
