# Generated by Django 4.2 on 2024-12-10 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('cuenta', '0003_alter_usuarioperfil_region'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuenta',
            options={'verbose_name': 'Cuenta de usuario', 'verbose_name_plural': 'Cuentas de usuarios'},
        ),
        migrations.AlterModelOptions(
            name='usuarioperfil',
            options={'verbose_name': 'Perfil de usuario', 'verbose_name_plural': 'Perfiles de usuarios'},
        ),
        migrations.AddField(
            model_name='cuenta',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='Los grupos a los que pertenece este usuario.', related_name='user_set', to='auth.group', verbose_name='grupos'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Permisos específicos para este usuario.', related_name='user_set', to='auth.permission', verbose_name='permisos de usuario'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='apellido',
            field=models.CharField(max_length=55, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='email',
            field=models.EmailField(max_length=50, unique=True, verbose_name='Correo electrónico'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='¿Está activo?'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='¿Es administrador?'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='¿Es staff?'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='is_superadmin',
            field=models.BooleanField(default=False, verbose_name='¿Es superadministrador?'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='Último inicio de sesión'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='telefono',
            field=models.CharField(max_length=50, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='username',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nombre de usuario'),
        ),
        migrations.AlterField(
            model_name='usuarioperfil',
            name='ciudad',
            field=models.CharField(blank=True, max_length=20, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='usuarioperfil',
            name='direccion_1',
            field=models.CharField(blank=True, max_length=100, verbose_name='Dirección principal'),
        ),
        migrations.AlterField(
            model_name='usuarioperfil',
            name='direccion_2',
            field=models.CharField(blank=True, max_length=100, verbose_name='Detalle Dirección'),
        ),
        migrations.AlterField(
            model_name='usuarioperfil',
            name='pais',
            field=models.CharField(blank=True, max_length=20, verbose_name='País'),
        ),
        migrations.AlterField(
            model_name='usuarioperfil',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default_profile.jpg', upload_to='userprofile/', verbose_name='Foto de Perfil'),
        ),
        migrations.AlterField(
            model_name='usuarioperfil',
            name='region',
            field=models.CharField(blank=True, max_length=20, verbose_name='Región'),
        ),
        migrations.AlterField(
            model_name='usuarioperfil',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
