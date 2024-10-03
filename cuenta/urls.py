from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='home'),  # Cambié el nombre a 'home' para evitar duplicados
    path('olvidar-password/', views.olvidarPassword, name='olvidarPassword'),
    path('reset-password-validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('borrar-password/', views.borrarPassword, name='borrarPassword'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('mis-pedidos/', views.mis_pedidos, name='mis_pedidos'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('cambio-password/', views.cambio_password, name='cambio_password'),
]

