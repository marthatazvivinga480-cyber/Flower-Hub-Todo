"""
WSGI config for todoproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoproject.settings')

application = get_wsgi_application()

if os.environ.get('RUN_MIGRATIONS_ON_STARTUP', 'True') == 'True':
    call_command('migrate', interactive=False, verbosity=1)
