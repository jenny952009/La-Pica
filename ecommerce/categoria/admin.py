from django.contrib import admin  # Importa el módulo admin de Django para poder registrar modelos en el panel de administración
from .models import Categoria

# Register your models here.
# Definición de la clase de administración para el modelo Categoria

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('categoria_nombre',)}     # Campo que permite generar automáticamente el slug basado en el nombre de la categoría
    list_display = ('categoria_nombre', 'slug')


# Registro del modelo Categoria junto con su clase de administración

admin.site.register(Categoria, CategoriaAdmin)
