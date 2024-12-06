from django import forms

from .models import Alumno, Comision, Curso


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"


class ComisionForm(forms.ModelForm):
    class Meta:
        model = Comision
        fields = "__all__"
        widgets = {
            "fecha_inicio": forms.DateInput(attrs={"type": "date"}),
        }


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = "__all__"
