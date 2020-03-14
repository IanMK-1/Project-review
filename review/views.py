from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, Project, Rating


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    all_projects = Project.objects.all()
    return render(request, 'home.html', {"all_projects": all_projects})


def profile(request):
    current_user = request.user
    try:
        user_profile = Profile.objects.get(user=current_user)
        user_projects = Project.objects.filter(user_project=current_user)
    except ObjectDoesNotExist:
        user_profile = Profile(user=current_user)
        user_profile.save_profile()
        user_profile = Profile.objects.get(user=current_user)
        user_projects = Project.objects.filter(user_project=current_user)

    return render(request, 'profile.html', {"user_profile": user_profile, "user_projects": user_projects})


def edit_profile(request):
    return render(request, 'edit_profile.html')