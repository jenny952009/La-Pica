from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),  
    path('olvidarPassword/', views.olvidarPassword, name='olvidarPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('borrarPassword/', views.borrarPassword, name='borrarPassword'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('mis_pedidos/', views.mis_pedidos, name='mis_pedidos'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('cambio_password/', views.cambio_password, name='cambio_password'),
    path('ayuda_y_contacto/', views.ayuda_y_contacto, name='ayuda_y_contacto'),

]

