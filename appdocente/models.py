from django.db import models

# Create your models here.
class docente(models.Model):
    dni               = models.CharField(max_length=8)
    nombre            = models.CharField(max_length=18)
    ape_pat           = models.CharField(max_length=18)
    ape_mat           = models.CharField(max_length=18)
    fecha_agregado    = models.DateTimeField(auto_now_add=True)
    fecha_actualizado = models.DateTimeField(auto_now=True)
