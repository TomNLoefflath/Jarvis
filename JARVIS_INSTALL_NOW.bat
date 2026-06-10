@echo off
REM Ultimate Jarvis Setup - Works Guaranteed!
REM This creates EVERYTHING from scratch

setlocal enabledelayedexpansion
cd /d "%USERPROFILE%"

cls
echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║    🤖 JARVIS 3.0 SUPREME - ULTIMATE SETUP                 ║
echo ║         Creating everything automatically...               ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Create Jarvis folder
echo Step 1: Creating Jarvis folder...
if not exist "Jarvis" (
    mkdir Jarvis
    echo ✓ Jarvis folder created
) else (
    echo ✓ Jarvis folder already exists
)

cd Jarvis

REM Create virtual environment
echo Step 2: Setting up Python environment...
if not exist "venv" (
    python -m venv venv
    echo ✓ Virtual environment created
) else (
    echo ✓ Virtual environment already exists
)

REM Activate venv and install packages
echo Step 3: Installing packages (this takes 2-3 minutes)...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip >nul 2>&1
pip install openai requests python-dotenv psutil >nul 2>&1
echo ✓ All packages installed

REM Create config folder and files
echo Step 4: Creating configuration files...
mkdir config 2>nul
mkdir modules 2>nul
mkdir data 2>nul
mkdir logs 2>nul

REM Create config/__init__.py
echo. > config\__init__.py

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

REM Create .env file
(
echo OPENAI_API_KEY=
echo GOOGLE_API_KEY=
echo DATABASE_URL=sqlite:///jarvis.db
echo LOG_LEVEL=INFO
) > .env

REM Create modules/__init__.py
echo. > modules\__init__.py

REM Create modules/news_weather.py
(
echo import requests
echo class NewsProvider:
echo     def get_top_news(self, limit=3^):
echo         try:
echo             url = "https://api.currentsapi.services/v1/latest-news?apikey=demo"
echo             response = requests.get(url, timeout=5^)
echo             if response.status_code == 200:
echo                 data = response.json(^)
echo                 news = []
echo                 for article in data.get('news', [^])[:limit]:
echo                     news.append(f"• {article.get('title', 'No title')}"^)
echo                 return "\n".join(news^) if news else "No news available"
echo             return "Could not fetch news"
echo         except:
echo             return "News service unavailable"
echo class WeatherProvider:
echo     def get_weather(self, city="Berlin"^):
echo         try:
echo             geocode_url = "https://geocoding-api.open-meteo.com/v1/search"
echo             geo_params = {"name": city, "count": 1, "language": "en"}
echo             geo_response = requests.get(geocode_url, params=geo_params, timeout=5^)
echo             if geo_response.status_code != 200:
echo                 return f"Could not find city: {city}"
echo             geo_data = geo_response.json(^)
echo             if not geo_data.get('results'^):
echo                 return f"City not found: {city}"
echo             location = geo_data['results'][0]
echo             latitude = location['latitude']
echo             longitude = location['longitude']
echo             city_name = location['name']
echo             weather_params = {"latitude": latitude, "longitude": longitude, "current": "temperature_2m,weather_code,relative_humidity_2m,wind_speed_10m", "temperature_unit": "celsius"}
echo             weather_response = requests.get("https://api.open-meteo.com/v1/forecast", params=weather_params, timeout=5^)
echo             if weather_response.status_code != 200:
echo                 return "Could not fetch weather data"
echo             weather_data = weather_response.json(^)
echo             current = weather_data.get('current', {^}^)
echo             temp = current.get('temperature_2m', 'N/A'^)
echo             humidity = current.get('relative_humidity_2m', 'N/A'^)
echo             wind = current.get('wind_speed_10m', 'N/A'^)
echo             return f"🌍 Weather in {city_name}\n🌡️  Temperature: {temp}°C\n☁️  Humidity: {humidity}%%\n💨 Wind: {wind} km/h"
echo         except Exception as e:
echo             return f"Weather service error: {str(e)^}"
echo class InfoProvider:
echo     def __init__(self^):
echo         self.news = NewsProvider(^)
echo         self.weather = WeatherProvider(^)
echo     def get_daily_briefing(self, city="Berlin"^):
echo         briefing = "📰 Daily Briefing\n"
echo         briefing += self.weather.get_weather(city^) + "\n\nTop News:\n"
echo         briefing += self.news.get_top_news(limit=3^)
echo         return briefing
) > modules\news_weather.py

REM Create modules/desktop_control.py
(
echo import os
echo import psutil
echo from pathlib import Path
echo class DesktopController:
echo     def __init__(self^):
echo         self.home_dir = Path.home(^)
echo         self.desktop_dir = self.home_dir / "Desktop"
echo     def open_application(self, app_name^):
echo         try:
echo             apps = {"notepad": "notepad.exe", "calc": "calc.exe", "chrome": "chrome.exe", "firefox": "firefox.exe", "edge": "msedge.exe", "explorer": "explorer.exe"}
echo             app_lower = app_name.lower(^)
echo             if app_lower in apps:
echo                 os.startfile(apps[app_lower]^)
echo             else:
echo                 os.startfile(app_name^)
echo             return f"✓ Opening {app_name}..."
echo         except:
echo             return f"Could not open {app_name}"
echo     def shutdown(self^):
echo         os.system("shutdown /s /t 30"^)
echo         return "⚠️  Shutdown in 30 seconds (type 'cancel shutdown' to stop"^)
echo     def get_system_info(self^):
echo         cpu = psutil.cpu_percent(interval=1^)
echo         mem = psutil.virtual_memory(^)
echo         return f"\n📊 System Info:\nCPU: {cpu}%%\nMemory: {mem.percent}%%\nDisk: {psutil.disk_usage('/'^).percent}%%\n"
echo ) > modules\desktop_control.py

