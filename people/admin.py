from django.contrib import admin
from . import models


# the admin of students
@admin.register(models.Students)
class StudentAdmin(admin.ModelAdmin):
    pass


# the admin of student profile
@admin.register(models.StudentProfiles)
class StudentProfilesAdmin(admin.ModelAdmin):
    pass


# the admin of teachers
@admin.register(models.Teachers)
class TeachersAdmin(admin.ModelAdmin):
    pass


# the admin of teacher profile
@admin.register(models.TeacherProfiles)
class TeacherProfilesAdmin(admin.ModelAdmin):
    pass
