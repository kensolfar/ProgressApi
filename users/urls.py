from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserDetail, UserListCreate, MeDetailView, LoginView, CustomTokenObtainPairView, CustomTokenRefreshView


urlpatterns = [
    path('', UserListCreate.as_view(), name='user-list-create'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('@me/', MeDetailView.as_view(), name='@me_detail'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),

]