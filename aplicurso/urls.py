from django.conf.urls import url
from .views import  curso, tipocurso
urlpatterns = [
    url(r'^admin/', admin.site.urls), 
    url(r'^addtipo/$', tipocurso),
    url(r'^addcurso/$', curso),
]
