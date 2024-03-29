"""
Django settings for leadtracker project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import boto3
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=714y(0&fs%4b+mpu8-bpkwj_&7fcx*nb3b*ae_@ouo-z9izva'

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
    'myapp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'leadtracker.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'leadtracker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





# Set your AWS credentials and region (replace 'your_access_key', 'your_secret_key', and 'your_region' with your actual AWS credentials and region)
AWS_ACCESS_KEY_ID = 'AKIAS3LJHOT555KCW2NV'
AWS_SECRET_ACCESS_KEY = '2FQpAHCzgMmNIOhgIHpTV5XAIIsjdmnqgtQgxI1h'
AWS_REGION = 'ap-south-1'



AWS_DYNAMODB_REGION = 'ap-south-1'
AWS_DYNAMODB_ACCESS_KEY_ID = 'AKIAS3LJHOT555KCW2NV'
AWS_DYNAMODB_SECRET_ACCESS_KEY = '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'

# Configure the DynamoDB resource
DYNAMODB_ENDPOINT_URL = f'https://dynamodb.{AWS_REGION}.amazonaws.com'
DYNAMODB_TABLE_NAME = 'myapp'  # Replace with your actual DynamoDB table name


# Connect to DynamoDB
dynamodb_resource = boto3.resource(
    'dynamodb',
    region_name='ap-south-1',
    aws_access_key_id=AWS_DYNAMODB_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_DYNAMODB_SECRET_ACCESS_KEY,
    endpoint_url=DYNAMODB_ENDPOINT_URL
)