from django.db import models

# The model or class for photo objects that will be used for the creation of Photo table in
# the local SQlite database
class Photo(models.Model):
    # the model attributes or table fields
    image = models.ImageField(upload_to='photos/')
    alt_text = models.CharField(max_length=250,blank=True,default='')

    # definition of how each photo will be printed in CMD when outputting photos from database
    def __str__(self):
        return f"{self.alt_text} ({self.image})"

# The model or class for contact objects that will be used for the creation of Contact table in
# the local SQlite database
class Contact(models.Model):
    # the model attributes or table fields
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)

    # definition of how each contact will be printed in CMD when outputting contacts
    def __str__(self):
        return f"{self.name} ({self.email}) ({self.message})"
    
    