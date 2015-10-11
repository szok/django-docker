from .base import *
import os


DEBUG = False
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*',).split(',')

ADMINS = (
    ('mk', 'Your email'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'blog'),
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', ''),
        'PORT': os.environ.get('DB_PORT', ''),
    }
}
