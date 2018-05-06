# active_users/consumers.py

from channels.generic.websocket import WebsocketConsumer
import json

class ActiveUserConsumer(WebsocketConsumer):

    def connect(self):
        
        print(self.scope)
        #self.username = self.scope['url_route']['kwargs']['username']
        
        """
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            "active"
        )
        """
        self.accept()
        
    def disconnect(self, close_code):
        pass
        
    def receive(self, text_data):
        
        text_data_json = json.loads(text_data)
        
        message = text_data_json['message']
        self.send(text_data=json.dumps({
            'message': message
        }))
        
