# Generated by Django 4.2.4 on 2023-08-06 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0005_alter_obra_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrito',
            old_name='estado',
            new_name='completado',
        ),
    ]
