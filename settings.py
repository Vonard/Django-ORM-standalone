import os
from dotenv import load_dotenv
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv("DATABASE_HOST"),
        'PORT': '5434',
        'NAME': os.getenv("DATABASE_NAME"),
        'USER': os.getenv("DATABASE_USER"),
        'PASSWORD': os.getenv("USER_PASSWORD"),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv("SITE_SECRET_KEY")

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
