# Generated by Django 4.2.4 on 2023-08-06 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CRUD', '0002_obra_imagen_alter_obra_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_orden', models.DateTimeField(auto_now_add=True)),
                ('estado', models.BooleanField(default=False, null=True)),
                ('id_orden', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='productocarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('fecha_añadido', models.DateTimeField(auto_now_add=True)),
                ('orden', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CRUD.carrito')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CRUD.obra')),
            ],
        ),
        migrations.CreateModel(
            name='direccionentrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=200, null=True)),
                ('ciudad', models.CharField(max_length=200, null=True)),
                ('region', models.CharField(max_length=200, null=True)),
                ('codigopostal', models.CharField(max_length=200, null=True)),
                ('fecha_añadido', models.DateTimeField(auto_now_add=True)),
                ('carrito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CRUD.carrito')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CRUD.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CRUD.cliente'),
        ),
    ]