from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
# Remember to register model in admin.py

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    country = models.CharField(max_length=40)
    state_region = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    occupation = models.CharField(max_length=25, blank=True, null=True)
    education = models.CharField(max_length=50, blank=True, null=True)
    bio = models.CharField(max_length=1000, blank=True, null=True)
    religion = models.CharField(max_length=25, blank=True, null=True)
    hobbies = models.CharField(max_length=250, blank=True, null=True)
    dietary_preferences = models.CharField(max_length=100, blank=True, null=True)
    alcohol = models.BooleanField(blank=True, null=True)
    smoking = models.BooleanField(blank=True, null=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})