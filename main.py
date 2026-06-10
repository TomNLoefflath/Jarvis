"""
Jarvis Main Application - SUPREME VERSION
Complete voice control + desktop control + news/weather
"""

import sys
import os
import threading
from pathlib import Path

# Add modules to path
sys.path.insert(0, str(Path(__file__).parent))

from config.settings import settings
from modules.news_weather import NewsProvider, WeatherProvider, InfoProvider
from modules.desktop_control import DesktopController

class Jarvis:
    def __init__(self):
        self.name = "Jarvis"
        self.version = "3.0.0 - SUPREME"
        self.news_provider = NewsProvider()
        self.weather_provider = WeatherProvider()
        self.info_provider = InfoProvider()
        self.desktop = DesktopController()
        self.user_city = "Berlin"
        self.is_running = True
        
    def start(self):
        """Start Jarvis"""
        self.display_welcome()
        self.main_loop()
    
    def display_welcome(self):
        """Show welcome screen"""
        print("\n")
        print("╔════════════════════════════════════════════════════════════╗")
        print("║              🤖 JARVIS 3.0 - SUPREME EDITION              ║")
        print("║        Your Personal AI with Full Desktop Control          ║")
        print("║              Iron Man Style - Iron Suit Ready!             ║")
        print("╚════════════════════════════════════════════════════════════╝")
        print()
        print("✓ Full Desktop Control Enabled")
        print("✓ Voice & Clap Recognition Ready")
        print("✓ Weather & News Available")
        print("✓ Application Launch Control")
        print("✓ System Information Display")
        print()
        print("Type 'help' for all commands or 'exit' to quit")
        print()
    
    def main_loop(self):
        """Main conversation loop"""
        while self.is_running:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                # Process command
                self.process_command(user_input)
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye, Sir!\n")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def process_command(self, command):
        """Process user commands"""
        cmd = command.lower()
        
        # ========== BASIC COMMANDS ==========
        if cmd in ["exit", "quit", "bye", "goodbye"]:
            print("\n👋 Goodbye, Sir!\n")
            self.is_running = False
            return
        
        if cmd == "help":
            self.show_help()
            return
        
        # ========== INFORMATION ==========
        if "weather" in cmd:
            self.show_weather(command)
            return
        
        if "news" in cmd or "headlines" in cmd:
            self.show_news()
            return
        
        if "briefing" in cmd or "update" in cmd:
            self.show_daily_briefing()
            return
        
        # ========== DESKTOP INFO ==========
        if "system" in cmd or "info" in cmd:
            print("\n" + self.desktop.get_system_info())
            return
        
        if "processes" in cmd or "running" in cmd:
            print("\n" + self.desktop.list_running_processes() + "\n")
            return
        
        if "desktop" in cmd and "info" in cmd:
            print("\n" + self.desktop.get_desktop_info())
            return
        
        # ========== FILE OPERATIONS ==========
        if "list files" in cmd or "show files" in cmd:
            if "downloads" in cmd:
                print("\n" + self.desktop.list_files("Downloads") + "\n")
            elif "documents" in cmd:
                print("\n" + self.desktop.list_files("Documents") + "\n")
            else:
                print("\n" + self.desktop.list_files("Desktop") + "\n")
            return
        
        if "search" in cmd and "file" in cmd:
            filename = cmd.replace("search file", "").replace("search for", "").strip()
            print("\n" + self.desktop.search_file(filename) + "\n")
            return
        
        if "create file" in cmd:
            parts = cmd.replace("create file", "").strip().split(" with content ")
            filename = parts[0].strip()
            content = parts[1].strip() if len(parts) > 1 else ""
            print("\n" + self.desktop.create_file(filename, content) + "\n")
            return
        
        if "delete file" in cmd or "remove file" in cmd:
            filename = cmd.replace("delete file", "").replace("remove file", "").strip()
            print("\n" + self.desktop.delete_file(filename) + "\n")
            return
        
        # ========== APPLICATION CONTROL ==========
        if "open" in cmd:
            app = cmd.replace("open", "").strip()
            print("\n" + self.desktop.open_application(app) + "\n")
            return
        
        if "close" in cmd:
            app = cmd.replace("close", "").strip()
            print("\n" + self.desktop.close_application(app) + "\n")
            return
        
        if "launch" in cmd:
            app = cmd.replace("launch", "").strip()
            print("\n" + self.desktop.open_application(app) + "\n")
            return
        
        # ========== SYSTEM CONTROL ==========
        if "shutdown" in cmd:
            if "cancel" in cmd:
                print("\n" + self.desktop.cancel_shutdown() + "\n")
            else:
                print("\n" + self.desktop.shutdown() + "\n")
            return
        
        if "restart" in cmd:
            print("\n" + self.desktop.restart() + "\n")
            return
        
        if "sleep" in cmd or "hibernate" in cmd:
            print("\n" + self.desktop.sleep() + "\n")
            return
        
        if "lock" in cmd or "lock screen" in cmd:
            print("\n" + self.desktop.lock_screen() + "\n")
            return
        
        # ========== BROWSER ==========
        if "open url" in cmd or "go to" in cmd:
            url = cmd.replace("open url", "").replace("go to", "").strip()
            print("\n" + self.desktop.open_url(url) + "\n")
            return
        
        if "google" in cmd or "search web" in cmd:
            query = cmd.replace("google", "").replace("search web", "").replace("for", "").strip()
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            print("\n" + self.desktop.open_url(url) + "\n")
            return
        
        # ========== SCREENSHOT ==========
        if "screenshot" in cmd or "take screenshot" in cmd:
            print("\n" + self.desktop.take_screenshot() + "\n")
            return
        
        # ========== CLIPBOARD ==========
        if "copy" in cmd:
            text = cmd.replace("copy", "").strip()
            print("\n" + self.desktop.copy_to_clipboard(text) + "\n")
            return
        
        # ========== SPECIAL ==========
        if "iron man" in cmd or "theme" in cmd or "suit up" in cmd:
            self.play_iron_man()
            return
        
        if "set city" in cmd:
            self.set_city(command)
            return
        
        # Default
        print(f"\nJarvis: Understood - {command}")
        print("Try: 'open notepad', 'weather', 'news', 'shutdown', 'help'\n")
    
    def show_help(self):
        """Show all available commands"""
        help_text = """
╔════════════════════════════════════════════════════════════╗
║                  🤖 JARVIS COMMAND REFERENCE              ║
╚════════════════════════════════════════════════════════════╝

🌤️  WEATHER & NEWS:
   • weather [city]           - Get weather
   • news                      - Get headlines
   • briefing                  - Weather + News
   • set city [city]           - Set default city

📁 FILE OPERATIONS:
   • list files                - Show Desktop files
   • search file [name]        - Find a file
   • create file [name]        - Create text file
   • delete file [name]        - Delete a file

💻 APPLICATIONS:
   • open [app name]           - Launch application
   • close [app name]          - Close application
   • list files                - Show applications
   • processes                 - Show running apps

🖥️  SYSTEM CONTROL:
   • system info              - CPU, RAM, Disk usage
   • desktop info             - Desktop overview
   • screenshot               - Take screenshot
   • lock                     - Lock screen
   • sleep                    - Put to sleep
   • shutdown                 - Power off (30 sec)
   • restart                  - Reboot system
   • cancel shutdown          - Cancel shutdown

🌐 BROWSER:
   • google [query]           - Search Google
   • open url [url]           - Open website
   • go to [website]          - Open website

🎵 SPECIAL:
   • iron man                 - Play Iron Man theme
   • help                     - Show this help
   • exit                     - Close Jarvis

════════════════════════════════════════════════════════════
"""
        print(help_text)
    
    def show_weather(self, command):
        """Show weather"""
        city = self.user_city
        if len(command.split()) > 1:
            city = " ".join(command.split()[1:])
        
        print()
        weather = self.weather_provider.get_weather(city)
        print(weather)
        print()
    
    def show_news(self):
        """Show news"""
        print("\n📰 TOP NEWS HEADLINES:\n")
        news = self.news_provider.get_top_news(limit=5)
        print(news)
        print()
    
    def show_daily_briefing(self):
        """Show complete daily briefing"""
        print("\n" + "=" * 60)
        briefing = self.info_provider.get_daily_briefing(self.user_city)
        print(briefing)
        print("=" * 60 + "\n")
    
    def set_city(self, command):
        """Set default city"""
        parts = command.lower().split("set city")
        if len(parts) > 1:
            self.user_city = parts[1].strip()
            print(f"\nJarvis: Your city has been set to {self.user_city}\n")
        else:
            print("\nJarvis: Usage - 'set city [city name]'\n")
    
    def play_iron_man(self):
        """Play Iron Man theme"""
        print("\n" + "=" * 60)
        print("🎵 JARVIS INITIALIZING - IRON MAN SUIT UP")
        print("=" * 60)
        print("""
    ██╗██████╗  ██████╗ ██╗   ██╗    ███╗   ███╗ █████╗ ██╗   ██╗
    ██║██╔══██╗██╔═══██╗██║   ██║    ████╗ ████║██╔══██╗██║   ██║
    ██║██████╔╝██║   ██║██║   ██║    ██╔████╔██║███████║██║   ██║
    ██║██╔══██╗██║   ██║╚██╗ ██╔╝    ██║╚██╔╝██║██╔══██║██║   ██║
    ██║██║  ██║╚██████╔╝ ╚████╔╝     ██║ ╚═╝ ██║██║  ██║╚██████╔╝
    ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═══╝      ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝
        
    ♪ ♪ ♪ 🎵 SUIT UP ACTIVATED ♪ ♪ ♪
    
    🔗 Playing: https://www.youtube.com/watch?v=wKCeO_7BJS0
    """)
        print("=" * 60 + "\n")

def main():
    """Main entry point"""
    try:
        jarvis = Jarvis()
        jarvis.start()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
