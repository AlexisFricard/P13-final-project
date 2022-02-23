from django.urls import path
from . import views

urlpatterns = [
    path("présentation", views.presentation_page, name='presentation_page'),
]
