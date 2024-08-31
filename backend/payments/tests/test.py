from .test_setup import UsersBaseTestCase
from django.urls import reverse
from unittest.mock import patch, MagicMock, ANY
from django.conf import settings
from payments.services import run_payment_notification
from users.models import Tenant
from django.utils import timezone
from apscheduler.triggers.cron import CronTrigger
from payments.scheduler import startScheduler


class UsersTestCase(UsersBaseTestCase):
    def test_list(self):
        res = self.client.get(reverse('payment_list'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data.get('results')), 1)

    def test_create(self):
        res = self.client.post(reverse('payment_list'), {
            'tenant': self.tenant.id,
            'property': self.property.id,
            'amount': 1000,
            'settled': False,
        })
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data.get('amount'), '1000.00')

    def test_retrieve(self):
        res = self.client.get(
            reverse('payment-details', args=[self.payment.id]))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data.get('settled'), False)

    def test_update(self):
        # test Authorized Update
        res = self.client.patch(reverse('payment-details', args=[self.payment.id]), {
            'settled': True,
        })
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data.get('settled'), True)

        # test Unauthorized Update
        self.AuthenticatedClient(self.secondUser)

        res = self.client.patch(reverse('payment-details', args=[self.payment.id]), {
            'settled': False,
        })
        self.assertEqual(res.status_code, 403)

    def test_delete(self):
        # test Authorized Delete
        res = self.client.delete(
            reverse('payment-details', args=[self.payment.id]))
        self.assertEqual(res.status_code, 204)

    def test_unauthorized_delete(self):
        # test Unauthorized Delete
        self.AuthenticatedClient(self.secondUser)
        res = self.client.delete(
            reverse('payment-details', args=[self.payment.id]))
        self.assertEqual(res.status_code, 403)

    @patch('payments.scheduler.BackgroundScheduler')
    @patch('payments.scheduler.DjangoJobStore')
    @patch('payments.scheduler.register_events')
    def test_start_schedular(self,  mock_register_events, mock_DjangoJobStore, mock_BackgroundScheduler):
        with patch.object(settings, 'TESTING', False):
            mock_schedular_instance = MagicMock()
            mock_BackgroundScheduler.return_value = mock_schedular_instance
            startScheduler()
            mock_BackgroundScheduler.assert_called_once()
            mock_schedular_instance.add_jobstore.assert_called_once_with(
                mock_DjangoJobStore(), 'default')

            mock_schedular_instance.add_job.assert_called_once_with(
                run_payment_notification,
                trigger=ANY,
                id='due_payment_notification',
                max_instances=1,
                replace_existing=True
            )

            mock_register_events.assert_called_once_with(
                mock_schedular_instance)
            mock_schedular_instance.start.assert_called_once()

    @patch('payments.services.send_mail')
    def test_run_payment_notification(self, mock_send_mail):
        Tenant.objects.create(
            user=self.firstUser,
            property=self.property,
            section_occupied='A',
            contract_start_date=timezone.now(),
            contract_end_date=timezone.now() + timezone.timedelta(days=365),
            last_payment_date=timezone.now() - timezone.timedelta(days=31)
        )
        run_payment_notification()
        mock_send_mail.assert_called_once()
