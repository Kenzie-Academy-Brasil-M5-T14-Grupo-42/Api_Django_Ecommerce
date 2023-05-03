from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User

class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_superuser
        )
    

class HasAdminPermission(permissions.BasePermission):

    def has_object_permission(
        self, request: Request, view: View, obj: User
    ) -> bool:
        return obj == request.user or request.user.is_superuser