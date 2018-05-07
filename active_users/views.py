from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from active_users.models import User
from active_users.forms import UserForm


# Create your views here.

from django.http import HttpResponse, JsonResponse


def index(request):
    
    form = UserForm()
            
    users = User.objects.all()
    
    return render(request, 'index.html', {'users': users,
                                          'form' : form})

def get_user(request, userid) :
    
    user = User.objects.get(id=userid)
    
    responsedata = {
        'username' : user.username
    }
    
    return JsonResponse(responsedata)

# serves a post request for user edition
def edit_user(request) :
    
    if request.method == 'POST' :
        
        previous = request.POST["previoususername"]
        new = request.POST["username"]
        
        User.objects.filter(username=previous).update(username=new,
                                                      active = False)
        
    return redirect("index")

# serves a get request for user deletion
def delete_user(request, username) :
    
    user = User.objects.get(username = username)
    user.delete()
    
    return redirect("index")

# serves a post request for user creation
def add_user(request) :
    
    if request.method == 'POST' :
        
        form = UserForm(request.POST)
        username = form['username'].value()
        does_not_exist = len(User.objects.filter(username=username)) == 0
        
        if form.is_valid() and does_not_exist :
            newUser = User(username = username)
            newUser.save()
        
    return redirect("index")


