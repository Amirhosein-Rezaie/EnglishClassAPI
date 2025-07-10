from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# users router
user_router = DefaultRouter()
user_router.register('', views.UserViewset)


# user profile router
user_profile_router = DefaultRouter()
user_profile_router.register('', views.UserProfileViewset)


# levels router
levels_router = DefaultRouter()
levels_router.register('', views.LevelViewset)

# books router
books_router = DefaultRouter()
books_router.register('', views.BookViewset)

# login router
logins_router = DefaultRouter()
logins_router.register('', views.LoginViewset)

urlpatterns = [
    path('users/', include(user_router.urls)),
    path('levels/', include(levels_router.urls)),
    path('books/', include(books_router.urls)),
    path('logins/', include(logins_router.urls)),
    path('user-profile/', include(user_profile_router.urls))
]
