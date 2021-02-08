from __future__ import absolute_import, unicode_literals

import dj_database_url
import dotenv
from weekend_vibes.settings.base import *

env = os.environ.copy()
ADMINS = (("Developer name", "Developer email"),)

DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ["launch-ready-domain.com"]

DATABASES = {}
DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)


# ToDo: get an email host provider
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_PASSWORD"]

EMAIL_PORT = 587
EMAIL_USE_TLS = True

