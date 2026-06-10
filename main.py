#!/usr/bin/env python3
"""
Jarvis - Your Personal AI Assistant
Main entry point for the application.
"""

import sys
import click
from config.settings import settings
from core.assistant import JarvisAssistant
from core.utils import print_section, print_response

@click.group()
def cli():
    """Jarvis - Your Personal AI Assistant"""
    pass

@cli.command()
@click.argument('command', nargs=-1, required=False)
def run(command):
    """Run Jarvis assistant."""
    # Validate settings
    settings.validate()
    
    # Initialize assistant
    assistant = JarvisAssistant()
    
    if command:
        # Command mode - execute single command
        cmd_string = ' '.join(command)
        response = assistant.process_command(cmd_string)
        if response:
            print(f"\nJarvis: {response}\n")
    else:
        # Interactive mode
        assistant.start()

@cli.command()
def status():
    """Show Jarvis status."""
    assistant = JarvisAssistant()
    print_section("Jarvis Status")
    print(f"Name: {assistant.name}")
    print(f"Version: {assistant.version}")
    print(f"Initialized: {assistant.initialized}")
    print(f"Modules Loaded: {len(assistant.modules)}")
    print(f"Modules: {', '.join(assistant.modules.keys())}")
    print()

@cli.command()
def modules():
    """List loaded modules."""
    assistant = JarvisAssistant()
    print_section("Loaded Modules")
    
    for name in assistant.modules.keys():
        print(f"  ✓ {name}")
    print()

@cli.command()
def config():
    """Show configuration."""
    print_section("Configuration")
    print(f"OpenAI API Key: {'Set' if settings.OPENAI_API_KEY else 'Not set'}")
    print(f"Google API Key: {'Set' if settings.GOOGLE_API_KEY else 'Not set'}")
    print(f"Email Address: {settings.EMAIL_ADDRESS if settings.EMAIL_ADDRESS else 'Not set'}")
    print(f"Database: {settings.DATABASE_URL}")
    print(f"Timezone: {settings.TIMEZONE}")
    print(f"Language: {settings.LANGUAGE}")
    print()

@cli.command()
def version():
    """Show Jarvis version."""
    assistant = JarvisAssistant()
    print(f"Jarvis v{assistant.version}")

if __name__ == '__main__':
    try:
        cli()
    except KeyboardInterrupt:
        print("\n")
        print_response("Interrupted by user", "info")
        sys.exit(0)
    except Exception as e:
        print_response(f"Error: {str(e)}", "error")
        sys.exit(1)
