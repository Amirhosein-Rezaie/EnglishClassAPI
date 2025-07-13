from . import serializers
from . import models
from rest_framework.viewsets import ModelViewSet
from EnglishClass.permissions import (DeleteForAdmin, IsAdminOrReadOnly)


# students
class StudentViewset(ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Students.objects.all()
    permission_classes = [DeleteForAdmin]


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


# teacher profiles
class TeacherProfileViewset(ModelViewSet):
    serializer_class = serializers.TeacherProfile
    queryset = models.TeacherProfiles.objects.all()
    permission_classes = [IsAdminOrReadOnly]
