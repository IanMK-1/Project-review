from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


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

    @classmethod
    def update_phone_no(cls, id, new_phone_no):
        cls.objects.filter(id=id).update(phone_no=new_phone_no)
        updated_phone_no = cls.objects.get(id=id)
        return updated_phone_no

    @classmethod
    def update_profile_pic(cls, id, new_profile_pic):
        cls.objects.filter(id=id).update(profile_pic=new_profile_pic)
        updated_profile_pic = cls.objects.get(id=id)
        return updated_profile_pic


class Project(models.Model):
    title = models.CharField(max_length=30)
    image = CloudinaryField('image')
    description = models.TextField()
    live_link = models.CharField(max_length=50)
    posted_on = models.DateTimeField(auto_now_add=True)
    user_project = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def update_project_title(cls, id, new_title):
        cls.objects.filter(id=id).update(title=new_title)
        updated_title = cls.objects.get(id=id)
        return updated_title

    @classmethod
    def update_project_description(cls, id, new_description):
        cls.objects.filter(id=id).update(description=new_description)
        updated_project_description = cls.objects.get(id=id)
        return updated_project_description

    @classmethod
    def update_project_image(cls, id, new_image):
        cls.objects.filter(id=id).update(image=new_image)
        updated_project_image = cls.objects.get(id=id)
        return updated_project_image

    @classmethod
    def update_project_live_link(cls, id, new_live_link):
        cls.objects.filter(id=id).update(live_link=new_live_link)
        updated_project_live_link = cls.objects.get(id=id)
        return updated_project_live_link


class Rating(models.Model):
    design = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    usability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    content = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_rating = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.design

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()

    @classmethod
    def update_design_rating(cls, id, new_design_rating):
        cls.objects.filter(id=id).update(design=new_design_rating)
        updated_design_rating = cls.objects.get(id=id)
        return updated_design_rating

    @classmethod
    def update_usability_rating(cls, id, new_usability_rating):
        cls.objects.filter(id=id).update(usability=new_usability_rating)
        updated_usability_rating = cls.objects.get(id=id)
        return updated_usability_rating

    @classmethod
    def update_content_rating(cls, id, new_content_rating):
        cls.objects.filter(id=id).update(content=new_content_rating)
        updated_content_rating = cls.objects.get(id=id)
        return updated_content_rating
