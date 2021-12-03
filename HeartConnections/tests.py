'''
Group #1 
Sovann Chang - sovann.d.chang@vanderbilt.edu
Kastur Koul - kastur.koul@vanderbilt.edu
Victoria Wang - victoria.m.wang@vanderbilt.edu
Kristen Wright - kristen.v.wright@vanderbilt.edu
Homework #3
'''

from django.test import TestCase, Client
from .models import Profile as ProfileModel
from .forms import ProfileForm
from django.urls import reverse
from django.test import override_settings
import datetime

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
        profile.birthdate = datetime.date(1998, 8, 21)
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
    
    def test_birthdate(self):
        profile = ProfileModel.objects.get(pk=1)
        birthdate = profile._meta.get_field('birthdate').verbose_name
        self.assertEqual(birthdate, 'birthdate')

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

    #### THESE TESTS REQUIRE HTML AND WILL NOT BE INCLUDED IN THE HOMEWORK 3 SUBMISSION ######
    def test_block_access_unmatched_profiles(self):
       response = self.client.get(reverse('unmatched_profiles'), follow=True)
       self.assertRedirects(response, '/accounts/login/?next=/HeartConnections/profile/unmatched/')
    
    def test_block_access_matched_profiles(self):
        response = self.client.get(reverse('matched_profiles'))
        self.assertRedirects(response, '/accounts/login/?next=/HeartConnections/profile/matched/')

    def test_block_access_matchmaker(self):
        response = self.client.get(reverse('admin_index'))
        self.assertRedirects(response, '/accounts/login/?next=/HeartConnections/matchmaker/')

    # Check if the profile is invalid (Missing first name, which is required)
    def test_createInvalidProfile(self):
        form = ProfileForm(data= {"last_name" : "Doe",
        "birthdate" : datetime.date(1998, 8, 21),
        "gender": "Male",
        "sexuality": "Straight",
        "country": "USA",
        "state_region": "Tenneesee",
        "city": "Nashville",
        "occupation": "Software Engineer",
        "company": "Amazon",
        "education": "Vanderbilt",
        "bio": "Hello!",
        "religion": "Python",
        "hobbies": "Coding",
        "dietary_preferences": "Everything",
        "alcohol": True,
        "smoking": False,
        "email": "johndoe@vanderbilt.edu"})
        self.assertFalse(form.is_valid())

# This class tests that the views in our views.py file are linked correctly
# This class uses Python's dummy client to send GET and POST requests to our server without a browser
### THE FOLLOWING TESTS REQUIRE HTML AND WILL NOT BE INCLUDED IN THE HOMEWORK 3 SUBMISSION ######
class SimpleViewsTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_RootPage(self):
        response = self.client.get('/', follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_AboutPage(self):
        response = self.client.get('/HeartConnections/about/', follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_ProfileCreatePage(self):
        response = self.client.get('/HeartConnections/profile/create/', follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_profile.html')

    '''def test_ProfileViewPage(self):
        response = self.client.get('/HeartConnections/profile/<int:pk>/', follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_detailed_view.html')'''

    def test_ProfileUnmatchedPage(self):
        response = self.client.get('/HeartConnections/profile/unmatched/', follow=True)
        self.assertEquals(response.status_code, 200)

    def test_ProfileMatchedPage(self):
        response = self.client.get('/HeartConnections/profile/matched/', follow=True)
        self.assertEquals(response.status_code, 200)

    def test_ContactPage(self):
        response = self.client.get('/HeartConnections/contact/', follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    ###### THIS IS A MANUAL TEST! #######
    # This tests that the send_mail function works when the client sends a valid POST request
    # To tests this: open a second terminal and set the pwd to LoveAajKal root directory
    # Set up a python virtual environment by running command: 'python3 -m venv env'
    # Activate the python environement by running command: 'source env/bin/activate'
    # Run the following command so that the server is listening for the client POST request:
    # 'python3 -m smtpd -n -c DebuggingServer localhost:1025'
    # Run this test function and an email should be 'delivered' in the second terminal
    # The email should be delivered in the terminal
    '''@override_settings(EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend')
    def test_emailContactForm(self):
         response = self.client.post('/HeartConnections/contact/', {'name': 'JOHN DOE', 'email': 'johndoe@gmail.com', 'message': 'TEST MESSAGE'}, follow=True)
         self.assertEquals(response.status_code, 200)
         self.assertTemplateUsed(response, 'contact.html')'''