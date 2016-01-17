from django.shortcuts import render
from .models import alumno

# Create your views here.
def alumno(request):
    return render(request, 'alumno.html')
