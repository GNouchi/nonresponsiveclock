from django.conf.urls import url
from . import views
# this page matches the url 
urlpatterns = [
    url(r'^random_word$', views.random_word),
    url(r'^random_word/reset$', views.reset),
    url(r'^',views.index),
]
