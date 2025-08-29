from django.shortcuts import render, get_object_or_404
from .models import Programa, Curso, Estudiante, Inscripcion

# Página de inicio
def home(request):
    return render(request, "estudiantes/home.html")

def lista_programas(request):
    programas = Programa.objects.all()
    return render(request, "estudiantes/lista_programas.html", {"programas": programas})

def detalle_programa(request, pk):
    programa = get_object_or_404(Programa, pk=pk)
    cursos = programa.curso_set.all()
    return render(request, "estudiantes/detalle_programa.html", {"programa": programa, "cursos": cursos})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, "estudiantes/lista_cursos.html", {"cursos": cursos})

def detalle_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    estudiantes = curso.estudiantes.all()  # M2M con Estudiante
    return render(request, "estudiantes/detalle_curso.html", {"curso": curso, "estudiantes": estudiantes})

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "estudiantes/lista_estudiantes.html", {"estudiantes": estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    cursos = estudiante.cursos.all()  # M2M con Curso
    return render(request, "estudiantes/detalle_estudiante.html", {"estudiante": estudiante, "cursos": cursos})

def lista_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, "estudiantes/lista_inscripciones.html", {"inscripciones": inscripciones})

def detalle_inscripcion(request, pk):
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    return render(request, "estudiantes/detalle_inscripcion.html", {"inscripcion": inscripcion})
