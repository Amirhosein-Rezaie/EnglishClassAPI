from django.shortcuts import render
from . import serializers
from rest_framework.viewsets import ModelViewSet
from . import models


# users viewset
class UserViewset(ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.Users.objects.all()


# levels viewset
class LevelViewset(ModelViewSet):
    serializer_class = serializers.LevelSerializer
    queryset = models.levels.objects.all()


# books viewset
class BookViewset(ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = models.Books.objects.all()


# logins viewset
class LoginViewset(ModelViewSet):
    serializer_class = serializers.LoginSerializer
    queryset = models.Logins.objects.all()
