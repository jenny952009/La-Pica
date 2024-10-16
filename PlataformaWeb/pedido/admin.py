from django.contrib import admin
from .models import Pago, Pedido, PedidoProducto


# Register your models here.
class PedidoProductoInline(admin.TabularInline):
    model = PedidoProducto
    readonly_fields = ('pago', 'user', 'producto', 'cantidad', 'producto_precio', 'ordered')  # Todos estos campos existen en el modelo PedidoProducto
    extra = 0


class PedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido_numero', 'nombre_completo', 'telefono', 'email', 'ciudad', 'pedido_total', 'impuesto', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['pedido_numero', 'nombre', 'apellido', 'telefono', 'email']
    list_per_page = 20
    inlines = [PedidoProductoInline]


admin.site.register(Pago)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(PedidoProducto)
