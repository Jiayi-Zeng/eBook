from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]

with open("/etc/secret_key.txt") as f:
    SECRET_KEY = f.read().strip()

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

DEBUG_PROPAGATE_EXCEPTIONS = True

try:
    from .local import *
except ImportError:
    pass

