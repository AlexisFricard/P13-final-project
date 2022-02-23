from django.urls import path
from . import views

urlpatterns = [
    path("et-après", views.after, name='after'),
]
