# ventas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('ventas/grafico/', views.ventas_por_fecha, name='grafico_ventas'),  # Ruta para el gráfico
]
