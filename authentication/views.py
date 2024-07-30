# authentication/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from social_django.utils import load_strategy, load_backend
from social_core.exceptions import MissingBackend, AuthForbidden
from rest_framework import authentication
from django.http import JsonResponse
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema



from .serializers import GoogleSocialAuthSerializer

class GoogleSocialAuthView(APIView):
    serializer_class = GoogleSocialAuthSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        access_token = serializer.validated_data['access_token']

        strategy = load_strategy(request)
        try:
            backend = load_backend(strategy=strategy, name='google-oauth2', redirect_uri=None)
        except MissingBackend:
            return Response({'error': 'Invalid backend'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = backend.do_auth(access_token)
        except AuthForbidden as error:
            return Response({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)

        if user and user.is_active:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Authentication failed'}, status=status.HTTP_400_BAD_REQUEST)
