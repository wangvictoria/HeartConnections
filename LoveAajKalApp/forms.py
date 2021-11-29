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
import datetime
from datetime import date, timedelta
from django.utils.translation import gettext_lazy as _

# Create your forms here

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'id',
            'first_name',
            'last_name',
            'birthdate',
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
            'email',
            'profile_pic')

        error_messages = {
            'birthdate': {
                'required': _(""),
            },
        }

    def __init__(self, *args, **kwargs):
      self.user = kwargs.pop('user')  # cache the user object you pass in
      super(ProfileForm, self).__init__(*args, **kwargs)  # and carry on to init the form

    def clean_birthdate(self):
        data = self.cleaned_data["birthdate"]
        if data < datetime.date(1900, 1, 1):
            raise forms.ValidationError("Invalid birthdate: You were not born before 1900")
        elif data > (datetime.date.today() - datetime.timedelta(days=6575)):
            raise forms.ValidationError("Invalid birthdate: You are under 18 years old")
        return data;            

class MatchmakerForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'matched',
            'notes',
            'matched_with',
        )

class MatchActionForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'matched_with',
        )

