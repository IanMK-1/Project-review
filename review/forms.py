from .models import Profile, Project, Rating
from django import forms


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio', 'phone_no']


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image', 'description', 'live_link']


class RateProjectForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content', 'project']
