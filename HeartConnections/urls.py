'''
Group #1 
Sovann Chang - sovann.d.chang@vanderbilt.edu
Kastur Koul - kastur.koul@vanderbilt.edu
Victoria Wang - victoria.m.wang@vanderbilt.edu
Kristen Wright - kristen.v.wright@vanderbilt.edu
Homework #3
'''

from django.urls import path, include, re_path
from . import views
#from .views import UnmatchedProfiles

"""The urls used in the website, their aliases, and which view they point to"""
urlpatterns = [
    path('', views.index, name='index'),
    path('matchmaker/', views.admin_index, name='admin_index'),
    path('profile/create/', views.CreateProfile, name='create_profile'),
    path('profile/create/success/', views.create_profile_success, name='create_profile_success'),
    path('profile/<int:pk>/', views.ProfileDetailedView.as_view(), name='profile_detailed_view'),
    path('profile/unmatched/', views.UnmatchedProfiles.as_view(), name='unmatched_profiles'),
    path('profile/matched/', views.MatchedProfiles.as_view(), name='matched_profiles'),
    path('profile/match_action/', views.match_action, name='match_action'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('export/', views.export, name='export'),
    path('logout/', views.logout, name='override_logout')
]


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]