from django.contrib import admin
from .models import Suscripcion

# Administrador para el modelo Suscripcion
class SuscripcionAdmin(admin.ModelAdmin):
    list_display = ['email', 'fecha_creacion', 'activo']
    list_filter = ['activo', 'fecha_creacion']
    search_fields = ['email']
    list_per_page = 20

# Registrar el modelo en el admin
admin.site.register(Suscripcion, SuscripcionAdmin)
