"""
Django settings for backend project.

SECRET_KEY:
    - Used for cryptographic signing in Django (e.g., session cookies, CSRF tokens, password reset tokens).
    - **Must be kept secret**: If exposed, attackers could forge cookies or tokens and compromise your app.[1][3][5]
    - Should never be hardcoded in production! Use environment variables or a secrets manager instead.[2][5][6][7][8][9]
    - Changing it will invalidate all existing signed data (users will be logged out, password reset links will break, etc).[2][5]
    - For development, a default value may be used, but always override in production.

Best practices:
    - Store in a `.venv` file or environment variable (not in version control).
    - Example of generating a new key:
        python3 manage.py shell
        from django.core.management.utils import get_random_secret_key
        print(get_random_secret_key())
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Load SECRET_KEY from environment variable, fallback for development only
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'insecure-dev-key-change-me')

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'backend.urls'
TEMPLATES = []
WSGI_APPLICATION = 'backend.wsgi.application'
ASGI_APPLICATION = 'backend.asgi.application'  # For ASGI/uvicorn

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
