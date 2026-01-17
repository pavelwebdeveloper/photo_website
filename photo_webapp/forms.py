#from django import forms
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    email= forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        error_messages={
            "invalid": "Please provide a valid email address (for example: name@email.com)"
        }
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"})
    )

    class Meta:
        model = Contact
        fields = ["name", "email", "message"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 3:
            raise forms.ValidationError("Name must be more than 2 characters")
        return name
    
    def clean_message(self):
        message = self.cleaned_data["message"]
        if len(message) < 5:
            raise forms.ValidationError("Please, provide more information about your message")
        return message
    
    
