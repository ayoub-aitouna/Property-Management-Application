from rest_framework import generics
from .serializers import PropertySerializer, PropertyDetailsSerializer
from .models import Properties
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .permissions import IsPropertyManager
# Create your views here.


class PropertyList(generics.ListCreateAPIView):
    queryset = Properties.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]

class PropertyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Properties.objects.all()
    serializer_class = PropertyDetailsSerializer
    permission_classes = [IsAuthenticated, IsPropertyManager]

