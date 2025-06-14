# Generated by Django 5.0.6 on 2024-06-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_alter_instrumentosdeejercicio_ejercicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaderutina',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='genero',
            name='descripcion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='miembroestado',
            name='descripcion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='miembrotipo',
            name='descripcion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='repeticion',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
