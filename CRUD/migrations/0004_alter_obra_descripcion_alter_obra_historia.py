# Generated by Django 4.2.4 on 2023-08-06 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0003_carrito_cliente_productocarrito_direccionentrega_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obra',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='obra',
            name='historia',
            field=models.TextField(),
        ),
    ]