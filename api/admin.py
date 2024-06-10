from django.contrib import admin
from .models import (
    Objetivo,
    Rutina,
    Instructor,
    Miembro,
    MiembroTipo,
    MiembroEstado,
    Genero,
    Medicion, UnidadDeMedida, Ejercicio, Repeticion, DiaDeRutina, EjerciciosPorDia, GrupoMuscular, Instrumento,
    MusculosPorDia, RecursosDeEjercicio, InstrumentosDeEjercicio, MusculosDeEjercicio, Recurso, Musculo
)


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


@admin.register(Miembro)
class MiembroAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellidos','tipo_membresia']
    list_filter = ['nombre']
    search_fields = ['nombre','apellidos']


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellidos']
    list_filter = ['nombre']
    search_fields = ['nombre','apellidos']


@admin.register(Objetivo)
class ObjetivoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    search_fields = ['nombre']


@admin.register(UnidadDeMedida)
class UnidadDeMedidaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    search_fields = ['nombre']


@admin.register(Medicion)
class MedicionAdmin(admin.ModelAdmin):
    list_display = ['miembro', 'fecha_medicion']
    list_filter = ['fecha_medicion', 'miembro']
    search_fields = ['miembro']


@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    search_fields = ['nombre']


@admin.register(Repeticion)
class RepeticionAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    search_fields = ['nombre']


@admin.register(Rutina)
class RutinaAdmin(admin.ModelAdmin):
    list_display = ['miembro','fecha']
    list_filter = ['miembro']
    search_fields = ['miembro','fecha']


@admin.register(DiaDeRutina)
class DiaDeRutinaAdmin(admin.ModelAdmin):
    list_display = ['rutina', 'descripcion']


@admin.register(EjerciciosPorDia)
class EjerciciosPorDianAdmin(admin.ModelAdmin):
    list_display = ['dia_de_rutina', 'ejercicio']
    list_filter = ['dia_de_rutina', 'ejercicio']
    search_fields = ['dia_de_rutina', 'ejercicio']


@admin.register(GrupoMuscular)
class GrupoMuscularAdmin(admin.ModelAdmin):
    list_display = ['nombre']


@admin.register(Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ['nombre']


@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ['nombre']


@admin.register(MusculosDeEjercicio)
class MusculosDeEjercicioAdmin(admin.ModelAdmin):
    list_display = ['ejercicio', 'musculo']


@admin.register(InstrumentosDeEjercicio)
class InstrumentosDeEjercicioAdmin(admin.ModelAdmin):
    list_display = ['ejercicio', 'instrumento']


@admin.register(RecursosDeEjercicio)
class RecursosDeEjercicioAdmin(admin.ModelAdmin):
    list_display = ['ejercicio']


@admin.register(MusculosPorDia)
class MusculosPorDiaAdmin(admin.ModelAdmin):
    list_display = ['dia_de_rutina', 'grupo_muscular']


@admin.register(Musculo)
class MusculoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'grupo_muscular']
    list_filter = [ 'grupo_muscular']