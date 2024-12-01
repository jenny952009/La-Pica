"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
#import pymysql
#pymysql.install_as_MySQLdb()
import os
from pathlib import Path

#from decouple import config
#pip install python-decouple


# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent            
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =123

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'empleados',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'categoria',
    'tienda',
    'carrito',
    'ventas',
    'pedido',
    'reservaciones',
    'suscripcion',
    'django_extensions',
    'import_export', #exportar datos del modelo de ventas a formatos como CSV, Excel o JSON 
    'cuenta',
]





MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
]


SESSION_EXPIRE_SECONDS = 1800
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_TIMEOUT_REDIRECT = 'cuenta/login'

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'categoria.context_processors.menu_links',
                'carrito.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'

AUTH_USER_MODEL = 'cuenta.Cuenta'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lapica',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',  #  dirección del servidor MySQL
        'PORT': '3306',       # El puerto predeterminado de MySQL
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}



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

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
#STATIC_ROOT = BASE_DIR /'static'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    'ecommerce/static'
]
#/media/
MEDIA_URL = '/media/'    # Esta es la URL pública para acceder a los archivos de medios
#MEDIA_ROOT = BASE_DIR /'media'   
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Ruta en el sistema de archivos donde se guardan los archivos
# import os 


from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR : 'danger',
}



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración del correo electrónico
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'cat20pam@gmail.com'  # Reemplaza con tu correo
EMAIL_HOST_PASSWORD = 'kvfi ogry raql huzw'  # Reemplaza con tu contraseña

JAZZMIN_SETTINGS = {
    "actions_sticky": True,  # Mantiene las acciones visibles al desplazarse
    "navigation_expanded": True,  # Expande la navegación para mayor claridad
   
    # Welcome text on the login screen
    "welcome_sign": "Bienvenidos al Panel de Administrador",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "images/logue.ico",  # Asegúrate de que esta ruta sea válida y el archivo esté en tu directorio estático
    # Title and header for the site
    "site_title": "Administración La Pica de la Chabelita",
    "site_header": "Panel de Administración LaPica",
    "site_brand": "La Pica de la Chabelita Restorant",
    "site_icon": "fa fa-cogs",  # Aquí puedes usar un icono de FontAwesome o uno personalizado

    # Customization for the user menu links
    "usermenu_links": [
        {"name": "Perfil", "url": "admin:auth_user_change", "permissions": ["auth.change_user"]},
        {"name": "Salir", "url": "/logout/", "permissions": ["auth.logout"]},
    ],
     # Top menu links (links at the top of the page)
    "topmenu_links": [
       # {"name": "Pedidos", "url": "/admin/app/pedido/", "permissions": ["auth.view_user"]},
       # {"name": "Ventas", "url": "/admin/app/ventas/", "permissions": ["auth.view_user"]},
        {"name": "Inicio", "url": "admin:index", "permissions": ["auth.view_user"]},
        #{"name": "Reportes", "url": "reportes/ventas", "permissions": ["auth.view_user"]},
    ],

    # Set to True if you want to see the UI builder (for admin customization)
    "show_ui_builder": False,

    # Controls whether the navigation menu on the left side is expanded or collapsed
    "show_navigation": True,


    # Control which apps are displayed in the sidebar (you can control the visibility of apps/modules)
    "hide_apps": [],  # Apps that you want to hide from the sidebar
    "show_apps": ["auth", "tienda", "carrito", "pedidos", "cuenta"],  # Visible apps
    
    # Customize the model links and the order they appear in the sidebar
    "order_with_respect_to": [ "auth", "cuenta","tienda", "carrito", "pedidos"],  # Apps order
    "actions_sticky": True,  # Mantiene las acciones visibles al desplazarse
    "navigation_expanded": True,  # Expande la navegación para mayor claridad

    # Sidebar customization
    "default_icon_type": "fa",  # Use FontAwesome icons
    "default_icon_color": "green",  # Set a default icon color
    "icons": {
        "auth": "fa fa-users",
        "tienda": "fa fa-store",
        "carrito": "fa fa-shopping-cart",
        "pedidos": "fa fa-box",
        "cuenta": "fa fa-user-circle",
    },

    # Footer settings
    "footer": "LaPica E-commerce - Todos los derechos reservados.",

    # Custom links or sections that you want to appear in the footer (optional)
    "footer_links": [
        {"name": "Documentación", "url": "https://docs.example.com"},
        {"name": "Soporte", "url": "https://support.example.com"},
    ],

    #"custom_links": {
       # "ventas": [{
        #    "name": "Gráfico de Ventas",
        #    "url": "admin:ventas_grafico",
        #    "icon": "fas fa-chart-pie",
        #}],
       
      #},
    
    #"custom_css": "static/css/custom.css",  # Puedes agregar tus propios estilos aquí.
    #"custom_js": "static/js/custom.js",    # Puedes incluir scripts personalizados aquí.
}




   

   
   

