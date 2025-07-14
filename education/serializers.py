from rest_framework.serializers import ModelSerializer
from . import models
from core.serializers import (
    BookSerializer,
    UserSerializer
)
from people.serializers import (
    StudentSerializer,
    TeacherSerializer,
)
from django.db.models import Sum


# Terms
class TermSerializer(ModelSerializer):
    student_book_detail = BookSerializer(source='student_book', read_only=True)
    work_book_detail = BookSerializer(source='work_book', read_only=True)
    story_book_detail = BookSerializer(source='story_book', read_only=True)
    teacher_detail = TeacherSerializer(source='teacher', read_only=True)
    user_detail = UserSerializer(source='user', read_only=True)

    class Meta:
        model = models.Terms
        fields = '__all__'


# registers
class RegisterSerializer(ModelSerializer):
    student_detail = StudentSerializer(source='student', read_only=True)
    term_detail = TermSerializer(source='term', read_only=True)
    user_detail = UserSerializer(source='user', read_only=True)

    class Meta:
        model = models.Registers
        fields = '__all__'


# grades
class GradeSerializer(ModelSerializer):
    term_detail = TermSerializer(source='term', read_only=True)
    student_detail = StudentSerializer(source='student', read_only=True)

    class Meta:
        model = models.Grades
        fields = '__all__'


# book sales
class BookSaleSerializer(ModelSerializer):
    student_detail = StudentSerializer(source='student', read_only=True)
    book_detail = BookSerializer(source='book', read_only=True)
    user_detail = UserSerializer(source='user', read_only=True)

    class Meta:
        model = models.BookSales
        fields = '__all__'
