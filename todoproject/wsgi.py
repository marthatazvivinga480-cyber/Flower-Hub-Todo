"""
WSGI config for todoproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoproject.settings')

application = get_wsgi_application()

if os.environ.get('RUN_MIGRATIONS_ON_STARTUP', 'True') == 'True':
    call_command('migrate', interactive=False, verbosity=1)

admin_username = os.environ.get('ADMIN_USERNAME', '').strip()
admin_password = os.environ.get('ADMIN_PASSWORD', '').strip()
admin_email = os.environ.get('ADMIN_EMAIL', '').strip()

if admin_username and admin_password:
    User = get_user_model()
    user, created = User.objects.get_or_create(
        username=admin_username,
        defaults={'email': admin_email, 'is_staff': True, 'is_superuser': True},
    )
    if created or not user.check_password(admin_password):
        user.email = admin_email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(admin_password)
        user.save()
        print(f"Admin user '{admin_username}' was {'created' if created else 'updated'}.")
    else:
        print(f"Admin user '{admin_username}' already exists.")
else:
    print('ADMIN_USERNAME and ADMIN_PASSWORD were not both set; admin user was not created.')
