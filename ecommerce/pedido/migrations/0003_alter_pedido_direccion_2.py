# Generated by Django 3.2.20 on 2024-11-18 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_remove_pedidoproducto_variacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='direccion_2',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
