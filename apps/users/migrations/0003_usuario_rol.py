# Generated by Django 5.1.7 on 2025-04-10 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_usuario_correo_alter_usuario_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('normal', 'Usuario Normal'), ('admin', 'Administrador')], default='normal', max_length=10),
        ),
    ]
