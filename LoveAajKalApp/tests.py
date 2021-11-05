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

# This is the video that shows unit tests in Django:
# https://www.youtube.com/watch?v=DmRpNoQEx2o&ab_channel=GoDjango 

# Create your tests here.
class ProfileTest(TestCase):   
    def test_createProfile(self):
        # Create a profile
        print("CREATE PROFILE")
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

        record = ProfileModel.objects.get(pk=1)
        self.assertEqual(record, profile)

    def test_createInvalidProfile(self):
        # Create a profile
        print("CREATE INVALID PROFILE")
        profile = ProfileModel()

        # No first name = invalid 
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

        record = ProfileModel.objects.get(pk=2)
        #self.assertNotEqual(record, profile)
        print(record)
        #self.assertEqual(record, None)
        self.assetFormError()

    '''def test_checkName(self):
        # If the profile has been added to the database,
        # we should be able to print the name of the User 
        print("Test Check Name")
        john_profile = ProfileModel.objects.all().filter(first_name="John")
        self.assertEqual(john_profile.first_name, "John")
        self.assertEqual(john_profile.last_name, "Doe")
        print("YEET")

    def emailProfiles(self):
        pass'''