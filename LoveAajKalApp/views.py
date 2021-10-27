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

def ProfileDetailedView(request):
    context = {}#'profile-id': None}
    return render(request, 'profile_default_view.html', context)
