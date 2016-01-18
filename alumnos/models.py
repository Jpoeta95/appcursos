from django.db import models

from aplicurso.models import curso
from appdocente.models import docente
# Create your models here.
class alumno(models.Model):
   descripcionalumno = models.CharField(max_length=100)
   dni               = models.CharField(max_length=8)
   fechanac          = models.DateField(auto_now=True)
   alumno_docente    = models.ManyToManyField(docente,blank=True)
   alumno_curso      = models.ManyToManyField(curso,blank=True)
   
   def __str__(self):
       return '%s' % (self.descripcionalumno)
