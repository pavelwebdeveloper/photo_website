from django.urls import path
from photo_webapp import views

urlpatterns = [
    path("", views.home, name="home"),
]