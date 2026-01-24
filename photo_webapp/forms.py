#from django import forms
from django import forms
from .models import Contact


# The model or class for contact form
class ContactForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    email= forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        # the message that will be output for users if email format is wrong
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
        # checking if the name is less than 3 characters long
        if len(name) < 3:
            # the message that will be output for users if name format is wrong
            raise forms.ValidationError("Name must be more than 2 characters")
        return name
    
    def clean_message(self):
        message = self.cleaned_data["message"]
        # checking if the message is less than 5 characters long
        if len(message) < 5:
            # the message that will be output for users if the message is not long enough
            raise forms.ValidationError("Please, provide more information about your message")
        return message
    
    