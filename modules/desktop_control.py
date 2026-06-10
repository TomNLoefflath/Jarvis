"""
Jarvis Desktop Control Module
Full control over Windows desktop, files, applications, and system
"""

import os
import subprocess
import shutil
from pathlib import Path
import psutil
import time

class DesktopController:
    """Complete desktop control for Jarvis"""
    
    def __init__(self):
        self.home_dir = Path.home()
        self.desktop_dir = self.home_dir / "Desktop"
    
    # ========== APPLICATION CONTROL ==========
    def open_application(self, app_name):
        """Open any application"""
        try:
            common_apps = {
                "notepad": "notepad.exe",
                "calc": "calc.exe",
                "calculator": "calc.exe",
                "paint": "mspaint.exe",
                "explorer": "explorer.exe",
                "file manager": "explorer.exe",
                "chrome": "chrome.exe",
                "firefox": "firefox.exe",
                "edge": "msedge.exe",
                "word": "winword.exe",
                "excel": "excel.exe",
                "powerpoint": "powerpnt.exe",
                "vlc": "vlc.exe",
                "cmd": "cmd.exe",
                "command prompt": "cmd.exe",
                "powershell": "powershell.exe",
                "settings": "ms-settings:",
                "task manager": "taskmgr.exe",
                "system": "systempropertiesadvanced.exe",
            }
            
            app_lower = app_name.lower()
            
            if app_lower in common_apps:
                os.startfile(common_apps[app_lower])
                return f"✓ Opening {app_name}..."
            else:
                # Try to open directly
                os.startfile(app_name)
                return f"✓ Opening {app_name}..."
        except Exception as e:
            return f"❌ Could not open {app_name}: {str(e)}"
    
    def close_application(self, app_name):
        """Close an application"""
        try:
            os.system(f"taskkill /IM {app_name}.exe /F 2>nul")
            return f"✓ Closed {app_name}"
        except:
            return f"Could not close {app_name}"
    
    # ========== FILE OPERATIONS ==========
    def create_file(self, filename, content=""):
        """Create a file"""
        try:
            file_path = self.desktop_dir / filename
            file_path.write_text(content)
            return f"✓ Created file: {filename} on Desktop"
        except Exception as e:
            return f"❌ Error creating file: {str(e)}"
    
    def delete_file(self, filename):
        """Delete a file"""
        try:
            file_path = self.desktop_dir / filename
            if file_path.exists():
                file_path.unlink()
                return f"✓ Deleted {filename}"
            else:
                return f"❌ File not found: {filename}"
        except Exception as e:
            return f"❌ Error deleting file: {str(e)}"
    
    def list_files(self, directory="Desktop"):
        """List files in a directory"""
        try:
            if directory.lower() == "desktop":
                path = self.desktop_dir
            elif directory.lower() == "documents":
                path = self.home_dir / "Documents"
            elif directory.lower() == "downloads":
                path = self.home_dir / "Downloads"
            else:
                path = Path(directory)
            
            if path.exists():
                files = list(path.iterdir())
                file_list = "\n".join([f"  • {f.name}" for f in files[:20]])
                return f"📁 Files in {directory}:\n{file_list}"
            else:
                return f"❌ Directory not found: {directory}"
        except Exception as e:
            return f"❌ Error listing files: {str(e)}"
    
    # ========== SYSTEM CONTROL ==========
    def shutdown(self):
        """Shutdown the computer"""
        os.system("shutdown /s /t 30 /c 'Jarvis initiating shutdown in 30 seconds. Type shutdown /a to cancel.'")
        return "⚠️  Shutdown initiated in 30 seconds (type 'cancel shutdown' to stop)"
    
    def restart(self):
        """Restart the computer"""
        os.system("shutdown /r /t 30 /c 'Jarvis initiating restart in 30 seconds. Type shutdown /a to cancel.'")
        return "⚠️  Restart initiated in 30 seconds (type 'cancel shutdown' to stop)"
    
    def cancel_shutdown(self):
        """Cancel shutdown/restart"""
        os.system("shutdown /a")
        return "✓ Shutdown cancelled"
    
    def sleep(self):
        """Put computer to sleep"""
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        return "✓ Computer going to sleep..."
    
    def lock_screen(self):
        """Lock the screen"""
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return "✓ Screen locked"
    
    # ========== BROWSER CONTROL ==========
    def open_url(self, url):
        """Open a URL in default browser"""
        try:
            if not url.startswith("http"):
                url = f"https://{url}"
            os.startfile(url)
            return f"✓ Opening {url} in browser..."
        except Exception as e:
            return f"❌ Could not open URL: {str(e)}"
    
    # ========== SCREENSHOT ==========
    def take_screenshot(self):
        """Take a screenshot"""
        try:
            from PIL import ImageGrab
            screenshot = ImageGrab.grab()
            filename = f"screenshot_{int(time.time())}.png"
            filepath = self.desktop_dir / filename
            screenshot.save(filepath)
            return f"✓ Screenshot saved: {filename}"
        except ImportError:
            return "❌ Screenshot feature requires PIL (Pillow)"
        except Exception as e:
            return f"❌ Error taking screenshot: {str(e)}"
    
    # ========== SYSTEM INFO ==========
    def get_system_info(self):
        """Get system information"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            info = f"""
