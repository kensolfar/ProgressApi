from django.urls import path, include
from .views import GoogleSocialAuthView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', obtain_auth_token),
    path('social/google/', GoogleSocialAuthView.as_view(), name='google-auth'),
]