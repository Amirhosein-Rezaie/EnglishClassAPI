from . import serializers
from rest_framework.viewsets import ModelViewSet
from . import models
from .serializers import (LevelSerializer)
from education import models as EducationModels
from education.serializers import (GradeSerializer)
from people import models as PeopleModels
from people.serializers import (TeacherSerializer, StudentSerializer)
from EnglishClass.permissions import (
    NotAllow, DeleteForAdmin, IsAdminUser, IsAdminOrReadOnly, AdminOrPersonel, IsAnonymousUser)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from drf_spectacular.utils import extend_schema, OpenApiParameter
from EnglishClass.helper import dynamic_search, description_search_swagger
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import check_password
from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from django.db.models import Q


# users viewset
class UserViewset(ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.Users.objects.all()

    @extend_schema(
        description=description_search_swagger
    )
    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(
                request=request, model=models.Users,
                serializer=serializers.UserSerializer
            )
        return super().list(request, *args, **kwargs)


# user profile
@extend_schema(
    parameters=[
        OpenApiParameter(
            name='all', description='برای ارسال تمام پروفایل ها برای ادمین', required=False, type=bool
        )
    ]
)
class UserProfileViewset(ModelViewSet):
    """
    ارسال تمام پروفایل ها برای ادمین، و برای هر کاربر ارسال پروفایل های خود
    """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    permission_classes = [AdminOrPersonel]

    def get_queryset(self):
        if dict(self.request.query_params).get('all') and self.request.user.role == models.Users.ROLES.ADMIN:
            return super().get_queryset()
        return models.UserProfile.objects.filter(user=self.request.user.pk)


# levels viewset
class LevelViewset(ModelViewSet):
    serializer_class = serializers.LevelSerializer
    queryset = models.levels.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    @extend_schema(
        description=description_search_swagger
    )
    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(
                request=request, model=models.levels,
                serializer=serializers.LevelSerializer
            )
        return super().list(request, *args, **kwargs)


# books viewset
class BookViewset(ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = models.Books.objects.all()
    permission_classes = [DeleteForAdmin, AdminOrPersonel]

    @extend_schema(
        description=description_search_swagger
    )
    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(
                request=request, model=models.Books,
                serializer=serializers.BookSerializer
            )
        return super().list(request, *args, **kwargs)


# logins viewset
class LoginViewset(ModelViewSet):
    serializer_class = serializers.LoginSerializer
    queryset = models.Logins.objects.all()

    def get_permissions(self):
        method = self.request.method
        if method in ['DELETE', 'UPDATE', 'POST']:
            return [NotAllow()]
        return super().get_permissions()

    @extend_schema(
        description=description_search_swagger
    )
    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(
                request=request, model=models.Logins,
                serializer=serializers.LoginSerializer
            )
        return super().list(request, *args, **kwargs)


# token view
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs):
        """
        set log for logins that the users take
        """
        permission_classes = [IsAnonymousUser]

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


# dashboard
@permission_classes([IsAdminUser])
class Dashboard(APIView):
    """
    آمار های کلی
    """

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
                total_grades.append(total_grade)
            if len(total_grades) > 0:
                students_avrg_grades[f'{first_name} {last_name}'] = sum(
                    total_grades) / len(total_grades)
        students['students_avrg_grades'] = students_avrg_grades
        result['students'] = students

        # terms
        terms = {}
        # # count of terms
        terms['terms_count'] = EducationModels.Terms.objects.all().count()
        # # count of terms by levels
        terms_level_count = {}
        for level in LevelSerializer(models.levels.objects.all(), many=True).data:
            level = level['title']
            terms_level_count[f"{level}"] = EducationModels.Terms.objects.filter(
                level__title=level).count()
        terms['terms_level_count'] = terms_level_count
        # # count number of students of per terms
        terms_queryset = EducationModels.Terms.objects.all()
        students_terms_count = {}
        for term in terms_queryset:
            count = PeopleModels.Students.objects.filter(Q(
                id__in=EducationModels.Registers.objects.filter(
                    term__id=term.pk).values_list('student', flat=True)
            )).distinct().count()
            students_terms_count[f'{term.title}__{term.pk}'] = count
        terms['students_terms_count'] = students_terms_count
        result['terms'] = terms

        # response
        return Response(result, status=status.HTTP_200_OK)
