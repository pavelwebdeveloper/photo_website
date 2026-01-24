from django.urls import path
from photo_webapp import views

# deciding which view to render depending on the urls
urlpatterns = [
    path("", views.photo_gallery, name="photo_gallery"),
    path("<int:pk>/", views.photo_details, name="photo_details"),
    path("contact_form/", views.contact_form, name="contact_form"),
    path("thank_you/", views.thank_you, name="thank_you"),
]
