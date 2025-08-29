from django.contrib import admin
from .models import Programa, Curso, Estudiante, Inscripcion


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'programa', 'descripcion')
    list_filter = ('programa',)
    search_fields = ('nombre',)
    ordering = ('programa', 'nombre')


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'programa')
    list_filter = ('programa',)
    search_fields = ('nombre', 'email')
    ordering = ('nombre',)


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id', 'estudiante', 'curso', 'fecha')
    list_filter = ('curso', 'fecha')
    search_fields = ('estudiante__nombre', 'curso__nombre')
    ordering = ('-fecha',)
