"""
Django settings for tienda project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from os import path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s&f92x^bztt53afi6l)oj-!1%aa6v9=ki@9p%lo!bu_wkx16c('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'core.middlewares.MyAppMessageMiddleware',
]

ROOT_URLCONF = 'tienda.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.global_render',
            ],
        },
    },
]

WSGI_APPLICATION = 'tienda.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# CONEXION A BD SQLITE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# CONEXION A BD ORACLE
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.oracle',
#         'NAME': '127.0.0.1:1521/xe',
#         'USER': 'c##ttstark',
#         'PASSWORD': 'ttstark',
#         'TEST': {
#             'USER': 'default_test',
#             'TBLSPACE': 'default_test_tbls',
#             'TBLSPACE_TMP': 'default_test_tbls_tmp',
#         },
#     },
# }

# CONEXION A BD SQL SERVER
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.oracle',
#         'NAME': '127.0.0.1:1521/xe',
#         'USER': 'c##ttstark',
#         'PASSWORD': 'ttstark',
#         'TEST': {
#             'USER': 'default_test',
#             'TBLSPACE': 'default_test_tbls',
#             'TBLSPACE_TMP': 'default_test_tbls_tmp',
#         },
#     },
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'America/Santiago'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# Parámetros para poder subir archivos a la carpeta "media"

MEDIA_ROOT = path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Parámetros para inicio de sesión

LOGIN_URL = '/ingresar'
LOGIN_REDIRECT_URL = '/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CONFIGURACIÓN PARA ENVIAR CORREOS ELECTRÓNICOS A TRAVÉS DEL SERVIDOR DE GMAIL
# Pasos a seguir:
# 1. Crear una cuenta de gmail, la mía es: "info.faithfulpet@gmail.com" password "Faith@fulpet@1990"
# 2. Ir a "Administrar tu cuenta de Google" que se encuentra seleccionando tu foto de perfil
# 3. Seleccionar la opción "Seguridad" en el menú de la izquierda
# 4. Activar la verificación en 2 pasos (opción "Teléfonos de la Verificación en 2 pasos")
# 5. Visitar: https://security.google.com/settings/security/apppasswords
# 6. Ingresar con tu correo y password de tu cuenta de gmail
#    En mi caso con la cuenta recién creada "info.faithfulpet@gmail.com" y contraseña "Faith@fulpet@1990"
# 7. En combobox "Seleccionar app" escoger "Otra (nombre personalizado)" y escibir "faithfulpet" (nombre de mi aplicación)
# 8. Presionar en botón "Generar"
# 9. Copiar la password 16 letras que aparece en pantalla y asignarla a la variable "EMAIL_HOST_PASSWORD"
# 10. Configurar las variables 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'info.faithfulpet@gmail.com'  # Reemplaza con tu dirección de correo Gmail
EMAIL_HOST_PASSWORD = 'qilcuwkdxlerbqae' # Reemplaza con tu contraseña de "aplicación generada"
