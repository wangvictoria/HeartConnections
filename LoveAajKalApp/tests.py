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
from django.urls import reverse

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


    # The 18 tests below are basic tests to see that each attribute of the Profile has submitted and been saved successfully.

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

    def test_gender(self):
        profile = ProfileModel.objects.get(pk=1)
        gender = profile._meta.get_field('gender').verbose_name
        self.assertEqual(gender, 'gender')

    def test_sexuality(self):
        profile = ProfileModel.objects.get(pk=1)
        sexuality = profile._meta.get_field('sexuality').verbose_name
        self.assertEqual(sexuality, 'sexuality')

    def test_country(self):
        profile = ProfileModel.objects.get(pk=1)
        country = profile._meta.get_field('country').verbose_name
        self.assertEqual(country, 'country')

    def test_state_region(self):
        profile = ProfileModel.objects.get(pk=1)
        state_region = profile._meta.get_field('state_region').verbose_name
        self.assertEqual(state_region, 'state region')

    def test_city(self):
        profile = ProfileModel.objects.get(pk=1)
        city = profile._meta.get_field('city').verbose_name
        self.assertEqual(city, 'city')

    def test_occupation(self):
        profile = ProfileModel.objects.get(pk=1)
        occupation = profile._meta.get_field('occupation').verbose_name
        self.assertEqual(occupation, 'occupation')

    def test_company(self):
        profile = ProfileModel.objects.get(pk=1)
        company = profile._meta.get_field('company').verbose_name
        self.assertEqual(company, 'company')

    def test_education(self):
        profile = ProfileModel.objects.get(pk=1)
        education = profile._meta.get_field('education').verbose_name
        self.assertEqual(education, 'education')

    def test_bio(self):
        profile = ProfileModel.objects.get(pk=1)
        bio = profile._meta.get_field('bio').verbose_name
        self.assertEqual(bio, 'bio')

    def test_religion(self):
        profile = ProfileModel.objects.get(pk=1)
        religion = profile._meta.get_field('religion').verbose_name
        self.assertEqual(religion, 'religion')

    def test_hobbies(self):
        profile = ProfileModel.objects.get(pk=1)
        hobbies = profile._meta.get_field('hobbies').verbose_name
        self.assertEqual(hobbies, 'hobbies')

    def test_dietary_preferences(self):
        profile = ProfileModel.objects.get(pk=1)
        dietary_preferences = profile._meta.get_field('dietary_preferences').verbose_name
        self.assertEqual(dietary_preferences, 'dietary preferences')

    def test_alcohol(self):
        profile = ProfileModel.objects.get(pk=1)
        alcohol = profile._meta.get_field('alcohol').verbose_name
        self.assertEqual(alcohol, 'alcohol')

    def test_smoking(self):
        profile = ProfileModel.objects.get(pk=1)
        smoking = profile._meta.get_field('smoking').verbose_name
        self.assertEqual(smoking, 'smoking')

    def test_email(self):
        profile = ProfileModel.objects.get(pk=1)
        email = profile._meta.get_field('email').verbose_name
        self.assertEqual(email, 'email')


    # The 15 tests below are basic tests to see that each string attribute of the Profile has the correct character limit

    def test_first_name_max_length(self):
        profile = ProfileModel.objects.get(pk=1)
        max_length = profile._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 30)

    def test_last_name_max_length(self):
        profile = ProfileModel.objects.get(pk=1)
        max_length = profile._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 40)

    def test_gender_max_length(self):
        profile = ProfileModel.objects.get(pk=1)
        max_length = profile._meta.get_field('gender').max_length
        self.assertEqual(max_length, 20)

    def test_sexuality_max_length(self):
        profile = ProfileModel.objects.get(pk=1)
        max_length = profile._meta.get_field('sexuality').max_length
        self.assertEqual(max_length, 25)

    def test_country_max_length(self):
        profile = ProfileModel.objects.get(pk=1)
        max_length = profile._meta.get_field('country').max_length
        self.assertEqual(max_length, 40)

    def test_state_region_max_length(self):
        profile = ProfileModel.objects.get(pk=1)
        max_length = profile._meta.get_field('state_region').max_length
        self.assertEqual(max_length, 20)

    def test_city_max_length(self):
        profile = ProfileModel.objects.get(pk=1)
        max_length = profile._meta.get_field('city').max_length
        self.assertEqual(max_length, 30)

    def test_occupation_max_length(self):
        profile = ProfileModel.objects.get(pk=1)
        max_length = profile._meta.get_field('occupation').max_length
        self.assertEqual(max_length, 25)

    def test_company_max_length(self):
        profile = ProfileModel.objects.get(pk=1)
        max_length = profile._meta.get_field('company').max_length
        self.assertEqual(max_length, 40)

    def test_education_max_length(self):
        profile = ProfileModel.objects.get(pk=1)
        max_length = profile._meta.get_field('education').max_length
        self.assertEqual(max_length, 50)

    def test_bio_max_length(self):
        profile = ProfileModel.objects.get(pk=1)
        max_length = profile._meta.get_field('bio').max_length
        self.assertEqual(max_length, 1000)

    def test_religion_max_length(self):
        profile = ProfileModel.objects.get(pk=1)
        max_length = profile._meta.get_field('religion').max_length
        self.assertEqual(max_length, 25)

    def test_hobbies_max_length(self):
        profile = ProfileModel.objects.get(pk=1)
        max_length = profile._meta.get_field('hobbies').max_length
        self.assertEqual(max_length, 250)

    def test_dietary_preferences_max_length(self):
        profile = ProfileModel.objects.get(pk=1)
        max_length = profile._meta.get_field('dietary_preferences').max_length
        self.assertEqual(max_length, 100)

    def test_email_max_length(self):
        profile = ProfileModel.objects.get(pk=1)
        max_length = profile._meta.get_field('email').max_length
        self.assertEqual(max_length, 50)


    
    # These tests check to see if different webpages are blocked to users who are not admins.
    # Each page should redirect the user to the admin login page, with the next page that the
    # site will access after that being the page the user attempted to access (if login is successful)
    
    def test_block_access_unmatched_profiles(self):
        response = self.client.get(reverse('unmatched_profiles'))
        self.assertRedirects(response, '/accounts/login/?next=/LoveAajKalApp/profile/unmatched_profiles/')
    
    def test_block_access_matched_profiles(self):
        response = self.client.get(reverse('matched_profiles'))
        self.assertRedirects(response, '/accounts/login/?next=/LoveAajKalApp/profile/matched_profiles')

    def test_block_access_matchmaker(self):
        response = self.client.get(reverse('admin_index'))
        self.assertRedirects(response, '/accounts/login/?next=/LoveAajKalApp/matchmaker/')
    

    '''

    #### NEED TO FINISH!!!! 
    def test_createInvalidProfile(self):
        form = ProfileForm(data= {"first_name": "John", "last_name" : "Doe",
        "profile.age" :25,
        "profile.gender": "Male",
        "profile.sexuality": "Straight",
        "profile.country": "USA",
        "profile.state_region": "Tenneesee",
        "profile.city": "Nashville",
        "profile.occupation": "Software Engineer",
        "profile.company": "Amazon",
        "profile.education": "Vanderbilt",
        "profile.bio": "Hello!",
        "profile.religion": "Coding",
        "profile.hobbies": "Coding, not sleeping",
        "profile.dietary_preferences": "Everything",
        "profile.alcohol": True,
        "profile.smoking": False,
        "profile.email": "johndoe@vanderbilt.edu"})
    '''
    
    '''class InvalidFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create an invalid profile
        profile = ProfileModel() 
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

    def test_createInvalidProfile(self):
        response = self.client.post() 
        self.assertEqual(response.status_code, 200)
        #self.assetFormError()

    def emailProfiles(self):
        pass
    '''