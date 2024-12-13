from django.contrib import admin
from .models import Carrito, CarritoItem
from tienda.models import Producto
from cuenta.models import Cuenta


# Administrador para el modelo CarritoItem
class CarritoItemAdmin(admin.ModelAdmin):
    # Mostrar todos los campos en la lista de administración
    list_display = ('user', 'producto', 'carro', 'cantidad', 'is_active', 'sub_total')

    # Configurar la búsqueda por producto, id del carrito y fecha agregada
    search_fields = ['carro__carrito_id', 'producto__nombre', 'carro__fecha_agregado']  # Búsqueda por carrito_id, producto y fecha

    # Filtros para los campos que podemos usar en la lista de administración
    list_filter = ('carro__fecha_agregado', 'producto', 'is_active')

    # Permitir que se editen todos los campos del modelo CarritoItem
    fieldsets = (
        (None, {
            'fields': ('user', 'producto', 'carro', 'cantidad', 'is_active')
        }),
        ('Total', {
            'fields': ('sub_total',),
            'classes': ('collapse',)
        }),
    )

    # Incluir el método sub_total en la lista
    readonly_fields = ('sub_total',)  # Para mostrar el sub_total como solo lectura

admin.site.register(CarritoItem, CarritoItemAdmin)


