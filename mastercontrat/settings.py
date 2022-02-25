
"""
Django settings for mastercontrat project.
"""
import mimetypes
import os
from pathlib import Path
# For Heroku settings
import dj_database_url
import django_heroku

# For Django mime types
mimetypes.add_type("text/javascript", ".js", True)
mimetypes.add_type("application/javascript", ".js", True)

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
# This is for redirect http to https
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True


SECRET_KEY = os.getenv("SECRET_KEY")

INSTALLED_APPS = [
    # Apps
    'frontpage.apps.FrontpageConfig',
    'contact.apps.ContactConfig',
    'presentation.apps.PresentationConfig',
    'ourstudent.apps.OurstudentConfig',
    'testimony.apps.TestimonyConfig',
    'association.apps.AssociationConfig',
    'dashboard.apps.DashboardConfig',
    'collabspace.apps.CollabspaceConfig',
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # For bucket storage
    'storages',
    # For real-time chat
    'chat',
    'channels',
]

# WSGI_APPLICATION = 'mastercontrat.wsgi.application'
ASGI_APPLICATION = 'mastercontrat.asgi.application'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
        'APP_DIRS': [os.path.join(BASE_DIR, 'templates.templates')],
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


# Heroku settings (disable collecstatic)
django_heroku.settings(locals(), staticfiles=False)

# Set your domain name here
ALLOWED_HOSTS = ['www.masteraffairescontrats-poitiers.fr']
# ALLOWED_HOSTS = ['masteraffairecontrats.herokuapp.com']

# Database
if os.getenv('ENV') == "PRODUCTION":
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES = {"default": {}}
    DATABASES['default'].update(db_from_env)

elif os.getenv('ENV') == "GITHUB":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': 5432,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('HEROKU_M2_DB_NAME'),
            'USER': os.getenv('HEROKU_M2_DB_USER'),
            'PASSWORD': os.getenv('HEROKU_M2_DB_PW'),
            'HOST': os.getenv('HEROKU_M2_DB_HOST'),
            'PORT': 5432,
        }
    }

if os.getenv('ENV') != "GITHUB":
    # AWS SETTINGS (ScaleWay)
    AWS_ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv("BUCKET_NAME")
    AWS_S3_REGION_NAME = os.getenv('S3_REGION_NAME')

    AWS_DEFAULT_ACL = 'public-read'
    AWS_LOCATION = 'static'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_S3_SIGNATURE_VERSION = 's3v4'

    AWS_QUERYSTRING_AUTH = False
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # AWS STATIC SETTINGS
    AWS_S3_HOST = 's3.%s.scw.cloud' % (AWS_S3_REGION_NAME,)
    AWS_S3_ENDPOINT_URL = 'https://%s' % (AWS_S3_HOST,)

    STATIC_URL = '{}/{}/'.format(AWS_S3_ENDPOINT_URL, AWS_LOCATION)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

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

    # TODO: Email service for passwords_reset and
    #       send user username & password & contact
    # SENDGRID_API_KEY = os.getenv('EMAIL_HOST_PASSWORD') 
    EMAIL_HOST = os.environ.get("EMAIL_HOST")
    EMAIL_PORT = os.environ.get("EMAIL_PORT")
    EMAIL_HOST_USER = os.environ.get("SENDGRID_USERNAME")
    EMAIL_HOST_PASSWORD = os.environ.get("SENDGRID_PASSWORD")
    EMAIL_USE_TLS = True
    # DEFAULT_FROM_EMAIL = 'Association des Master Contrats de Poitiers'
    # EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

    # Keep our policy as strict as possible
    # CSP_DEFAULT_SRC = ("'self'", f'{STATIC_URL}', f'{MEDIA_URL}')
    # CSP_STYLE_SRC = ("'self'", f'{STATIC_URL}')
    CSP_SCRIPT_SRC = ("'self'", f'{STATIC_URL}')
    # CSP_FONT_SRC = ("'self'", f'{STATIC_URL}')
    # CSP_IMG_SRC = (
    #   "'self'", f'{STATIC_URL}',
    #   'data: maps.gstatic.com *.googleapis.com *.ggpht.com'
    # )

    # For tchat
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            "CONFIG": {
                "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
            },
            },
    }
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    MEDIA_URL = '/media/'
