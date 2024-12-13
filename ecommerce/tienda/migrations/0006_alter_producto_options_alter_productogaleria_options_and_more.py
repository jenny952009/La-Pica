# Generated by Django 4.2 on 2024-12-11 02:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tienda', '0005_producto_ventas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['-created_date'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelOptions(
            name='productogaleria',
            options={'ordering': ['producto'], 'verbose_name': 'Galería de producto', 'verbose_name_plural': 'Galerías de productos'},
        ),
        migrations.AlterModelOptions(
            name='reseñarating',
            options={'ordering': ['-created_at'], 'verbose_name': 'Reseña y calificación', 'verbose_name_plural': 'Reseñas y calificaciones'},
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categoria.categoria', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, max_length=500, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='images',
            field=models.ImageField(upload_to='fotos/productos', verbose_name='Imagen del producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Disponible'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='producto_nombre',
            field=models.CharField(max_length=200, unique=True, verbose_name='Nombre del producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='slug',
            field=models.CharField(max_length=200, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(verbose_name='Stock'),
        ),
        migrations.AlterField(
            model_name='productogaleria',
            name='image',
            field=models.ImageField(max_length=255, upload_to='tienda/productos', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='productogaleria',
            name='producto',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tienda.producto', verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='reseñarating',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado el'),
        ),
        migrations.AlterField(
            model_name='reseñarating',
            name='ip',
            field=models.CharField(blank=True, max_length=20, verbose_name='Dirección IP'),
        ),
        migrations.AlterField(
            model_name='reseñarating',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.producto', verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='reseñarating',
            name='rating',
            field=models.FloatField(verbose_name='Calificación Reseña'),
        ),
        migrations.AlterField(
            model_name='reseñarating',
            name='reseña',
            field=models.CharField(blank=True, max_length=500, verbose_name='Reseña'),
        ),
        migrations.AlterField(
            model_name='reseñarating',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='reseñarating',
            name='titulo',
            field=models.CharField(blank=True, max_length=100, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='reseñarating',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Actualizado el'),
        ),
        migrations.AlterField(
            model_name='reseñarating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
