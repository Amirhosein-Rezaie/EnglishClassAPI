from . import models
from . import serializers
from rest_framework.viewsets import ModelViewSet
from EnglishClass.permissions import (DeleteForAdmin, NotAllow)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from EnglishClass.helper import dynamic_search


# terms
class TermViewset(ModelViewSet):
    serializer_class = serializers.TermSerializer
    queryset = models.Terms.objects.all()
    permission_classes = [DeleteForAdmin]

    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(request=request, model=models.Terms,
                                  serializer=serializers.TermSerializer)
        return super().list(request, *args, **kwargs)


# register
class RegisterViewset(ModelViewSet):
    serializer_class = serializers.RegisterSerializer
    queryset = models.Registers.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['DELETE']:
            return [NotAllow()]
        return super().get_permissions()

    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(request=request, model=models.Registers,
                                  serializer=serializers.RegisterSerializer)
        return super().list(request, *args, **kwargs)


# grades
class GradeViewset(ModelViewSet):
    serializer_class = serializers.GradeSerializer
    queryset = models.Grades.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['DELETE']:
            return [NotAllow()]
        return super().get_permissions()

    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(request=request, model=models.Grades,
                                  serializer=serializers.GradeSerializer)
        return super().list(request, *args, **kwargs)


# book sales
class BookSaleViewset(ModelViewSet):
    serializer_class = serializers.BookSaleSerializer
    queryset = models.BookSales.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['DELETE']:
            return [NotAllow()]
        return super().get_permissions()

    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(request=request, model=models.BookSales,
                                  serializer=serializers.BookSaleSerializer)
        return super().list(request, *args, **kwargs)
