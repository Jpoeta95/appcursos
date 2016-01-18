from django.conf.urls import url, include
from .views import docent,eliminardoc,actualizardoc

urlpatterns = [
    url(r'^docente/$', docent ),
    url(r'^eliminardocente/(?P<pkd>\d+)$', eliminardoc),
    url(r'^docente/(?P<pk>\d+)$', actualizardoc),
]
