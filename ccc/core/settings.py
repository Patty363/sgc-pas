# -*- coding: UTF-8 -*-

#         app: Control de Planes de Acción
#      modulo: ccc.core.settings
# descripcion: Configuración del Proyecto
#       autor: Javier Sanchez Toledano
#       fecha: miércoles, 1 de octubre de 2014


from unipath import Path

PROJECT_DIR = Path(__file__).ancestor(2)
MEDIA_ROOT = PROJECT_DIR.child("media")
STATIC_URL = '/assets/'
MEDIA_URL = '/media/'
STATIC_ROOT = PROJECT_DIR.child("static")
STATICFILES_DIRS = (
    PROJECT_DIR.child("assets"),
)
TEMPLATE_DIRS = (
    PROJECT_DIR.child("templates"),
)

SECRET_KEY = 'l^$i9+644l_!7$v+z4orhd2x*$$9bavkimblp5327#3)-ue&e%'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'annoying',
    'smart_selects',
    'tinymce',

    'pas',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': Path(PROJECT_DIR, 'data/pas.db'),
    }
}

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'Mexico/General'
USE_I18N = True
USE_L10N = True
USE_TZ = True
