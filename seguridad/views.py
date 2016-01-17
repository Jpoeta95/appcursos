from django.shortcuts import render
from .models import alumno 

# Create your views here.
def login(request):
    return render(request,'login.html')
