from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from core.models import Users


# is admin
class IsAdminUser(BasePermission):
    def has_permission(self, request: Request, view):
        condition = bool(
            request.user.is_authenticated and
            request.user.role == Users.ROLES.ADMIN
        )
        return condition
