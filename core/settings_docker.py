from core.settings import *

ALLOWED_HOSTS = ["0.0.0.0"]

USE_CACHE = True

SECRET_KEY = 'django-insecure-&s$0xki157_)(sv-d61sp(#6y*7g%9nord4f2mi$nuhux2x&m4'

CACHES['default']['LOCATION'] = "redis://redis-cache:6379/"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",  # set in docker-compose.yml
        "PORT": 5432,  # default postgres port
    }
}