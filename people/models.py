from django.db import models


# the model of students
class Students(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    national_code = models.CharField(max_length=100, null=False, blank=False)
    birthday = models.DateField(null=True, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# the model of student profiles
class StudentProfiles(models.Model):
    student = models.ForeignKey(Students, null=False, blank=False)
    image = models.ImageField(null=True, blank=True,
                              upload_to='iamges/profiles/students/')

    def __str__(self):
        return self.student


# the model of teacher
class Teachers(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    national_code = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# the model of student profiles
class TeacherProfiles(models.Model):
    teacher = models.ForeignKey(Teachers, null=False, blank=False)
    image = models.ImageField(null=True, blank=True,
                              upload_to='iamges/profiles/teachers/')

    def __str__(self):
        return self.teacher
