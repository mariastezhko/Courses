from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/delete/(?P<number>\d+)$', views.delete),
    url(r'^courses/add/?$', views.create),
    url(r'^courses/delete_form/(?P<number>\d+)$', views.delete_form)

]
