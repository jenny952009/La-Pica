# Generated by Django 3.2.20 on 2024-11-20 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0004_auto_20241118_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='usuarioperfil',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default_profile.jpg', upload_to='userprofile/'),
        ),
    ]
