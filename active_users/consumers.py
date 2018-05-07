# active_users/consumers.py

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class ActiveUserConsumer(WebsocketConsumer):

    def connect(self):
        
        remaining_path_elems = self.scope['path_remaining'].split('/')
        
        self.username = remaining_path_elems[1]
        
        
        async_to_sync(self.channel_layer.group_add)(
            "active",
            self.channel_name
        )
        
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            "active",
            {
                'type': 'receive',
                'message': self.username,
                'status' : "active"
            }
        )
        
        self.accept()
    
    def status(self, arg) :
        print(arg)
    
    def disconnect(self, close_code):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            "active",
            {
                'type': 'receive',
                'message': self.username,
                'status' : "inactive"
            }
        )
        
    def receive(self, text_data):
        
        text_data_json = text_data
        message = text_data_json['message']
        self.send(text_data=json.dumps({
            'message': message,
            'status' : text_data_json['status']
        }))
        
