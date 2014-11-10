"""
Django settings for ygg_django project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u!hi1r#q6c^b(i22(byzk_kqy2@h$n0r-=$-pu4q&q-la@vmr&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ygg_django.urls'

WSGI_APPLICATION = 'ygg_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = '/home/test/ygg/db/sqlite3/ygg_test.db'

# MongoDB
# import mongoengine
#
# SESSION_ENGINE = 'mongoengine.django.sessions'
#
# _MONGODB_USER = 'yggmongo'
# _MONGODB_PASSWD = 'yggmongo1234'
# _MONGODB_HOST = '127.0.0.1'
# _MONGODB_NAME = 'yggtest'
# _MONGODB_DATABASE_HOST = \
# 	'mongodb://%s/%s' \
# 	% (_MONGODB_HOST, _MONGODB_NAME)
# #
# mongoengine.connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)

# AUTHENTICATION_BACKENDS = (
# 	'mongoengine.django.auth.MongoEngineBackend',
# )

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/home/test/ygg/ygg_test/ygg_django/ygg_django/static'

TEMPLATE_DIRS = (
    '/home/test/ygg/ygg_test/ygg_django/template',
)

# add app
INSTALLED_APPS += (
	'ygg_app',		# ygg app
	'rest_framework',	# RESTful
    'south',     # south
)

# RESTful
REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
 #   'DEFAULT_AUTHENTICATION_CLASSES': (
 #   'rest_framework.authentication.BasicAuthentication',
 #   'rest_framework.authentication.SessionAuthentication',
 #   ),
    # pagination
    'PAGINATE_BY': 10
}