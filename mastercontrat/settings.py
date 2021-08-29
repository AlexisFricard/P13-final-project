"""
Django settings for mastercontrat project.
"""
import os
from pathlib import Path
# For Heroku settings
import dj_database_url
import django_heroku


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

INSTALLED_APPS = [
    'bootstrap4',
    'frontpage.apps.FrontpageConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
]

WSGI_APPLICATION = 'mastercontrat.wsgi.application'

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mastercontrat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': [os.path.join(BASE_DIR, 'frontpage.templates')],
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

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',    # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',    # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',    # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',    # noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

if os.environ.get('ENV') == 'PRODUCTION':

    # Heroku settings (disable collecstatic)
    django_heroku.settings(locals(), staticfiles=False)
    DEBUG = False

    # Set your domain name here
    ALLOWED_HOSTS = ['www.masteraffairescontrats-poitiers.fr']

    # Database
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES = {"default": {}}
    DATABASES['default'].update(db_from_env)

    # AWS SETTINGS (ScaleWay)
    AWS_ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')

    AWS_STORAGE_BUCKET_NAME = os.getenv("BUCKET_NAME")
    AWS_S3_REGION_NAME = os.getenv('S3_REGION_NAME')
    AWS_S3_HOST = 's3.%s.scw.cloud' % (AWS_S3_REGION_NAME,)
    AWS_S3_ENDPOINT_URL = 'https://%s' % (AWS_S3_HOST,)
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    AWS_LOCATION = 'static'
    AWS_DEFAULT_ACL = 'public-read'
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_SIGNATURE_VERSION = 's3v4'

    # AWS STATIC SETTINGS
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_URL = '{}/{}/'.format(AWS_S3_ENDPOINT_URL, AWS_LOCATION)
    STATIC_ROOT = 'static/'
    # AWS MEDIA SETTINGS
    PUBLIC_MEDIA_LOCATION = 'media/'
    MEDIA_URL = (
        f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}' +
        f'/{PUBLIC_MEDIA_LOCATION}'
    )

    # TODO: Add file storage_backends in frontpage/
    DEFAULT_FILE_STORAGE = 'frontpage.storage_backends.PublicMediaStorage'

    # Default primary key field type
    # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    # TODO: Email service for passwords_reset and send user username & password
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))

else:
    STATIC_URL = '/static/'
