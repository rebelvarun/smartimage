import os

from env_settings.base import *

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'smartimage.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static/'),)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates')
)

