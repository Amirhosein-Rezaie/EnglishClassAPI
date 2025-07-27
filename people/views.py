from . import serializers
from . import models
from rest_framework.viewsets import ModelViewSet
from EnglishClass.permissions import (DeleteForAdmin, IsAdminOrReadOnly)
from rest_framework.request import Request
from EnglishClass.helper import (
    dynamic_search, description_search_swagger, limit_paginate)
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from rest_framework.views import APIView
from .helper import export_excel
from rest_framework.response import Response
from rest_framework import status
from education.models import (Grades)
from education.serializers import (GradeSerializer)
from EnglishClass.pagination import DynamicPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


# paginator
paginator = DynamicPagination()


# students
class StudentViewset(ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Students.objects.all()
    permission_classes = [DeleteForAdmin]

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


# get students grades of hole time
@extend_schema(
    parameters=[
        OpenApiParameter(
            name='student-id', type=int, description='شناسه زبان آموز', required=True
        )
    ]
)
@permission_classes([IsAuthenticated])
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


# student profiles
class StudentProfileViewset(ModelViewSet):
    serializer_class = serializers.StudentProfile
    queryset = models.StudentProfiles.objects.all()
    permission_classes = [DeleteForAdmin]


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
    permission_classes = [IsAdminOrReadOnly]


# export excel files
# # export students file
class export_students_excel(APIView):
    """
    خروجی فایل اکسل برای تمامی زبان آموزان
    """

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
