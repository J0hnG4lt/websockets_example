# active_users/consumers.py

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from active_users.models import User

class ActiveUserConsumer(WebsocketConsumer):

    def connect(self):
        """
        remaining_path_elems = self.scope['path_remaining'].split('/')
        
        self.username = remaining_path_elems[1]
        
        self.current_user = User.objects.get(username = self.username)
        
        self.current_user.active = True
        self.current_user.save()
        
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
        """
        async_to_sync(self.channel_layer.group_add)(
            "active",
            self.channel_name
        )
        
        self.accept()
    
    def status(self, arg) :
        print(arg)
    
    def disconnect(self, close_code):
        # Send message to room group
        self.current_user.active = False
        self.current_user.save()
        async_to_sync(self.channel_layer.group_send)(
            "active",
            {
                'type': 'receive',
                'message': self.username,
                'status' : "inactive"
            }
        )
        
    def receive(self, text_data):
        
        if type(text_data) is str :
            text_data_json = json.loads(text_data)
        else :
            text_data_json = text_data
        
        message = text_data_json['message']
        
        if "include" in text_data_json :
            
            self.current_user = User.objects.get(username = message)
            self.current_user.active = True
            self.current_user.save()
            self.username = message
            
        
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                "active",
                {
                    'type': 'receive',
                    'message': message,
                    'status' : "active"
                }
            )    
        
        if "exclude" in text_data_json :
            
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                "active",
                {
                    'type': 'receive',
                    'message': message,
                    'status' : "inactive"
                }
            )
        
        self.send(text_data=json.dumps({
            'message': message,
            'status' : text_data_json['status']
        }))
        
