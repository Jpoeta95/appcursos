from django.conf.urls import url
from .views import  curso, tipocurso, prerequisito
urlpatterns = [
    url(r'^admin/', admin.site.urls), 
    url(r'^addtipo/$', tipocurso),
    url(r'^addcurso/$', curso),
]
