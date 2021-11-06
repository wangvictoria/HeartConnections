'''
Group #1 
Sovann Chang - sovann.d.chang@vanderbilt.edu
Kastur Koul - kastur.koul@vanderbilt.edu
Victoria Wang - victoria.m.wang@vanderbilt.edu
Kristen Wright - kristen.v.wright@vanderbilt.edu
Homework #3
'''

from django.urls import path, include
from . import views
#from .views import UnmatchedProfiles

urlpatterns = [
    path('', views.index, name='index'),
    path('matchmaker/', views.admin_index, name='admin_index'),
    path('profile/create/', views.CreateProfile, name='create_profile'),
    path('profile/<int:pk>', views.ProfileDetailedView.as_view(), name='profile_detailed_view'),
    path('profile/unmatched/', views.UnmatchedProfiles.as_view(), name='unmatched_profiles'),
    # path('profile/unmatched_profiles/', views.unmatched_profiles, name='unmatched_profiles'),
    path('profile/matched/', views.MatchedProfiles.as_view(), name='matched_profiles'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    #path('profile/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
    #path('profile/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
]

#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]