# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
from .base import *  # NOQA
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

