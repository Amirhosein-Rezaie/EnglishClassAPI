from django.db import models


# the model of students
class Students(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    national_code = models.CharField(max_length=100, null=False, blank=False)
    birthday = models.DateField(null=True, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)

    class Meta:
        db_table = 'Students'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# the model of student profiles
class StudentProfiles(models.Model):
    student = models.ForeignKey(
        Students, null=False, blank=False, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True,
                              upload_to='images/profiles/students/')

    class Meta:
        db_table = 'StudentProfiles'

    def __str__(self):
        return f"{self.student}"


# the model of teacher
class Teachers(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    national_code = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)

    class Meta:
        db_table = 'Teachers'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# the model of student profiles
class TeacherProfiles(models.Model):
    teacher = models.ForeignKey(
        Teachers, null=False, blank=False, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True,
                              upload_to='images/profiles/teachers/')

    class Meta:
        db_table = 'TeacherProfiles'

    def __str__(self):
        return f"{self.teacher}"
