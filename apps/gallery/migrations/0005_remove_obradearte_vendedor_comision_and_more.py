# Generated by Django 5.1.7 on 2025-05-15 19:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_obradearte_imagenes_adicionales'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obradearte',
            name='vendedor',
        ),
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('estilo', models.CharField(max_length=100)),
                ('tecnica', models.CharField(max_length=100)),
                ('tema', models.CharField(max_length=100)),
                ('imagen_principal', models.ImageField(upload_to='comisiones/')),
                ('imagen_adicional_1', models.ImageField(blank=True, null=True, upload_to='comisiones/')),
                ('imagen_adicional_2', models.ImageField(blank=True, null=True, upload_to='comisiones/')),
                ('imagen_adicional_3', models.ImageField(blank=True, null=True, upload_to='comisiones/')),
                ('precio_basico', models.DecimalField(decimal_places=2, max_digits=8)),
                ('descripcion_basico', models.TextField()),
                ('precio_estandar', models.DecimalField(decimal_places=2, max_digits=8)),
                ('descripcion_estandar', models.TextField()),
                ('precio_premium', models.DecimalField(decimal_places=2, max_digits=8)),
                ('descripcion_premium', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comisiones', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='comentario',
            name='obra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='gallery.comision'),
        ),
    ]
