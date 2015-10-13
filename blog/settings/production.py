from .base import *
import os


DEBUG = False
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = os.environ["SECRET_KEY"]
STATIC_ROOT = os.environ['STATIC_PATH']
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

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://{redis_host}:6379/{redis_db}".format(
            redis_host=os.environ.get('REDIS_HOST', 'redis'),
            redis_db=os.environ.get('REDIS_DB', '1'),
        ),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
