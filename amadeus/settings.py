"""
Django settings for amadeus project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

import dj_database_url

db_from_ev = dj_database_url.config(conn_max_age=500)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$=8)c!5)iha85a&8q4+kv1pyg0yl7_xe_x^z=2cn_1d7r0hny4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'widget_tweaks',
    'rolepermissions',
    'rest_framework',
    'django_bootstrap_breadcrumbs',
    's3direct',

    'users',
    'core',
    'app',
    'courses',
    'forum',
    'poll',
    'links',

]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    #libs-middleware

]

ROOT_URLCONF = 'amadeus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'core.context_processors.notifications',
                'courses.context_processors.courses',
            ],
        },
    },
]

WSGI_APPLICATION = 'amadeus.wsgi.application'


# Database
# https://docs.djangopr/*oject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': db_from_ev
}


#superuser: admin pass: amadeus2358

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Files
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'uploads')
MEDIA_URL = '/uploads/'

# Users
LOGIN_REDIRECT_URL = 'app:index'
LOGIN_URL = 'core:home'
AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
ROLEPERMISSIONS_MODULE = 'amadeus.roles'

LOGS_URL = 'logs/'
#https://github.com/squ1b3r/Djaneiro


# E-mail
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'admin@admin.com'

# Messages
from django.contrib.messages import constants as messages_constants
MESSAGE_TAGS = {
    messages_constants.DEBUG: 'debug',
    messages_constants.INFO: 'info',
    messages_constants.SUCCESS: 'success',
    messages_constants.WARNING: 'warning',
    messages_constants.ERROR: 'danger',
}

#Send email for forgot Password
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'amadeusteste@gmail.com'
EMAIL_HOST_PASSWORD = 'amadeusteste'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#s3direct

# AWS keys
AWS_SECRET_ACCESS_KEY = ''
AWS_ACCESS_KEY_ID = ''
AWS_STORAGE_BUCKET_NAME = ''

S3DIRECT_REGION = 'sa-east-1'

from uuid import uuid4

S3DIRECT_DESTINATIONS = {
    # Specify a non-default bucket for PDFs
    'material': (lambda original_filename: 'uploads/material/'+str(uuid4())+'.pdf', lambda u: True, ['application/pdf']),

}

try:
    from .local_settings import *
except ImportError:
    pass
