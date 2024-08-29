from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PaymentList.as_view(), name='payment_list'),
    path('<int:pk>/', views.PaymentDetails.as_view(),
         name='payment-details'),
]
