
#import pymysql
#pymysql.install_as_MySQLdb()
import os
from pathlib import Path


#from decouple import config
#pip install python-decouple


# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent            
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =123

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'categoria',
    'cuenta',
    'tienda',
    'carrito',
    'pedido',
    'reservaciones',
    'suscripcion',
    #'cuenta.apps.CuentaConfig',  # Registro de la clase de configuración
    'django_extensions',
    'django.contrib.humanize',
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
# Duración máxima de la sesión sin actividad (en segundos)
SESSION_EXPIRE_SECONDS = 1800  # 30 minutos
SESSION_COOKIE_AGE = 1800  # 30 minutos
SESSION_EXPIRE_SECONDS = 1800
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
# La sesión se cerrará automáticamente al cerrar el navegador
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

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
        'HOST': 'localhost',  # o la dirección del servidor MySQL
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

STATIC_URL = '/static/'   # se modifvo para prodcucion
#STATIC_ROOT = BASE_DIR /'static'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    'ecommerce/static'
]
#/media/
MEDIA_URL = '/media/'
#MEDIA_ROOT = BASE_DIR /'media'   
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
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
    "navigation_expanded": False,  # Expande la navegación para mayor claridad
    "show_sidebar":True,

    # Welcome text on the login screen
    "welcome_sign": " Bienvenido al Panel de Administrador",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "images/logue.ico",  # Asegúrate de que esta ruta sea válida y el archivo esté en tu directorio estático
 # Título y encabezado para el sitio
    "site_title": "Administración La Pica de la Chabelita",
    "site_header": "Panel de Administración LaPica",
    "site_brand": "La Pica de la Chabelita Restorant",
    "site_icon": "fa fa-cogs",  # Aquí puedes usar un icono de FontAwesome o uno personalizado

    # Personalización de los enlaces del menú de usuario
    "usermenu_links": [
        {"name": "Perfil", "url": "admin:auth_user_change", "permissions": ["auth.change_user"]},
        {"name": "Salir", "url": "/logout/", "permissions": ["auth.logout"]},
    ],
     # Top menu links (links at the top of the page)
    "topmenu_links": [
        {"name": "Dashboard", "url": "dashboard_ventas", "permissions": ["auth.view_user"]},
       # {"name": "Ventas", "url": "/admin/app/ventas/", "permissions": ["auth.view_user"]},
        {"name": "Inicio", "url": "admin:index", "permissions": ["auth.view_user"]},
        # Elimina o comenta el enlace al perfil para evitar que aparezca
    # {"name": "Perfil", "url": "admin:auth_user_change", "permissions": ["auth.change_user"]},
    # {"name": "Salir", "url": "logout", "permissions": ["auth.view_user"]},
    ],
    
    
    # Set to True if you want to see the UI builder (for admin customization)
    "show_ui_builder": False,

    # Controls whether the navigation menu on the left side is expanded or collapsed
    "show_navigation": True,
    # Controla qué aplicaciones se muestran en la barra lateral
    "hide_apps": [],  # Apps that you want to hide from the sidebar
    "show_apps": ["auth", "tienda", "carrito", "pedidos", "cuenta"],  # Visible apps
    
    # Personalización del orden de las aplicaciones en la barra lateral
    "order_with_respect_to": [ "auth", "cuenta","tienda", "carrito", "pedidos"],  # Apps order
    "navigation_expanded": True,  # Expande la navegación para mayor claridad

    # Personalización de iconos en la barra lateral
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
    # Enlaces personalizados en el pie de página (opcional)

    # Custom links or sections that you want to appear in the footer (optional)
    #"footer_links": [
    #    {"name": "Documentación", "url": "https://docs.example.com"},
    #    {"name": "Soporte", "url": "https://support.example.com"},
    #],

    #"custom_links": {
    #    "pedido": [{
    #        "name": "Dashboard de ventas",
    #       "url": "dashboard_ventas",
    #       "icon": "fas fa-chart-pie",
    #    }],
       
    #  },
    
    #"custom_css": "static/css/custom.css",  # Puedes agregar tus propios estilos aquí.
    #"custom_js": "static/js/custom.js",    # Puedes incluir scripts personalizados aquí.
}


