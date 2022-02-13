from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

from user.models import Profile

class FollowTestCase(TestCase):
    def setUp(self):
        self.web_client = Client()

        """ Datos """

        self.user_x = User.objects.create(username = "user_x")
        self.user_y = User.objects.create(username = "user_y")

        self.user_x.save()
        self.user_y.save()

        self.user_x.profile = Profile.objects.create(user = self.user_x)
        self.user_y.profile = Profile.objects.create(user = self.user_y)

        """ Estado inicial """

        self.web_client.force_login(user = self.user_x)

    def test_follow(self):
        self.web_client.get(f"/user/seguir/{self.user_y.id}")
        assert self.user_y.profile in self.user_x.profile.following.all()

    def test_self_follow(self):
        self.web_client.get(f"/user/seguir/{self.user_x.id}")
        assert self.user_x.profile not in self.user_x.profile.following.all()


class GetFollowersTestCase(TestCase):
    def setUp(self):
        self.web_client = Client()

        """ Datos de prueba """
        self.user_x = User.objects.create(username = "user_x")
        self.seguidor1 = User.objects.create(username = "seguidor1")
        self.seguidor2 = User.objects.create(username = "seguidor2")

        self.user_x.save()
        self.seguidor1.save()
        self.seguidor2.save()

        self.user_x.profile = Profile.objects.create(user = self.user_x)
        self.seguidor1.profile = Profile.objects.create(user = self.seguidor1)
        self.seguidor2.profile = Profile.objects.create(user = self.seguidor2)

        """ Estado inicial """

        self.seguidor1.profile.following.add(self.user_x.profile)
        self.seguidor2.profile.following.add(self.user_x.profile)

        self.web_client.force_login(user = self.user_x)

    def test_consultar_seguidores(self):
        response = self.web_client.get(f"/user/seguidores/{self.user_x.id}")
        assert self.seguidor1.username in response.content.decode("UTF-8")
        assert self.seguidor2.username in response.content.decode("UTF-8")
