'''
Group #1 
Sovann Chang - sovann.d.chang@vanderbilt.edu
Kastur Koul - kastur.koul@vanderbilt.edu
Victoria Wang - victoria.m.wang@vanderbilt.edu
Kristen Wright - kristen.v.wright@vanderbilt.edu
Homework #3
'''

from django.shortcuts import render, redirect
from .forms import ProfileForm, MatchmakerForm, MatchActionForm
from django.views import generic
from .models import Profile
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Kastur's Edit for CSV Stuff -- referenced Youtube video (line 195 has the link)
import csv
from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

"""View function for home page of site."""
def index(request):

    context = {}

    return render(request, 'index.html', context)


"""View function for home page of site for Reshma."""
@login_required
def admin_index(request):

    context = {}

    return render(request, 'admin_index.html', context)


"""View function for "about Reshma" page"""
def about(request):

    context = {}
    return render(request, 'about.html', context)


"""View function for contact page"""
def contact(request):

    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        # send email
        send_mail(
             'Message From: ' + message_name + ' Email: ' + message_email,  # subject
            message,  # message
            message_email,  # from email
            ['reshmaharithsa@gmail.com']  # To Email
        )
        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})

def delete_profile(request, pk):
    #From Stackoverflow
    Profile.objects.filter(id=pk).delete()
    return render(request, 'admin_index.html', {})

"""View function for profile creation page"""
def CreateProfile(request):

    form = ProfileForm(request.POST, request.FILES or None)
    model = Profile
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            '''form.save()
            name = form.cleaned_data['first_name']
            print(name)
            form = ProfileForm(request.POST or None)
            '''
            #post = form.save(commit=False)
            ## KASTUR'S EDIT IS BELOW, USED https://www.youtube.com/watch?v=qwE9TFNub84
            form.save()
            # post.user = request.user
            # post.save

            #test = form.cleaned_data['first_name']
            return redirect('create_profile_success')
        else:
            form = ProfileForm(request.POST or None)
    
    return render(request, 'create_profile.html', context)


"""View function for page shown upon successful profile creation"""
def create_profile_success(request):
    
    context = {}
    return render(request, 'create_profile_success.html', context)


"""View for matching one profile with another"""
def match_action(request):

    model = Profile
    form = MatchActionForm(request.POST or None)
    context = {'available_list': None}
    available_list = Profile.objects.all().filter(matched=False)
    context['available_list'] = available_list
    if request.method == 'POST':
        if form.is_valid():
            profile_instance = Profile.objects.get()
            profile_instance.matched_with = form.cleaned_data.get('matched_with')
            return redirect('match_action_success')
        else:
            form = MatchActionForm(request.POST or None)

    return render(request, 'match_action.html', context)


"""View class for page containing unmatched profiles"""
class UnmatchedProfiles(LoginRequiredMixin, generic.ListView):

    model = Profile
    context_object_name = 'unmatched_list'
    queryset = Profile.objects.filter(matched=False)
    template_name = 'unmatched_profiles.html'


"""View class for page containing matched profiles"""
class MatchedProfiles(LoginRequiredMixin, generic.ListView):

    model = Profile
    context_object_name = 'matched_list'
    queryset = Profile.objects.filter(matched=True)
    template_name = 'matched_profiles.html'


"""View class for page with all details of a profile"""
class ProfileDetailedView(generic.edit.FormMixin, generic.DetailView):

    model = Profile
    form_class = MatchmakerForm
    success_url = '../unmatched'
    template_name = 'profile_detailed_view.html'

    def get_success_url(self):
        if 'delete' in self.request.POST:
                
            id = self.object.id
            Profile.objects.filter(id=id).delete()
            return reverse('admin_index')
        else:
            return reverse('profile_detailed_view', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailedView, self).get_context_data(**kwargs)
        # context['form'] = MatchmakerForm(initial={'notes': self.object})
        context['unmatched_list'] = Profile.objects.filter(matched=False)
        context['available_list'] = Profile.objects.filter(matched=False).exclude(id=self.object.id)
        context['form'] = self.get_form()
        if self.object.matched:
            match_list = self.object.matched_with.strip().split(" ")
            context['match_list'] = Profile.objects.filter(id__in=match_list)
            # q = Profile()
            # for match in matched_with_list:
            #     q = q | Profile(id=match)
            # Profile.objects.filter(q)
                # context['matched_with_id'] += i + ","
                # context['matched_with_first'] += Profile.objects.filter(id=i)[0].first_name
                # context['matched_with_last'] += Profile.objects.filter(id=i)[0].last_name
                # context['matched_with_notes'] += Profile.objects.filter(id=i)[0].notes
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object.notes = form.cleaned_data.get('notes')
        if form.cleaned_data.get('matched_with') != "none":
            match_profile = Profile.objects.filter(id=form.cleaned_data.get('matched_with'))[0]

            # If there was a previous person matched with, remove the match

            if self.object.matched:
                previous_match = Profile.objects.filter(id=int(self.object.matched_with))[0]
                previous_match.matched_with = ""
                previous_match.matched = False
                previous_match.save()

            # Match the two profiles
            self.object.matched_with = ""
            match_profile.matched_with = ""
            self.object.matched_with += str(match_profile.id) + " "
            match_profile.matched_with += str(self.object.id) + " "
            self.object.matched = True
            match_profile.matched = True
            match_profile.save()
        # self.object.matched_with = f'{match_profile.first_name} {match_profile.last_name}'
        #match_profile.matched_with = f'{self.object.first_name} {self.object.last_name}'
        #self.object.matched = True
        #match_profile.matched = True
        self.object.save()
        if 'delete' in self.request.POST:
            # If there was a previous person matched with, remove the match
            if self.object.matched:
                previous_match = Profile.objects.filter(id=int(self.object.matched_with))[0]
                previous_match.matched_with = ""
                previous_match.matched = False
                previous_match.save()
                
            self.object.delete()
        if 'unmatch' in self.request.POST:
            match_profile = Profile.objects.filter(id=form.cleaned_data.get('matched_with'))[0]
            # CANNOT INITIALIZE HERE
            self.object.matched_with = ""
            match_profile.matched_with = ""
            self.object.matched = False
            match_profile.matched = False
            match_profile.save()
            self.object.save()
        return super(ProfileDetailedView, self).form_valid(form)



# Kastur's CSV stuff 
#   USING THIS: https://www.youtube.com/watch?v=lE8SXffJUmI
"""View for page containing export functionality"""
def export(request):

    response = HttpResponse(content_type = 'text/csv')
    #   Response has a write method, so we can use the csv writer 
    #   write the csv data directly into the response 

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Birthdate', 
                    'Gender', 'Sexuality', 'Country', 'State/Region',
                    'City', 'Occupation', 'Company', 'Education', 'Bio', 
                    'Religion', 'Hobbies', 'Diet', 'Alcohol', 'Smoking', 
                    'Email', 'Matched', 'Matched With','Notes'])
    
    for profile in Profile.objects.all().values_list('id', 'first_name', 'last_name', 'birthdate',
                                                    'gender','sexuality','country','state_region','city',
                                                    'occupation','company','education','bio','religion',
                                                    'hobbies','dietary_preferences','alcohol','smoking',
                                                    'email','matched','matched_with','notes'):
        writer.writerow(profile)
    
    response['Content-Dispotition'] = 'attachment; filename="profiles.csv"'

    return response


"""View for admin logout page"""
def logout(request):

    context = {}
    return render(request, 'registration/logout.html', context)