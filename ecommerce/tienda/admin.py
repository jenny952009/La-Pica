from django.contrib import admin
from django.urls import reverse
from .models import Producto, ReseñaRating, ProductoGaleria
from django.utils.html import format_html

# Definición del Inline para ProductoGaleria
class ProductoGaleriaInLine(admin.TabularInline):
    model = ProductoGaleria  # El modelo que quieres editar de manera inline
    extra = 1  # Número de formularios vacíos adicionales que se mostrarán
    fields = ('image',)  # Campos que deseas mostrar, en este caso la imagen
    readonly_fields = ('image',)  # Puedes hacerlo solo lectura si lo prefieres
# Paginación de 20 elementos por página
    list_per_page = 20

# Definición del admin para Producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('mostrar_imagen', 'producto_nombre', 'precio', 'stock', 'categoria', 'is_available', 'created_date','opciones_crud')
    list_editable = ('precio', 'stock', 'is_available')  # Permite editar directamente desde la lista
    list_filter = ('producto_nombre','categoria__categoria_nombre','is_available', 'created_date')
    search_fields = ('producto_nombre', 'categoria__categoria_nombre')
    prepopulated_fields = {'slug': ('producto_nombre',)}  # Genera el slug automáticamente
    # Paginación de 20 elementos por página
    list_per_page = 20

    # Incluir el Inline para ProductoGaleria
    inlines = [ProductoGaleriaInLine]

    actions = ['marcar_como_disponible', 'marcar_como_no_disponible']

    def marcar_como_disponible(self, request, queryset):
        queryset.update(is_available=True)
        self.message_user(request, "Los productos seleccionados ahora están disponibles.")

    def marcar_como_no_disponible(self, request, queryset):
        queryset.update(is_available=False)
        self.message_user(request, "Los productos seleccionados ahora no están disponibles.")

    marcar_como_disponible.short_description = "Marcar como disponible"
    marcar_como_no_disponible.short_description = "Marcar como no disponible"

    def mostrar_imagen(self, obj):
        if obj.images:
            return format_html('<img src="{}" width="50" style="border-radius: 5px;" />', obj.images.url)
        return "Sin imagen"

    mostrar_imagen.short_description = "Imagen"
    
    # Añade una columna con enlaces para las opciones de CRUD
    def opciones_crud(self, obj):
        return format_html(
            '<a class="button" href="{}">Editar</a>&nbsp;'
            '<a class="button" href="{}">Eliminar</a>',
            reverse('admin:tienda_producto_change', args=[obj.id]),  # Enlace para editar
            reverse('admin:tienda_producto_delete', args=[obj.id])   # Enlace para eliminar
        )
    
    opciones_crud.short_description = "Opciones"

# ReseñaRatingAdmin y ProductoGaleriaAdmin como ya los tienes definidos
class ReseñaRatingAdmin(admin.ModelAdmin):
    list_display = ('producto', 'user', 'titulo','reseña', 'rating', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'rating')
    search_fields = ('producto__producto_nombre', 'user__email', 'titulo')
    readonly_fields = ('created_at',)  # Esto hace que 'created_at' no sea editable

    # Paginación de 20 elementos por página
    list_per_page = 20


class ProductoGaleriaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'mostrar_galeria','cantidad_imagenes','get_stars')
    ordering = ('-producto__reseñarating__rating',)  # Orden descendente por estrellas promedio

    search_fields = ('producto__producto_nombre',)
# Paginación de 20 elementos por página
    list_per_page = 20
    
    def mostrar_galeria(self, obj):
        # Obtener todas las imágenes asociadas al producto
        galeria = ProductoGaleria.objects.filter(producto=obj.producto)
        
       # Crear HTML para mostrar todas las miniaturas
        if galeria.exists():
            imagenes_html = ''.join(
                f'<img src="{imagen.image.url}" width="50" style="border-radius: 5px; margin-right: 5px;" />'
                for imagen in galeria
            )
            return format_html(imagenes_html)
        
        return "Sin imágenes"

    mostrar_galeria.short_description = "Galería"


    # Función para contar la cantidad de imágenes asociadas a cada producto
    def cantidad_imagenes(self, obj):
        count = ProductoGaleria.objects.filter(producto=obj.producto).count()
        return count

    cantidad_imagenes.short_description = "Cantidad de imágenes"


# Registro de los modelos
admin.site.register(Producto, ProductoAdmin)
admin.site.register(ReseñaRating, ReseñaRatingAdmin)
admin.site.register(ProductoGaleria, ProductoGaleriaAdmin)