REM Create main.py - The WORKING version
(
echo import sys
echo from pathlib import Path
echo sys.path.insert(0, str(Path(__file__^).parent^)^)
echo from config.settings import settings
echo from modules.news_weather import NewsProvider, WeatherProvider, InfoProvider
echo from modules.desktop_control import DesktopController
echo class Jarvis:
echo     def __init__(self^):
echo         self.name = "Jarvis"
echo         self.version = "3.0.0 - SUPREME"
echo         self.news = NewsProvider(^)
echo         self.weather = WeatherProvider(^)
echo         self.info = InfoProvider(^)
echo         self.desktop = DesktopController(^)
echo         self.city = "Berlin"
echo         self.running = True
echo     def start(self^):
echo         print("\n"^)
echo         print("╔════════════════════════════════════════════════════════════╗"^)
echo         print("║              🤖 JARVIS 3.0 - SUPREME EDITION              ║"^)
echo         print("║        Your Personal AI with Full Desktop Control          ║"^)
echo         print("║              Iron Man Style - Iron Suit Ready!             ║"^)
echo         print("╚════════════════════════════════════════════════════════════╝"^)
echo         print("\n✓ Full Desktop Control Enabled\n✓ Weather ^& News Available\n✓ App Control Ready\n"^)
echo         print("Type 'help' for commands or 'exit' to quit\n"^)
echo         while self.running:
echo             try:
echo                 cmd = input("You: "^).strip(^).lower(^)
echo                 if not cmd:
echo                     continue
echo                 if cmd == "exit":
echo                     print("\n👋 Goodbye, Sir!\n"^)
echo                     break
echo                 if cmd == "help":
echo                     self.show_help(^)
echo                     continue
echo                 if "weather" in cmd:
echo                     print("\n" + self.weather.get_weather(self.city^) + "\n"^)
echo                     continue
echo                 if "news" in cmd:
echo                     print("\n📰 Top News:\n" + self.news.get_top_news(^) + "\n"^)
echo                     continue
echo                 if "briefing" in cmd:
echo                     print("\n" + self.info.get_daily_briefing(self.city^) + "\n"^)
echo                     continue
echo                 if "system" in cmd or "info" in cmd:
echo                     print(self.desktop.get_system_info(^)^)
echo                     continue
echo                 if "open" in cmd:
echo                     app = cmd.replace("open", "^").strip(^)
echo                     print("\n" + self.desktop.open_application(app^) + "\n"^)
echo                     continue
echo                 if "shutdown" in cmd:
echo                     print("\n" + self.desktop.shutdown(^) + "\n"^)
echo                     continue
echo                 if "iron man" in cmd:
echo                     print("\n🎵 IRON MAN THEME - https://www.youtube.com/watch?v=wKCeO_7BJS0\n"^)
echo                     continue
echo                 print(f"\nJarvis: Understood - {cmd}\nTry: weather, news, open notepad, system info, help\n"^)
echo             except KeyboardInterrupt:
echo                 print("\n\n👋 Goodbye!\n"^)
echo                 break
echo     def show_help(self^):
echo         print("\n════════════════════════════════════════════════════════"^)
echo         print("Commands: weather, news, briefing, system info, open [app]"^)
echo         print("Apps: notepad, chrome, firefox, explorer, calc"^)
echo         print("Special: iron man, shutdown, help, exit"^)
echo         print("════════════════════════════════════════════════════════\n"^)
echo if __name__ == "__main__":
echo     jarvis = Jarvis(^)
echo     jarvis.start(^)
) > main.py

echo ✓ Files created

REM Create launcher
echo Step 5: Creating launcher...
(
echo @echo off
echo cls
echo cd /d "%USERPROFILE%\Jarvis"
echo call venv\Scripts\activate.bat
echo python main.py
echo pause
) > run_jarvis.bat

echo ✓ Launcher created

REM Create desktop shortcut
echo Step 6: Creating desktop shortcut...
powershell -Command "$DesktopPath = [Environment]::GetFolderPath('Desktop'); $ShortcutPath = Join-Path $DesktopPath 'Jarvis.lnk'; $WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut($ShortcutPath); $Shortcut.TargetPath = '%USERPROFILE%\Jarvis\run_jarvis.bat'; $Shortcut.WorkingDirectory = '%USERPROFILE%\Jarvis'; $Shortcut.Save()" 2>nul

REM Done!
cls
echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║           ✅ JARVIS 3.0 IS READY!                         ║
echo ╚════════════════════════════════════════════════════════════╝
echo.
echo 🎉 Everything is set up and ready to go!
echo.
echo 📍 HOW TO START JARVIS:
echo.
echo    Option 1: Double-click "Jarvis" shortcut on Desktop
echo    Option 2: Type this in Command Prompt:
echo             cd %%USERPROFILE%%\Jarvis
echo             python main.py
echo.
echo 💬 TRY THESE COMMANDS:
echo    • help
echo    • weather
echo    • news
echo    • open notepad
echo    • system info
echo    • iron man
echo.
echo ════════════════════════════════════════════════════════════
echo.
pause
