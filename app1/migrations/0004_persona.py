# Generated by Django 3.1.5 on 2021-02-20 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_categoria_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_crea', models.DateTimeField(auto_now_add=True)),
                ('fecha_modifica', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=8)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Personas',
            },
        ),
    ]