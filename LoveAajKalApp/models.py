from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    country = models.CharField(max_length=40)
    state_region = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    occupation = models.CharField(max_length=25)
    education = models.CharField(max_length=50)
    bio = models.CharField(max_length=1000)
    religion = models.CharField(max_length=25)
    hobbies = models.CharField(max_length=250)
    dietary_preferences = models.CharField(max_length=100)
    alcohol = models.BooleanField()
    smoking = models.BooleanField()