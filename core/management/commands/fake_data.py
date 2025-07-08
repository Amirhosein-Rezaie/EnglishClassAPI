from django.core.management.base import BaseCommand
from faker import Faker

import random

# the models
from core import models as CoreModels
from people import models as PeopleModels
from education import models as EducationModels


class Command(BaseCommand):
    # # fake data for core app
    print("\nCreating the fake data in db ... \n")

    def handle(self, *args, **options):
        fake = Faker('fa_IR')

        # the insert data into user table
        print("Inserting to Users ...", end=' ')
        for _ in range(5):
            CoreModels.Users.objects.create(
                username=fake.user_name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                national_code=fake.random_number(digits=10),
                phone=fake.bothify(text="09#########"),
                role=random.choice(list(CoreModels.Users.ROLES)),
                password=fake.password()
            )
        print('OK')

        # insert data into user's profile
        print("Inserting to user's profile ...", end=' ')
        for _ in range(5):
            CoreModels.UserProfile.objects.create(
                image=fake.image_url(),
                user=random.choice(list(CoreModels.Users.objects.all()))
            )
        print('OK')

        # the insert data into levels table
        print("Inserting to levels ...", end=' ')
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
        print('OK')

        # insert into the books models
        print("Inserting to Books ...", end=' ')
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
        print('OK')

        # insert into the logins model
        print("The inserting logins ...", end=' ')
        fake = Faker('fa-IR')
        for _ in range(30):
            CoreModels.Logins.objects.create(
                user=random.choice(list(CoreModels.Users.objects.all())),
                status=fake.boolean(),
                date=fake.date()
            )
        print('OK')

        # # fake data for poeple app
        # insert to students
        print("Inserting to the students ...", end=' ')
        for _ in range(20):
            PeopleModels.Students.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                national_code=fake.random_number(digits=10),
                birthday=fake.date_of_birth(),
                phone=fake.bothify(text="09#########"),
            )
        print('OK')

        # insert to StudentProfiles
        print("Inserting to StudentProfiles ...", end=' ')
        for _ in range(5):
            PeopleModels.StudentProfiles.objects.create(
                student=random.choice(
                    list(PeopleModels.Students.objects.all())),
                image=fake.image_url(),
            )
        print('OK')

        # insert to Teachers
        print("Inserting to the Teachers ...", end=' ')
        for _ in range(10):
            PeopleModels.Teachers.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                national_code=fake.random_number(digits=10),
                phone=fake.bothify(text="09#########"),
            )
        print('OK')

        # insert to TeacherProfiles
        print("Inserting to TeacherProfiles ...", end=' ')
        for _ in range(5):
            PeopleModels.TeacherProfiles.objects.create(
                teacher=random.choice(
                    list(PeopleModels.Teachers.objects.all())),
                image=fake.image_url(),
            )
        print('OK')
