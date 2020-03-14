from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, Project, Rating
from .forms import EditProfileForm
import cloudinary.uploader


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    all_projects = Project.objects.all()
    return render(request, 'home.html', {"all_projects": all_projects})


@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile_pic = form.cleaned_data['profile_pic']
            bio = form.cleaned_data['bio']
            phone_no = form.cleaned_data['phone_no']
            Profile.update_phone_no(current_user, phone_no)
            Profile.update_bio(current_user, bio)
            user_profile = Profile.objects.get(user=current_user)
            user_profile.profile_pic = cloudinary.uploader.upload(profile_pic)['public_id']
            user_profile.save()

            return redirect("Profile")
    else:
        form = EditProfileForm()

    return render(request, 'edit_profile.html', {"form": form})