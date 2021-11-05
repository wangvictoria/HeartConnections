'''
Group #1 
Sovann Chang - sovann.d.chang@vanderbilt.edu
Kastur Koul - kastur.koul@vanderbilt.edu
Victoria Wang - victoria.m.wang@vanderbilt.edu
Kristen Wright - kristen.v.wright@vanderbilt.edu
Homework #3
'''

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
    sexuality = models.CharField(max_length=25, default='Prefer not to say')
    country = models.CharField(max_length=40)
    state_region = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    occupation = models.CharField(max_length=25, blank=True, null=True)
    company = models.CharField(max_length=40, blank=True, null=True)
    education = models.CharField(max_length=50, blank=True, null=True)
    bio = models.CharField(max_length=1000, blank=True, null=True)
    religion = models.CharField(max_length=25, blank=True, null=True)
    hobbies = models.CharField(max_length=250, blank=True, null=True)
    dietary_preferences = models.CharField(max_length=100, blank=True, null=True)
    alcohol = models.BooleanField(blank=True, null=True)
    smoking = models.BooleanField(blank=True, null=True)
    email = models.CharField(max_length=50)

    matched = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})