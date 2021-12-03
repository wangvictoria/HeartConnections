'''
Group #1 
Sovann Chang - sovann.d.chang@vanderbilt.edu
Kastur Koul - kastur.koul@vanderbilt.edu
Victoria Wang - victoria.m.wang@vanderbilt.edu
Kristen Wright - kristen.v.wright@vanderbilt.edu
Homework #3
'''

import datetime
from datetime import date, timedelta
from django.db import models
from django.db.models.fields import BooleanField
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
# Remember to register model in admin.py

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    birthdate = models.DateField(default=datetime.date(1900, 1, 1), validators=[MinValueValidator(datetime.date(1900, 1, 1)), MaxValueValidator(datetime.date.today() - datetime.timedelta(days=6575))])
    gender = models.CharField(max_length=20)
    sexuality = models.CharField(max_length=25)
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
    email = models.EmailField(max_length=50)

    matched = models.BooleanField(default=False)
    matched_with = models.CharField(max_length=100, blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)

    profile_pic = models.ImageField(null=True, blank=True)


    def get_absolute_url(self):
        # print(f"self.pk >>>>>>>>>>>>>>>>>>>>>>{self.pk}")
        return reverse('profile_detailed_view', kwargs={'pk': self.pk})
        #return ('profile_detailed_view', (), {'id': self.id})
        #return reverse('profile_detailed_view', args=[str(self.id)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    