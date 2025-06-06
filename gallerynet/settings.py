from pathlib import Path
import os
import dj_database_url
from google.oauth2 import service_account
import json
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', default='django-insecure-00*dhdo9(og(6cjjzy2g!x*$w5z@0ggx6p7^6tk@qhtk9c$o6y')
DEBUG = 'RENDER' not in os.environ
ALLOWED_HOSTS = [] 
""" DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(' ') """

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'storages',

    # apps
    'apps.users',
    'apps.gallery',
    'apps.sales',
    'apps.backoffice',
    'apps.categories',
    'apps.mensajes',
   
    'widget_tweaks',
]

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

ROOT_URLCONF = 'gallerynet.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'gallerynet.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('gallerynet'),
        'USER': os.environ.get('postgres'),
        'PASSWORD': os.environ.get('superidol110105'),
        'HOST': os.environ.get('localhost'),
        'PORT': os.environ.get('DB_PORT', ''),
    }
}
DATABASES['default'] = dj_database_url.parse("postgresql://gallerynet_user:nh58KDAagJiRjGtRDC2QTpoTehzPkN5u@dpg-d107p50gjchc73aes2k0-a.frankfurt-postgres.render.com/gallerynet")

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.Usuario'


# Configuración de Google Cloud Storage
GCS_KEY_CONTENT = os.environ.get('GCS_SERVICE_ACCOUNT_KEY_JSON')
GS_BUCKET_NAME = 'gallerynet_bucket'
GS_DEFAULT_ACL = 'publicRead'


STATIC_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/static/'
if GCS_KEY_CONTENT:
    try:
        credentials_data = json.loads(GCS_KEY_CONTENT)
        temp_key_path = BASE_DIR / 'gcs_temp_key.json'
        with open(temp_key_path, 'w') as f:
            json.dump(credentials_data, f)
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = str(temp_key_path)
        GS_CREDENTIALS = service_account.Credentials.from_service_account_file(str(temp_key_path))
        print("GCS credentials loaded from environment variable.", file=sys.stderr)
    except json.JSONDecodeError:
        print("Error: GCS_SERVICE_ACCOUNT_KEY_JSON is not valid JSON.", file=sys.stderr)
    except Exception as e:
        print(f"Error processing GCS service account key: {e}", file=sys.stderr)
else:
    print("Warning: GCS_SERVICE_ACCOUNT_KEY_JSON environment variable not found.", file=sys.stderr)
    # Intenta cargar desde el archivo local solo en desarrollo
    if DEBUG:
        try:
            local_key_path = os.path.join(BASE_DIR, 'handy-math-461909-u8-8ec4ca4ffc16.json')
            GS_CREDENTIALS = service_account.Credentials.from_service_account_file(local_key_path)
        except FileNotFoundError:
            print("Warning: Local GCS credentials file not found.", file=sys.stderr)

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
MEDIA_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/'
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

LOGIN_URL = '/users/login/'

#configuracion de correo
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # motor de envío de correos
EMAIL_HOST = 'smtp.gmail.com' 
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'gallerynet2025@gmail.com'  # Tu correo genérico
EMAIL_HOST_PASSWORD = 'qjer jhgi anlx jswn'  # Tu contraseña de aplicación
DEFAULT_FROM_EMAIL = 'gallerynet2025@gmail.com'