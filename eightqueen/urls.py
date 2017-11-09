from django.conf.urls import url

from . import views,check,solution

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^check$', check.index, name='check'),
    url(r'^solution$', solution.index, name='solution'),
]