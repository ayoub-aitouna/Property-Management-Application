import logging
from django.core.mail import send_mail
from django.utils import timezone
from users.models import Tenant

logger = logging.getLogger(__name__)

def run_payment_notification():
    try:
        print('Running Payment Notification')
        last_month = timezone.now() - timezone.timedelta(days=30)
        due_payment_tenants = Tenant.objects.filter(
            last_payment_date__lte=last_month)
        for tenant in due_payment_tenants:
            print(f'Notifying {tenant.user.email} for due payment')
            send_mail(
                'Due Payment Notification',
                'This is a reminder that your payment is due',
                from_email='mock@mail.com',
                recipient_list=[tenant.user.email],
                fail_silently=True,
            )
        print('Payment Notification Completed')
    except Exception as e:
        logger.error(f'Error while Running Payment Notification: {e}')
