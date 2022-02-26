# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # path('select', views.select, name='select'),
    path('discussion/<str:room_name>/', views.room, name='room'),
    path('get_data', views.get_data)
]
