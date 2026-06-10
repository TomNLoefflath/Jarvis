"""
Jarvis Quick Launcher for Windows
Starts Jarvis from the installed location
"""

import sys
import os
import subprocess
from pathlib import Path

def main():
    """Launch Jarvis from Windows installation"""
    
    # Jarvis installation path
    jarvis_path = Path(os.path.expanduser("~")) / "Jarvis"
    
    if not jarvis_path.exists():
        print("❌ Jarvis is not installed yet!")
        print("Please run the JarvisInstaller.exe first")
        input("Press Enter to exit...")
        return
    
    # Path to Python in virtual environment
    venv_python = jarvis_path / "venv" / "Scripts" / "python.exe"
    main_py = jarvis_path / "main.py"
    
    if not venv_python.exists():
        print("❌ Virtual environment not found!")
        print("Please reinstall Jarvis")
        input("Press Enter to exit...")
        return
    
    if not main_py.exists():
        print("❌ Jarvis files not found!")
        print("Please reinstall Jarvis")
        input("Press Enter to exit...")
        return
    
    # Run Jarvis
    print("🚀 Starting Jarvis AI Assistant...")
    print("=" * 60)
    
    try:
        subprocess.run([str(venv_python), str(main_py)], check=True)
    except KeyboardInterrupt:
        print("\n" + "=" * 60)
        print("👋 Jarvis shut down")
    except Exception as e:
        print(f"❌ Error running Jarvis: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
