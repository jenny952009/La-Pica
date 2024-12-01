# Generated by Django 3.2.20 on 2024-11-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='cat_image',
            field=models.ImageField(blank=True, upload_to='photos/categorias', verbose_name='Imagen Categoría'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='categoria_nombre',
            field=models.CharField(max_length=20, unique=True, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='slug',
            field=models.CharField(max_length=100, unique=True, verbose_name='Slug'),
        ),
    ]
