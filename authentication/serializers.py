# authentication/serializers.py

from rest_framework import serializers

class GoogleSocialAuthSerializer(serializers.Serializer):
    access_token = serializers.CharField()