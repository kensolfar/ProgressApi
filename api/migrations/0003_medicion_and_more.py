# Generated by Django 5.0.6 on 2024-05-28 18:20

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_instructor_objetivo_rutina_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_medicion', models.DateField(auto_now_add=True)),
                ('peso', models.FloatField(null=True)),
                ('imc', models.FloatField(null=True)),
                ('porcentaje_grasa', models.FloatField(null=True)),
                ('estatura', models.FloatField(null=True)),
                ('pecho', models.FloatField(null=True)),
                ('cintura', models.FloatField(null=True)),
                ('brazo_izquierdo', models.FloatField(null=True)),
                ('brazo_derecho', models.FloatField(null=True)),
                ('pierna_izquierda', models.FloatField(null=True)),
                ('pierna_derecha', models.FloatField(null=True)),
            ],
        ),
        migrations.RenameIndex(
            model_name='miembro',
            new_name='api_miembro_nombre_9f8902_idx',
            old_name='nombre_idx',
        ),
        migrations.AddField(
            model_name='miembro',
            name='usuario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='fecha_de_registro',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='miembro',
            name='fecha_registro',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rutina',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rutina',
            name='semanas',
            field=models.IntegerField(default=6, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddIndex(
            model_name='instructor',
            index=models.Index(fields=['apellidos', 'nombre'], name='api_instruc_apellid_b589f0_idx'),
        ),
        migrations.AddIndex(
            model_name='instructor',
            index=models.Index(fields=['nombre'], name='api_instruc_nombre_600b9b_idx'),
        ),
        migrations.AddField(
            model_name='medicion',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.instructor'),
        ),
        migrations.AddField(
            model_name='medicion',
            name='miembro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.miembro'),
        ),
        migrations.AddField(
            model_name='medicion',
            name='rutina',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.rutina'),
        ),
        migrations.AlterIndexTogether(
            name='medicion',
            index_together={('miembro', 'fecha_medicion')},
        ),
    ]
