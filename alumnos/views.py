from django.shortcuts import render
from .models import alumno
from .form import alumnoForm

# Create your views here.
def alumn(request):
    cu = alumno.objects.all()
    formulario = alumnoForm()

    if request.method == "POST":
        f = alumnoForm(request.POST)
        if f.is_valid():
            f.save()
        else:
            formulario = f

    return render(request, 'alumno.html', {'formu': formulario, 'alumno':cu })

def actualizaralum(request, pk):
    a = get_object_or_404(alumno, pk= int(pk))
    formulario = alumnoForm(instance = a)

    if request.method == "POST":

        f = alumnoForm(request.POST, instance = a)

        if f.is_valid():
            f.save()
            return HttpResponseRedirect("'alumno.html'")
        else:
            formulario = f

    return render(request, 'alumno.html', {'formu': formulario})

def eliminaralum(request, pk):
    u = alumno.objects.get(pk=int(pk)).delete()
    return HttpResponseRedirect("alumno.html")