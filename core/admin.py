from django.contrib import admin
from . import models


# add user to admin panel
@admin.register(models.Users)
class UserAdmin(admin.ModelAdmin):
    pass


# add user profile to admin panel
@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


# add books to admin panel
@admin.register(models.Books)
class BooksAdmin(admin.ModelAdmin):
    pass


# add levels to admin panel
@admin.register(models.levels)
class levelsAdmin(admin.ModelAdmin):
    pass


# add Logins to admin panel
@admin.register(models.Logins)
class LoginsAdmin(admin.ModelAdmin):
    pass
