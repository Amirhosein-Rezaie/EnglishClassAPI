from django.core.management.base import BaseCommand
from django.db import models
from core import models as CoreModels
from people import models as PeopleModels
from education import models as EducationModels


def empty(model: models.Model):
    model.objects.all().delete()
    print(f"the {model.__name__} is empty ... !")


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Empty the db ...")

        # empty the core app
        empty(CoreModels.Users)
        empty(CoreModels.levels)
        empty(CoreModels.Books)
        empty(CoreModels.Logins)
        empty(CoreModels.UserProfile)
        # empty the poeple app
        empty(PeopleModels.Students)
        empty(PeopleModels.StudentProfiles)
        empty(PeopleModels.Teachers)
        empty(PeopleModels.TeacherProfiles)
        # empty the education app
        empty(EducationModels.Terms)
        empty(EducationModels.Registers)
        empty(EducationModels.Grades)
        empty(EducationModels.BookSales)
