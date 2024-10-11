#!/usr/bin/env python #tells run project in python
"""Django's command-line utility for administrative tasks."""
import os
import sys #allow script to interact with python runtime enviorment


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'support_ukraine.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv) #This line takes whatever command you type in the terminal (like runserver or migrate) and tells Django to execute it.


if __name__ == '__main__':
    main()
