from .models import Profile, Project, Rating
from django import forms


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio', 'phone_no']