from django.urls import path
from . import views

urlpatterns = [
    path('tenants-list/', views.TenantList.as_view(), name='tenant_list'),
    path('tenants-details/<int:pk>/',
         views.TenantDetails.as_view(), name='tenant-details'),

]
