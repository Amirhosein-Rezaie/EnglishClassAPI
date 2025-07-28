from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
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
            (request.user.is_authenticated) and
            (request.user.role == Users.ROLES.ADMIN or
             request.method in SAFE_METHODS)
        )


# not allow
class NotAllow(BasePermission):
    def has_permission(self, request, view):
        return False


# permissions for students
class IsStudent(BasePermission):
    def has_permission(self, request: Request, view):
        return bool(
            (request.user or request.user.is_authnticated) and
            (request.user.role == Users.ROLES.STUDENT)
        )


# get for students only
class GetStudentsOnly(BasePermission):
    def has_permission(self, request: Request, view):
        return bool(
            (request.user and request.user.is_authenticated) and
            (request.user.role ==
             Users.ROLES.STUDENT and request.method in ['GET'])
        )


# is not in [ADMIN, PERSONEL]
class AdminOrPersonel(BasePermission):
    def has_permission(self, request: Request, view):
        return bool(
            (request.user and request.user.is_authenticated) and
            (request.user.role in [Users.ROLES.ADMIN, Users.ROLES.PERSONEL])
        )
