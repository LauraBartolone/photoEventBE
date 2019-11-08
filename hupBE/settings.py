"""
Django settings for hupBE project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import datetime
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cm4npdhd5#!t@g_i4g=+w15vv&l$=hwzy@#z23+(dei3(3+bak'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'oauth2_provider',
    'corsheaders',
    'hup.apps.HupConfig',
    'events.apps.EventsConfig',
    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'imagekit',
    'django_extensions',
    'drf_yasg',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:4200',
]


ROOT_URLCONF = 'hupBE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'hupBE.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hup',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

REST_USE_JWT = True

REST_AUTH_SERIALIZERS = {
    'JWT_SERIALIZER ': 'rest_auth.serializers.JWTSerializer',
}

JWT_AUTH = {
  #'JWT_ENCODE_HANDLER':
  #'rest_framework_jwt.utils.jwt_encode_handler',

  #'JWT_DECODE_HANDLER':
  #'rest_framework_jwt.utils.jwt_decode_handler',

  #'JWT_PAYLOAD_HANDLER':
  #'rest_framework_jwt.utils.jwt_payload_handler',

  #'JWT_PAYLOAD_GET_USER_ID_HANDLER':
  #'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

  #'JWT_RESPONSE_PAYLOAD_HANDLER':
  #'rest_framework_jwt.utils.jwt_response_payload_handler',

  #'JWT_GET_USER_SECRET_KEY': None,
  #'JWT_PUBLIC_KEY': None,
  #'JWT_PRIVATE_KEY': None,
  #'JWT_ALGORITHM': 'HS256',
  #'JWT_VERIFY': True,
  #'JWT_VERIFY_EXPIRATION': True,
  #'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=36000),
  #'JWT_AUDIENCE': None,
  #'JWT_ISSUER': None,

  #'JWT_ALLOW_REFRESH': False,
  #'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

  #'JWT_AUTH_HEADER_PREFIX': 'JWT',
  #'JWT_AUTH_COOKIE': None,

}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    #{
    #   'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #},
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'