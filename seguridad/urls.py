from django.conf.urls import url
from .views import login,logie
urlpatterns = [
    url(r'^$', login),
    url(r'^logie/$', logie),
]
