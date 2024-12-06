from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre


class Comision(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    numero = models.PositiveIntegerField()
    fecha_inicio = models.DateField()

    def __str__(self):
        return f"{self.curso} - {self.numero}"


class Alumno(models.Model):
    comision = models.ForeignKey(Comision, on_delete=models.SET_NULL, null=True)
    dni = models.IntegerField()
