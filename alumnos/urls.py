from django.conf.urls import url, include
from .views import alumn,eliminaralum,actualizaralum

urlpatterns = [
    url(r'^alumno/$', alumn ),
    url(r'^eliminaralumno/(?P<pk>\d+)$', eliminaralum),
    url(r'^alumno/(?P<pk>\d+)$', actualizaralum),
]