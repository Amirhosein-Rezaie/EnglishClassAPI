from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    MinValueValidator,
)


# the model of users
class Users(AbstractUser):
    class ROLES(models.TextChoices):
        ADMIN = "ADMIN"
        PERSONEL = "PERSONEL"

    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    national_code = models.CharField(max_length=25, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    role = models.CharField(
        choices=ROLES, default=ROLES.PERSONEL, null=False, blank=False)

    def __str__(self):
        return self.username


# the model of user profile
class UserProfile(models.Model):
    image = models.ImageField(
        upload_to='images/profiles/users/', null=True, blank=True)
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.user


# the model of levels
class levels(models.Model):
    title = models.CharField(
        primary_key=True, unique=True, null=False, blank=False, max_length=100)

    def __str__(self):
        return self.title


# the model of books
class Books(models.Model):
    class TYPES_BOOK(models.TextChoices):
        STUDENT_BOOK = "STUDENT_BOOK"
        WORK_BOOK = "WORK_BOOK"
        STORY_BOOK = "STORY_BOOK"

    title = models.CharField(max_length=100, null=False, blank=False)
    level = models.OneToOneField(
        levels, on_delete=models.SET_NULL, null=False, blank=False)
    type = models.CharField(
        max_length=50, choices=TYPES_BOOK, null=False, blank=False)
    number = models.IntegerField(validators=[
        MinValueValidator(1)
    ], null=False, blank=False)
    image = models.ImageField(upload_to='images/books/', null=True, blank=True)

    def __str__(self):
        return self.title


# the model of login's log
class Logins(models.Model):
    user = models.ForeignKey(Users, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return self.user
