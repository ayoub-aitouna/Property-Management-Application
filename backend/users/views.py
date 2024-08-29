from rest_framework import generics
from .models import Tenant
from .serializers import TenantSerializer, TenantDetailsSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManager


class TenantList(generics.ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticated]


class TenantDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantDetailsSerializer
    permission_classes = [IsAuthenticated, IsManager]

