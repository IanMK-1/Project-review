from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project, Profile, Rating


# Create your tests here.
class ProfileClassTest(TestCase):

    def setUp(self) -> None:
        # creating a new user and saving it
        self.new_user = User(password='weareone', username='ian', first_name='ian', last_name='mark',
                             email='imk@gmail.com')
        self.new_user.save()

        # creating a new profile and saving it
        self.new_profile = Profile(profile_pic='imk.jpg', bio='hello', phone_no='0711223344', user=self.new_user)
        self.new_profile.save()

    def tearDown(self) -> None:
        User.objects.all().delete()
        Profile.objects.all().delete()
