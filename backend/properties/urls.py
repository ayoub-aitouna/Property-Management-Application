from django.urls import path
from . import views

urlpatterns = [
    path('', views.PropertyList.as_view(), name='property_list'),
    path('<int:pk>/', views.PropertyDetails.as_view(), name='property-details'),
]
