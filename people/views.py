from . import serializers
from . import models
from rest_framework.viewsets import ModelViewSet
from EnglishClass.permissions import (DeleteForAdmin, IsAdminOrReadOnly)
from rest_framework.request import Request
from EnglishClass.helper import dynamic_search, description_search_swagger
from drf_spectacular.utils import extend_schema


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
            return dynamic_search(request=request, model=models.Students, serializer=serializers.StudentSerializer)
        return super().list(request, *args, **kwargs)


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
            return dynamic_search(request=request, model=models.Teachers, serializer=serializers.TeacherSerializer)
        return super().list(request, *args, **kwargs)


# teacher profiles
class TeacherProfileViewset(ModelViewSet):
    serializer_class = serializers.TeacherProfile
    queryset = models.TeacherProfiles.objects.all()
    permission_classes = [IsAdminOrReadOnly]
