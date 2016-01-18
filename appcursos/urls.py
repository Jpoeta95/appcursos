from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('appdocente.urls')),
    url(r'^', include('seguridad.urls')),
    url(r'^', include('alumnos.urls')),
    url(r'^', include('aplicurso.urls')),

]
