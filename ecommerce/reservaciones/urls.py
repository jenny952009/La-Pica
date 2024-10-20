from django.urls import path
from . import views

urlpatterns = [
    path('reservaciones/', views.reservacion, name='reservacion'),  
    path('descargar_boleta/', views.descargar_boleta, name='descargar_boleta'),
]

