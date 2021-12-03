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

"""The main form for a user to create a profile"""
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


    """Checks the "birthdate" field to ensure that the user is not too young or older than anyone in the world"""
    def clean_birthdate(self):
        data = self.cleaned_data["birthdate"]
        if data < datetime.date(1900, 1, 1):
            raise forms.ValidationError("Invalid birthdate: You were not born before 1900")
        elif data > (datetime.date.today() - datetime.timedelta(days=6575)):
            raise forms.ValidationError("Invalid birthdate: You are under 18 years old")
        return data;            


"""The form used by Reshma to matchmake"""
class MatchmakerForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'matched',
            'notes',
            'matched_with',
        )


"""The form used by Reshma when actually making a match"""
class MatchActionForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'matched_with',
        )

