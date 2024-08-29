from rest_framework import serializers
from .models import Tenant
from django.contrib.auth.models import User


class TenantSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='tenant-details', lookup_field='pk')
    name = serializers.ReadOnlyField(source='user.get_full_name')

    class Meta:
        model = Tenant
        fields = ['id', 'name', 'section_occupied', 'contract_start_date',
                  'contract_end_date', 'url']


class TenantDetailsSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='user.get_full_name')
    property = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Tenant
        fields = ['id', 'name', 'section_occupied', 'property', 'contract_start_date',
                  'contract_end_date']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'password', 'first_name', 'last_name']
