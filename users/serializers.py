from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['access_token_expiration'] = datetime.fromtimestamp(refresh.access_token['exp'])
        data['refresh_token_expiration'] = datetime.fromtimestamp(refresh['exp'])

        return data

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = RefreshToken(attrs['refresh'])
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['access_token_expiration'] = datetime.fromtimestamp(refresh.access_token['exp'])
        data['refresh_token_expiration'] = datetime.fromtimestamp(refresh['exp'])

        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True, 'required': False}
        }

    def create(self, validated_data):
        # Extraer los datos del usuario
        user_data = {key: validated_data[key] for key in validated_data if key != 'password'}
        password = validated_data.get('password')

        # Crear el usuario
        user = User.objects.create(**user_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        # Actualizar todos los campos del usuario excepto la contraseña si no se proporciona
        for attr, value in validated_data.items():
            if attr == 'password':
                if value:  # Solo cambiar la contraseña si se proporciona un valor
                    instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
