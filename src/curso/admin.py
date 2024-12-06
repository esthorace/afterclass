from django.contrib import admin

from .models import Alumno, Comision, Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre",)


@admin.register(Comision)
class ComisionAdmin(admin.ModelAdmin):
    list_display = ("curso__nombre", "numero", "fecha_inicio")


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("comision", "dni")
