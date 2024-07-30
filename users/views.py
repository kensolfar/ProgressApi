from rest_framework import generics
from django.contrib.auth.models import User, Group, Permission
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Miembro

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class MeDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):

        user = request.user
        miembro = Miembro.objects.get(usuario=user)

        # Obtener los grupos del usuario
        groups = user.groups.values_list('name', flat=True)

        # Obtener los permisos del usuario y los permisos de los grupos
        user_permissions = user.user_permissions.values_list('codename', flat=True)
        group_permissions = Permission.objects.filter(group__user=user).values_list('codename', flat=True)
        all_permissions = set(user_permissions).union(set(group_permissions))

        imagen_url = miembro.imagen_de_perfil.url if miembro.imagen_de_perfil else None

        user_data = {
            'id': user.id,
            'miembro': miembro.id,
            'imagen': imagen_url,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'is_superuser': user.is_superuser,
            'is_staff': user.is_staff,
            'is_active': user.is_active,
            'date_joined': user.date_joined,
            'last_login': user.last_login,
            'groups': list(groups),
            'user_permissions': list(all_permissions),
            'miembro': miembro.id,
        }
        return Response(user_data)
