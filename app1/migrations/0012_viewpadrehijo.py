# Generated by Django 3.1.5 on 2021-03-07 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_empleado_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewPadreHijo',
            fields=[
                ('idpadre', models.IntegerField(primary_key=True, serialize=False)),
                ('nombrepadre', models.CharField(max_length=50)),
                ('idhijo', models.IntegerField()),
                ('nombrehijo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'view_padrehijo',
                'managed': False,
            },
        ),
    ]
