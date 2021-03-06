# Generated by Django 4.0.4 on 2022-05-13 18:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Nombres')),
                ('dni', models.CharField(max_length=9, unique=True, verbose_name='Nombres')),
                ('entrada', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now_add=True)),
                ('edad', models.IntegerField(default=0)),
                ('genero', models.CharField(max_length=50)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=9)),
                ('estado', models.BooleanField(default=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/d')),
                ('cv', models.FileField(blank=True, null=True, upload_to='cvitae/%Y/%m/d')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.type')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleado',
                'ordering': ['-id'],
            },
        ),
    ]
