#!/usr/bin/env python

# Standard Library
import os
import sys

# Third Party
from django.core.management import execute_from_command_line
from dotenv import load_dotenv

if __name__ == "__main__":
    # Read .env file and set key/value inside it as environment variables
    load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.development")

    execute_from_command_line(sys.argv)
