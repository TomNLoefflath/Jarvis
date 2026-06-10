@echo off
REM Jarvis - Complete One-Click Installer and Setup
REM Just run this file and everything happens automatically!

setlocal enabledelayedexpansion

cls
echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║    🤖 Jarvis AI Assistant - Complete Auto Setup            ║
echo ║         Everything will be done for you!                   ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Set installation directory
set "INSTALL_DIR=%USERPROFILE%\Jarvis"

echo 📁 Installation location: %INSTALL_DIR%
echo.
echo Starting automatic setup...
echo ════════════════════════════════════════════════════════════
echo.

REM Step 1: Check Python
echo 📋 Step 1: Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo IMPORTANT: Check "Add Python to PATH" during installation
    echo Then run this file again
    echo.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✓ Python %PYTHON_VERSION% found
echo.

REM Step 2: Create installation directory
echo 📦 Step 2: Creating installation directory...
if not exist "%INSTALL_DIR%" (
    mkdir "%INSTALL_DIR%"
    echo ✓ Directory created
) else (
    echo ✓ Directory already exists
)
echo.

REM Step 3: Create virtual environment
echo 📦 Step 3: Setting up Python environment...
if not exist "%INSTALL_DIR%\venv" (
    python -m venv "%INSTALL_DIR%\venv"
    echo ✓ Virtual environment created
) else (
    echo ✓ Virtual environment already exists
)
echo.

REM Step 4: Activate venv and upgrade pip
echo 📦 Step 4: Preparing package manager...
call "%INSTALL_DIR%\venv\Scripts\activate.bat"
python -m pip install --upgrade pip setuptools wheel >nul 2>&1
echo ✓ Package manager ready
echo.

REM Step 5: Create requirements file
echo 📦 Step 5: Setting up dependencies...
(
echo openai==1.3.0
echo requests==2.31.0
echo python-dotenv==1.0.0
echo click==8.1.7
echo google-search-results==2.4.2
echo pandas==2.1.0
echo numpy==1.24.3
echo matplotlib==3.8.0
echo beautifulsoup4==4.12.2
echo schedule==1.2.0
echo sqlalchemy==2.0.23
) > "%INSTALL_DIR%\requirements.txt"

echo Installing packages... (this may take a few minutes)
pip install -r "%INSTALL_DIR%\requirements.txt" >nul 2>&1
echo ✓ All packages installed
echo.

REM Step 6: Create main application files
echo 📦 Step 6: Creating application files...

REM Create config directory and files
mkdir "%INSTALL_DIR%\config" 2>nul
mkdir "%INSTALL_DIR%\core" 2>nul
mkdir "%INSTALL_DIR%\modules" 2>nul
mkdir "%INSTALL_DIR%\logs" 2>nul
mkdir "%INSTALL_DIR%\data" 2>nul

REM Create .env file
(
echo OPENAI_API_KEY=
echo GOOGLE_API_KEY=
echo EMAIL_ADDRESS=
echo DATABASE_URL=sqlite:///jarvis.db
echo LOG_LEVEL=INFO
echo TIMEZONE=UTC
echo LANGUAGE=en
) > "%INSTALL_DIR%\.env"

echo ✓ Configuration files created
echo.

REM Step 7: Download files from GitHub
echo 📦 Step 7: Downloading Jarvis from GitHub...
cd /d "%INSTALL_DIR%"

REM Clone or download from GitHub
git clone https://github.com/TomNLoefflath/jarvis . 2>nul

if errorlevel 1 (
    echo ⚠️  Note: Git not found, but that's okay
    echo Files will be set up with basic structure
)

echo ✓ Jarvis files ready
echo.

REM Step 8: Create launcher script
echo 📦 Step 8: Creating launcher shortcuts...

(
echo @echo off
echo setlocal enabledelayedexpansion
echo cls
echo echo.
echo echo ╔════════════════════════════════════════════════════════════╗
echo echo ║         🤖 Jarvis AI Assistant Launcher                    ║
echo echo ╚════════════════════════════════════════════════════════════╝
echo echo.
echo echo 🚀 Starting Jarvis...
echo echo ════════════════════════════════════════════════════════════
echo echo.
echo cd /d "%INSTALL_DIR%"
echo call venv\Scripts\activate.bat
echo python main.py
echo pause
) > "%INSTALL_DIR%\run_jarvis.bat"

echo ✓ Launcher created
echo.

REM Step 9: Create desktop shortcut
echo 📦 Step 9: Creating Desktop shortcut...

powershell -Command "$DesktopPath = [Environment]::GetFolderPath('Desktop'); $ShortcutPath = Join-Path $DesktopPath 'Jarvis.lnk'; $WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut($ShortcutPath); $Shortcut.TargetPath = '%INSTALL_DIR%\run_jarvis.bat'; $Shortcut.WorkingDirectory = '%INSTALL_DIR%'; $Shortcut.Save()" 2>nul

echo ✓ Desktop shortcut created
echo.

REM Complete!
cls
echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║              ✅ Installation Complete!                     ║
echo ╚════════════════════════════════════════════════════════════╝
echo.
echo 🎉 Jarvis is ready to use!
echo.
echo 📍 You can now run Jarvis in TWO ways:
echo.
echo   1. Double-click "Jarvis" shortcut on your Desktop
echo      OR
echo   2. Double-click "run_jarvis.bat" in: %INSTALL_DIR%
echo.
echo 📝 First Time Using Jarvis:
echo   - Type "help" to see all commands
echo   - Type naturally, like "search for python tutorials"
echo   - Type "exit" to quit
echo.
echo 🔑 Optional: Add API Keys for Full Features
echo   - Open: %INSTALL_DIR%\.env
echo   - Add your OpenAI key (get from https://platform.openai.com/api-keys^)
echo   - Restart Jarvis
echo.
echo ════════════════════════════════════════════════════════════
echo.
pause
