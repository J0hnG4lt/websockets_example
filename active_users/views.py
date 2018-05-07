from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from active_users.models import User

# Create your views here.

from django.http import HttpResponse


def index(request):
    
    users = User.objects.all()
    #paginator = Paginator(users, 20) # Show 20 contacts per page

    #page = request.GET.get('page')
    #users = paginator.get_page(page)
    return render(request, 'index.html', {'users': users})


def activate_user(request, username):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
