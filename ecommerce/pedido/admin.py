from django.contrib import admin
from .models import Pago, Pedido, PedidoProducto
from django.utils.html import format_html


# Filtro personalizado para productos en pedidos
class ProductoFilter(admin.SimpleListFilter):
    title = 'Producto'
    parameter_name = 'producto'

    def lookups(self, request, model_admin):
        productos = set(
            PedidoProducto.objects.values_list('producto__id', 'producto__producto_nombre')
        )
        return [(producto[0], producto[1]) for producto in productos]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(productos__producto__id=self.value())
        return queryset


# Inline para mostrar los productos asociados a un pedido
class PedidoProductoInline(admin.TabularInline):
    model = PedidoProducto
    readonly_fields = ('producto', 'cantidad', 'producto_precio', 'ordered')  # Solo lectura
    extra = 0  # Sin filas adicionales
    can_delete = False  # Deshabilita eliminación desde el inline
    verbose_name = "Producto"
    verbose_name_plural = "Productos en el Pedido"


# Administrador de Pedido
class PedidoAdmin(admin.ModelAdmin):
    list_display = [
        'pedido_numero', 'usuario_pedido',  
        'mostrar_imagen', 'telefono', 'email', 'direccion_completa', 'pedido_total', 'impuesto', 
         'estado_accion_cliente', 'is_ordered', 'created_at', 'updated_at','pedido_nota'
    ]
    list_filter = ['status', 'is_ordered', 'created_at', 'updated_at', ProductoFilter]  # Filtro por producto
    search_fields = ['pedido_numero', 'nombre', 'apellido', 'telefono', 'email']  # Búsqueda
    list_per_page = 20  # Paginación
    inlines = [PedidoProductoInline]  # Inline para productos del pedido
    actions = ['mark_as_approved',  'mark_as_completed','mark_as_in_New', 'mark_as_Acepted','mark_as_in_Completed', 'mark_as_Cancelled',]

    # Función para mostrar el usuario asociado al pedido
    def usuario_pedido(self, obj):
        return obj.user.nombre_completo() if obj.user else "No asignado"
    usuario_pedido.short_description = 'Usuario del Pedido'

    # Función para mostrar los productos pedidos y sus cantidades
    def mostrar_imagen(self, obj):
        # Obtener los productos relacionados al pedido
        productos = PedidoProducto.objects.filter(pedido=obj)
        imagenes = []

        for pedido_producto in productos:
            if pedido_producto.producto.images:
                imagenes.append(format_html('<img src="{}" width="50" style="border-radius: 5px;" />', pedido_producto.producto.images.url))

        if imagenes:
            return format_html(" ".join(imagenes))  # Muestra todas las imágenes de los productos en el pedido
        return "Sin imagen"

    mostrar_imagen.short_description = "Imagenes de productos"
    
    # Función para mostrar el estado del pedido con colores
    def estado_accion_cliente(self, obj):
        estado_colores = {
            'New': 'blue',
            'Accepted': 'green',
            'Completed': 'gray',
            'Cancelled': 'red'
        }
        color = estado_colores.get(obj.status, 'orange')
        return format_html('<span style="color: {};">{}</span>', color, obj.get_status_display())
    estado_accion_cliente.short_description = "Estado del Pedido"


    def mark_as_New(self, request, queryset):
        queryset.update(status='New')
        self.message_user(request, "Estado de pedido Nuevo o Pendiente")
    mark_as_New.short_description = "Marcar como Aprobado"

    def mark_as_in_Accepted(self, request, queryset):
        queryset.update(status='Accepted')
        self.message_user(request, "Estado de pedido actualizado a En Preparación.")
    mark_as_in_Accepted.short_description = "Marcar como En Preparación"

    def mark_as_cancelled(self, request, queryset):
        queryset.update(status='Cancelled')
        self.message_user(request, "Estado de pedido actualizado ha no realizado.")
    mark_as_cancelled.short_description = "Marcar como Cancelado"

    def mark_as_completed(self, request, queryset):
        queryset.update(status='Completed')
        self.message_user(request, "Estado de pedido Finalizado entregado.")
    mark_as_completed.short_description = "Marcar como Terminado"


# Administrador de Pago
class PagoAdmin(admin.ModelAdmin):
    list_display = ['user', 'pago_id', 'pago_method', 'monto_id', 'status', 'created_at']
    list_filter = ['status', 'pago_method', 'created_at']  # Filtros
    search_fields = ['pago_id', 'user__email']  # Búsqueda
    list_per_page = 20  # Paginación


from django.contrib import admin
from .models import PedidoProducto

class PedidoProductoAdmin(admin.ModelAdmin):
    list_display = [
        'user', 
        'producto', 
        'cantidad', 
        'producto_precio', 
        'total_pago', 
        'forma_pago', 
        'ordered', 
        'created_at', 
        'updated_at'
    ]
    
    # Filtros
    list_filter = ['ordered', 'created_at', 'cantidad', 'producto']

    # Búsqueda
    search_fields = ['pedido__pedido_numero', 'producto__producto_nombre']

    # Paginación
    list_per_page = 20

    # Método para calcular el total del producto
    def total_producto(self, obj):
        return obj.cantidad * obj.producto_precio
    total_producto.short_description = "Total Producto"  # Etiqueta para el método

    # Método para calcular el total del pedido (suma de todos los productos relacionados)
    def total_pago(self, obj):
        return obj.pedido.pedido_total  # Total del pedido en el modelo Pedido
    total_pago.short_description = "Total Pedido"

    # Método para mostrar la forma de pago
    def forma_pago(self, obj):
        if obj.pedido.pago:
            return obj.pedido.pago.pago_method  # Forma de pago relacionada con el pedido
        return "Sin forma de pago"
    forma_pago.short_description = "Forma de Pago"



# Registro de los modelos en el administrador
admin.site.register(Pago, PagoAdmin)  # Registro de Pago
admin.site.register(Pedido, PedidoAdmin)  # Registro de Pedido
admin.site.register(PedidoProducto, PedidoProductoAdmin)  # Registro de PedidoProducto
