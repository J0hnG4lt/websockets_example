from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^add_user', views.add_user, name="add_user"),
    url(r'^delete/(?P<username>.*)', views.delete_user, name="delete_user"),
    #url(r'(?P<username>[^/]+)/', views.activate_user, name='activate_user'),
]

