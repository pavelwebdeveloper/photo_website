from django.urls import path
from photo_webapp import views

urlpatterns = [
    path("", views.photo_gallery, name="photo_gallery"),
    path("<int:pk>/", views.photo_details, name="photo_details"),
]