from . import serializers
from . import models
from rest_framework.viewsets import ModelViewSet


# students
class StudentViewset(ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Students.objects.all()


# student profiles
class StudentProfileViewset(ModelViewSet):
    serializer_class = serializers.StudentProfile
    queryset = models.StudentProfiles.objects.all()


# teacher
class TeacherViewset(ModelViewSet):
    serializer_class = serializers.TeacherSerializer
    queryset = models.Teachers.objects.all()


# teacher profiles
class TeacherProfileViewset(ModelViewSet):
    serializer_class = serializers.TeacherProfile
    queryset = models.TeacherProfiles.objects.all()
