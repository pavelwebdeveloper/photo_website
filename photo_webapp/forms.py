#from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    #your_name = forms.CharField(label="Your name", max_length=100)
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
