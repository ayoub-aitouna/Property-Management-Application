from .test_setup import UsersBaseTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone


class UsersTestCase(UsersBaseTestCase):
    def test_list(self):
        res = self.client.get(reverse('tenant_list'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data.get('results')), 1)

    def test_create(self):
        thirdUser = get_user_model().objects.create_user(
            username='thirdUser', password='password', first_name='User', last_name='Three')
        res = self.client.post(reverse('tenant_list'), {
            'user': thirdUser.id,
            'property': self.property.id,
            'contract_start_date': timezone.now().date(),
            'contract_end_date': timezone.now().date() + timezone.timedelta(days=365),
            'section_occupied': 'B',
        })
        print(f'Create Response: {res.data}, {res.status_code}')
        self.assertEqual(res.status_code, 201)

    def test_retrieve(self):
        res = self.client.get(reverse('tenant-details', args=[self.tenant.id]))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data.get('section_occupied'), 'A')

    def test_update(self):
        # test Authorized Update
        res = self.client.patch(reverse('tenant-details', args=[self.tenant.id]), {
            'section_occupied': 'B',
        })
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data.get('section_occupied'), 'B')

        # test Unauthorized Update
        self.AuthenticatedClient(self.secondUser)
        res = self.client.patch(reverse('tenant-details', args=[self.tenant.id]), {
            'section_occupied': 'C',
        })
        self.assertEqual(res.status_code, 403)

    def test_delete(self):
        # test Authorized Delete
        res = self.client.delete(
            reverse('tenant-details', args=[self.tenant.id]))
        self.assertEqual(res.status_code, 204)

    def test_unauthorized_delete(self):
        # test Unauthorized Delete
        self.AuthenticatedClient(self.secondUser)
        res = self.client.delete(
            reverse('tenant-details', args=[self.tenant.id]))
        self.assertEqual(res.status_code, 403)
