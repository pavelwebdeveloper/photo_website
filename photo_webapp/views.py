from django.shortcuts import render, redirect
from photo_webapp.models import Photo
from .forms import ContactForm
from django.db.models import Q

# Create your views here.

def photo_gallery(request):

    query = request.GET.get("searchFor", "")

    photos = Photo.objects.all()

    if query:
        photos = photos.filter(
            Q(image__icontains=query) |
            Q(alt_text__icontains=query)
        )

        return render(request, "photo_webapp/photo_gallery.html", context = {
        "photos": photos
    }) 
    else:
        return render(request, "photo_webapp/photo_gallery.html", context = {
        "photos": photos
    })
    
    

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



