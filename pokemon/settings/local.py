from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xdyfkcj64i@(#a$hevbc0l*e(!6**kfxwnadkzlsce5kha-=bc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False # Cuando está en False, el aplicativo no va a mostrara ningún error cuando lo haya detectado en alguna
# parte del código.

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_pokemon',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost', #127.0.0.1
        'PORT': 5432
    }
}

"""
-> Base de Datos relacionales:
 - mysql
 - postgresql
 - sqlserver
 - RDS (AWS)

-> Base de Datos no relaciones:
- firebase
- mongo DB
- Dynamo DB (AWS)
"""

STATIC_URL = 'static/'

STATICFILES_DIR = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'