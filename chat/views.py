from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def room(request, room_name):
    users = User.objects.all()
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'users': users
    })
