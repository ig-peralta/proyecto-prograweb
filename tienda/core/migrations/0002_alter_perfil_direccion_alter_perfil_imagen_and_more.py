# Generated by Django 5.0.6 on 2024-06-30 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='direccion',
            field=models.CharField(max_length=800, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='imagen',
            field=models.ImageField(default='perfiles/user_profile.png', upload_to='perfiles/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=800, verbose_name='Descripción'),
        ),
    ]
