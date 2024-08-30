from rest_framework import serializers
from .models import Tenant
from django.contrib.auth.models import User


class TenantBaseValidator():
    def validate_contract_dates(self, data):
        contract_start_date = data.get('contract_start_date')
        contract_end_date = data.get('contract_end_date')

        if contract_end_date != None and contract_start_date != None and contract_end_date < contract_start_date:
            raise serializers.ValidationError({
                'contract_end_date': 'Contract end date must be greater than contract start date.'
            })

        return data


class TenantSerializer(serializers.ModelSerializer, TenantBaseValidator):
    url = serializers.HyperlinkedIdentityField(
        view_name='tenant-details', lookup_field='pk')
    name = serializers.ReadOnlyField(source='user.get_full_name')

    class Meta:
        model = Tenant
        fields = ['id', 'name', 'user', 'property', 'section_occupied', 'contract_start_date',
                  'contract_end_date', 'url']

    def validate(self, data):
        return self.validate_contract_dates(data)


class TenantDetailsSerializer(serializers.ModelSerializer, TenantBaseValidator):
    from properties.serializers import PropertySerializer

    name = serializers.ReadOnlyField(source='user.get_full_name')
    property = PropertySerializer(many=False, read_only=True)

    class Meta:
        model = Tenant
        fields = ['id', 'name', 'section_occupied', 'property', 'contract_start_date',
                  'contract_end_date']

    def validate(self, data):
        return self.validate_contract_dates(data)
