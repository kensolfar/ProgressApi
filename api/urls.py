from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include

from .views import MiembroViewSet, MiembroEstadoViewSet, MiembroTipoViewSet, GeneroViewSet, InstructorViewSet, \
    ObjetivoViewSet, RutinaViewSet, MedicionViewSet

router = routers.DefaultRouter()
router.register('miembro', MiembroViewSet)
router.register('miembro_estado', MiembroEstadoViewSet)
router.register('miembro_tipo', MiembroTipoViewSet)
router.register('genero', GeneroViewSet)
router.register('instructor', InstructorViewSet)
router.register('objetivo', ObjetivoViewSet)
router.register('rutina', RutinaViewSet)
router.register('medicion', MedicionViewSet)

urlpatterns = [
    path('', include(router.urls))
]
