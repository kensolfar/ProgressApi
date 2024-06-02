from rest_framework.generics import ListAPIView

from .models import Miembro
from .serializers import MiembroSerializer
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