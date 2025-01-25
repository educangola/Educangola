import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from seu_app import consumers  # Importe o Consumer da sua aplicação

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ANGOLA_EDUCA.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(  # WebSocket com autenticação
        URLRouter([
            path('ws/mensagem/', consumers.MensagemConsumer.as_asgi()),  # Adiciona o URL do WebSocket
        ])
    ),
})
