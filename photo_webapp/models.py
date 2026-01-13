from django.db import models

# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    alt_text = models.CharField(max_length=100,blank=True,default='')
    