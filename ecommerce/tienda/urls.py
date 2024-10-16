from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name="tienda"),
    path('categoria/<slug:category_slug>/', views.tienda, name="productos_por_categoria"),
    path('categoria/<slug:category_slug>/<slug:product_slug>/', views.producto_detalle, name="producto_detalle"),
    path('search/', views.search, name='search'),
    path('submit_review/<int:producto_id>/', views.submit_review, name='submit_review'),
]
