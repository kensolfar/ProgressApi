# Generated by Django 5.0.6 on 2024-06-09 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_musculo_delete_musculos'),
    ]

    operations = [
        migrations.AddField(
            model_name='musculo',
            name='funciones_principales',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='musculo',
            name='insercion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='musculo',
            name='origen',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
