from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


# students router
student_router = DefaultRouter()
student_router.register('', views.StudentViewset)

# students router
student_profiles_router = DefaultRouter()
student_profiles_router.register('', views.StudentProfileViewset)

# teacher router
teacher_router = DefaultRouter()
teacher_router.register('', views.TeacherViewset)

# teacher profile router
teacher_profile_router = DefaultRouter()
teacher_profile_router.register('', views.TeacherProfileViewset)


urlpatterns = [
    path('students/', include(student_router.urls),
         name='students'),
    path("students-excel/", views.export_students_excel.as_view(),
         name="students_excel"),
    path('student-profiles/', include(student_profiles_router.urls),
         name='student-profiles'),
    path('student-grades/', views.students_grades.as_view(),
         name='student_grades'),
    path("student-me/", views.StudentMe.as_view(),
         name="student-me"),
    path('teachers/', include(teacher_router.urls),
         name='teachers'),
    path('teachers-excel/', views.export_teachers_excel.as_view(),
         name='teachers_excel'),
    path('teacher-profile/', include(teacher_profile_router.urls),
         name='teacher-profiles')
]
