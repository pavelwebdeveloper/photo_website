from django.shortcuts import render
from photo_webapp.models import Photo

# Create your views here.

def photo_gallery(request):
    photos = Photo.objects.all()
    context = {
        "photos": photos
    }
    return render(request, "photo_webapp/photo_gallery.html", context)

def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    context = {
        "photo": photo
    }
    return render(request, "photo_webapp/photo_details.html", context)