# Generated by Django 5.1.7 on 2025-05-06 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='obradearte',
            name='categoria',
            field=models.CharField(choices=[('pintura', 'Pintura'), ('escultura', 'Escultura'), ('fotografia', 'Fotografía'), ('digital', 'Arte Digital'), ('otro', 'Otro')], default='otro', max_length=20),
        ),
        migrations.AlterField(
            model_name='obradearte',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
