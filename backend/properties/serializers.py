from rest_framework import serializers
from .models import Properties
from users.serializers import TenantSerializer
from authentication.serializers import UserSerializer


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


class PropertyFilterSerializer(serializers.Serializer):
    location = serializers.CharField(
        required=False, help_text='Filter by location substring.')
    rental_min_cost = serializers.DecimalField(
        max_digits=10, decimal_places=2, required=False, help_text='Filter by minimum rental cost.')
    rental_max_cost = serializers.DecimalField(
        max_digits=10, decimal_places=2, required=False, help_text='Filter by maximum rental cost.')
    apartment_type = serializers.CharField(
        required=False, help_text='Filter by apartment type.')
    sort_by = serializers.ChoiceField(choices=['name', 'address', 'apartment_type',
                                      'number_of_units', 'rental_cost'], required=False, help_text='Sort by field.')
