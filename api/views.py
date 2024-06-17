from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Miembro, UnidadDeMedida, Medicion, Rutina, MiembroTipo, MiembroEstado
from .serializers import MiembroSerializer, UnidadDeMedidaSerializer, MedicionSerializer, \
    RutinaDetalleSerializer, RutinaSerializer, MiembroMinSerializer, MiembroTipoSerializer, MiembroEstadoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import authentication
from rest_framework import  filters
from django_filters.rest_framework import DjangoFilterBackend


class MiembroLista(ListAPIView):
    """
    Lista a todos los miembros, o crea uno nuevo.
    """
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
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

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Miembro.objects.all()
    serializer_class = MiembroMinSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nombre', 'apellidos', 'estado_membresia', 'tipo_membresia']
    search_fields = ['nombre', 'apellidos']


class MiembroDetalle(APIView):
    """
    Devuelve, actualiza o borra una instancia de miembro
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_miembro(self, id):
        try:
            return Miembro.objects.get(id=id)
        except Miembro.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        miembro = self.get_miembro(id)
        serializer = MiembroSerializer(miembro)
        return Response(serializer.data)

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


class UnidadDeMedidaView(ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UnidadDeMedidaSerializer
    queryset = UnidadDeMedida.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'simbolo']


class TipoMiembroView(ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MiembroTipoSerializer
    queryset = MiembroTipo.objects.all()
    filter_backends = [DjangoFilterBackend]


class EstadoMiembroView(ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MiembroEstadoSerializer
    queryset = MiembroEstado.objects.all()
    filter_backends = [DjangoFilterBackend]


class MedicionView(ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
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
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

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
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
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
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

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
