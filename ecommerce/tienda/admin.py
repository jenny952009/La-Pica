from django.contrib import admin
from django.urls import reverse
from .models import Producto, ReseñaRating, ProductoGaleria
from django.utils.html import format_html

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('mostrar_imagen', 'producto_nombre', 'precio', 'stock', 'categoria', 'is_available', 'created_date','opciones_crud')
    list_editable = ('precio', 'stock', 'is_available')  # Permite editar directamente desde la lista
    list_filter = ('categoria', 'is_available', 'created_date')
    search_fields = ('producto_nombre', 'categoria__nombre')
    prepopulated_fields = {'slug': ('producto_nombre',)}  # Genera el slug automáticamente

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

class ReseñaRatingAdmin(admin.ModelAdmin):
    list_display = ('producto', 'user', 'titulo', 'rating', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'rating')
    search_fields = ('producto__producto_nombre', 'user__email', 'titulo')


class ProductoGaleriaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'mostrar_galeria','get_stars')
    ordering = ('-producto__reseñarating__rating',)  # Orden descendente por estrellas promedio

    search_fields = ('producto__producto_nombre',)

    
    def mostrar_galeria(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" style="border-radius: 5px;" />', obj.image.url)
        return "Sin imagen"

    mostrar_galeria.short_description = "Galería"

# Registro de los modelos
admin.site.register(Producto, ProductoAdmin)
admin.site.register(ReseñaRating, ReseñaRatingAdmin)
admin.site.register(ProductoGaleria, ProductoGaleriaAdmin)
