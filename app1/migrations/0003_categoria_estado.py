# Generated by Django 3.1.5 on 2021-02-20 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20210219_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=8),
        ),
    ]
