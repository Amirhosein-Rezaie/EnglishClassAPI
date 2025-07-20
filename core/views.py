from . import serializers
from rest_framework.viewsets import ModelViewSet
from . import models
from education import models as EducationModels
from education.serializers import (GradeSerializer)
from people import models as PeopleModels
from people.serializers import (TeacherSerializer, StudentSerializer)
from EnglishClass.permissions import (NotAllow, DeleteForAdmin)
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from drf_spectacular.utils import extend_schema
from EnglishClass.helper import dynamic_search, description_search_swagger
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import check_password
from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# users viewset
class UserViewset(ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.Users.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return super().get_permissions()

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

    @extend_schema(
        description=description_search_swagger
    )
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

    @extend_schema(
        description=description_search_swagger
    )
    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(request=request, model=models.Logins,
                                  serializer=serializers.LoginSerializer)
        return super().list(request, *args, **kwargs)


# token view
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs):
        """
        set log for logins that the users take
        """
        data = request.data
        username = data['username']
        password = data['password']

        user = models.Users.objects.get(username=username)
        status = check_password(password, user.password)

        models.Logins.objects.create(
            user=user or None,
            status=status
        )

        return super().post(request, *args, **kwargs)


class Dashboard(APIView):
    def get(self, request: Request):
        result = {}

        # users
        users = {}
        # # count of users
        users['users_count'] = models.Users.objects.all().count()
        # # count each of roles
        for role in models.Users.ROLES:
            users[f"{role.lower()}_count"] = models.Users.objects.filter(
                role=role).count()
        result['users'] = users

        # registers
        registers = {}
        # # count each of pay status
        for pay in EducationModels.STATUS_PAY:
            registers[f"{pay.lower()}_count"] = EducationModels.Registers.objects.filter(
                status=pay).count()
        result['registers'] = registers

        # teachers
        teachers = {}
        # # count of teachers
        teachers['teachers_count'] = PeopleModels.Teachers.objects.all().count()
        # # names of teacher that have the highest average point
        average_points = {}
        for teacher in TeacherSerializer(PeopleModels.Teachers.objects.all(), many=True).data:
            id = teacher['id']
            first_name = teacher['first_name']
            last_name = teacher['last_name']

            average = EducationModels.Points.objects.filter(teacher=id).aggregate(
                Avg('point')
            )['point__avg']
            average_points[f"{first_name} {last_name}"] = average
        teachers['average_points'] = average_points
        result['teachers'] = teachers

        # book sales
        book_sales = {}
        # # count all of the book sales
        book_sales['book_sales_count'] = EducationModels.BookSales.objects.all().count()
        # # count each book sales by status
        for status_pay in EducationModels.STATUS_PAY:
            book_sales[f"{status_pay.lower()}_count"] = EducationModels.BookSales.objects.filter(
                status=status_pay).count()
        result['book_sales'] = book_sales

        # students
        students = {}
        # # count of students
        students['students_count'] = PeopleModels.Students.objects.all().count()
        # # names of students with average grades
        students_avrg_grades = {}
        for student in StudentSerializer(PeopleModels.Students.objects.all(), many=True).data:
            id = student['id']
            total_grades = []
            first_name = student['first_name']
            last_name = student['last_name']
            for grade in GradeSerializer(EducationModels.Grades.objects.filter(student=id), many=True).data:
                total_grade = grade['class_grade'] + grade['workbook_grade'] + grade['Storybook_grade'] + \
                    grade['Videoclip_grade'] + \
                    grade['Film_grade'] + grade['Exam_grade']
                print(total_grade)
                total_grades.append(total_grade)
            students_avrg_grades[f'{first_name} {last_name}'] = sum(
                total_grades) / len(total_grades)
        students['students_avrg_grades'] = students_avrg_grades
        result['students'] = students

        # response
        return Response(result, status=status.HTTP_200_OK)
