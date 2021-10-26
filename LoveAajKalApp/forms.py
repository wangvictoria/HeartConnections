from django import forms
from .models import Profile

# Create your forms here

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'id',
            'first_name',
            'last_name',
            'age',
            'gender', 
            'country',
            'state_region',
            'city',
            'occupation',
            'education', 
            'bio',
            'religion',
            'hobbies',
            'dietary_preferences',
            'alcohol',
            'smoking',
            'username',
            'password',
            'email')

# Creating a form to add a profile.
    # form = ProfileForm()