📊 SYSTEM INFORMATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CPU Usage: {cpu_percent}%
Memory: {memory.percent}% ({memory.used // (1024**3)}GB / {memory.total // (1024**3)}GB)
Disk: {disk.percent}% ({disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
            return info
        except Exception as e:
            return f"❌ Error getting system info: {str(e)}"
    
    # ========== RUNNING PROCESSES ==========
    def list_running_processes(self):
        """List running processes"""
        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name']):
                processes.append(proc.info['name'])
            
            # Return top 15 most important
            important = [p for p in processes if any(x in p.lower() for x in ['chrome', 'firefox', 'edge', 'word', 'excel', 'python', 'vlc', 'spotify'])]
            process_list = "\n".join([f"  • {p}" for p in important[:15]])
            return f"🔄 Running Applications:\n{process_list}"
        except Exception as e:
            return f"❌ Error listing processes: {str(e)}"
    
    # ========== VOLUME CONTROL ==========
    def set_volume(self, level):
        """Set system volume (0-100)"""
        try:
            level = max(0, min(100, int(level)))
            os.system(f'powershell -Command "([mediainfo].psbase.basetype.getmember(\"Volume\", [System.Reflection.BindingFlags]::NonPublic).invoke($null,$null)).volume = {level}"')
            return f"✓ Volume set to {level}%"
        except Exception as e:
            return f"❌ Could not set volume: {str(e)}"
    
    # ========== SEARCH FILES ==========
    def search_file(self, filename):
        """Search for a file"""
        try:
            results = []
            for root, dirs, files in os.walk(self.home_dir):
                for file in files:
                    if filename.lower() in file.lower():
                        results.append(os.path.join(root, file))
                        if len(results) >= 10:
                            break
                if len(results) >= 10:
                    break
            
            if results:
                result_list = "\n".join([f"  • {r}" for r in results[:10]])
                return f"🔍 Found {len(results)} files:\n{result_list}"
            else:
                return f"❌ No files found matching: {filename}"
        except Exception as e:
            return f"❌ Error searching: {str(e)}"
    
    # ========== CLIPBOARD ==========
    def copy_to_clipboard(self, text):
        """Copy text to clipboard"""
        try:
            os.system(f'echo {text} | clip')
            return f"✓ Copied to clipboard: {text[:50]}..."
        except Exception as e:
            return f"❌ Error copying: {str(e)}"
    
    def get_desktop_info(self):
        """Get desktop overview"""
        try:
            desktop_items = list(self.desktop_dir.iterdir())
            info = f"""
🖥️  DESKTOP OVERVIEW:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Items on Desktop: {len(desktop_items)}
User: {os.getenv('USERNAME')}
Computer: {os.getenv('COMPUTERNAME')}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
            return info
        except Exception as e:
            return f"❌ Error: {str(e)}"
