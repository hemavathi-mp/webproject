from django.shortcuts import render

# Create your views here.
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MachineDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        await self.send(text_data=json.dumps({
            'type': 'machine_data',
            'data': "Your real-time machine data"
        }))