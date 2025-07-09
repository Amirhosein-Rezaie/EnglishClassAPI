from . import serializers
from . import models
from rest_framework.viewsets import ModelViewSet


# students
class StudentViewset(ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Students.objects.all()


# students
class TeacherViewset(ModelViewSet):
    serializer_class = serializers.TeacherSerializer
    queryset = models.Teachers.objects.all()


# student profiles
class StudentProfileViewset(ModelViewSet):
    serializer_class = serializers.StudentProfile
    queryset = models.StudentProfiles.objects.all()
