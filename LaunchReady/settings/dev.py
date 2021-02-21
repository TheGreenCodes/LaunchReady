import os
from dotenv import load_dotenv

from LaunchReady.settings.base import *

load_dotenv()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = os.getenv("SECRET_KEY")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        # "PORT": os.getenv("DATABASE_PORT"),
    }
}


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ALLOWED_HOSTS = ["*"]
