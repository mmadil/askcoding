"""
WSGI config for askcoding project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

# Standard Library
import os

# Third Party
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.production")

application = get_wsgi_application()
