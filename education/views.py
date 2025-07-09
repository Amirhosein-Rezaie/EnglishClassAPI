from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.viewsets import ModelViewSet


# terms
class TermViewset(ModelViewSet):
    serializer_class = serializers.TermSerializer
    queryset = models.Terms.objects.all()


# register
class RegisterViewset(ModelViewSet):
    serializer_class = serializers.RegistersViewset
    queryset = models.Registers.objects.all()


# grades
class GradeViewset(ModelViewSet):
    serializer_class = serializers.GradeSerializer
    queryset = models.Grades.objects.all()


# book sales
class BookSaleViewset(ModelViewSet):
    serializer_class = serializers.BookSaleSerializer
    queryset = models.BookSales.objects.all()
