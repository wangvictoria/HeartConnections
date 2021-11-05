'''
Group #1 
Sovann Chang - sovann.d.chang@vanderbilt.edu
Kastur Koul - kastur.koul@vanderbilt.edu
Victoria Wang - victoria.m.wang@vanderbilt.edu
Kristen Wright - kristen.v.wright@vanderbilt.edu
Homework #3
'''

from django.test import TestCase
from .models import Profile as ProfileModel
from .forms import ProfileForm

# This is the video that shows unit tests in Django:
# https://www.youtube.com/watch?v=DmRpNoQEx2o&ab_channel=GoDjango 

# Create your tests here.
class ProfileTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a profile
        profile = ProfileModel()

        profile.first_name = "John"
        profile.last_name = "Doe" 
        profile.age = 25
        profile.gender = "Male"
        profile.sexuality = "Straight",
        profile.country = "USA"
        profile.state_region = "Tenneesee"
        profile.city = "Nashville"
        profile.occupation = "Software Engineer"
        profile.company = "Amazon"
        profile.education = "Vanderbilt" 
        profile.bio = "Hello!"
        profile.religion = "Coding"
        profile.hobbies = "Coding, not sleeping"
        profile.dietary_preferences = "Everything"
        profile.alcohol = True 
        profile.smoking = False 
        profile.email = "johndoe@vanderbilt.edu"
        profile.save()

    def test_first_name(self):
        profile = ProfileModel.objects.get(pk=1)
        first_name = profile._meta.get_field('first_name').verbose_name
        self.assertEqual(first_name, 'first name')

    def test_last_name(self):
        profile = ProfileModel.objects.get(pk=1)
        last_name = profile._meta.get_field('last_name').verbose_name
        self.assertEqual(last_name, 'last name')
    
    def test_age(self):
        profile = ProfileModel.objects.get(pk=1)
        age = profile._meta.get_field('age').verbose_name
        self.assertEqual(age, 'age')

    '''def test_createInvalidProfile(self):
        response = self.client.post() #EEEEEEEEEEEE D: 
        self.assertEqual(response.status_code, 200)
        self.assetFormError()

    def emailProfiles(self):
        pass'''