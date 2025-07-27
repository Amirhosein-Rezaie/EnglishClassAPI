from rest_framework.serializers import ModelSerializer
from . import models


# student profiles
class StudentProfile(ModelSerializer):
    class Meta:
        model = models.StudentProfiles
        fields = '__all__'


# Students
class StudentSerializer(ModelSerializer):
    profiles = StudentProfile(
        many=True, source='student_profile', read_only=True)

    class Meta:
        model = models.Students
        fields = '__all__'


# teacher profiles
class TeacherProfile(ModelSerializer):
    class Meta:
        model = models.TeacherProfiles
        fields = '__all__'


# teachers
class TeacherSerializer(ModelSerializer):
    profiles = TeacherProfile(many=True, source='teacher_profile')

    class Meta:
        model = models.Teachers
        fields = '__all__'
