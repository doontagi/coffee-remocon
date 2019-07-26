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
JWT_AUTH={
	'JWT_EXPIRATION_DELTA' : datetime.timedelta(hours=1),
	'JWT_ALLOW_REFRESH':True,
}
REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES':(
		'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
	),
}
REST_USE_JWT = True


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

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


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'OPTIONS': {
#            'read_default_file': os.path.join(SECRET_DIR, "mysql.cnf"),
#            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  # strict mode 설정 추가
#        },
#        'NAME': 'coffeeremocon2',
#        'USER': 'suamzzz',
#        'PASSWORD' : 'flahzhs11',
#        'HOST' : 'coffeeremocon2.c9v6glqksa93.ap-northeast-2.rds.amazonaws.com',
#        'PORT' : '3306'
#    }
#}



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
DATABASES = {
	'default':{
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}
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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

