# websocket_example/routing.py


from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import active_users.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
                    URLRouter(
                        active_users.routing.websocket_urlpatterns
                    )
                 ),
})
