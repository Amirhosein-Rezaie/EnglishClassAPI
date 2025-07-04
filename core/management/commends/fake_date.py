from django.core.management.base import BaseCommand
from faker import Faker

# the models
from core import models as CoreModels
from people import models as PeopleModels
from education import models as EducationModels

class commend(BaseCommand):
    help = "Creating the fake data in db ... "

    def handle(self, *args, **options):
        pass

        return super().handle(*args, **options)