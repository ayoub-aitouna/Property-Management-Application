from django.test import TestCase
from rest_framework.test import APIClient
from properties.models import Properties
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class PropertiesBaseTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.firstUser = get_user_model().objects.create_user(
            username='firstUser', password='password', first_name='User', last_name='One')
        self.secondUser = get_user_model().objects.create_user(
            username='secondUser', password='password', first_name='User', last_name='Two')
        self.AuthenticatedClient(self.firstUser)
        self.firstProperty = Properties.objects.create(
            name='Property 1',
            address='123 Main St',
            apartment_type='house',
            number_of_units=10,
            rental_cost=1000,
            manager=self.firstUser)

        self.secondProperty = Properties.objects.create(
            name='Property 2',
            address='456 Elm St',
            apartment_type='apartment',
            number_of_units=20,
            rental_cost=2000,
            manager=self.secondUser)

    def AuthenticatedClient(self, user):
        refresh = RefreshToken.for_user(user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')
