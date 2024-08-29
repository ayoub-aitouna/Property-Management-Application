from rest_framework import permissions


class IsPropertyManager(permissions.BasePermission):
    """
    Custom permission to only allow managers of a property to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        return obj.manager == request.user
