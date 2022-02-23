from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("actualité", views.actuality, name='actuality'),
    path("actualités", views.actualities, name="actualités"),
    path('setcookie', views.setcookie),
]
