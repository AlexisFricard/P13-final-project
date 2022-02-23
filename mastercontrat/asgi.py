"""
ASGI config for mastercontrat project.
"""
import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing



if os.environ.get('ENV') == "DEV":
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'mastercontrat.dev_settings'
        )

    application = ProtocolTypeRouter({
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )
        ),
    })

else:
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'mastercontrat.settings'
        )

    application = ProtocolTypeRouter({
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )
        ),
    })
