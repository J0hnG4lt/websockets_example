from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #url(r'(?P<username>[^/]+)/', views.activate_user, name='activate_user'),
]

