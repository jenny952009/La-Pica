from django.contrib import admin
from .models import Cuenta, UsuarioPerfil
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

# Administrador de Cuenta
class CuentaAdmin(UserAdmin):
    # Asegúrate de incluirlas como campos de solo lectura
    readonly_fields = ('date_joined', 'last_login')
    # Campos que se mostrarán en la lista de usuarios
    list_display = [
        'email', 'username', 'nombre_completo', 'telefono', 'is_active', 'is_staff', 'is_admin', 'date_joined', 'last_login'
    ]
    # Filtros por estado de usuario y fecha
    list_filter = ['is_active', 'is_staff', 'is_admin', 'date_joined']
    # Búsqueda por correo electrónico, nombre completo y username
    search_fields = ['email', 'nombre', 'apellido', 'username']
    # Paginación de 20 elementos por página
    list_per_page = 20
    # Campos editables en el formulario de usuario
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Información personal', {'fields': ('nombre', 'apellido', 'telefono')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superadmin', 'groups', 'user_permissions')}),  # Los permisos
        ('Fechas', {'fields': ('date_joined', 'last_login')}),  # Mostrar las fechas
    )
    
    filter_horizontal = ('groups', 'user_permissions')  # Para permitir múltiples selecciones

    # Campos que se mostrarán en el formulario de edición de usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'nombre', 'apellido', 'telefono', 'is_active', 'is_staff', 'is_admin')}
        ),
    )
    # Función para mostrar el nombre completo del usuario
    def nombre_completo(self, obj):
        return obj.nombre_completo()
    nombre_completo.short_description = 'Nombre Completo'

# Administrador de UsuarioPerfil
class UsuarioPerfilAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de perfiles
    list_display = ['user', 'direccion_completa', 'ciudad', 'region', 'pais', 'profile_picture']
    # Filtros por ciudad y país
    list_filter = ['ciudad', 'pais']
    # Búsqueda por nombre de usuario y correo electrónico
    search_fields = ['user__username', 'user__email', 'ciudad', 'pais']
    # Paginación de 20 elementos por página
    list_per_page = 20
    # Campos del formulario de edición
    fieldsets = (
        ('Información de la cuenta', {'fields': ('user',)}),
        ('Dirección', {'fields': ('direccion_1', 'direccion_2', 'ciudad', 'region', 'pais')}),
        ('Imagen de perfil', {'fields': ('profile_picture',)}),
    )

    # Función para mostrar la dirección completa del usuario
    def direccion_completa(self, obj):
        return obj.direccion_completa()
    direccion_completa.short_description = 'Dirección Completa'

    # Previsualización de la imagen de perfil
    def profile_picture_preview(self, obj):
        if obj.profile_picture:
            return format_html(f'<img src="{obj.profile_picture.url}" style="width: 50px; height: 50px; border-radius: 25px;" />')
        return "Sin imagen"
    profile_picture_preview.short_description = "Imagen de perfil"

# Registrar los modelos en el admin
admin.site.register(Cuenta, CuentaAdmin)  # Registro de Cuenta con su admin
admin.site.register(UsuarioPerfil, UsuarioPerfilAdmin)  # Registro de UsuarioPerfil
