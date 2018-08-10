from django.conf.urls import url 
from . import views 
# this page matches the url 
urlpatterns = [
    url(r'^create$', views.create), 
    url(r'^', views.index),