from django.db import models

# Create your models here.
class menmodel(models.Model):
    img = models.ImageField(upload_to="static/media/", default=None)
    name= models.CharField(max_length=15, default=None)
    age= models.IntegerField(default=None)
    city= models.CharField(max_length=15, default=None)
    salary = models.IntegerField(default=None)
