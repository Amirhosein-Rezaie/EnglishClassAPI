from . import serializers
from rest_framework.viewsets import ModelViewSet
from . import models
from EnglishClass.permissions import (NotAllow, DeleteForAdmin)
from rest_framework.request import Request
from drf_spectacular.utils import extend_schema
from EnglishClass.helper import dynamic_search


# fields
description_search_swagger = "ارسال گویری پارامتر برای جست و جو براساس فیلد های دیتابیس"


# users viewset
class UserViewset(ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.Users.objects.all()

    @extend_schema(
        description=description_search_swagger
    )
    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(request=request, model=models.Users,
                                  serializer=serializers.UserSerializer)
        return super().list(request, *args, **kwargs)


# user profile
class UserProfileViewset(ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()


# levels viewset
class LevelViewset(ModelViewSet):
    serializer_class = serializers.LevelSerializer
    queryset = models.levels.objects.all()

    @extend_schema(
        description=description_search_swagger
    )
    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(request=request, model=models.levels,
                                  serializer=serializers.LevelSerializer)
        return super().list(request, *args, **kwargs)


# books viewset
class BookViewset(ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = models.Books.objects.all()
    permission_classes = [DeleteForAdmin]

    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(request=request, model=models.Books,
                                  serializer=serializers.BookSerializer)
        return super().list(request, *args, **kwargs)


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

    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(request=request, model=models.Logins,
                                  serializer=serializers.LoginSerializer)
        return super().list(request, *args, **kwargs)
