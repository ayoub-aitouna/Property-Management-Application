from django.test import TestCase
from rest_framework.test import APIClient
from properties.models import Properties
from users.models import Tenant
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from payments.models import Payment


class UsersBaseTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.firstUser = get_user_model().objects.create_user(
            username='firstUser', password='password', first_name='User', last_name='One')
        self.secondUser = get_user_model().objects.create_user(
            username='secondUser', password='password', first_name='User', last_name='Two')

        self.property = Properties.objects.create(
            name='Property 1',
            address='123 Main St',
            apartment_type='house',
            number_of_units=10,
            rental_cost=1000,
            manager=self.firstUser)

        self.tenant = Tenant.objects.create(
            user=self.secondUser,
            property=self.property,
            section_occupied='A',
            contract_start_date=timezone.now(),
            contract_end_date=timezone.now() + timezone.timedelta(days=365)
        )

        self.payment = Payment.objects.create(
            tenant=self.tenant,
            property=self.property,
            amount=1000,
            payment_date=timezone.now(),
            settled=False)

        self.AuthenticatedClient(self.firstUser)

    def AuthenticatedClient(self, user):
        refresh = RefreshToken.for_user(user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')
