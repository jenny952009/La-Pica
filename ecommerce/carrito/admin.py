from django.contrib import admin
from django.utils.html import format_html
from .models import Carrito, CarritoItem

# Administrador para el modelo Carrito
class CarritoAdmin(admin.ModelAdmin):
    list_display = ['carrito_id', 'fecha_agregado', 'total_items']
    list_filter = ['fecha_agregado']
    search_fields = ['carrito_id']
    list_per_page = 20

    # Método para calcular el total de items en el carrito
    def total_items(self, obj):
        return obj.carritoitem_set.count()  # Cuenta los items relacionados con el carrito
    total_items.short_description = 'Total de Items'

# Administrador para el modelo CarritoItem
class CarritoItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'producto', 'cantidad', 'sub_total', 'is_active']
    list_filter = ['is_active']
    search_fields = ['producto__producto_nombre', 'user__email']
    list_per_page = 20

    # Método para calcular el subtotal del carrito item
    def sub_total(self, obj):
        return obj.sub_total()  # Usa la función sub_total que ya está definida
    sub_total.short_description = 'Subtotal'

# Registrar los modelos en el admin
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(CarritoItem, CarritoItemAdmin)
