from django.conf.urls import url
from .views import  cursooo, tipocurso, eliminarcurso, actualizarcurso
urlpatterns = [
    url(r'^addtipo/$', tipocurso),
    url(r'^addcurso/$', cursooo),
    url(r'^eliminarcurso/(?P<pk>\d+)$', eliminarcurso),
    url(r'^addcurso/(?P<pk>\d+)$', actualizarcurso),
]
