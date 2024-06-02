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
    Medicion, UnidadDeMedida
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


class MiembroExpSerializer(serializers.ModelSerializer):
    estado_membresia = MiembroEstadoSerializer(many=False)
    tipo_membresia = MiembroTipoSerializer(many=False)
    genero = GeneroSerializer(many=False)
    usuario = UserSerializer(many=False)
    
    class Meta:
        model = Miembro
        fields = [
            'id',
            'nombre',
            'apellidos',
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
            'estado_membresia',
            'tipo_membresia',
            'fecha_nacimiento',
            'fecha_registro',
            'genero',
            'contacto',
            'contacto_de_emergencia',
            'imagen_de_perfil',
            'ultimo_pago',
            'usuario'
        ]


class FindMiembroPorEstadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Miembro
        fields = [
            'id',
            'nombre',
            'apellidos',
            'estado_membresia',
            'tipo_membresia',
            'fecha_nacimiento',
            'direccion',
            'genero',
            'contacto',
            'contacto_de_emergencia',
            'imagen_de_perfil',
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
            'rutina',
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