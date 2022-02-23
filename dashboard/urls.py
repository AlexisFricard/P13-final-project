from django.urls import path
from . import views

urlpatterns = [
    # DASHBOARD
    path('gestion-du-site/<str:inview>', views.dashboard, name="dashboard"),
    path("add_data", views.add_data, name="add_data"),
    path('mod_data', views.mod_data, name="mod_data"),
    path('del_', views.delete_it),
]
