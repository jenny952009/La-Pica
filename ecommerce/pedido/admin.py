from django.contrib import admin
from .models import Pago, Pedido, PedidoProducto
from django.utils.html import format_html
from django.db.models import Sum

# Inline para mostrar los productos en el detalle del pedido
class PedidoProductoInline(admin.TabularInline):
    model = PedidoProducto
    readonly_fields = ('producto', 'cantidad', 'producto_precio', 'ordered')  # Solo lectura para estos campos
    extra = 0  # No agregar filas vacías adicionales

# Administrador de Pedido
class PedidoAdmin(admin.ModelAdmin):
    list_display = [
        'pedido_numero', 'nombre_completo', 'usuario_pedido', 'telefono', 'email', 'ciudad', 'pedido_total', 
        'impuesto', 'status', 'estado_accion_cliente', 'is_ordered', 'created_at', 'updated_at', 'mostrar_imagen_producto'
    ]
    list_filter = ['status', 'is_ordered', 'created_at', 'updated_at']  # Filtros por estado, ordenado y fechas
    search_fields = ['pedido_numero', 'nombre', 'apellido', 'telefono', 'email']  # Búsqueda por diversos campos
    list_per_page = 20  # Paginación de 20 elementos por página
    inlines = [PedidoProductoInline]  # Inline para mostrar los productos del pedido

    # Función para mostrar el usuario del pedido
    def usuario_pedido(self, obj):
        return obj.user.nombre_completo() if obj.user else "No asignado"
    usuario_pedido.short_description = 'Usuario del Pedido'

    # Función para mostrar la acción del cliente
    def estado_accion_cliente(self, obj):
        if obj.status == 'New':
            return format_html('<span style="color: blue;">Nuevo</span>')
        elif obj.status == 'Accepted':
            return format_html('<span style="color: green;">Aceptado</span>')
        elif obj.status == 'Completed':
            return format_html('<span style="color: gray;">Completado</span>')
        elif obj.status == 'Cancelled':
            return format_html('<span style="color: red;">Cancelado</span>')
        else:
            return format_html('<span style="color: orange;">Desconocido</span>')
    estado_accion_cliente.short_description = "Estado Acción Cliente"

    # Función para mostrar el total del pedido
    def mostrar_imagen_producto(self, obj):
        if obj.productos.exists():
            producto = obj.productos.first().producto  # Obtiene el primer producto del pedido
            if producto.images:
                return format_html('<img src="{}" width="50" height="50"/>', producto.images.url)
        return "No image"
    mostrar_imagen_producto.short_description = "Imagen del Producto"

# Administrador de Pago
class PagoAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'pago_id', 'pago_method', 'monto_id', 'status', 'created_at'
    ]
    list_filter = ['status', 'pago_method', 'created_at']  # Filtros por estado, método de pago y fecha
    search_fields = ['pago_id', 'user__nombre_completo']  # Búsqueda por ID de pago y nombre del usuario
    list_per_page = 20  # Paginación para los pagos

# Administrador de PedidoProducto
class PedidoProductoAdmin(admin.ModelAdmin):
    list_display = [
        'pedido', 'producto', 'cantidad', 'producto_precio', 'ordered', 'created_at', 'updated_at'
    ]
    list_filter = ['ordered', 'created_at', 'updated_at']  # Filtros por estado de orden y fechas
    search_fields = ['pedido__pedido_numero', 'producto__producto_nombre']  # Búsqueda por número de pedido y producto
    list_per_page = 20  # Paginación para los productos de los pedidos

# Registrar los modelos en el admin
admin.site.register(Pago, PagoAdmin)  # Registro de Pago
admin.site.register(Pedido, PedidoAdmin)  # Registro de Pedido con su admin
admin.site.register(PedidoProducto, PedidoProductoAdmin)  # Registro de PedidoProducto
