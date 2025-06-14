from rest_framework.generics import ListAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Miembro, UnidadDeMedida, Medicion, Rutina, MiembroTipo, MiembroEstado, Genero, Asistencia
from .serializers import MiembroSerializer, UnidadDeMedidaSerializer, MedicionSerializer, \
    RutinaDetalleSerializer, RutinaSerializer, MiembroMinSerializer, MiembroTipoSerializer, MiembroEstadoSerializer, \
    MiembroDetalleSerializer, MiembroImageSerializer, AsistenciaSerializer, UserSerializer

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib import admin
admin.autodiscover()

class AsistenciaView(ListCreateAPIView):
    """
    Lista a todos los miembros, o crea uno nuevo.
    """
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['miembro', 'timestamp']
    search_fields = ['miembro', 'timestamp']

    def post(self, request, format=None):
        serializer = AsistenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MiembroLista(ListAPIView):
    """
    Lista a todos los miembros, o crea uno nuevo.
    """
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nombre', 'apellidos', 'estado_membresia', 'tipo_membresia']
    search_fields = ['nombre', 'apellidos']

    def post(self, request, format=None):
        serializer = MiembroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MiembroListaMinView(ListAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Miembro.objects.all()
    serializer_class = MiembroMinSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nombre', 'apellidos', 'estado_membresia', 'tipo_membresia']
    search_fields = ['nombre', 'apellidos']


class MiembroDetalle(APIView):
    """
    Devuelve, actualiza o borra una instancia de miembro
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_miembro(self, id):
        try:
            return Miembro.objects.get(id=id)
        except Miembro.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        expand = self.request.query_params.get('expand')
        miembro = self.get_miembro(id)
        serializer = MiembroSerializer(miembro)
        if expand == 'details':
            serializer = MiembroDetalleSerializer(miembro)
        return Response(serializer.data)
        #return Response(expand)

    def put(self, request, id, format=None):
        miembro = self.get_miembro(id)
        serializer = MiembroSerializer(miembro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        miembro = self.get_miembro(id)
        miembro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MiembroImageView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_miembro(self, id):
        try:
            return Miembro.objects.get(id=id)
        except Miembro.DoesNotExist:
            raise Http404

    def put(self, request, id, format=None):
        miembro = self.get_miembro(id)
        serializer = MiembroImageSerializer(miembro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id, format=None):
        miembro = self.get_miembro(id)
        serializer = MiembroImageSerializer(miembro)
        return Response(serializer.data)




class UnidadDeMedidaView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UnidadDeMedidaSerializer
    queryset = UnidadDeMedida.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'simbolo']


class TipoMiembroView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = MiembroTipoSerializer
    queryset = MiembroTipo.objects.all()
    filter_backends = [DjangoFilterBackend]


class EstadoMiembroView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = MiembroEstadoSerializer
    queryset = MiembroEstado.objects.all()
    filter_backends = [DjangoFilterBackend]


class GeneroView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = MiembroEstadoSerializer
    queryset = Genero.objects.all()
    filter_backends = [DjangoFilterBackend]

class MedicionView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = MedicionSerializer
    queryset = Medicion.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['miembro', 'unidad']
    search_fields = ['miembro']

    def post(self, request, format=None):
        serializer = MedicionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicionDetalle(APIView):
    """
    Devuelve, actualiza o borra una instancia de miembro
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_medicion(self, id):
        try:
            return Medicion.objects.get(id=id)
        except Medicion.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        medicion = self.get_medicion(id)
        serializer = MedicionSerializer(medicion)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        medicion = self.get_medicion(id)
        serializer = MedicionSerializer(medicion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        medicion = self.get_medicion(id)
        medicion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RutinaView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = RutinaDetalleSerializer
    queryset = Rutina.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['fecha', 'miembro']
    search_fields = ['miembro']

    def post(self, request, format=None):
        serializer = RutinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RutinaDetalleView(APIView):
    """
    Devuelve, actualiza o borra una instancia de Rutina
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_rutina(self, id):
        try:
            return Rutina.objects.get(id=id)
        except Rutina.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        rutina = self.get_rutina(id)
        serializer = MedicionSerializer(rutina)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        rutina = self.get_rutina(id)
        serializer = MedicionSerializer(rutina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        medicion = self.get_rutina(id)
        medicion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
