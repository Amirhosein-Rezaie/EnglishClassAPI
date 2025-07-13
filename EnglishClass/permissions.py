from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from core.models import Users


# is admin
class IsAdminUser(BasePermission):
    def has_permission(self, request: Request, view):
        return bool(
            request.user.is_authenticated and
            request.user.role == Users.ROLES.ADMIN
        )


# add update get allow for users
class DeleteForAdmin(BasePermission):
    def has_permission(self, request: Request, view):
        return bool(
            request.user.is_authenticated and
            request.user.role == Users.ROLES.ADMIN or
            request.method not in ['DELETE']
        )


# is admin or just read allow
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request: Request, view):
        return bool(
            request.user.is_authenticated and
            request.user.role == Users.ROLES.ADMIN or
            request.method in SAFE_METHODS
        )


# not allow
class NotAllow(BasePermission):
    def has_permission(self, request, view):
        return False
