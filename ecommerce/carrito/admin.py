from django.contrib import admin
from .models import Carrito, CarritoItem

# Inline para CarritoItem
class CarritoItemInline(admin.TabularInline):  # Usa TabularInline para una presentación compacta en tabla
    model = CarritoItem
    extra = 0  # No agrega filas vacías adicionales por defecto
    fields = ['user', 'producto', 'cantidad', 'is_active', 'sub_total']  # Campos que se mostrarán en el inline
    readonly_fields = ['sub_total']  # El subtotal es de solo lectura
    can_delete = True  # Permite eliminar items desde el inline

    # Método para calcular el subtotal en el inline
    def sub_total(self, obj):
        return f"${obj.sub_total():,.2f}"  # Calcula y da formato al subtotal
    sub_total.short_description = 'Subtotal'

# Administrador para Carrito
class CarritoAdmin(admin.ModelAdmin):
    list_display = ['carrito_id', 'fecha_agregado']  # Muestra el ID del carrito y la fecha de agregado
    list_filter = ['fecha_agregado']  # Filtro por fecha de agregado
    search_fields = ['carrito_id']  # Búsqueda por ID de carrito
    inlines = [CarritoItemInline]  # Agrega los items del carrito como inline

# Registrar solo Carrito en el admin
admin.site.register(Carrito, CarritoAdmin)
