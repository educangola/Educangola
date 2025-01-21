import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MensagemConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Conectar ao grupo de mensagens
        self.group_name = "mensagens_group"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Receber uma mensagem do WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        mensagem = data['message']

        # Enviar mensagem para o grupo de WebSocket
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'mensagem_enviada',
                'message': mensagem
            }
        )

    # Enviar mensagem para WebSocket
    async def mensagem_enviada(self, event):
        mensagem = event['message']

        # Enviar a mensagem para o WebSocket
        await self.send(text_data=json.dumps({
            'message': mensagem
        }))
