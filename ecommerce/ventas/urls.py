from django.urls import path
from . import views

urlpatterns = [
    path('ventas_diarias/', views.ventas_diarias, name='ventas_diarias'),
    # Otras rutas para la app de ventas
]
