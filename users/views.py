from datetime import datetime
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User, Group, Permission
from api.models import Miembro
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer
from django.utils import timezone

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class MeDetailView(APIView):
    authentication_classes = [JWTAuthentication]
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


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            # Verificar si es la primera vez que el usuario se loguea
            first_login = user.last_login is None

            # Actualizar el campo last_login
            user.last_login = timezone.localtime()
            user.save(update_fields=['last_login'])

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # Tratar de obtener el Miembro relacionado, si no existe, manejar la excepción
            try:
                miembro = Miembro.objects.get(usuario=user)
                imagen_url = miembro.imagen_de_perfil.url if miembro.imagen_de_perfil else None
                miembro_id = miembro.id
            except Miembro.DoesNotExist:
                miembro = None
                imagen_url = None
                miembro_id = None

            # Obtener los grupos del usuario
            groups = user.groups.values_list('name', flat=True)

            # Obtener los permisos del usuario y los permisos de los grupos
            user_permissions = user.user_permissions.values_list('codename', flat=True)
            group_permissions = Permission.objects.filter(group__user=user).values_list('codename', flat=True)
            all_permissions = set(user_permissions).union(set(group_permissions))

            user_data = {
                'id': user.id,
                'miembro': miembro_id,
                'imagen': imagen_url,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'is_superuser': user.is_superuser,
                'is_staff': user.is_staff,
                'is_active': user.is_active,
                'date_joined': user.date_joined,
                'last_login': None if first_login else user.last_login,
                'groups': list(groups),
                'user_permissions': list(all_permissions),
            }

            response_data = {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'access_token_expiration': datetime.fromtimestamp(refresh.access_token['exp']),
                'refresh_token_expiration': datetime.fromtimestamp(refresh['exp']),
                'user': user_data
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)