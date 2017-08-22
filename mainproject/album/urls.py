from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.practice1, name='practice1'),
    url(r'^assignment1$', views.assignment1, name='assignment1'),
    url(r'^assignment2$', views.assignment2, name='assignment2'),
    url(r'^assignment3$', views.assignment3, name='assignment3'),

]