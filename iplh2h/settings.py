"""
Django settings for iplh2h project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
ON_HEROKU = True
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
DEFAULT_SECRET_KEY = '@wrb6az#8==dpd#e84yw%z=fk5cy1!4#e*c@zysr%^d9%#gqqf'
SECRET_KEY = os.environ.get('SECRET_KEY', DEFAULT_SECRET_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
# ALLOWED_HOSTS = []

# try to load local_settings.py if it exists
try:
    from local_settings import *
except Exception as e:
    pass

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'h2h',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'iplh2h.urls'

WSGI_APPLICATION = 'iplh2h.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if ON_HEROKU:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
        }
    }
    # Parse database configuration from $DATABASE_URL
    DATABASES['default'] =  dj_database_url.config()
else:    
    DATABASES = {
        'default': {
            # "ENGINE": "django.db.backends.postgresql_psycopg2",
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# ref: https://realpython.com/blog/python/migrating-your-django-project-to-heroku/
# https://realpython.com/blog/python/digging-deeper-into-migrations/
# http://stackoverflow.com/questions/27195215/django-1-7-1-keeps-on-using-the-dummy-db-engine
# http://stackoverflow.com/questions/26080303/improperlyconfigured-settings-databases-is-improperly-configured-please-supply
# http://stackoverflow.com/questions/11826326/django-error-in-heroku-please-supply-the-engine-value
# http://stackoverflow.com/questions/26094390/django-sqlite-overriding-postgresql-db-on-heroku-when-pushing-from-local-develo