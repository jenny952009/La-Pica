from django.contrib import admin
from .models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
    # Configurar los campos predefinidos para generar automáticamente el slug
    prepopulated_fields = {'slug': ('categoria_nombre',)}  # Generar automáticamente el slug a partir de 'categoria_nombre'
    
    # Configurar la lista de campos para mostrar en el panel de administración
    list_display = ('categoria_nombre', 'slug', 'cat_image_preview')  # Muestra el nombre, slug y vista previa de la imagen
    
    # Configurar la búsqueda de categorías por nombre y por slug
    search_fields = ['categoria_nombre', 'slug']  # Se puede buscar por nombre de categoría y por slug
    
    # Configurar los filtros en el panel de administración (por ejemplo, por nombre de categoría)
    list_filter = ('categoria_nombre',)  # Puedes agregar más filtros según sea necesario
    
    # Método para mostrar una vista previa de la imagen de la categoría
    def cat_image_preview(self, obj):
        if obj.cat_image:
            return f'<img src="{obj.cat_image.url}" width="50" height="50" />'
        return "Sin imagen"
    
    # Permitir el uso de etiquetas HTML para la vista previa de la imagen
    cat_image_preview.allow_tags = True  # Permitir etiquetas HTML
    cat_image_preview.short_description = 'Vista previa de la imagen'  # Nombre de la columna
    
# Registrar el modelo 'Categoria' con su administrador personalizado
admin.site.register(Categoria, CategoriaAdmin)





