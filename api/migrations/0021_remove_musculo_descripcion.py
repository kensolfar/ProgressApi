# Generated by Django 5.0.6 on 2024-06-09 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_instrumento_imagen_musculo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musculo',
            name='descripcion',
        ),
    ]
