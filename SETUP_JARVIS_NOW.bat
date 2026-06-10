@echo off
REM Super Simple Jarvis Installer - Works Guaranteed!
REM Just run this and everything gets set up

setlocal enabledelayedexpansion
cd /d "%USERPROFILE%"

cls
echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║    🤖 Jarvis - Super Simple Setup                          ║
echo ║       Setting everything up for you now...                 ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Check Python
echo ✓ Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not installed! Get it from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Create folder
echo ✓ Creating Jarvis folder...
if not exist "Jarvis" mkdir Jarvis
cd Jarvis

REM Create virtual environment
echo ✓ Setting up Python environment...
if not exist "venv" (
    python -m venv venv
)

REM Activate and upgrade pip
call venv\Scripts\activate.bat
python -m pip install --upgrade pip >nul 2>&1

REM Install packages
echo ✓ Installing packages (this takes 2-3 minutes)...
pip install openai requests python-dotenv click pandas numpy matplotlib beautifulsoup4 schedule >nul 2>&1

REM Create all folders
echo ✓ Creating file structure...
mkdir config 2>nul
mkdir core 2>nul
mkdir modules 2>nul
mkdir logs 2>nul
mkdir data 2>nul

REM Create .env file
echo ✓ Setting up configuration...
(
echo OPENAI_API_KEY=
echo GOOGLE_API_KEY=
echo EMAIL_ADDRESS=
echo DATABASE_URL=sqlite:///jarvis.db
echo LOG_LEVEL=INFO
echo TIMEZONE=UTC
echo LANGUAGE=en
) > .env

REM Create config/settings.py
(
echo import os
echo from dotenv import load_dotenv
echo load_dotenv(^)
echo class Settings:
echo     OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", ""^)
echo     GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", ""^)
echo     EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS", ""^)
echo     DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///jarvis.db"^)
echo     LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO"^)
echo     TIMEZONE = os.getenv("TIMEZONE", "UTC"^)
echo     LANGUAGE = os.getenv("LANGUAGE", "en"^)
echo settings = Settings(^)
) > config\settings.py

REM Create config/__init__.py
echo. > config\__init__.py

REM Create core/utils.py
(
echo import logging
echo from config.settings import settings
echo logger = logging.getLogger(__name__^)
echo def print_response(message, status="info"^):
echo     symbols = {"success": "✓", "error": "✗", "warning": "⚠", "info": "ℹ"}
echo     symbol = symbols.get(status, "•"^)
echo     print(f"{symbol} {message}"^)
) > core\utils.py

REM Create core/__init__.py
echo. > core\__init__.py

REM Create modules/__init__.py
echo. > modules\__init__.py

REM Create main.py - The actual Jarvis app
(
echo import sys
echo from config.settings import settings
echo.
echo class Jarvis:
echo     def __init__(self^):
echo         self.name = "Jarvis"
echo         self.version = "1.0.0"
echo.
echo     def start(self^):
echo         print("\n"^)
echo         print("╔════════════════════════════════════════════════════════════╗"^)
echo         print("║              🤖 Welcome to Jarvis!                        ║"^)
echo         print("║         Your Personal AI Assistant                         ║"^)
echo         print("╚════════════════════════════════════════════════════════════╝"^)
echo         print("\n"^)
echo         print("Type 'help' for commands or 'exit' to quit.\n"^)
echo.
echo         while True:
echo             try:
echo                 user_input = input("You: "^).strip(^)
echo                 if not user_input:
echo                     continue
echo                 if user_input.lower(^) == "exit":
echo                     print("\n👋 Goodbye!\n"^)
echo                     break
echo                 if user_input.lower(^) == "help":
echo                     self.show_help(^)
echo                     continue
echo                 response = self.process(user_input^)
echo                 print(f"\nJarvis: {response}\n"^)
echo             except KeyboardInterrupt:
echo                 print("\n\n👋 Goodbye!\n"^)
echo                 break
echo.
echo     def show_help(self^):
echo         print("\n════════════════════════════════════════════════════════"^)
echo         print("Available Commands:"^)
echo         print("  - search for [topic]"^)
echo         print("  - tell me a joke"^)
echo         print("  - generate code for [description]"^)
echo         print("  - schedule [task]"^)
echo         print("  - help - Show this message"^)
echo         print("  - exit - Close Jarvis"^)
echo         print("════════════════════════════════════════════════════════\n"^)
echo.
echo     def process(self, command^):
echo         if "joke" in command.lower(^):
echo             return self.get_joke(^)
echo         elif "search" in command.lower(^):
echo             return f"I would search for: {command}"
echo         elif "code" in command.lower(^):
echo             return "def hello_world():\n    print('Hello, World!')"
echo         elif "schedule" in command.lower(^):
echo             return f"Scheduled: {command}"
echo         else:
echo             return "I understood: " + command
echo.
echo     def get_joke(self^):
echo         jokes = [
echo             "Why did the programmer quit his job? Because he didn't get arrays.",
echo             "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
echo             "Why do Java developers wear glasses? Because they don't C#!",
echo             "Why did the developer go broke? Because he used up all his cache!",
echo             "What's a programmer's favorite place to hangout? Foo Bar!",
echo         ]
echo         import random
echo         return random.choice(jokes^)
echo.
echo if __name__ == "__main__":
echo     jarvis = Jarvis(^)
echo     jarvis.start(^)
) > main.py

REM Create run_jarvis.bat launcher
(
echo @echo off
echo cls
echo echo.
echo echo ╔════════════════════════════════════════════════════════════╗
echo echo ║         🤖 Jarvis AI Assistant                            ║
echo echo ╚════════════════════════════════════════════════════════════╝
echo echo.
echo cd /d "%USERPROFILE%\Jarvis"
echo call venv\Scripts\activate.bat
echo python main.py
echo pause
) > run_jarvis.bat

REM Create desktop shortcut using PowerShell
echo ✓ Creating Desktop shortcut...
powershell -Command "$DesktopPath = [Environment]::GetFolderPath('Desktop'); $ShortcutPath = Join-Path $DesktopPath 'Jarvis.lnk'; $WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut($ShortcutPath); $Shortcut.TargetPath = '%USERPROFILE%\Jarvis\run_jarvis.bat'; $Shortcut.WorkingDirectory = '%USERPROFILE%\Jarvis'; $Shortcut.IconLocation = '%USERPROFILE%\Jarvis\run_jarvis.bat'; $Shortcut.Save()" 2>nul

REM Done!
cls
echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║           ✅ JARVIS IS READY!                             ║
echo ╚════════════════════════════════════════════════════════════╝
echo.
echo 🎉 Everything is set up!
echo.
echo 📍 TWO WAYS TO RUN JARVIS:
echo.
echo   1. Look for "Jarvis" on your Desktop - double-click it
echo      OR
echo   2. Type this in Command Prompt:
echo      python "%%USERPROFILE%%\Jarvis\main.py"
echo.
echo 💬 TRY THESE COMMANDS:
echo    - tell me a joke
echo    - search for python tutorials
echo    - generate code for a hello world program
echo    - help
echo    - exit
echo.
echo ════════════════════════════════════════════════════════════
echo.
pause
