from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from active_users.models import User
from active_users.forms import UserForm

# Create your views here.

from django.http import HttpResponse


def index(request):
    
    form = UserForm()
            
    users = User.objects.all()
    
    return render(request, 'index.html', {'users': users,
                                          'form' : form})

def delete_user(request, username) :
    
    user = User.objects.get(username = username)
    user.delete()
    
    return redirect("index")

def add_user(request) :
    
    if request.method == 'POST' :
        
        form = UserForm(request.POST)
        username = form['username'].value()
        does_not_exist = len(User.objects.filter(username=username)) == 0
        
        if form.is_valid() and does_not_exist :
            newUser = User(username = username)
            newUser.save()
        
    return redirect("index")

def activate_user(request, username):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
