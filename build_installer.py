"""
Jarvis Installer for Windows
This creates a standalone executable installer that handles everything.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def install_pyinstaller():
    """Install PyInstaller if not already installed."""
    try:
        import PyInstaller
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def create_installer_script():
    """Create the installer script that will become an .exe"""
    script_content = '''
import os
import sys
import subprocess
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
import time

class JarvisInstaller:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jarvis AI Assistant - Windows Installer")
        self.root.geometry("600x400")
        self.root.configure(bg="#1e1e1e")
        
        self.install_path = Path(os.path.expanduser("~")) / "Jarvis"
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the installer UI"""
        # Title
        title = tk.Label(
            self.root,
            text="🤖 Jarvis AI Assistant",
            font=("Arial", 24, "bold"),
            bg="#1e1e1e",
            fg="#00ff00"
        )
        title.pack(pady=20)
        
        # Subtitle
        subtitle = tk.Label(
            self.root,
            text="Your Personal AI Assistant",
            font=("Arial", 12),
            bg="#1e1e1e",
            fg="#888888"
        )
        subtitle.pack(pady=5)
        
        # Status label
        self.status_label = tk.Label(
            self.root,
            text="Ready to install",
            font=("Arial", 10),
            bg="#1e1e1e",
            fg="#00ff00"
        )
        self.status_label.pack(pady=20)
        
        # Progress bar (simple)
        self.progress_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 9),
            bg="#1e1e1e",
            fg="#ffff00"
        )
        self.progress_label.pack(pady=10)
        
        # Install button
        self.install_btn = tk.Button(
            self.root,
            text="Install Jarvis",
            command=self.start_installation,
            font=("Arial", 12, "bold"),
            bg="#00ff00",
            fg="#000000",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.install_btn.pack(pady=20)
        
        # Info label
        info = tk.Label(
            self.root,
            text=f"Installation location: {self.install_path}",
            font=("Arial", 8),
            bg="#1e1e1e",
            fg="#666666"
        )
        info.pack(pady=10)
        
        self.root.mainloop()
    
    def update_status(self, message):
        """Update status message"""
        self.status_label.config(text=message)
        self.root.update()
    
    def update_progress(self, message):
        """Update progress message"""
        self.progress_label.config(text=message)
        self.root.update()
    
    def start_installation(self):
        """Start the installation process"""
        self.install_btn.config(state="disabled")
        
        try:
            self.update_status("Checking Python installation...")
            self.update_progress("Step 1/5")
            self.check_python()
            
            self.update_status("Creating installation directory...")
            self.update_progress("Step 2/5")
            self.create_directories()
            
            self.update_status("Downloading Jarvis files...")
            self.update_progress("Step 3/5")
            self.download_files()
            
            self.update_status("Installing dependencies...")
            self.update_progress("Step 4/5")
            self.install_dependencies()
            
            self.update_status("Setting up configuration...")
            self.update_progress("Step 5/5")
            self.setup_config()
            
            self.update_status("✓ Installation complete!")
            messagebox.showinfo(
                "Success",
                f"Jarvis has been installed successfully!\\n\\n"
                f"Installation path: {self.install_path}\\n\\n"
                f"To run Jarvis:\\n"
                f"1. Open Command Prompt\\n"
                f"2. Type: cd {self.install_path}\\n"
                f"3. Type: python main.py\\n\\n"
                f"Enjoy your AI Assistant!"
            )
            self.root.quit()
            
        except Exception as e:
            messagebox.showerror("Installation Error", f"Error during installation:\\n{str(e)}")
            self.install_btn.config(state="normal")
    
    def check_python(self):
        """Verify Python is installed"""
        try:
            result = subprocess.run(
                [sys.executable, "--version"],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                raise Exception("Python not found")
        except Exception as e:
            raise Exception(
                f"Python is not installed or not in PATH.\\n"
                f"Download from: https://www.python.org/downloads/\\n"
                f"Make sure to check 'Add Python to PATH' during installation."
            )
    
    def create_directories(self):
        """Create installation directories"""
        self.install_path.mkdir(parents=True, exist_ok=True)
        (self.install_path / "venv").mkdir(exist_ok=True)
        (self.install_path / "modules").mkdir(exist_ok=True)
        (self.install_path / "config").mkdir(exist_ok=True)
        (self.install_path / "core").mkdir(exist_ok=True)
        (self.install_path / "logs").mkdir(exist_ok=True)
        (self.install_path / "data").mkdir(exist_ok=True)
    
    def download_files(self):
        """Download Jarvis files from GitHub"""
        import urllib.request
        import json
        
        repo_url = "https://api.github.com/repos/TomNLoefflath/jarvis/contents"
        
        # Create virtual environment
        subprocess.run(
            [sys.executable, "-m", "venv", str(self.install_path / "venv")],
            check=True
        )
    
    def install_dependencies(self):
        """Install Python dependencies"""
        pip_path = self.install_path / "venv" / "Scripts" / "pip.exe"
        
        # Create a basic requirements.txt
        req_file = self.install_path / "requirements.txt"
        requirements = """openai==1.3.0
requests==2.31.0
python-dotenv==1.0.0
click==8.1.7
google-search-results==2.4.2
pandas==2.1.0
numpy==1.24.3
matplotlib==3.8.0
beautifulsoup4==4.12.2
schedule==1.2.0
"""
        req_file.write_text(requirements)
        
        subprocess.run(
            [str(pip_path), "install", "-r", str(req_file)],
            check=True
        )
    
    def setup_config(self):
        """Setup configuration files"""
        # Create .env file
        env_file = self.install_path / ".env"
        env_content = """OPENAI_API_KEY=
GOOGLE_API_KEY=
EMAIL_ADDRESS=
DATABASE_URL=sqlite:///jarvis.db
LOG_LEVEL=INFO
TIMEZONE=UTC
LANGUAGE=en
"""
        env_file.write_text(env_content)

if __name__ == "__main__":
    installer = JarvisInstaller()
'''
    
    return script_content

def create_launcher_script():
    """Create a launcher script that starts Jarvis"""
    script_content = '''
import sys
import os
import subprocess
from pathlib import Path

# Add Jarvis to path
jarvis_path = Path(os.path.expanduser("~")) / "Jarvis"
sys.path.insert(0, str(jarvis_path))

# Activate virtual environment and run Jarvis
venv_python = jarvis_path / "venv" / "Scripts" / "python.exe"

if venv_python.exists():
    main_py = jarvis_path / "main.py"
    subprocess.run([str(venv_python), str(main_py)])
else:
    print("Jarvis not properly installed. Please run the installer first.")
'''
    return script_content

def main():
    """Main function to create the installer"""
    print("Creating Jarvis Windows Installer...")
    
    # Install PyInstaller
    install_pyinstaller()
    
    # Create temporary directory for build files
    build_dir = Path("jarvis_installer_build")
    build_dir.mkdir(exist_ok=True)
    
    # Write installer script
    installer_script = build_dir / "jarvis_installer.py"
    installer_script.write_text(create_installer_script())
    
    # Write launcher script
    launcher_script = build_dir / "jarvis_launcher.py"
    launcher_script.write_text(create_launcher_script())
    
    print("Building executable...")
    
    # Build the installer EXE
    subprocess.run([
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--windowed",
        "--icon=ICON.ico" if Path("ICON.ico").exists() else "",
        "--name=JarvisInstaller",
        "--distpath=./dist",
        "--buildpath=./build",
        "--specpath=./",
        str(installer_script)
    ], check=True)
    
    print("✓ Installer created: dist/JarvisInstaller.exe")
    print("✓ Users can now double-click to install Jarvis!")

if __name__ == "__main__":
    main()
'''
    return script_content

# Write the installer creator
if __name__ == "__main__":
    installer_creator = create_installer_script()
    print(installer_creator)
