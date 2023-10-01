import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'tu_clave_secreta_generada_aleatoriamente'

DEBUG = True  # Cambia a False en un entorno de producción

ALLOWED_HOSTS = ['tudominio.com', 'www.tudominio.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tu_app_blog',  # Cambia 'tu_app_blog' al nombre real de tu aplicación de blogs
    'tu_app_auth',  # Cambia 'tu_app_auth' al nombre real de tu aplicación de autenticación
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Configura el directorio donde se redirigirá después del inicio de sesión
LOGIN_REDIRECT_URL = '/accounts/profile/'
LOGOUT_REDIRECT_URL = '/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de la base de datos (por ejemplo, PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_tu_basededatos',
        'USER': 'tu_usuario_de_basededatos',
        'PASSWORD': 'tu_contraseña_de_basededatos',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Configuración de la zona horaria
TIME_ZONE = 'America/New_York'  # Cambia a la zona horaria adecuada

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Rutas de archivos estáticos y medios
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
