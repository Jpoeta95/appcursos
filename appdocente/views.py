from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import docente
from .forms import docenteForm

# Create your views here.
def docent(request):
    cu = docente.objects.all()
    formulario = docenteForm()

    if request.method == "POST":
        f = docenteForm(request.POST)
        if f.is_valid():
            f.save()
        else:
            formulario = f

    return render(request, 'appdocente/docente.html', {'formu': formulario, 'docentes':cu })

def actualizardoc(request, pk):
    a = get_object_or_404(docente, pk= int(pk))
    formulario = docenteForm(instance = a)

    if request.method == "POST":

        f = docenteForm(request.POST, instance = a)

        if f.is_valid():
            f.save()
            return HttpResponseRedirect("/docente")
        else:
            formulario = f

    return render(request, 'appdocente/docente.html', {'formu': formulario})

def eliminardoc(request, pkd):
    print("hola jose")
    u = docente.objects.get(pk=int(pkd)).delete()
    return HttpResponseRedirect("/docente")