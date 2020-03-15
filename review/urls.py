from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('home/', views.home, name='Home'),
    path('profile/', views.profile, name='Profile'),
    path('edit_profile/', views.edit_profile, name='Editprofile'),
    path('add_project/', views.add_project, name="Addproject"),
    re_path('project/(\d+)/', views.project_details, name="Project"),
    path('rate_project/', views.rate_project, name="Rateproject"),
    path('search_results/', views.search_project, name="Searchproject"),
    path('api/profiles/', views.ProfileView.as_view()),
    path('api/projects/', views.ProjectView.as_view()),
]
