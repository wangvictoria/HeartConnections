from django.urls import path
from . import views
from .views import CreateProfile

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/create/', views.CreateProfile, name='create_profile'),
    path('profile/view/', views.ProfileDetailedView, name='profile_detailed_view'),
    path('profile/saved/', views.saved, name='saved'),
    path('profile/recommended', views.recommended, name='recommended'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    #path('profile/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
    #path('profile/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
]