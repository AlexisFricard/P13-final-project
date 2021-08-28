from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("présentation", views.presentation, name='presentation'),
    path("etAprès", views.after, name='after'),
    path("nosDiplômés", views.ourstudent, name='ourstudent'),
    path("monEspace", views.myspace, name="myspace"),
    path("log_out", views.log_out, name="log_out"),
    path("add_data", views.add_data, name="add_data"),
    path("ticket", views.ticket, name="ticket"),
    path("add_user", views.add_user, name="add_user"),
    path("gestionDuSite", views.manage, name="manage"),
    path("association", views.association, name='association'),
    path("helpdashboard", views.helpdashboard, name='helpdashboard'),
    path("actualité", views.actuality, name='actuality'),
    path("monCompte", views.myaccount, name="myaccount")
]
