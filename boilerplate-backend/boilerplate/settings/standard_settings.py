from boilerplate.settings.base_settings import *
from datetime import timedelta

INSTALLED_APPS += [
    # Apps
    'documents.apps.DocumentsConfig',
    # Third party
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    'corsheaders',
    'django_cleanup',  # should go after your apps
]

MIDDLEWARE += [

]


# DJANGO LOCAL-MEMORY CACHE ----------------------------------------------------------------------

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'FileVault',
    }
}


# STATIC FILES -----------------------------------------------------------------------------------

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'public'

MEDIA_URL = 'assets/'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = (
    BASE_DIR / 'static',
)


# AUTH -----------------------------------------------------------------------------------


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'rest_framework.authentication.TokenAuthentication',
]

LOGIN_REDIRECT_URL = '/documents/'


# REST FRAMEWORK -----------------------------------------------------------------------------------


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}


# CORS -----------------------------------------------------------------------------------


CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = ['http://localhost:8080']
CSRF_TRUSTED_ORIGINS = ['http://localhost:8080']
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT'
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with'
]
