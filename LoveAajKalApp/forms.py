'''
Group #1 
Sovann Chang - sovann.d.chang@vanderbilt.edu
Kastur Koul - kastur.koul@vanderbilt.edu
Victoria Wang - victoria.m.wang@vanderbilt.edu
Kristen Wright - kristen.v.wright@vanderbilt.edu
Homework #3
'''

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
            'sexuality',
            'country',
            'state_region',
            'city',
            'occupation',
            'company',
            'education', 
            'bio',
            'religion',
            'hobbies',
            'dietary_preferences',
            'alcohol',
            'smoking',
            'email',)
            # Creating a form to add a profile.
            # form = ProfileForm()

class MatchmakerForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'matched',
            'notes',
        )

class MatchActionForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'matched_with',
        )

