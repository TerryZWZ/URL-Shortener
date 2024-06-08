"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

# Set up Django
django.setup()

# Run migrations
try:
    execute_from_command_line(['manage.py', 'migrate'])
except Exception as e:
    print(f"Error running migrations: {e}")

application = get_wsgi_application()

app = application
