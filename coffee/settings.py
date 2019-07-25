# -*- coding: utf-8 -*-

import os, json, datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ROOT_DIR = os.path.dirname(BASE_DIR)

DEBUG = True


# 공통부분, 개발모드/배포모드 로 나누어 파일 참조함. 위의 DEBUG=True값만 조정해주면 됨.
SECRET_DIR = os.path.join(BASE_DIR, '.config_secret')
SECRET_COMMON_FILE = os.path.join(SECRET_DIR, 'common.json')
if DEBUG:
    SECRET_FILE = os.path.join(SECRET_DIR, 'development.json')
else:
    SECRET_FILE = os.path.join(SECRET_DIR, 'deploy.json')

secret_common = json.loads(open(SECRET_COMMON_FILE).read())
secret_other = json.loads(open(SECRET_FILE).read())

SECRET_KEY = secret_common['django']["secret_key"]
ALLOWED_HOSTS = secret_other['django']['allowed_hosts']

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'corsheaders',
    'menu',
    'order',
    'rest_framework',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
    'social_django',
    'rest_framework.authtoken',
]

SITE_ID = 1





# Configure the JWTs to expire after 1 hour, and allow users to refresh near-expiration tokens
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=1),
    'JWT_ALLOW_REFRESH': True,
}

# Make JWT Auth the default authentication mechanism for Django
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

# Enables django-rest-auth to use JWT tokens instead of regular tokens.
REST_USE_JWT = True


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
## TO BE CHANGED
CORS_ORIGIN_WHITELIST = (
    'localhost:3000/'
    'localhost:3000'
    'https://mockup-pg-web.kakao.com'
)

ROOT_URLCONF = 'coffee.urls'

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

WSGI_APPLICATION = 'coffee.wsgi.application'

# User Substitution
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_TZ = True
TIME_ZONE = 'Asia/Seoul'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'