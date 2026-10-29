from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    ci = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Curso(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Inscripcion(models.Model):
    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE
    )

    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.alumno} - {self.curso}"