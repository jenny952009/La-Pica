from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('tienda/', include('tienda.urls')),
    path('carro/', include('carrito.urls')),
    path('cuenta/', include('cuenta.urls')),
    path('pedido/', include('pedido.urls')),
    path('', include('reservaciones.urls')),
    path('suscripcion/', include('suscripcion.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# Agregar la configuración para servir archivos de medios durante el desarrollo

