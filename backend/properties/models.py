from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Properties(models.Model):
    APARTMENT_CHOICES = [
        ('apartment', 'Apartment'),
        ('house', 'House')]
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    apartment_type = models.CharField(
        max_length=100, choices=APARTMENT_CHOICES)
    number_of_units = models.IntegerField()
    rental_cost = models.DecimalField(max_digits=12, decimal_places=2)
    manager = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='manager')

    def __str__(self) -> str:
        return self.name
