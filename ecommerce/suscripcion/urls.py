# suscripcion/urls.py
from django.urls import path
#from .views import suscribir
#from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('suscribir/', views.suscribir, name='suscribir'),
    path('exito/',views.exito, name='exito'),
    path('desuscribir/<str:email>/', views.desuscribir, name='desuscribir'),

]
    
