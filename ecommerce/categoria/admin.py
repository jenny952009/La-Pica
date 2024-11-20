from django.contrib import admin
from .models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('categoria_nombre',)}  # Generar automáticamente el slug
    list_display = ('categoria_nombre', 'slug', 'cat_image_preview')  # Agregar la vista previa de la imagen

    # Método para mostrar una vista previa de la imagen en la lista de categorías
    def cat_image_preview(self, obj):
        if obj.cat_image:
            return f'<img src="{obj.cat_image.url}" width="50" height="50" />'
        return "Sin imagen"
    
    cat_image_preview.allow_tags = True  # Permitir el uso de etiquetas HTML
    cat_image_preview.short_description = 'Vista previa de la imagen'  # Nombre en la columna

# Registrar el modelo y la clase admin
admin.site.register(Categoria, CategoriaAdmin)
