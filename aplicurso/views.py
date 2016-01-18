from django.shortcuts import render, HttpResponse, HttpResponseRedirect,get_object_or_404
from .models import tipocurso, curso
from .forms import cursoForm
# Create your views here.

def tipocursos(request):
    if request.method == "POST": #esto sirve para preguntar si el método es post
        f = tipocursoForm(request.POST) #esto sirve para rescatar los datos del formulario

        if f.is_valid(): #esto sirve para validad formulario
            tp = tipocurso()
            tp.descripciontipocurso = request.POST["descripciontipocurso"]
            tp.save()

            tc = tipocurso.objects.all()
            formulario = tipocursoForm()

        else:
            formulario = f
    else:
        tc = tipocurso.objects.all().order_by('id')[:5]
        print(tc.query)
        formulario = tipocursoForm()
    return render(request, 'tipocurso.html', {'formu': formulario, 'tipocurso':tc})


def cursooo(request):
    cu = curso.objects.all()
    formulario = cursoForm()

    if request.method == "POST":
        f = cursoForm(request.POST)
        if f.is_valid():
            f.save()
        else:
            formulario = f

    return render(request, 'curso.html', {'formu': formulario, 'cursos':cu })

def actualizarcurso(request, pk):
    a = get_object_or_404(curso, pk= int(pk))
    formulario = cursoForm(instance = a)

    if request.method == "POST":

        f = cursoForm(request.POST, instance = a)

        if f.is_valid():
            f.save()
            return HttpResponseRedirect("/addcurso")
        else:
            formulario = f

    return render(request, 'actualiza_curso.html', {'formu': formulario})


def eliminarcurso(request, pk):
    u = curso.objects.get(pk=int(pk)).delete()
    return HttpResponseRedirect("/addcurso")