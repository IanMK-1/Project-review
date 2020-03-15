from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    bio = serializers.CharField(max_length=500)
    phone_no = serializers.CharField(max_length=20)
    profile_pic = serializers.ImageField()


class ProjectSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=500)
    live_link = serializers.CharField(max_length=20)
    image = serializers.ImageField()
    posted_on = serializers.DateTimeField()
    user_project_username = serializers.ReadOnlyField(source='user_project.username')
    user_project_email = serializers.ReadOnlyField(source='user_project.email')
