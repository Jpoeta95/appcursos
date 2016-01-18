from django.conf.urls import url, include
from .views import docent,eliminardoc,actualizardoc

urlpatterns = [
    url(r'^docente/$', docent ),
    url(r'^eliminardocente/(?P<pk>\d+)$', eliminardoc),
    url(r'^actual/(?P<pk>\d+)$', actualizardoc),
]
