from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    profile_pic = CloudinaryField('image', blank=True)
    bio = models.TextField(blank=True)
    phone_no = models.CharField(max_length=20, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_bio(cls, id, new_bio):
        cls.objects.filter(id=id).update(bio=new_bio)
        updated_bio = cls.objects.get(id=id)
        return updated_bio

class Project(models.Model):
    title = models.CharField(max_length=30)
    image = CloudinaryField('image')
    description = models.TextField()
    live_link = models.CharField(max_length=50)
    user_project = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Rating(models.Model):
    design = models.PositiveIntegerField(max_length=10)
    usability = models.PositiveIntegerField(max_length=10)
    content = models.PositiveIntegerField(max_length=10)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_rating = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.design
