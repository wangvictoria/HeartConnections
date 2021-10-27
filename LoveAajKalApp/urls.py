from django.urls import path
from . import views
from .views import ProfileCreateView, ProfileUpdateView, ProfileDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/add/', ProfileCreateView.as_view(), name='profile-add'),
    path('profile/<int:pk>/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile-delete'),
]