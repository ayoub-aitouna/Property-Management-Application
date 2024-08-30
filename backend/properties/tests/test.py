from .test_setup import PropertiesBaseTestCase
from django.urls import reverse
from properties.models import Properties


class PropertiesTestCase(PropertiesBaseTestCase):
    def test_list(self):
        res = self.client.get(reverse('property_list'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data.get('results')), 2)

    def test_create(self):
        res = self.client.post(reverse('property_list'), {
            'name': 'Property 3',
            'address': '789 Oak St',
            'apartment_type': 'house',
            'number_of_units': 30,
            'rental_cost': 3000,
        })
        self.assertEqual(res.status_code, 201)
        self.assertEqual(Properties.objects.count(), 3)

    def test_retrieve(self):
        res = self.client.get(
            reverse('property-details', args=[self.firstProperty.id]))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data.get('name'), 'Property 1')

    def test_update(self):
        # test Authorized Update
        res = self.client.patch(
            reverse('property-details', args=[self.firstProperty.id]), {
                'name': 'Property 1 Updated',
            })
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Properties.objects.get(
            id=self.firstProperty.id).name, 'Property 1 Updated')

        # test Unauthorized Update
        self.AuthenticatedClient(self.secondUser)
        res = self.client.patch(
            reverse('property-details', args=[self.firstProperty.id]), {
                'name': 'Property 1 Updated Again',
            })
        self.assertEqual(res.status_code, 403)

    def test_delete(self):
        # test Authorized Delete
        res = self.client.delete(
            reverse('property-details', args=[self.firstProperty.id]))
        self.assertEqual(res.status_code, 204)
        self.assertEqual(Properties.objects.count(), 1)

    def test_unauthorized_delete(self):
        # test Unauthorized Delete
        self.AuthenticatedClient(self.secondUser)
        res = self.client.delete(
            reverse('property-details', args=[self.firstProperty.id]))
        self.assertEqual(res.status_code, 403)
        self.assertEqual(Properties.objects.count(), 2)
    
    def test_filters(self):
        res = self.client.get(reverse('property_list'), {
            'location': 'Main',
            'rental_min_cost': 1000,
            'rental_max_cost': 2000,
            'apartment_type': 'house',
            'sort_by': 'name'
        })
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data.get('results')), 1)
        self.assertEqual(res.data.get('results')[0].get('name'), 'Property 1')
        