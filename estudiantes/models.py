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

    def __str__(self):
        return self.nombre


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='inscripciones')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripciones')
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('estudiante', 'curso')  

    def __str__(self):
        return f"{self.estudiante} inscrito en {self.curso}"
