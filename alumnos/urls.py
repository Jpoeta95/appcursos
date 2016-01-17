from django.conf.urls import url
from .views import alumno

urlpatterns = [
    url(r'^$', alumno),
]
