from django.shortcuts import render, redirect
from photo_webapp.models import Photo
from .forms import ContactForm

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

def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("thank_you")
    else:
        form = ContactForm()

    return render(request, "photo_webapp/contact_form.html", {"form": form})

def thank_you(request):
    return render(request, "photo_webapp/thank_you.html")
