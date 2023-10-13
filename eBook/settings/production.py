from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

ALLOWED_HOSTS = ["47.103.202.117", '127.0.0.1']

with open("/etc/secret_key.txt") as f:
    SECRET_KEY = f.read().strip()

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True