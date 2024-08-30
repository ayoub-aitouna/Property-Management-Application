from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tenant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(
        'properties.Properties', on_delete=models.CASCADE, related_name='tenants')
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()
    section_occupied = models.CharField(max_length=100)
    last_payment_date = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs) -> None:
        if self.contract_start_date > self.contract_end_date:
            raise ValueError(
                'Contract start date cannot be greater than contract end date')
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.user.username
