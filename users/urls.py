from django.urls import path
from .views import UserDetail, UserListCreate, MeDetailView

urlpatterns = [
    path('', UserListCreate.as_view(), name='user-list-create'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('@me/', MeDetailView.as_view(), name='@me_detail')
]