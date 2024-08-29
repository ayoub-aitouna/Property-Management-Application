from django.shortcuts import render
from rest_framework import generics
from .models import Payment
from .serializers import PaymentSerializer, PaymentDetailsSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsManager

# Create your views here.
class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class PaymentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentDetailsSerializer
    permission_classes = [IsAuthenticated, IsManager]
