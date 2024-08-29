from rest_framework import serializers
from .models import Properties
from users.serializers import TenantSerializer, UserSerializer


class PropertySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='property-details', lookup_field='pk')

    class Meta:
        model = Properties
        fields = ['id', 'name', 'address', 'apartment_type',
                  'number_of_units', 'rental_cost', 'url']

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['manager'] = user
        return super().create(validated_data)


class PropertyDetailsSerializer(serializers.ModelSerializer):
    tenants = TenantSerializer(many=True, read_only=True)
    manager = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Properties
        fields = ['id', 'name', 'address', 'apartment_type',
                  'number_of_units', 'rental_cost', 'manager', 'tenants']

