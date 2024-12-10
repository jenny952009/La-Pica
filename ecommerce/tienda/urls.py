from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name="tienda"),  # URL principal para la tienda
    path('categoria/<slug:category_slug>/', views.tienda, name="productos_por_categoria"),
    path('categoria/<slug:category_slug>/<slug:product_slug>/', views.producto_detalle, name="producto_detalle"),# URL para la vista de detalles de un producto
    path('search/', views.search, name='search'),# URL de búsqueda
    path('agregar_reseña/<int:producto_id>/', views.agregar_reseña, name='agregar_reseña'),# URL para agregar una reseña a un producto
    path('actualizar-productos/', views.actualizar_productos, name='actualizar_productos'),



]

