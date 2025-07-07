from django.core.management.base import BaseCommand
from faker import Faker

import random

# the models
from core import models as CoreModels
from people import models as PeopleModels
from education import models as EducationModels


class Command(BaseCommand):
    print("Creating the fake data in db ... \n")

    def handle(self, *args, **options):
        fake = Faker('fa_IR')

        # the insert data into user table
        print("Inserting to Users ... ")
        for _ in range(5):
            CoreModels.Users.objects.create(
                username=fake.user_name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                national_code=fake.random_number(digits=10),
                phone=fake.phone_number(),
                role=random.choice(list(CoreModels.Users.ROLES)),
                password=fake.password()
            )
        print("The inserting data to users has been done ... Ok \n")

        # the insert data into levels table
        print("inserting to levels ... ")
        levels = [
            'Elemntary',
            'Intermdiant',
            'Pre-Intermdiant',
            'Upper-Intermduant',
            'Advanced',
            'Proficiency'
        ]
        for index in range(len(levels)):
            CoreModels.levels.objects.create(
                title=levels[index]
            )
        print("The inserting data to levels has been done ... Ok \n")

        # insert into the books models
        print("Inserting to Books ... ")
        fake = Faker()
        for _ in range(5):
            CoreModels.Books.objects.create(
                title=fake.sentence(nb_words=3).rstrip('.'),
                level=random.choice(CoreModels.levels.objects.all()),
                type=random.choice(list(CoreModels.Books.TYPES_BOOK)),
                number=random.randint(1, 100),
                image=fake.image_url(),
                price=random.randint(100000, 1000000)
            )
        print("The inserting data to books has been done ... Ok \n")
