from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.viewsets import ModelViewSet
from EnglishClass.permissions import (DeleteForAdmin, NotAllow)
from rest_framework.permissions import IsAuthenticated


# terms
class TermViewset(ModelViewSet):
    serializer_class = serializers.TermSerializer
    queryset = models.Terms.objects.all()
    permission_classes = [DeleteForAdmin]


# register
class RegisterViewset(ModelViewSet):
    serializer_class = serializers.RegistersViewset
    queryset = models.Registers.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['DELETE']:
            return [NotAllow()]
        return super().get_permissions()


# grades
class GradeViewset(ModelViewSet):
    serializer_class = serializers.GradeSerializer
    queryset = models.Grades.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['DELETE']:
            return [NotAllow()]
        return super().get_permissions()


# book sales
class BookSaleViewset(ModelViewSet):
    serializer_class = serializers.BookSaleSerializer
    queryset = models.BookSales.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['DELETE']:
            return [NotAllow()]
        return super().get_permissions()
