from rest_framework.serializers import ModelSerializer
from . import models
from core.serializers import (
    BookSerializer,
    UserSerializer
)
from django.db.models import Sum


# Terms
class TermSerializer(ModelSerializer):
    student_book = BookSerializer()
    work_book = BookSerializer()
    story_book = BookSerializer()
    # teacher = -> need teacher serializer in people app
    user = UserSerializer()

    class Meta:
        model = models.Terms
        fields = '__all__'


# registers
class RegistersViewset(ModelSerializer):
    # student -> need student serializer in people
    term = TermSerializer()
    user = UserSerializer()

    class Meta:
        model = models.Registers
        fields = '__all__'


# grades
class GradeSerializer(ModelSerializer):
    term = TermSerializer()

    class Meta:
        model = models.Grades
        fields = '__all__'


# book sales
class BookSaleSerializer(ModelSerializer):
    # student -> need student serializer in people app
    book = BookSerializer()
    user = UserSerializer()

    class Meta:
        model = models.BookSales
        fields = '__all__'
