from .test_setup import UsersBaseTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone


class UsersTestCase(UsersBaseTestCase):
    def test_token(self):
        res = self.client.post(reverse('token_obtain_pair'), {
                               'username': 'User', 'password': 'password'})
        self.assertEqual(res.status_code, 200)
        self.assertTrue('access' in res.data)
        self.assertTrue('refresh' in res.data)

    def test_refresh_token(self):
        res = self.client.post(reverse('token_obtain_pair'), {
                               'username': 'User', 'password': 'password'})
        self.assertEqual(res.status_code, 200)
        refresh = res.data['refresh']

        res = self.client.post(reverse('token_refresh'), {'refresh': refresh})
        self.assertEqual(res.status_code, 200)
        self.assertTrue('access' in res.data)

    def test_register(self):
        res = self.client.post(reverse('register'), {
                               'username': 'User2', 'password': 'password', 'first_name': 'User', 'last_name': 'Two'})
        self.assertEqual(res.status_code, 201)
        self.assertEqual(get_user_model().objects.count(), 2)