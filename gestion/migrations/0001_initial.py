# Generated by Django 4.1.2 on 2022-11-08 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Informacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_descripcion', models.CharField(max_length=255, verbose_name='Nombre y descripción')),
                ('proveedor', models.CharField(max_length=255, verbose_name='Proveedor')),
                ('direccion_proveedor', models.CharField(max_length=255, verbose_name='Dirección del proveedor')),
                ('numero_proveedor', models.CharField(max_length=255, verbose_name='Número del contacto del proveedor')),
                ('fecha_modificacion', models.DateField(max_length=20, verbose_name='Fecha de modificación')),
                ('fecha_vencimiento', models.DateField(max_length=20, verbose_name='Fecha de vencimiento')),
                ('categoria_producto', models.CharField(choices=[('1', 'Alimentos'), ('2', 'Bebidas'), ('3', 'Limpieza'), ('4', 'Otros')], max_length=100, verbose_name='Categoria del producto')),
                ('cantidad_productos', models.IntegerField(verbose_name='Cantidad actual')),
                ('stock_maximo', models.IntegerField(verbose_name='Stock minima')),
                ('peso_unidad', models.FloatField(verbose_name='Peso por unidad')),
                ('stock_minimo', models.IntegerField(verbose_name='Stock maxima')),
                ('unidades', models.CharField(choices=[('1', 'Kg'), ('2', 'g'), ('3', 'L'), ('4', 'Unidades'), ('5', 'Otros')], max_length=255, verbose_name='Unidades')),
            ],
            options={
                'verbose_name_plural': 'Información',
            },
        ),
    ]
