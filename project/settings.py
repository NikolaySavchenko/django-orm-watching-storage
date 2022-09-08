import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'checkpoint.devman.org',
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': 'osim5',
    }
}

INSTALLED_APPS = ['datacenter', 'django.contrib.staticfiles', 'debug_toolbar',]

MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware',]

INTERNAL_IPS = ['127.0.0.1',]

SECRET_KEY = 'REPLACE_ME'

DEBUG = True

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

STATIC_URL = '/static/'
