"""
ASGI config for backend project.

ASGI (Asynchronous Server Gateway Interface) is the standard for Python asynchronous web apps and servers.
This file exposes the ASGI callable as a module-level variable named `application`.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
application = get_asgi_application()
