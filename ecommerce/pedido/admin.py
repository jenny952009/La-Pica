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
    verbose_name = "Producto en el Pedido"
    verbose_name_plural = "Productos en el Pedido"


# Administrador de Pedido
class PedidoAdmin(admin.ModelAdmin):
    list_display = [
        'pedido_numero', 'nombre_completo', 'usuario_pedido',  
        'fotos_productos', 'telefono', 'email', 'ciudad', 'pedido_total', 'impuesto', 
        'status', 'estado_accion_cliente', 'is_ordered', 'created_at', 'updated_at'
    ]
    list_filter = ['status', 'is_ordered', 'created_at', 'updated_at', ProductoFilter]  # Filtro por producto
    search_fields = ['pedido_numero', 'nombre', 'apellido', 'telefono', 'email']  # Búsqueda
    list_per_page = 20  # Paginación
    inlines = [PedidoProductoInline]  # Inline para productos del pedido

    # Función para mostrar el usuario asociado al pedido
    def usuario_pedido(self, obj):
        return obj.user.nombre_completo() if obj.user else "No asignado"
    usuario_pedido.short_description = 'Usuario del Pedido'

    # Función para mostrar los productos pedidos y sus cantidades
    def fotos_productos(self, obj):
        productos = obj.productos.all()  # Obtener los productos asociados al pedido
        imagenes = []

        for pedido_producto in productos:
        # Asegúrate de que `images` exista en el producto y tenga una URL
            if pedido_producto.producto.images and hasattr(pedido_producto.producto.images, 'url'):
                imagen_url = pedido_producto.producto.images.url
                imagenes.append(format_html(
                    '<img src="{}" width="50" height="50" style="margin-right: 5px;"/>',
                    imagen_url
                ))

    # Si hay imágenes, las devuelve. Si no, muestra "Sin imágenes"
        return format_html("".join(imagenes)) if imagenes else "Sin imágenes"
    fotos_productos.short_description = "Fotos de Productos"

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


# Administrador de Pago
class PagoAdmin(admin.ModelAdmin):
    list_display = ['user', 'pago_id', 'pago_method', 'monto_id', 'status', 'created_at']
    list_filter = ['status', 'pago_method', 'created_at']  # Filtros
    search_fields = ['pago_id', 'user__email']  # Búsqueda
    list_per_page = 20  # Paginación


# Administrador de PedidoProducto
class PedidoProductoAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'producto', 'cantidad', 'producto_precio', 'ordered', 'created_at', 'updated_at'
    ]
    list_filter = ['ordered', 'created_at', 'updated_at', 'producto']  # Filtros
    search_fields = ['pedido__pedido_numero', 'producto__producto_nombre']  # Búsqueda
    list_per_page = 20  # Paginación


# Registro de los modelos en el administrador
admin.site.register(Pago, PagoAdmin)  # Registro de Pago
admin.site.register(Pedido, PedidoAdmin)  # Registro de Pedido
admin.site.register(PedidoProducto, PedidoProductoAdmin)  # Registro de PedidoProducto
""""
--------------
from django.contrib import admin
from .models import Pago, Pedido, PedidoProducto
from django.utils.html import format_html
from django.db.models import Q


# Filtro personalizado para productos en pedidos
class ProductoFilter(admin.SimpleListFilter):
    title = 'Producto'
    parameter_name = 'producto'

    def lookups(self, request, model_admin):
        # Genera una lista de productos disponibles en los pedidos
        productos = set(
            PedidoProducto.objects.values_list('producto__id', 'producto__producto_nombre')
        )
        return [(producto[0], producto[1]) for producto in productos]

    def queryset(self, request, queryset):
        # Filtra los pedidos que contienen el producto seleccionado
        if self.value():
            return queryset.filter(productos__producto__id=self.value())
        return queryset


# Inline para mostrar los productos asociados a un pedido
class PedidoProductoInline(admin.TabularInline):
    model = PedidoProducto
    readonly_fields = ('producto', 'cantidad', 'producto_precio', 'ordered')  # Solo lectura
    extra = 0  # Sin filas adicionales
    can_delete = False  # Deshabilita eliminación desde el inline
    verbose_name = "Producto en el Pedido"
    verbose_name_plural = "Productos en el Pedido"


# Administrador de Pedido
class PedidoAdmin(admin.ModelAdmin):
    list_display = [
        'pedido_numero', 'nombre_completo', 'usuario_pedido', 'productos_pedidos', 
        'fotos_productos', 'telefono', 'email', 'ciudad', 'pedido_total', 'impuesto', 
        'status', 'estado_accion_cliente', 'is_ordered', 'created_at', 'updated_at'
    ]
    list_filter = ['status', 'is_ordered', 'created_at', 'updated_at', ProductoFilter]  # Añade filtro por producto
    search_fields = ['pedido_numero', 'nombre', 'apellido', 'telefono', 'email']  # Búsqueda
    list_per_page = 20  # Paginación
    inlines = [PedidoProductoInline]  # Inline para productos del pedido

    # Función para mostrar el usuario asociado al pedido
    def usuario_pedido(self, obj):
        return obj.user.nombre_completo() if obj.user else "No asignado"
    usuario_pedido.short_description = 'Usuario del Pedido'

    # Función para mostrar los productos pedidos y sus cantidades
    def productos_pedidos(self, obj):
        productos = obj.productos.all()  # Relación definida en `related_name='productos'` en el modelo
        detalles = [
            f"{pedido_producto.producto.producto_nombre} ({pedido_producto.cantidad})"
            for pedido_producto in productos
        ]
        return ", ".join(detalles) if detalles else "Sin productos"
    productos_pedidos.short_description = 'Productos Pedidos'

    # Función para mostrar imágenes de los productos
    def fotos_productos(self, obj):
        productos = obj.productos.all()
        imagenes = [
            format_html('<img src="{}" width="50" height="50" style="margin-right: 5px;"/>', 
                        pedido_producto.producto.images.url)
            for pedido_producto in productos if pedido_producto.producto.images
        ]
        return format_html("".join(imagenes)) if imagenes else "Sin imágenes"
    fotos_productos.short_description = "Fotos de Productos"

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


# Administrador de Pago
class PagoAdmin(admin.ModelAdmin):
    list_display = ['user', 'pago_id', 'pago_method', 'monto_id', 'status', 'created_at']
    list_filter = ['status', 'pago_method', 'created_at']  # Filtros
    search_fields = ['pago_id', 'user__email']  # Búsqueda
    list_per_page = 20  # Paginación


# Administrador de PedidoProducto
class PedidoProductoAdmin(admin.ModelAdmin):
    list_display = [
        'pedido', 'producto', 'cantidad', 'producto_precio', 'ordered', 'created_at', 'updated_at'
    ]
    list_filter = ['ordered', 'created_at', 'updated_at','producto']  # Filtros
    search_fields = ['pedido__pedido_numero', 'producto__producto_nombre']  # Búsqueda
    list_per_page = 20  # Paginación


# Registrar modelos en el administrador
admin.site.register(Pago, PagoAdmin)  # Registro de Pago
admin.site.register(Pedido, PedidoAdmin)  # Registro de Pedido
admin.site.register(PedidoProducto, PedidoProductoAdmin)  # Registro de PedidoProducto

"""


