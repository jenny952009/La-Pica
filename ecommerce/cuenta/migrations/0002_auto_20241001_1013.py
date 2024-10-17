# Generated by Django 3.2.20 on 2024-10-01 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]