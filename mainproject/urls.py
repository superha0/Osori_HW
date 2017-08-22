from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^test_board/', include('mainproject.boards.urls')),
    url(r'^',include('mainproject.album.urls')),
]