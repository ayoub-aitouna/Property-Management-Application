from django.test import TestCase
from rest_framework.test import APIClient
from properties.models import Properties
from users.models import Tenant
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone


class UsersBaseTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.User = get_user_model().objects.create_user(
            username='User', password='password', first_name='User', last_name='One')
