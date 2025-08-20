from django.contrib import admin

from .models import Programa, Curso, Estudiante

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'programa')
    list_filter = ('programa',)
    search_fields = ('nombre',)

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'programa')
    list_filter = ('programa',)
    search_fields = ('nombre', 'email')
    filter_horizontal = ('cursos',)  