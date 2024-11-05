from django.urls import path
from . import views

urlpatterns = [
    path('reservaciones/', views.reservacion, name='reservacion'),  
    path('Descargar_Ticket/', views.Descargar_Ticket, name='Descargar_Ticket'),
]

