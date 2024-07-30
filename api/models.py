from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class MiembroEstado(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre


class MiembroTipo(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, null=True, blank=True)


class Canton(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, null=True, blank=True)


class Distrito(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255, null=True, blank=True)


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
    anotaciones = models.CharField(max_length=500, null=True, blank=True, default='')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'

    class Meta:
        indexes = [
            models.Index(fields=["apellidos", "nombre"]),
            models.Index(fields=["nombre"]),
            models.Index(fields=['estado_membresia'])
        ]


class Asistencia(models.Model):
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE, related_name='asistencia')
    timestamp = models.DateTimeField()

    def __str__(self):
        return str(self.timestamp)

    class Meta:
        indexes = [
            models.Index(fields=["miembro", "timestamp"]),
            models.Index(fields=["timestamp"]),
            models.Index(fields=["miembro"]),
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


class UnidadDeMedida(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    simbolo = models.CharField(max_length=5, unique=True)


    def __str__(self):
        return str(self.simbolo)


class Medicion(models.Model):
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE)
    fecha_medicion = models.DateField(auto_now_add=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)
    unidad = models.ForeignKey(UnidadDeMedida, on_delete=models.PROTECT, default=1)
    peso = models.FloatField(null=True, blank=True)
    imc = models.FloatField(null=True, blank=True)
    porcentaje_grasa = models.FloatField(null=True, blank=True)
    estatura = models.FloatField(null=True, blank=True)
    pecho = models.FloatField(null=True, blank=True)
    espalda = models.FloatField(null=True, blank=True)
    cintura = models.FloatField(null=True, blank=True)
    brazo_izquierdo = models.FloatField(null=True, blank=True)
    brazo_derecho = models.FloatField(null=True, blank=True)
    pierna_izquierda = models.FloatField(null=True, blank=True)
    pierna_derecha = models.FloatField(null=True, blank=True)
    pantorrilla_izquierda = models.FloatField(null=True, blank=True)
    pantorrilla_derecha = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.miembro} - {self.fecha_medicion}'

    class Meta:
        index_together = ('miembro', 'fecha_medicion')


class Ejercicio(models.Model):
    nombre = models.CharField(max_length=255)
    ejecucion = models.CharField(max_length=1000, null=True, blank=True)
    comentarios = models.CharField(max_length=1000, null=True, blank=True)
    errores_frecuentes = models.CharField(max_length=1000, null=True, blank=True)
    imagen = models.ImageField(upload_to='ejercicios/', null=True, blank=True)

    def __str__(self):
        return str(self.nombre)


class Repeticion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.nombre)


class Rutina(models.Model):
    fecha = models.DateField(auto_now_add=True)
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE, related_name='miembro')
    instructor = models.ForeignKey(Instructor, on_delete=models.RESTRICT, related_name='instructor')
    semanas = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=6)
    duracion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)], default=5)
    objetivo = models.ForeignKey(Objetivo, on_delete=models.SET_NULL, null=True, related_name='objetivo')
    activa = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=["fecha", "miembro"]),
            models.Index(fields=["miembro"]),
            models.Index(fields=["fecha"]),
            models.Index(fields=["instructor"]),
        ]
        unique_together = (('fecha', 'miembro', 'instructor'),)

    def __str__(self):
        return str(f'{self.fecha} - {self.miembro}')


class DiaDeRutina(models.Model):
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, related_name='dias_de_rutina')
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.rutina, self.descripcion)


class EjerciciosPorDia(models.Model):
    dia_de_rutina = models.ForeignKey(DiaDeRutina, on_delete=models.CASCADE, related_name='ejercicios')
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    repeticion = models.ForeignKey(Repeticion, on_delete=models.PROTECT)

    class Meta:
        unique_together = ['dia_de_rutina', 'ejercicio']


class GrupoMuscular(models.Model):
    nombre = models.CharField(max_length=255)
    comentario = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.nombre)


class Instrumento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    imagen = models.ImageField(upload_to='instrumentos/', null=True, blank=True)

    def __str__(self):
        return str(self.nombre)


class Recurso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.nombre)


class Musculo(models.Model):
    nombre = models.CharField(max_length=255)
    origen = models.CharField(max_length=255, null=True, blank=True)
    insercion = models.CharField(max_length=255, null=True, blank=True)
    funciones_principales = models.CharField(max_length=255, null=True, blank=True)
    grupo_muscular = models.ForeignKey(GrupoMuscular, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='musculos/', null=True, blank=True)

    def __str__(self):
        return '%s: %s' % (self.grupo_muscular, self.nombre)


class MusculosDeEjercicio(models.Model):
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, related_name='musculos')
    musculo = models.ForeignKey(Musculo, on_delete=models.CASCADE, related_name='ejercicio')

    class Meta:
        unique_together = ['ejercicio', 'musculo']

    def __str__(self):
        return '%s' % self.musculo


class InstrumentosDeEjercicio(models.Model):
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, related_name='instrumentos')
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE, related_name='ejercicio')

    class Meta:
        unique_together = ['ejercicio', 'instrumento']

    def __str__(self):
        return '%s' % self.instrumento


class RecursosDeEjercicio(models.Model):
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, related_name='recursos')
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE, related_name='ejercicio')

    class Meta:
        unique_together = ['ejercicio', 'recurso']

    def __str__(self):
        return '%s' % self.recurso


class MusculosPorDia(models.Model):
    dia_de_rutina = models.ForeignKey(DiaDeRutina, on_delete=models.CASCADE, related_name='grupos_musculares')
    grupo_muscular = models.ForeignKey(GrupoMuscular, on_delete=models.CASCADE, related_name='dia')

    class Meta:
        unique_together = ['dia_de_rutina', 'grupo_muscular']

    def __str__(self):
        return '%s' % self.grupo_muscular

