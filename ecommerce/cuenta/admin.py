from django.contrib import admin
from .models import Cuenta, UsuarioPerfil
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

class CuentaAdmin(UserAdmin):
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
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superadmin')}),
        ('Fechas', {'fields': ()}),
    )
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

# Registrar los modelos en el admin
admin.site.register(Cuenta, CuentaAdmin)  # Registro de Cuenta con su admin
admin.site.register(UsuarioPerfil, UsuarioPerfilAdmin)  # Registro de UsuarioPerfil


""""


from django.contrib import admin
from .models import Cuenta, UsuarioPerfil
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

# Administrador de Cuenta
class CuentaAdmin(UserAdmin):
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
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superadmin')}),
        # Eliminar 'date_joined' de los fieldsets
        ('Fechas', {'fields': ()}),
    )
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

# Registrar los modelos en el admin
admin.site.register(Cuenta, CuentaAdmin)  # Registro de Cuenta con su admin
admin.site.register(UsuarioPerfil, UsuarioPerfilAdmin)  # Registro de UsuarioPerfil

"""
"""
from django.contrib import admin
from .models import Cuenta, UsuarioPerfil
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

# Administrador de Cuenta
class CuentaAdmin(UserAdmin):
    # Campos que se mostrarán en la lista de usuarios
    list_display = [
        'email', 'username', 'nombre_completo', 'telefono', 'is_active', 'is_staff', 'is_admin', 'date_joined', 'last_login'
    ]
    # Filtros por estado de usuario y fecha
    list_filter = ['is_active', 'is_staff', 'is_admin', 'date_joined', 'last_login']
    # Búsqueda por correo electrónico, nombre completo y username
    search_fields = ['email', 'nombre', 'apellido', 'username']
    # Paginación de 20 elementos por página
    list_per_page = 20
    # Campos editables en el formulario de usuario
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Información personal', {'fields': ('nombre', 'apellido', 'telefono')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superadmin')}),
        ('Fechas', {'fields': ('last_login',)}),
    )
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

# Registrar los modelos en el admin
admin.site.register(Cuenta, CuentaAdmin)  # Registro de Cuenta con su admin
admin.site.register(UsuarioPerfil, UsuarioPerfilAdmin)  # Registro de UsuarioPerfil
"""