from django.contrib import admin
from .models import Producto, Variacion, RevisarRating, ProductoGaleria
import admin_thumbnails # type: ignore      #revisarrrrrrrrrrr


@admin_thumbnails.thumbnail('image')
class ProductoGaleriaInLine(admin.TabularInline):
    model = ProductoGaleria
    extra = 1


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('producto_nombre', 'precio', 'stock', 'categoria', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('producto_nombre',)}
    inlines = [ProductoGaleriaInLine]


class VariacionAdmin(admin.ModelAdmin):
    list_display = ('producto', 'variacion_categoria', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('producto', 'variacion_categoria', 'variation_value', 'is_active')


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Variacion, VariacionAdmin)
admin.site.register(RevisarRating)
admin.site.register(ProductoGaleria)
