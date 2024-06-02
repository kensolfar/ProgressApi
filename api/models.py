from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class MiembroEstado(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class MiembroTipo(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Miembro(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    estado_membresia = models.ForeignKey(MiembroEstado, related_name='estado_membresia', default=1, on_delete=models.RESTRICT)
    tipo_membresia = models.ForeignKey(MiembroTipo, related_name='tipo_membresia', on_delete=models.RESTRICT, default=1)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True)
    fecha_registro = models.DateField(auto_now_add=True)
    genero = models.ForeignKey(Genero, related_name='genero', on_delete=models.RESTRICT, null=True)
    contacto = models.CharField(max_length=15, null=True, blank=True)
    contacto_de_emergencia = models.CharField(max_length=15, null=True, blank=True)
    imagen_de_perfil = models.ImageField(upload_to='images/', null=True, blank=True)
    ultimo_pago = models.DateField(null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'

    class Meta:
        indexes = [
            models.Index(fields=["apellidos", "nombre"]),
            models.Index(fields=["nombre"]),
            models.Index(fields=['estado_membresia'])
        ]


class Instructor(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    fecha_de_registro = models.DateField(auto_now_add=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        indexes = [
            models.Index(fields=["apellidos", "nombre"]),
            models.Index(fields=["nombre"]),
        ]


class Objetivo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Rutina(models.Model):
    fecha = models.DateField(auto_now_add=True)
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE, related_name='miembro')
    instructor = models.ForeignKey(Instructor, on_delete=models.RESTRICT, related_name='instructor')
    semanas = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=6)
    objetivo = models.ForeignKey(Objetivo, on_delete=models.SET_NULL, null=True, related_name='objetivo')

    class Meta:
        indexes = [
            models.Index(fields=["fecha", "miembro"]),
            models.Index(fields=["miembro"]),
            models.Index(fields=["fecha"]),
            models.Index(fields=["instructor"]),
        ]
        unique_together = (('fecha', 'miembro', 'instructor'),)

    def __str__(self):
        return self.miembro


class Medicion(models.Model):
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE)
    fecha_medicion = models.DateField(auto_now_add=True)
    rutina = models.ForeignKey(Rutina, on_delete=models.SET_NULL, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)
    #unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    peso = models.FloatField(null=True)
    imc = models.FloatField(null=True)
    porcentaje_grasa = models.FloatField(null=True)
    estatura = models.FloatField(null=True)
    pecho = models.FloatField(null=True)
    espalda = models.FloatField(null=True)
    cintura = models.FloatField(null=True)
    brazo_izquierdo = models.FloatField(null=True)
    brazo_derecho = models.FloatField(null=True)
    pierna_izquierda = models.FloatField(null=True)
    pierna_derecha = models.FloatField(null=True)
    pantorrilla_izquierda = models.FloatField(null=True)
    pantorrilla_derecha = models.FloatField(null=True)

    def __str__(self):
        return self.miembro

    class Meta:
        index_together = ('miembro', 'fecha_medicion')
