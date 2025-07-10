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
    path('students/', include(student_router.urls)),
    path('student-profiles/', include(student_profiles_router.urls)),
    path('teachers/', include(teacher_router.urls)),
    path('teacher-profile/', include(teacher_profile_router.urls))
]
