from django.contrib import admin
from .models import Objetivo, Rutina, Miembro, MiembroTipo, MiembroEstado, Genero, Medicion

@admin.register(Objetivo)
class ObjetivoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    search_fields = ['nombre']


@admin.register(Miembro)
class MiembroAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellidos','tipo_membresia']
    list_filter = ['nombre']
    search_fields = ['nombre','apellidos']


@admin.register(Rutina)
class RutinaAdmin(admin.ModelAdmin):
    list_display = ['miembro','fecha']
    list_filter = ['miembro']
    search_fields = ['miembro','fecha']


@admin.register(MiembroEstado)
class MiembroEstadoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    search_fields = ['nombre']


@admin.register(MiembroTipo)
class MiembroTipoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    search_fields = ['nombre']


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    search_fields = ['nombre']


@admin.register(Medicion)
class MedicionAdmin(admin.ModelAdmin):
    list_display = ['miembro', 'fecha_medicion']
    list_filter = ['fecha_medicion', 'miembro']
    search_fields = ['miembro']