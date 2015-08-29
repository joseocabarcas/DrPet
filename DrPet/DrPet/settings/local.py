from .base import *
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'xe',
        'USER': 'system',
        'PASSWORD': 'oracle',
        'HOST': 'localhost',
        'PORT': '1521',
    }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

#Directorios de archivos estaticos, Bootstrap, etc..
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)