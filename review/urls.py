from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('home/', views.home, name='Home'),
    path('profile/', views.profile, name='Profile'),
    path('edit_profile/', views.edit_profile, name='Editprofile'),
]
