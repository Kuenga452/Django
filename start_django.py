#!/usr/bin/env python3
"""
Django Development Server Startup Script
This script will start your Django development server with the correct settings.
"""

import os
import subprocess
import sys

def main():
    print("🚀 Starting Django Development Server...")
    print("=" * 50)
    
    # Change to the correct directory
    project_dir = r"C:\Users\user\Desktop\PRG(TPelden)\Django\firstDjango"
    os.chdir(project_dir)
    
    print(f"📁 Working directory: {os.getcwd()}")
    print("")
    
    # Command to run Django server
    command = ["pipenv", "run", "python", "myFirstProject/manage.py", "runserver"]
    
    print("🔧 Running command:", " ".join(command))
    print("")
    print("🌐 Your Django app will be available at: http://127.0.0.1:8000/")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 50)
    print("")
    
    try:
        # Run the Django server
        subprocess.run(command, check=True)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running Django server: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ pipenv not found. Please make sure pipenv is installed.")
        sys.exit(1)

if __name__ == "__main__":
    main()

