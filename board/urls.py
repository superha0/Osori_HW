from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
#	url(r'^board/', views.test_board, name = 'test_board'),
]
