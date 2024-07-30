from django.contrib.auth.models import User
from rest_framework import serializers

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
