from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from active_users.models import User

class ActiveUserConsumer(WebsocketConsumer):

    def connect(self):
        
        # when an user connects, he is registered to a group
        async_to_sync(self.channel_layer.group_add)(
            "active",
            self.channel_name
        )
        
        self.current_user = None
        
        self.accept()
    
    
    def disconnect(self, close_code):
        
        # notify all the group members about this disconnection
        
        if hasattr(self, "current_user") and self.current_user :
            self.current_user.active = False
            self.current_user.save()
            
            async_to_sync(self.channel_layer.group_send)(
                "active",
                {
                    'type': 'receive',
                    'message': self.username,
                    'status' : "inactive",
                    'userid' : self.current_user.id
                }
            )
            self.current_user = None
        
    def receive(self, text_data):
        
        if type(text_data) is str :
            text_data_json = json.loads(text_data)
        else :
            text_data_json = text_data
        
        message = text_data_json['message']
        
        exists = len(User.objects.filter(username=message)) > 0
        userid = text_data_json['userid']
        
        # if include appears, then one user has selected a username
        if "include" in text_data_json and exists :
               
            self.current_user = User.objects.get(id = userid)
            self.current_user.active = True
            self.current_user.save()
            self.username = message
            
        
            # notify all the group members
            async_to_sync(self.channel_layer.group_send)(
                "active",
                {
                    'type': 'receive',
                    'message': message,
                    'status' : "active",
                    'userid' : self.current_user.id
                }
            )    
        
        # if exclude appears, then one user has closed its tab
        if "exclude" in text_data_json :
            
            User.objects.filter(id=userid).update(active=False)
            
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                "active",
                {
                    'type': 'receive',
                    'message': message,
                    'status' : "inactive",
                    'userid' : userid
                }
            )
        
        # send oneself a username with status
        self.send(text_data=json.dumps({
            'message': message,
            'status' : text_data_json['status'],
            'userid' : userid
        }))
        
