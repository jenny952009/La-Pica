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



"""
from django.contrib import admin
from .models import Carrito, CarritoItem
from django.apps import AppConfig


# Register your models here.
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('carrito_id', 'fecha_agregado')
    search_fields = ('carrito_id', 'fecha_agregado')  # Campos por los que puedes buscar
    list_filter = ['fecha_agregado']  # Opcional: filtros en el lateral

class Meta:
        model = Carrito

class CarritoItemAdmin(admin.ModelAdmin):
    list_display = ('producto', 'carro', 'cantidad', 'is_active')
    search_fields = ('carro','producto' )  # Campos por los que puedes buscar
    list_filter =  ['carro','producto' ] # Opcional: filtros en el lateral

#Se agrego de rama pam
class CarritoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carrito'


admin.site.register(Carrito, CarritoAdmin)
admin.site.register(CarritoItem, CarritoItemAdmin)


----------------------


# Administrador para el modelo Carrito
class CarritoAdmin(admin.ModelAdmin):
    # Mostrar los campos de la lista en el panel de administración
    list_display = ('carrito_id', 'fecha_agregado')

    # Configurar el campo de búsqueda para el id del carrito
    search_fields = ['carrito_id']  # Buscar por el id del carrito

    # Filtro de lista por fecha
    list_filter = ('fecha_agregado',)

admin.site.register(Carrito, CarritoAdmin)
"""