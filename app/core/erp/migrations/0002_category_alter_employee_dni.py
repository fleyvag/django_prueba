# Generated by Django 4.0.4 on 2022-05-14 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre de la categoria')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='employee',
            name='dni',
            field=models.CharField(max_length=9, unique=True, verbose_name='dni'),
        ),
    ]
