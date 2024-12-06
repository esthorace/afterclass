from django.shortcuts import redirect, render

from .forms import AlumnoForm, ComisionForm, CursoForm
from .models import Alumno, Comision, Curso


def index(request):
    return render(request, "curso/index.html")


def about(request):
    return render(request, "curso/about.html")


def curso_list(request):
    query = Curso.objects.all()
    context = {"object_list": query}
    return render(request, "curso/curso_list.html", context)


def curso_create(request):
    if request.method == "GET":
        form = CursoForm()
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("curso:curso_list")
    return render(request, "curso/curso_form.html", {"form": form})


def comision_list(request):
    query = Comision.objects.all()
    context = {"object_list": query}
    return render(request, "curso/comision_list.html", context)


def comision_create(request):
    if request.method == "GET":
        form = ComisionForm()
    if request.method == "POST":
        form = ComisionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("curso:comision_list")
    return render(request, "curso/comision_form.html", {"form": form})


def alumno_list(request):
    query = Alumno.objects.all()
    context = {"object_list": query}
    return render(request, "curso/alumno_list.html", context)


def alumno_create(request):
    if request.method == "GET":
        form = AlumnoForm()
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("curso:alumno_list")
    return render(request, "curso/alumno_form.html", {"form": form})
