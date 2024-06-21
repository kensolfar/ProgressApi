from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Objetivo,
    Rutina,
    Instructor,
    Miembro,
    MiembroTipo,
    MiembroEstado,
    Genero,
    Medicion, UnidadDeMedida, DiaDeRutina, EjerciciosPorDia, InstrumentosDeEjercicio, Instrumento, Ejercicio,
    MusculosDeEjercicio, Musculo
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'last_login',
            'is_superuser',
            'email',
            'is_staff',
            'is_active',
            'date_joined'
        ]


class MiembroEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiembroEstado
        fields = [
            'id',
            'nombre',
            'descripcion'
        ]


class MiembroTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiembroTipo
        fields = [
            'id',
            'nombre',
            'descripcion'
        ]


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = [
            'id',
            'nombre',
            'descripcion'
        ]


class MiembroDetalleSerializer(serializers.ModelSerializer):
    estado_membresia = serializers.StringRelatedField(many=False)
    tipo_membresia = serializers.StringRelatedField(many=False)
    genero = serializers.StringRelatedField(many=False)
    usuario = UserSerializer(many=False, read_only=True)
    
    class Meta:
        model = Miembro
        fields = [
            'id',
            'nombre',
            'apellidos',
            'direccion',
            'estado_membresia',
            'tipo_membresia',
            'fecha_nacimiento',
            'genero',
            'contacto',
            'contacto_de_emergencia',
            'imagen_de_perfil',
            'ultimo_pago',
            'usuario'
        ]


class MiembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = [
            'id',
            'nombre',
            'apellidos',
            'direccion',
            'estado_membresia',
            'tipo_membresia',
            'fecha_nacimiento',
            'genero',
            'contacto',
            'contacto_de_emergencia',
            'imagen_de_perfil',
            'ultimo_pago',
            'usuario'
        ]

class MiembroMinSerializer(serializers.ModelSerializer):

    estado_membresia = serializers.StringRelatedField(many=False)
    tipo_membresia = serializers.StringRelatedField(many=False)
    usuario = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Miembro

        fields = [
            'id',
            'nombre',
            'apellidos',
            'estado_membresia',
            'tipo_membresia',
            'direccion',
            'ultimo_pago',
            'usuario'
        ]


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = [
            'id',
            'nombre',
            'apellidos',
            'fecha_de_registro',
            'usuario'
        ]


class ObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objetivo
        fields = [
            'id',
            'nombre',
            'descripcion'
        ]


class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields = [
            'id',
            'fecha',
            'miembro',
            'instructor',
            'semanas',
            'objetivo'
        ]


class UnidadDeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadDeMedida
        fields = [
            'id',
            'nombre',
            'simbolo'
        ]


class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = [
            'id',
            'miembro',
            'fecha_medicion',
            'instructor',
            'peso',
            'imc',
            'porcentaje_grasa',
            'estatura',
            'pecho',
            'cintura',
            'brazo_izquierdo',
            'brazo_derecho',
            'pierna_izquierda',
            'pierna_derecha',
            'pantorrilla_izquierda',
            'pantorrilla_derecha'
        ]


class MedicionDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = [
            'id',
            'miembro',
            'fecha_medicion',
            'instructor',
            'peso',
            'imc',
            'porcentaje_grasa',
            'estatura',
            'pecho',
            'cintura',
            'brazo_izquierdo',
            'brazo_derecho',
            'pierna_izquierda',
            'pierna_derecha',
            'pantorrilla_izquierda',
            'pantorrilla_derecha'
        ]


class NombreMiembro(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = ['id','nombre']


class NombreInstructor(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = ['id','nombre']


class InstrumentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instrumento
        fields = [
            'nombre',
            'descripcion',
            'imagen'
        ]


class InstrumentosDeEjercicioSerializer(serializers.ModelSerializer):
    instrumento = InstrumentoSerializer(many=True)

    class Meta:
        model = InstrumentosDeEjercicio
        fields = ['instrumento']


class MusculoSerializer(serializers.ModelSerializer):
    grupo_muscular = serializers.StringRelatedField(many=False)

    class Meta:
        model = Musculo
        fields = [
            'nombre',
            'origen',
            'insercion',
            'funciones_principales',
            'grupo_muscular',
            'imagen'
        ]


class EjercicioSerializer(serializers.ModelSerializer):
    musculos = serializers.StringRelatedField(many=True)
    instrumentos = serializers.StringRelatedField(many=True)
    recursos = serializers.StringRelatedField(many=True)

    class Meta:
        model = Ejercicio
        fields = [
            'nombre',
            'ejecucion',
            'comentarios',
            'errores_frecuentes',
            'musculos',
            'instrumentos',
            'recursos',
            'imagen'
        ]


class EjerciciosPorDiaSerializer(serializers.ModelSerializer):
    ejercicio = EjercicioSerializer(many=False)
    repeticion = serializers.StringRelatedField(many=False)

    class Meta:
        model = EjerciciosPorDia
        fields = ['repeticion', 'ejercicio']


class DiasDeRutinaSerializer(serializers.ModelSerializer):
    ejercicios = EjerciciosPorDiaSerializer(many=True)
    grupos_musculares = serializers.StringRelatedField(many=True)

    class Meta:
        model = DiaDeRutina
        fields = ['descripcion', 'grupos_musculares', 'ejercicios']


class RutinaDetalleSerializer(serializers.ModelSerializer):

    miembro = serializers.StringRelatedField(many=False)
    instructor = serializers.StringRelatedField(many=False)
    objetivo = serializers.StringRelatedField(many=False)
    dias_de_rutina = DiasDeRutinaSerializer(many=True)

    class Meta:
        model = Rutina
        fields = [
            'fecha',
            'miembro',
            'instructor',
            'semanas',
            'objetivo',
            'dias_de_rutina'
        ]


class RutinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rutina
        fields = [
            'fecha',
            'miembro',
            'instructor',
            'semanas',
            'objetivo'
        ]