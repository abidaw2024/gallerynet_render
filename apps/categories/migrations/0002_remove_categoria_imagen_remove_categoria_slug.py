# Generated by Django 5.1.7 on 2025-05-16 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='slug',
        ),
    ]
