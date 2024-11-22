from django.shortcuts import render
from import_export import resources # type: ignore
from import_export.admin import ExportMixin # type: ignore

from django.contrib import admin
from .models import Venta, Cupon
from django.urls import path
from django.template.response import TemplateResponse
from django.db.models import Count

@admin.register(Cupon)
class CuponAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descuento', 'activo', 'fecha_expiracion')
    list_filter = ('activo', 'fecha_expiracion')
    search_fields = ('codigo',)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('user', 'producto', 'cantidad', 'total_venta', 'estado_pedido', 'region', 'pais', 'fecha_venta')
    list_filter = ('fecha_venta', 'estado_pedido', 'region', 'pais')
    search_fields = ('user__email', 'producto__producto_nombre')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('grafico/', self.admin_site.admin_view(self.grafico_view), name='ventas_grafico'),
        ]
        return custom_urls + urls

    
    def grafico_view(self, request):
        ventas = Venta.objects.values('estado_pedido').annotate(total=Count('id'))
        estados = [venta['estado_pedido'] for venta in ventas]
        datos = [venta['total'] for venta in ventas]
        context = {
            'estados': estados,
            'datos': datos,
        }
        #return TemplateResponse(request, 'admin/ventas/grafico.html', context)
        return render(request, 'ventas/grafico.html')


class VentaResource(resources.ModelResource):
    class Meta:
        model = Venta
        fields = ('user__email', 'producto__producto_nombre', 'cantidad', 'total_venta', 'estado_pedido', 'region', 'pais', 'fecha_venta')
