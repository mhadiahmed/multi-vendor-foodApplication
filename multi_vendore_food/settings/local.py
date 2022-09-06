from email.policy import default
from .base import *
from decouple import config
INSTALLED_APPS += ["debug_toolbar"]

DEBUG=config("DEBUG", default=True, cast=bool)

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
