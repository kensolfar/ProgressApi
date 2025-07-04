# Generated by Django 5.0.6 on 2024-06-02 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_remove_medicion_rutina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicion',
            name='brazo_derecho',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='brazo_izquierdo',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='cintura',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='espalda',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='estatura',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='imc',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='pantorrilla_derecha',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='pantorrilla_izquierda',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='pecho',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='peso',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='pierna_derecha',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='pierna_izquierda',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='porcentaje_grasa',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
