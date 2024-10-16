from django.urls import path
from . import views

urlpatterns = [
    path('', views.carro, name='carro'),
    path('agregar_carrito/<int:producto_id>', views.agregar_carrito, name='agregar_carrito'),
    path('remover_carrito/<int:producto_id>/<int:carrito_item_id>', views.remover_carrito, name='remover_carrito'),
    path('remover_carrito_item/<int:producto_id>/<int:carrito_item_id>', views.remover_carrito_item, name='remover_carrito_item'),
    path('checkout/', views.checkout, name="checkout"),
]
