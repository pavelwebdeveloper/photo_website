from django.shortcuts import render, redirect
from photo_webapp.models import Photo
from .forms import ContactForm
from django.db.models import Q

# The views for the website.

def photo_gallery(request):

    query = request.GET.get("searchFor", "")

    # Getting all the Photo objects from the local SQlite database
    photos = Photo.objects.all()

    # Selecting the photo objects that satisfy the search criteria provided through 
    # the search form in the header
    if query:
        photos = photos.filter(
            Q(image__icontains=query) |
            Q(alt_text__icontains=query)
        )

        # returning the photo_gallery.html page with the selected photo objects if a request is sent
        return render(request, "photo_webapp/photo_gallery.html", context = {
        "photos": photos
    }) 
    else:
        # returning the photo_gallery.html page with all the photos if no specific photos
        # are requested
        return render(request, "photo_webapp/photo_gallery.html", context = {
        "photos": photos
    })
    
    

def photo_details(request, pk):
    # getting the photo object that is requested 
    photo = Photo.objects.get(pk=pk)
    # providing the photo to return it with the photo_details.html page
    context = {
        "photo": photo
    }
    return render(request, "photo_webapp/photo_details.html", context)

def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        # checking if the data submitted through the form is valid
        if form.is_valid():
            # if valid then saving the data
            form.save()
            # navigating to the thank you page
            return redirect("thank_you")
    else:
        # if request method is not POST then preparing an empty form to return with 
        # the contact_form.html page
        form = ContactForm()

    return render(request, "photo_webapp/contact_form.html", {"form": form})

def thank_you(request):
    return render(request, "photo_webapp/thank_you.html")
