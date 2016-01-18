from django.shortcuts import render
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
            return HttpResponseRedirect("'appdocente/docente.html'")
        else:
            formulario = f

    return render(request, 'appdocente/docente.html', {'formu': formulario})

def eliminardoc(request, pk):
    u = docente.objects.get(pk=int(pk)).delete()
    return HttpResponseRedirect("appdocente/docente.html")