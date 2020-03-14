from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html')
