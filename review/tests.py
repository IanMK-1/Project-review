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

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))
        self.assertTrue(isinstance(self.new_user, User))

    def test_save_profile_method(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_update_bio(self):
        self.new_profile.save_profile()
        updated_profile = Profile.update_bio(self.new_user, 'bye')
        self.assertEqual(updated_profile.bio, 'bye')

    def test_update_phone_no(self):
        self.new_profile.save_profile()
        updated_profile = Profile.update_phone_no(self.new_user, '0777889944')
        self.assertEqual(updated_profile.phone_no, '0777889944')

    def test_update_profile_pic(self):
        self.new_profile.save_profile()
        updated_profile = Profile.update_profile_pic(self.new_user, 'gp.jpg')
        self.assertTrue(updated_profile.profile_pic != self.new_profile.profile_pic)


class ProjectClassTest(TestCase):

    def setUp(self) -> None:
        # creating a new user and saving it
        self.new_user = User(password='weareone', username='ian', first_name='ian', last_name='mark',
                             email='imk@gmail.com')
        self.new_user.save()

        # creating a new profile and saving it
        self.new_profile = Profile(profile_pic='imk.jpg', bio='hello', phone_no='0711223344', user=self.new_user)
        self.new_profile.save()

        # creating a new project and saving it
        self.new_project = Project(title='instagram', image='insta.jpg', description='instagram app',
                                   live_link='instagram.com',
                                   user_project=self.new_user, user_profile=self.new_profile)
        self.new_project.save()

    def tearDown(self) -> None:
        User.objects.all().delete()
        Profile.objects.all().delete()
        Project.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))
        self.assertTrue(isinstance(self.new_user, User))
        self.assertTrue(isinstance(self.new_project, Project))

    def test_save_project(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_project(self):
        self.new_project.save_project()
        self.new_project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)

    def test_update_project_title(self):
        self.new_project.save_project()
        updated_project = Project.update_project_title(self.new_project.id, 'the instagram')
        self.assertEqual(updated_project.title, 'the instagram')

    def test_update_project_description(self):
        self.new_project.save_project()
        updated_project = Project.update_project_description(self.new_project.id, 'the instagram app')
        self.assertEqual(updated_project.description, 'the instagram app')

    def test_update_project_live_link(self):
        self.new_project.save_project()
        updated_project = Project.update_project_live_link(self.new_project.id, 'www.instagram.io')
        self.assertEqual(updated_project.live_link, 'www.instagram.io')

    def test_update_project_image(self):
        self.new_project.save_project()
        updated_project = Project.update_project_image(self.new_project.id, 'instagram.jpg')
        self.assertTrue(updated_project.image != self.new_project.image)


class RatingTestClass(TestCase):
    def setUp(self) -> None:
        # creating a new user and saving it
        self.new_user = User(password='weareone', username='ian', first_name='ian', last_name='mark',
                             email='imk@gmail.com')
        self.new_user.save()

        # creating a new profile and saving it
        self.new_profile = Profile(profile_pic='imk.jpg', bio='hello', phone_no='0711223344', user=self.new_user)
        self.new_profile.save()

        # creating a new project and saving it
        self.new_project = Project(title='instagram', image='insta.jpg', description='instagram app',
                                   live_link='instagram.com',
                                   user_project=self.new_user, user_profile=self.new_profile)
        self.new_project.save()

        # creating a new rating for project and saving it
        self.new_rating = Rating(design=1, usability=6, content=8, project=self.new_project, user_rating=self.new_user)
        self.new_rating.save()

    def tearDown(self) -> None:
        User.objects.all().delete()
        Profile.objects.all().delete()
        Project.objects.all().delete()
        Rating.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))
        self.assertTrue(isinstance(self.new_user, User))
        self.assertTrue(isinstance(self.new_project, Project))
        self.assertTrue(isinstance(self.new_rating, Rating))

    def test_save_rating(self):
        self.new_rating.save_rating()
        ratings = Rating.objects.all()
        self.assertTrue(len(ratings) > 0)

    def test_delete_rating(self):
        self.new_rating.save_rating()
        self.new_rating.delete_rating()
        ratings = Rating.objects.all()
        self.assertTrue(len(ratings) == 0)

    def test_update_design_rating(self):
        self.new_rating.save_rating()
        updated_rating = Rating.update_design_rating(self.new_project, 5)
        self.assertEqual(updated_rating.design, 5)

    def test_update_usability_rating(self):
        self.new_rating.save_rating()
        updated_rating = Rating.update_usability_rating(self.new_project, 9)
        self.assertEqual(updated_rating.usability, 9)

    def test_update_content_rating(self):
        self.new_rating.save_rating()
        updated_rating = Rating.update_content_rating(self.new_project, 2)
        self.assertEqual(updated_rating.content, 2)
