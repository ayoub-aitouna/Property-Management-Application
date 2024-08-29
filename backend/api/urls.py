from django.urls import path, include

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('users/', include('users.urls')),
    path('properties/', include('properties.urls')),
    path('payments/', include('payments.urls')),
]
