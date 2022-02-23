from django.urls import path
from . import views

urlpatterns = [
    path("nos-diplômés", views.ourstudent, name='ourstudent'),
]
