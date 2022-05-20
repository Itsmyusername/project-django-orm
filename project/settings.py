import os
from environs import Env
from dotenv import load_dotenv
import dj_database_url


load_dotenv()
DATABASES = {'default': dj_database_url.config()}

INSTALLED_APPS = ['datacenter']

SECERT_KEY=os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG')
ALLOWED_HOSTS=os.environ.get('ALLOWED_HOSTS')

ROOT_URLCONF = 'project.urls'




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
