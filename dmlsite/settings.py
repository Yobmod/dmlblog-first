
import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'u8&hn$a@%16^xvg+t5#abg(p6+&+y&qms6!@$cf*$-q3!^lge+'

# SECURITY WARNING: don't run with debug turned on in production!

#ALLOWED_HOSTS = []

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'yobmod@gmail.com'
EMAIL_HOST_PASSWORD = '3Monsters'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# Application definition


INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.admindocs',
	'django.contrib.auth',
	'django.contrib.sites',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	'dmlblog',
	'dmlpolls',
	'dmlmain',

	'taggit',
	'embed_video',
	'registration',
	'sitetree',
	'crispy_forms',
	'storages',
	
]

ACCOUNT_ACTIVATION_DAYS = 28 # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True # Automatically log the user in after registration.
SITE_ID = 1


TAGGIT_CASE_INSENSITIVE = True
CRISPY_TEMPLATE_PACK = 'bootstrap3' #or bootstap, bootstrap4, uni-forms

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'dmlsite.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				"django.template.context_processors.request",
				"django.template.context_processors.media",
			],
		},
	},
]

WSGI_APPLICATION = 'dmlsite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'dmlsite',
		'USER': 'dmlsite',
		'PASSWORD': '',
		'HOST': 'localhost',
		'PORT': '',
		'CONN_MAX_AGE': 600,
	}
}

DATABASES['default'] = dj_database_url.config()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
DEBUG = False

try:
	from .local_settings import *
except ImportError:
	pass


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/1.10/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'GB'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_URL = '/static/'
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'), )
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static_root')
LOGIN_REDIRECT_URL = '/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media', 'media_root')
