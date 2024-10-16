from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cuenta, UsuarioPerfil
from django.utils.html import format_html


class CuentaAdmin(UserAdmin):
    list_display = ('email', 'nombre', 'apellido', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_link = ('email', 'nombre', 'apellido')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class UsuarioPerfilAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        if object.profile_picture:
            return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
        else:
            return "No Image"
    thumbnail.short_description = "Imagen de perfil"
    list_display = ('thumbnail', 'user', 'ciudad', 'region', 'pais')


# Register your models here.
admin.site.register(Cuenta, CuentaAdmin)
admin.site.register(UsuarioPerfil, UsuarioPerfilAdmin)
