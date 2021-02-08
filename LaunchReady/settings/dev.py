from __future__ import absolute_import, unicode_literals

from LaunchReady.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xq6k9fg%-4$j8096ckith@u1@a)sgu$44kh+g=f$0m-k0gjw(7'

# SECRET_KEY = os.environ["SECTRET_KEY"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR + "/db.sqlite3",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ALLOWED_HOSTS = ["*"]
