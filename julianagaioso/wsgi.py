"""
WSGI config for julianagaioso project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# Adicione o caminho do projeto ao sys.path
sys.path.append('/home/ubuntu/juliana_gaioso/julianagaioso')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "julianagaioso.settings")

application = get_wsgi_application()
