from django.shortcuts import render
from .forms import ProfileForm
#from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from .models import Profile
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    """View function for home page of site."""
    context = {'name': None} # initialize context

    context['name'] = 'Victoria' # define name
    return render(request, 'index.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def CreateProfile(request):
    form = ProfileForm(request.POST or None)
    model = Profile
    context = {'form': form}   
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            name = form.cleaned_data['first_name']
            print(name)
        else:
            form = ProfileForm(request.POST or None)
    
    return render(request, 'create_profile.html', context)

'''
def ProfileDetailedView(request):
    model = Profile
    context = {'first_name': model.first_name,
               'last_name': model.last_name,
               'age': model.age,
               'gender': model.gender,
               'country': model.country,
               'state_region': model.state_region,
               'city': model.city,
               'occupation': model.occupation,
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
               'education': 'Flavortown U',
               'bio': "I'm the host of Diners, Drive-Ins, and Dives. I love what I do because I get to eat tons of good food. Let me take you to Flavortown on our first date.",
               'religion': "Frosted Tips",
               'hobbies': "Cooking, Eating, Driving",
               'dietary_preferences': "Whatever you can cook, I can eat. Except eggs.",
               'alcohol': True,
               'smoking': False}
    
    return render(request, 'profile_default_view.html', context)
