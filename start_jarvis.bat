@echo off
REM One-Click Jarvis Starter for Windows
REM This script starts Jarvis from your Windows installation

setlocal enabledelayedexpansion

cls
echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║         🤖 Jarvis AI Assistant Launcher                    ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Check if Jarvis is installed
set "JARVIS_PATH=%USERPROFILE%\Jarvis"
set "PYTHON_EXE=%JARVIS_PATH%\venv\Scripts\python.exe"
set "MAIN_PY=%JARVIS_PATH%\main.py"

if not exist "%JARVIS_PATH%" (
    echo ❌ Jarvis is not installed yet!
    echo.
    echo Please run the JarvisInstaller.exe first
    echo.
    pause
    exit /b 1
)

if not exist "%PYTHON_EXE%" (
    echo ❌ Virtual environment not found!
    echo Please reinstall Jarvis
    echo.
    pause
    exit /b 1
)

if not exist "%MAIN_PY%" (
    echo ❌ Jarvis files not found!
    echo Please reinstall Jarvis
    echo.
    pause
    exit /b 1
)

echo ✓ Jarvis installation found at: %JARVIS_PATH%
echo.
echo 🚀 Starting Jarvis...
echo ════════════════════════════════════════════════════════════
echo.

REM Run Jarvis
"%PYTHON_EXE%" "%MAIN_PY%"

echo.
echo ════════════════════════════════════════════════════════════
echo 👋 Jarvis has been closed
echo.
pause
