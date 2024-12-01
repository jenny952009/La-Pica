"""""
from django.contrib import admin
from django.utils.html import format_html
from .models import Venta  # Suponiendo que tienes un modelo Venta en ventas
from pedido.models import Pedido, PedidoProducto
from django.db.models import Sum

# Función para obtener el total de ventas
def obtener_total_ventas():
    total_ventas = Pedido.objects.filter(status='Completed').aggregate(total=Sum('pedido_total'))
    return total_ventas['total'] or 0

# Función para obtener las ventas por producto
def obtener_ventas_por_producto():
    ventas_por_producto = PedidoProducto.objects.values('producto__producto_nombre').annotate(total_ventas=Sum('producto_precio'))
    return ventas_por_producto

# Vista de Ventas 
class VentaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'total_venta', 'ventas_por_producto')
    list_filter = ('pedido__status',)  # Filtro por estado de venta (relacionado con el modelo Pedido)
    search_fields = ('producto__producto_nombre', 'pedido__pedido_numero')  # Permite buscar por producto o número de pedido
    date_hierarchy = 'pedido__created_at'  # Filtro por fecha (relacionado con el modelo Pedido)

    def total_venta(self, obj):
        return obtener_total_ventas()

    def ventas_por_producto(self, obj):
        ventas = obtener_ventas_por_producto()
        return format_html('<br>'.join([f"{venta['producto__producto_nombre']}: {venta['total_ventas']}" for venta in ventas]))

    ventas_por_producto.short_description = 'Ventas por Producto'

# Registrar las funciones en el admin
admin.site.register(Venta, VentaAdmin)
"""