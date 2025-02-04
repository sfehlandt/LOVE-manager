"""
Django settings for manager project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import ldap
from django_auth_ldap.config import LDAPSearch

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define wether the system is being tested or not:
TESTING = os.environ.get('TESTING', False)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tbder3gzppu)kl%(u3awhhg^^zu#j&!ceh@$n&v0d38sjx43s8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost', 'love-manager-mount', 'love-nginx-mount', 'manager',
    'love-manager', 'love-nginx', '10.0.100.1', '10.0.100.209', '127.0.0.1'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'webpack_loader',
    'channels',
    'rest_framework',
    # 'rest_framework.authtoken',
    'corsheaders',
    'api',
    'subscription',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'api.middleware.GetTokenMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# CORS Configuration
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

WSGI_APPLICATION = 'manager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Password for other processes
PROCESS_CONNECTION_PASS = os.environ.get('PROCESS_CONNECTION_PASS', 'dev_pass')


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        # 'api.authentication.TokenAuthentication',
        'api.authentication.ExpiringTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}
TOKEN_EXPIRED_AFTER_DAYS = 30


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/manager/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_files"),
]

# Channels
ASGI_APPLICATION = 'manager.routing.application'
REDIS_HOST = os.environ.get('REDIS_HOST', False)
REDIS_PASS = os.environ.get('REDIS_PASS', False)
if REDIS_HOST and not TESTING:
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {
                "hosts": ["redis://:" + REDIS_PASS + "@" + REDIS_HOST + ":6379/0"],
                "symmetric_encryption_keys": [SECRET_KEY],
            },
        },
    }
else:
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels.layers.InMemoryChannelLayer',
        },
    }

# LDAP
# Baseline configuration:
AUTH_LDAP_SERVER_URI = os.environ.get('AUTH_LDAP_SERVER_URI', False)

# Only use LDAP activation backend if there is an AUTH_LDAP_SERVER_URI
# configured in the OS ENV:
if AUTH_LDAP_SERVER_URI and not TESTING:
    AUTHENTICATION_BACKENDS = [
        'django_auth_ldap.backend.LDAPBackend',
    ]

    AUTH_LDAP_BIND_DN = ''
    AUTH_LDAP_BIND_PASSWORD = ''

    AUTH_LDAP_USER_SEARCH = LDAPSearch(
        'ou=people,dc=planetexpress,dc=com',
        ldap.SCOPE_SUBTREE,
        '(uid=%(user)s)',
    )
