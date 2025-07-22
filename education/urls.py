from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


# terms router
term_router = DefaultRouter()
term_router.register('', views.TermViewset)

# registers router
register_router = DefaultRouter()
register_router.register('', views.RegisterViewset)

# grades router
grade_router = DefaultRouter()
grade_router.register('', views.GradeViewset)

# book sales router
booksale_router = DefaultRouter()
booksale_router.register('', views.BookSaleViewset)

urlpatterns = [
    path('terms/', include(term_router.urls)),
    path('terms-excel/', views.export_terms_excel.as_view(), name='terms_excel'),
    path('registers/', include(register_router.urls)),
    path('grades/', include(grade_router.urls)),
    path('book-sales/', include(booksale_router.urls)),
]
