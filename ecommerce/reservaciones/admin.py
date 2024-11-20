from django.contrib import admin
from .models import Reserva

# Administrador para el modelo Reserva
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['codigo_reserva', 'nombre', 'apellido', 'numero_mesa', 'fecha_reserva', 'hora_comienzo', 'personas', 'dia_reserva']
    list_filter = ['fecha_reserva', 'hora_comienzo', 'dia_reserva']
    search_fields = ['codigo_reserva', 'nombre', 'apellido', 'email']
    list_per_page = 20

    # Método que calcula la cantidad de personas por reserva
    def cantidad_personas(self, obj):
        return obj.personas
    cantidad_personas.short_description = 'Cantidad de Personas'

# Registrar el modelo en el admin
admin.site.register(Reserva, ReservaAdmin)
