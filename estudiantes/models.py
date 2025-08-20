
from django.db import models

class Programa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    programa = models.ForeignKey(Programa, on_delete=models.SET_NULL, null=True, blank=True)
    cursos = models.ManyToManyField(Curso, related_name='estudiantes', blank=True)

    def __str__(self):
        return self.nombre