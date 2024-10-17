# Generated by Django 3.2.20 on 2024-10-17 02:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tienda', '0002_rename_revisar_revisarrating_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrito_id', models.CharField(blank=True, max_length=250)),
                ('fecha_agregado', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarritoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('carro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carrito.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.producto')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('variacion', models.ManyToManyField(blank=True, to='tienda.Variacion')),
            ],
        ),
    ]
