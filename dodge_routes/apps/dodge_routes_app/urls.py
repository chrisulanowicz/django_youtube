from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^dodge$', views.show, {'car':'all'}),
    url(r'^dodge/(?P<car>\w+)$', views.show)
]