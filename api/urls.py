from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from . import views

urlpatterns = [
    path('miembro', views.MiembroLista.as_view()),
    path('miembro/<int:id>', views.MiembroDetalle.as_view()),
]
