from django.shortcuts import render
from . import serializers
from rest_framework.viewsets import ModelViewSet
from . import models
from EnglishClass.permissions import (NotAllow, DeleteForAdmin)


# users viewset
class UserViewset(ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.Users.objects.all()


# user profile
class UserProfileViewset(ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()


# levels viewset
class LevelViewset(ModelViewSet):
    serializer_class = serializers.LevelSerializer
    queryset = models.levels.objects.all()


# books viewset
class BookViewset(ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = models.Books.objects.all()
    permission_classes = [DeleteForAdmin]


# logins viewset
class LoginViewset(ModelViewSet):
    serializer_class = serializers.LoginSerializer
    queryset = models.Logins.objects.all()

    def get_permissions(self):
        method = self.request.method
        if method in ['DELETE', 'UPDATE', 'POST']:
            return [NotAllow()]
        # if method in ['POST']:
        #     return [AllowAny()]
        return super().get_permissions()
