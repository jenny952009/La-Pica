# Generated by Django 3.2.20 on 2024-11-24 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservaciones', '0002_reserva_dia_reserva'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='hora_fin',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora_comienzo',
            field=models.CharField(max_length=100),
        ),
    ]