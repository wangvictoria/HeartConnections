'''
Group #1 
Sovann Chang - sovann.d.chang@vanderbilt.edu
Kastur Koul - kastur.koul@vanderbilt.edu
Victoria Wang - victoria.m.wang@vanderbilt.edu
Kristen Wright - kristen.v.wright@vanderbilt.edu
Homework #3
'''

from django.shortcuts import render
from .forms import ProfileForm
from django.views import generic
from .models import Profile
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """View function for home page of site."""
    context = {}

    return render(request, 'index.html', context)

@login_required
def admin_index(request):
    """View function for home page of site for Reshma."""
    context = {}

    return render(request, 'admin_index.html', context)

@login_required
class UnmatchedProfiles(generic.ListView):
    # context = {'unmatched_list': None, 'sec_list': None}
    # unmatched_profiles = Profile.objects.all().filter(matched=False)
    # context['unmatched_list'] = unmatched_profiles
    # context['first_profiles'] = unmatched_profiles[1::2]
    # context['second_profiles'] = unmatched_profiles[::2]
    # context['third_profiles'] = unmatched_profiles[::3]
    model = Profile
    context_object_name = 'umatched_list'
    template_name = 'profile_detailed_view.html'
    queryset = Profile.objects.filter(matched=False)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(UnmatchedProfiles, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['first_name'] = 'some data'
        return context

@login_required
def matched_profiles(request):
    context = {}
    return render(request, 'matched_profiles.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        # send email
        send_mail(
            'message from ' + message_name,  # subject
            message,  # message
            message_email,  # from email
            ['kristen.v.wright@vanderbilt.edu']  # To Email
        )
        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})

def CreateProfile(request):
    form = ProfileForm(request.POST or None)
    model = Profile
    context = {'form': form}   
    if request.method == 'POST':
        if form.is_valid:
            '''form.save()
            name = form.cleaned_data['first_name']
            print(name)
            form = ProfileForm(request.POST or None)
            '''
            #post = form.save(commit=False)
            ## KASTUR'S EDIT IS BELOW, USED https://www.youtube.com/watch?v=qwE9TFNub84
            post = form.save()
            post.user = request.user
            post.save 

            test = form.cleaned_data['first_name']
            form = ProfileForm(request.POST or None)
        else:
            form = ProfileForm(request.POST or None)
    
    return render(request, 'create_profile.html', context)

def ProfileDetailedView(request):
    model = Profile
    context = {'first_name': model.first_name,
               'last_name': model.last_name,
               'age': model.age,
               'gender': model.gender,
               'sexuality': model.sexuality,
               'country': model.country,
               'state_region': model.state_region,
               'city': model.city,
               'occupation': model.occupation,
               'company': model.company,
               'education': model.education,
               'bio': model.bio,
               'religion': model.religion,
               'hobbies': model.hobbies,
               'dietary_preferences': model.dietary_preferences,
               'alcohol': model.alcohol,
               'smoking': model.smoking}

    return render(request, 'profile_default_view.html', context)

'''
def ProfileDetailedView(request):
    model = Profile
    context = {'first_name': 'Guy',
               'last_name': 'Fieri',
               'age': 53,
               'gender': 'Male',
               'country': 'United States',
               'state_region': 'New York',
               'city': 'Flavortown',
               'occupation': 'Chef',
               'company': 'Guy Fieri Company',
               'education': 'Flavortown U',
               'bio': "I'm the host of Diners, Drive-Ins, and Dives. I love what I do because I get to eat tons of good food. Let me take you to Flavortown on our first date.",
               'religion': "Frosted Tips",
               'hobbies': "Cooking, Eating, Driving",
               'dietary_preferences': "Whatever you can cook, I can eat. Except eggs.",
               'alcohol': True,
               'smoking': False}
    
    return render(request, 'profile_default_view.html', context)
'''