from core.settings import *

ALLOWED_HOSTS = ["0.0.0.0"]

CACHES['default']['LOCATION'] = "redis://redis-cache:6379/"
