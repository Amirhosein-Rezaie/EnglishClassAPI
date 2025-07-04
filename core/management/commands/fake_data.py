from django.core.management.base import BaseCommand
from faker import Faker

# the models
from core import models as CoreModels
from people import models as PeopleModels
from education import models as EducationModels

class Command(BaseCommand):
    help = "Creating the fake data in db ... "

    def handle(self, *args, **options):
        fake = Faker('fa_IR')

        # the insert data into user table
        print("Inserting to Users ... ")
        for _ in range(5):
            CoreModels.Users.objects.create(
                username = fake.user_name(),
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                national_code = fake.random_number(digits=10),
                phone = fake.phone_number(),
                role = 'PERSONEL',
                password = fake.password()
            )
        print("The inserting date to users has been done ... Ok")
