from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


# students router
student_router = DefaultRouter()
student_router.register('', views.StudentViewset)


urlpatterns = [
    path('students/', include(student_router.urls)),
    path('teachers/', include(student_router.urls)),
]
