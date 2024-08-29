from rest_framework import serializers
from .models import Payment
from django.contrib.auth.models import User
from properties.serializers import PropertySerializer
from users.serializers import TenantSerializer


class PaymentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='payment-details', lookup_field='pk')

    class Meta:
        model = Payment
        fields = ['id', 'tenant', 'property', 'payment_date',
                  'settled', 'amount', 'url']


class PaymentDetailsSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(many=False, read_only=True)
    property = PropertySerializer(many=False, read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'
