"""
WSGI config for ygg_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import sys
import os

sys.path.append("/home/test/ygg/ygg_test/ygg_django")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ygg_django.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
