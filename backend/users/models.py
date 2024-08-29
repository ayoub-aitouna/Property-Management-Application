from django.db import models
from django.contrib.auth.models import User


class Tenant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(
        'properties.Properties', on_delete=models.CASCADE, related_name='tenants')
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()
    section_occupied = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.username
