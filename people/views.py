from . import serializers
from . import models
from rest_framework.viewsets import ModelViewSet
from EnglishClass.permissions import (
    DeleteForAdmin, IsAdminOrReadOnly, AdminOrPersonel, IsStudent, StudentAdminPersonel)
from rest_framework.request import Request
from EnglishClass.helper import (
    dynamic_search, description_search_swagger, limit_paginate)
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.views import APIView
from .helper import export_excel
from rest_framework.response import Response
from rest_framework import status
from education.models import (Grades, Terms, Registers)
from education.serializers import (GradeSerializer, TermSerializer)
from EnglishClass.pagination import DynamicPagination
from rest_framework.decorators import permission_classes
from core.models import Users
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from rest_framework.exceptions import ValidationError


# paginator
paginator = DynamicPagination()


# students
class StudentViewset(ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Students.objects.all()
    permission_classes = [DeleteForAdmin, AdminOrPersonel]

    @extend_schema(
        description=description_search_swagger
    )
    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(
                request=request, model=models.Students,
                serializer=serializers.StudentSerializer
            )
        return super().list(request, *args, **kwargs)

    def create(self, request: Request, *args, **kwargs):
        student = request.data
        Users.objects.create(
            username=student['national_code'],
            password=make_password(student['phone']),
            role=Users.ROLES.STUDENT
        )
        return super().create(request, *args, **kwargs)


# get students grades of hole time
@extend_schema(
    parameters=[
        OpenApiParameter(
            name='student-id', type=int, description='شناسه زبان آموز', required=True
        )
    ]
)
@permission_classes([AdminOrPersonel])
class students_grades(APIView):
    """
    تمام نمرات یک زبان آموز در تمامی ترم ها
    """

    def get(self, request: Request):
        student_id = request.query_params.get('student-id')

        if not student_id:
            return Response({
                "error": 'شناسه ای یافت نشد',
                "details": 'شناسه زبان آموزی ارسال نشده'
            }, status=status.HTTP_400_BAD_REQUEST)

        grades = Grades.objects.filter(student=student_id)

        # paginate
        paginator.page_size = limit_paginate(request)
        paginated_grades = paginator.paginate_queryset(
            request=request, queryset=grades)
        # serialize and response
        serialized_grades = GradeSerializer(paginated_grades, many=True).data
        return Response(serialized_grades, status=status.HTTP_200_OK)


# me students
class StudentMe(APIView):
    permission_classes = [IsStudent]

    def get(self, request: Request):
        student_username = request.user
        return Response(
            serializers.StudentSerializer(models.Students.objects.filter(
                national_code=student_username
            ), many=True).data,
            status=status.HTTP_200_OK
        )


# terms of one student
@extend_schema(
    parameters=[
        OpenApiParameter(
            name='student-id',
            description='شناسه زبان آموز اجباری در صورت لاگین نبودن زبان آموز',
            required=True,
            type=int
        )
    ],
    responses=TermSerializer(many=True),
)
class TermsOfStudent(APIView):
    """
    a view get terms of one student
    """
    permission_classes = [StudentAdminPersonel]

    def get(self, request: Request):
        role = self.request.user.role

        student_id = None
        if role == Users.ROLES.STUDENT:
            student_id = models.Students.objects.get(
                national_code=self.request.user.username).pk
        elif role != Users.ROLES.STUDENT:
            if request.query_params.get('student-id'):
                student_id = request.query_params.get('student-id')
            else:
                raise ValidationError(
                    detail="شناسه زبان آموز ارسال نشده ... !",
                    code=status.HTTP_400_BAD_REQUEST
                )

        terms = Terms.objects.filter(Q(
            id__in=Registers.objects.filter(
                student=student_id).values_list('term', flat=True)
        ))

        paginator.page_size = limit_paginate(request)
        paginated_data = paginator.paginate_queryset(terms, request)

        return paginator.get_paginated_response(
            TermSerializer(
                paginated_data, many=True
            ).data
        )


# student profiles
class StudentProfileViewset(ModelViewSet):
    serializer_class = serializers.StudentProfile
    queryset = models.StudentProfiles.objects.all()
    permission_classes = [DeleteForAdmin, AdminOrPersonel]


# teacher
class TeacherViewset(ModelViewSet):
    serializer_class = serializers.TeacherSerializer
    queryset = models.Teachers.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    @extend_schema(
        description=description_search_swagger
    )
    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(
                request=request, model=models.Teachers,
                serializer=serializers.TeacherSerializer
            )
        return super().list(request, *args, **kwargs)


# teacher profiles
class TeacherProfileViewset(ModelViewSet):
    serializer_class = serializers.TeacherProfile
    queryset = models.TeacherProfiles.objects.all()
    permission_classes = [IsAdminOrReadOnly, AdminOrPersonel]


# export excel files
# # export students file
class export_students_excel(APIView):
    """
    خروجی فایل اکسل برای تمامی زبان آموزان
    """
    permission_classes = [AdminOrPersonel]

    def get(self, request: Request):
        return export_excel(
            model=models.Students,
            serializer=serializers.StudentSerializer,
            columns=[
                'نام', 'نام خانوادگی', 'کد ملی',
                'تاریخ تولد', 'شماره تماس'
            ],
            filename='students'
        )


# # export teachers file
class export_teachers_excel(APIView):
    """
    خروجی فایل اکسل برای تمامی معلم ها
    """
    permission_classes = [AdminOrPersonel]

    def get(self, request: Request):
        return export_excel(
            model=models.Teachers,
            serializer=serializers.TeacherSerializer,
            columns=[
                'نام', 'نام خانوادگی',
                'کد ملی', 'شماره تلفن'
            ],
            filename='teachers'
        )
