from django.db import models
from users.models import Tenant
import datetime


class Payment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    payment_date = models.DateField(default=datetime.date.today)
    settled = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    property = models.ForeignKey(
        'properties.Properties', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.tenant.user.username} Deposit {str(self.amount)} on {str(self.payment_date)}.'
