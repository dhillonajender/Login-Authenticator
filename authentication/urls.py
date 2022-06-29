from django.urls import path
from . import views

urlpatterns = [
    path("", views.auth, name="auth"),
    path("app/",views.app_interface, name="app_interface"),
     
]