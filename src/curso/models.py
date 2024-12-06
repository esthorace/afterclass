import unicodedata

from django.core.exceptions import ValidationError
from django.db import models


def normalizar_texto(texto: str) -> str:
    """Transforma el texto a una forma normalizada NFD
    (Normalization Form Decomposition).
    Esto significa que los caracteres compuestos,
    como las letras con tildes o diacríticos,
    se descomponen en su forma base y sus marcas diacríticas separadas.
    Ej: la letra "é" se descompone en "e" + un carácter de tilde combinable (U+0301).
    Convierte la cadena en bytes usando la codificación ASCII.
    Si un carácter no puede representarse en ASCII (por ejemplo, una "ñ" o una "é"),
    se ignora debido al parámetro "ignore".
    Luego, convierte los bytes resultantes nuevamente a una cadena de texto utilizando la codificación UTF-8."""
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")
    return texto


class Curso(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def validate_unique(self, exclude=None):
        """
        Valida que el modelo cumpla con las restricciones de unicidad definidas,
        incluyendo las personalizadas. Método propio de Django.
        """
        super().validate_unique(exclude)
        texto_normalizado = normalizar_texto(self.nombre)
        if Curso.objects.filter(nombre__iexact=texto_normalizado).exists():
            raise ValidationError("Ya existe. Se ha considerado tildes y mayúsculas.")

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
