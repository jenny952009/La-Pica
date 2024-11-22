from django.contrib import admin
from .models import Empleado
from .forms import EmpleadoForm


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    form = EmpleadoForm  # Asigna el formulario personalizado
    list_display = ('usuario','nombre_completo', 'cargo', 'sueldo', 'fecha_contrato', 'activo', 'entrada', 'salida', 'entrada_almuerzo', 'salida_almuerzo')
    list_filter = ('activo', 'cargo')
    search_fields = ('usuario__username', 'cargo')
    fieldsets = (
        ('Información del empleado', {
            'fields': ('usuario', 'rut','cargo', 'sueldo', 'fecha_contrato', 'activo')
        }),
        ('Horarios', {
            'fields': ('entrada', 'salida', 'entrada_almuerzo', 'salida_almuerzo')
        }),
    )

    # Definir un método adicional para mostrar el nombre completo
    def nombre_completo(self, obj):
        return f"{obj.usuario.nombre} {obj.usuario.apellido}"
    nombre_completo.short_description = 'Nombre Completo'

"""
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'cargo', 'sueldo', 'horario', 'fecha_contrato', 'activo']
    list_filter = ['activo', 'cargo', 'fecha_contrato']
    search_fields = ['usuario__nombre', 'usuario__apellido', 'cargo']
    ordering = ['fecha_contrato']
    list_per_page = 20
    fieldsets = (
        (None, {'fields': ('usuario', 'cargo')}),
        ('Información laboral', {'fields': ('sueldo', 'horario', 'fecha_contrato', 'activo')}),
    )
"""