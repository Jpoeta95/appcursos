from django.db import models

# Create your models here.
class tipocurso(models.Model):
   descripciontipocurso = models.CharField(max_length=15)
   estadotipo           = models.BooleanField(default=True)
   fechaagregado        = models.DateTimeField(auto_now_add=True)
   fechaactualizado     = models.DateTimeField(auto_now=True)
   def __str__(self):
       return '%s' % (self.descripciontipocurso)

class curso(models.Model):
   descripcioncurso     = models.CharField(max_length=255)
   creditos             = models.IntegerField()
   ciclo                = models.CharField(max_length=8)
   prerequisito         = models.ManyToManyField('self', blank=True)
   tipocurso            = models.ForeignKey(tipocurso)
   estadocurso          = models.BooleanField(default=True)
   fechaagregado        = models.DateTimeField(auto_now_add=True)
   fechaactualizado     = models.DateTimeField(auto_now=True)

   def __str__(self):
       return '%s' % (self.descripcioncurso)

