from rest_framework import serializers
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class ProfileSerializer(serializers.Serializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    bio = serializers.CharField(max_length=500)
    phone_no = serializers.CharField(max_length=20)
    profile_pic = CloudinaryField('image')


class ProjectSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=500)
    live_link = serializers.CharField(max_length=20)
    posted_on = serializers.DateTimeField()
    user_project_username = serializers.ReadOnlyField(source='user_project.username')
    user_project_email = serializers.ReadOnlyField(source='user_project.email')