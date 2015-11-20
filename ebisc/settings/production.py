from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['ebisc-prod.douglasconnect.com']

SERVER_EMAIL = 'EBiSC Production <joh@douglasconnect.com>'

# -----------------------------------------------------------------------------
# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ebisc',
        'USER': 'www',
    }
}

ELASTIC_INDEX = 'ebisc'
ELASTIC_HOSTS = [{'host': 'localhost', 'port': 9200}]

# -----------------------------------------------------------------------------