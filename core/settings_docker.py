import os

import environ

from core.settings import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

ALLOWED_HOSTS = [env('HOST')]

USE_CACHE = True

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

CACHES = {
    'default': env.cache_url('REDIS_URL')
}

DATABASES = {
    "default": env.db()
}