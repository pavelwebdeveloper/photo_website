from django.shortcuts import render
from photo_webapp.models import Photo

# Create your views here.

def home(request):
    photos = Photo.objects.all()
    context = {
        "photos": photos
    }
    return render(request, "home.html", context)

def photo_detail(request, pk):
    photo = Photo.objects.get(pk=pk)
    context = {
        "photo": photo
    }
    return render(request, "photo_details.html", context)