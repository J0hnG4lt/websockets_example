# active_users/routing.py

from django.conf.urls import url
from . import consumers


websocket_urlpatterns = [
    #route('websocket.connect', consumers.ActiveUserConsumer.connect),
    #url('/ws/active_users/', consumers.ActiveUserConsumer),
    url('', consumers.ActiveUserConsumer)
]
