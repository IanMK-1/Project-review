from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, Project, Rating
from .forms import EditProfileForm, AddProjectForm, RateProjectForm
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


@login_required(login_url='/accounts/login/')
def add_project(request):
    current_user = request.user
    if request.method == "POST":
        form = AddProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            live_link = form.cleaned_data['live_link']
            user_profile = Profile.objects.get(user=current_user)
            project = Project(title=title, image=image, description=description, live_link=live_link,
                              user_project=current_user,
                              user_profile=user_profile)
            project.save_project()

            return redirect('Profile')
    else:
        form = AddProjectForm()

    return render(request, 'add_project.html', {"form": form})


@login_required(login_url='/accounts/login/')
def project_details(request, id):
    project = Project.objects.get(id=id)
    ratings = Rating.objects.filter(project=project).all()
    count = ratings.count()
    overall_average = 0
    user_avg = {}
    if ratings:
        average = 0
        for rating in ratings:
            average += (rating.design + rating.usability + rating.content) / 3
            user_avg[rating.id] = round(average, 2)

        overall_average = average / count

    value = round(overall_average, 2)
    return render(request, 'project.html', {"project": project, "ratings": ratings, "overall_avg": value,
                                            "user_avg": user_avg})


@login_required(login_url='/accounts/login/')
def rate_project(request):
    current_user = request.user
    if request.method == "POST":
        form = RateProjectForm(request.POST, request.FILES)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            project = form.cleaned_data['project']
            user_rating = Rating(design=design, usability=usability, content=content, project=project,
                                 user_rating=current_user)
            user_rating.save()

            return redirect('Home')
    else:
        form = RateProjectForm()

    return render(request, 'rating.html', {"form": form})


def search_project(request):
    try:
        if 'search_project' in request.GET and request.GET["search_project"]:
            search_term = request.GET.get("search_project")
            searched_project = Project.objects.filter(title__icontains=search_term).all()

    except ObjectDoesNotExist:
        searched_project = None

    return render(request, 'search_results.html', {"projects": searched_project, "search_item": search_term})
