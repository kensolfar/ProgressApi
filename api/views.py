from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ObjetivoSerializer, RutinaSerializer, InstructorSerializer, MiembroSerializer, \
    MiembroTipoSerializer, MiembroEstadoSerializer, GeneroSerializer, MedicionSerializer
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
from rest_framework.authentication import TokenAuthentication


class ObjetivoViewSet(viewsets.ModelViewSet):
    serializer_class = ObjetivoSerializer
    queryset = Objetivo.objects.all()
    authentication_classes = (TokenAuthentication,)


class RutinaViewSet(viewsets.ModelViewSet):
    serializer_class = RutinaSerializer
    queryset = Rutina.objects.all()
    authentication_classes = (TokenAuthentication,)


class InstructorViewSet(viewsets.ModelViewSet):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()
    authentication_classes = (TokenAuthentication,)


class MiembroViewSet(viewsets.ModelViewSet):
    serializer_class = MiembroSerializer
    queryset = Miembro.objects.all()
    authentication_classes = (TokenAuthentication,)


class MiembroTipoViewSet(viewsets.ModelViewSet):
    serializer_class = MiembroTipoSerializer
    queryset = MiembroTipo.objects.all()
    authentication_classes = (TokenAuthentication,)


class MiembroEstadoViewSet(viewsets.ModelViewSet):
    serializer_class = MiembroEstadoSerializer
    queryset = MiembroEstado.objects.all()
    authentication_classes = (TokenAuthentication,)


class GeneroViewSet(viewsets.ModelViewSet):
    serializer_class = GeneroSerializer
    queryset = Genero.objects.all()
    authentication_classes = (TokenAuthentication,)


class MedicionViewSet(viewsets.ModelViewSet):
    serializer_class = MedicionSerializer
    queryset = Medicion.objects.all()
    authentication_classes = (TokenAuthentication,)
