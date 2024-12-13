from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('pago/', views.pago, name='pago'),
    path('pedido_completo/', views.pedido_completo, name='pedido_completo'),
    path('dashboard_ventas/',views.dashboard_ventas, name='dashboard_ventas')
]
