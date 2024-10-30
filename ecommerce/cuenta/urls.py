from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),# Ruta para registrar un nuevo usuario
    path('login/', views.login, name='login'),# Ruta para iniciar sesión
    path('logout/', views.logout, name='logout'),# Ruta para cerrar sesión del usuario
    path('dashboard/', views.dashboard, name='dashboard'),# Ruta para acceder al panel de control del usuario
    path('', views.dashboard, name='dashboard'),   # Ruta predeterminada que redirige al panel de control
    path('olvidarPassword/', views.olvidarPassword, name='olvidarPassword'), # Ruta para la recuperación de contraseña 
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),# validar la solicitud de restablecimiento de contraseña
    path('borrarPassword/', views.borrarPassword, name='borrarPassword'), # Ruta para permitir a los usuarios borrar su contraseña
    path('activate/<uidb64>/<token>/', views.activate, name='activate'), # Ruta para activar la cuenta de un usuario utilizando un token
    path('mis_pedidos/', views.mis_pedidos, name='mis_pedidos'),  # Ruta para mostrar los pedidos realizados por el usuario
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),# Ruta para que el usuario edite su perfil
    path('cambio_password/', views.cambio_password, name='cambio_password'),  # Ruta para que el usuario cambie su contraseña
]

