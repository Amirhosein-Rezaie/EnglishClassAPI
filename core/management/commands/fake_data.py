from django.core.management.base import BaseCommand
from faker import Faker

# the models
from core import models as CoreModels
from people import models as PeopleModels
from education import models as EducationModels

class Command(BaseCommand):
    help = "Creating the fake data in db ... "

    def handle(self, *args, **options):
        print("done")