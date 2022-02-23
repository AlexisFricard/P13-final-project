from django.urls import path
from . import views

urlpatterns = [
    path("espace-collaboratif/<str:inview>", views.myspace, name="myspace"),
    path("log_out", views.log_out, name="log_out"),
    path("log_in", views.log_in, name="log_in"),
    path("mon-compte", views.myaccount, name="myaccount"),
]
