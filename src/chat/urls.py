# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('select', views.select, name='select'),
    path('chat/<str:room_name>/', views.room, name='room'),
]
