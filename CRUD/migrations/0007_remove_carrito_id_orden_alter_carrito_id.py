# Generated by Django 4.2.4 on 2023-08-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0006_rename_estado_carrito_completado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='id_orden',
        ),
        migrations.AlterField(
            model_name='carrito',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
