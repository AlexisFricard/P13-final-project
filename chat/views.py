from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
import json

from frontpage.models import Image
from mastercontrat.settings import MEDIA_URL


@login_required
def room(request, room_name):
    users = User.objects.all()
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'users': users,
        'media_url': MEDIA_URL
    })


def get_data(request):

    data = json.loads(request.body)
    username_ = data['author']
    user = User.objects.get(username=username_)

    try:
        img_obj = Image.objects.get(title=f'img_{user.id}')
        img_link = img_obj.image
    except:    # noqa
        img_link = 'grey.png'

    data = {
        'img_link':f'{img_link}'    # noqa
    }

    return JsonResponse(data)
