from .base import *
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'drpet',
        'USER': 'drpet',
        'PASSWORD': 'drpet',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

#Directorios de archivos estaticos, Bootstrap, etc..
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)