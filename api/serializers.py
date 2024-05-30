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
    Medicion
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
            'nombre',
            'descripcion'
        ]


class MiembroTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiembroTipo
        fields = [
            'nombre',
            'descripcion'
        ]


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = [
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


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = [
            'nombre',
            'apellidos',
            'fecha_de_registro',
            'usuario'
        ]


class ObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objetivo
        fields = [
            'nombre',
            'descripcion'
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


class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = [
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