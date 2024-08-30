from rest_framework import generics
from .serializers import PropertySerializer, PropertyDetailsSerializer, PropertyFilterSerializer
from .models import Properties
from rest_framework.permissions import IsAuthenticated
from .permissions import IsPropertyManager
from django_filters import rest_framework as filters


class PropertyFilter(filters.FilterSet):
    location = filters.CharFilter(field_name='address', lookup_expr='icontains')
    rental_min_cost = filters.NumberFilter(field_name='rental_cost', lookup_expr='gte')
    rental_max_cost = filters.NumberFilter(field_name='rental_cost', lookup_expr='lte')
    apartment_type = filters.CharFilter(field_name='apartment_type')
    sort_by = filters.OrderingFilter(fields=['name', 'address', 'apartment_type', 'number_of_units', 'rental_cost'])

    class Meta:
        model = Properties
        fields = ['location', 'rental_min_cost', 'rental_max_cost', 'apartment_type', 'sort_by']


class PropertyList(generics.ListCreateAPIView):
    queryset = Properties.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PropertyFilter
    
    # def get_queryset(self):
    #     queryset = Properties.objects.all()

    #     try:
    #         filter_serializer = PropertyFilterSerializer(
    #             data=self.request.query_params)
    #         filter_serializer.is_valid(raise_exception=True)
    #         filters = filter_serializer.validated_data
            
    #         # Filters
    #         location = filters.get('location')
    #         rental_min_cost = filters.get('rental_min_cost')
    #         rental_max_cost = filters.get('rental_max_cost')
    #         apartment_type = filters.get('apartment_type')
    #         sort_by = filters.get('sort_by')
    #         # Apply Filters
    #         if location:
    #             queryset.filter(address__icontains=location)
    #         if rental_min_cost:
    #             queryset.filter(rental_cost__gte=rental_min_cost)
    #         if rental_max_cost:
    #             queryset.filter(rental_cost__lte=rental_min_cost)
    #         if apartment_type:
    #             queryset.filter(apartment_type=apartment_type)
    #         if sort_by:
    #             queryset.order_by(sort_by)
    #         return queryset
    #     except Exception as e:
    #         return []


class PropertyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Properties.objects.all()
    serializer_class = PropertyDetailsSerializer
    permission_classes = [IsAuthenticated, IsPropertyManager]
