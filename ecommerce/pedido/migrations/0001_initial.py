# Generated by Django 3.2.20 on 2024-10-18 02:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tienda', '0002_rename_revisar_revisarrating_review'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pago_id', models.CharField(max_length=100)),
                ('pago_method', models.CharField(max_length=100)),
                ('monto_id', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido_numero', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('direccion_1', models.CharField(max_length=100)),
                ('direccion_2', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=20)),
                ('pedido_nota', models.CharField(blank=True, max_length=100)),
                ('pedido_total', models.FloatField()),
                ('impuesto', models.FloatField()),
                ('status', models.CharField(choices=[('New', 'Nuevo'), ('Accepted', 'Aceptado'), ('Completed', 'Completado'), ('Cancelled', 'Cancelado')], default='New', max_length=50)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('is_ordered', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pago', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pedido.pago')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PedidoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('producto_precio', models.FloatField()),
                ('ordered', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pago', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedido.pago')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.producto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('variacion', models.ManyToManyField(blank=True, to='tienda.Variacion')),
            ],
        ),
    ]
