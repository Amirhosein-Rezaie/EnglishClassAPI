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

    national_code = models.CharField(max_length=25, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    role = models.CharField(
        choices=ROLES.choices, default=ROLES.PERSONEL, null=False, blank=False, max_length=20
    )

    groups = None
    user_permissions = None
    date_joined = None
    last_login = None
    is_staff = None
    # is_active = None
    is_superuser = None

    class Meta:
        db_table = 'Users'

    def __str__(self):
        return self.username


# the model of user profile
class UserProfile(models.Model):
    image = models.ImageField(
        upload_to='images/profiles/users/', null=True, blank=True)
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, null=False, blank=False, related_name="user_profiles")

    class Meta:
        db_table = 'UserProfiles'

    def __str__(self):
        return self.user.username


# the model of levels
class levels(models.Model):
    title = models.CharField(
        primary_key=True, unique=True, null=False, blank=False, max_length=100)

    class Meta:
        db_table = 'Levels'

    def __str__(self):
        return self.title


# the model of books
class Books(models.Model):
    class TYPES_BOOK(models.TextChoices):
        STUDENT_BOOK = "STUDENT_BOOK"
        WORK_BOOK = "WORK_BOOK"
        STORY_BOOK = "STORY_BOOK"

    title = models.CharField(max_length=100, null=False, blank=False)
    level = models.ForeignKey(
        levels, on_delete=models.CASCADE, null=False, blank=False, related_name="books")
    type = models.CharField(
        max_length=50, choices=TYPES_BOOK.choices, null=False, blank=False)
    number = models.IntegerField(validators=[
        MinValueValidator(1)
    ], null=False, blank=False)
    image = models.ImageField(upload_to='images/books/', null=True, blank=True)
    price = models.IntegerField(
        validators=[
            MinValueValidator(1)
        ],
        null=False, blank=False
    )

    class Meta:
        db_table = 'Books'

    def __str__(self):
        return self.title


# the model of login's log
class Logins(models.Model):
    user = models.ForeignKey(Users, null=False, blank=False,
                             on_delete=models.CASCADE, related_name="login_logs")
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(null=False, blank=False)

    class Meta:
        db_table = 'Logins'

    def __str__(self):
        return f"{self.user.username} - {'Success' if self.status else 'Failed'}"
