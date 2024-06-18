from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from . import views

router = routers.DefaultRouter()
router.register('unidad', viewset=views.UnidadDeMedidaView)
router.register('tipomiembro', viewset=views.TipoMiembroView)
router.register('estadomiembro', viewset=views.EstadoMiembroView)
router.register('genero', viewset=views.GeneroView)

urlpatterns = [
    path('', include(router.urls)),
    path('miembro', views.MiembroLista.as_view()),
    path('miembro/<int:id>', views.MiembroDetalle.as_view()),
    path('miembros', views.MiembroListaMinView.as_view()),
    path('medicion', views.MedicionView.as_view()),
    path('medicion/<int:id>', views.MedicionDetalle.as_view()),
    path('rutina', views.RutinaView.as_view()),
    path('rutina/<int:id>', views.RutinaView.as_view()),
]
