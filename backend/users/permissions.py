from rest_framework import permissions


class IsManager(permissions.BasePermission):
    """
    Custom permission to only allow managers of a property to edit it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.property.manager == request.user
