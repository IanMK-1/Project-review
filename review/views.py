from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, Project, Rating


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    all_projects = Project.objects.all()
    return render(request, 'home.html', {"all_projects": all_projects})
