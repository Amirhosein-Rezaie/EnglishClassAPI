from django.core.management.base import BaseCommand
from django.db import models
from core import models as CoreModels


def empty(model: models.Model):
    model_len = model.objects.all().count()
    for _ in range(model_len):
        model.objects.all().delete()
    print(f"the {model.__name__} is empty ... !")


class Command(BaseCommand):
    help = "Empty the db ..."

    def handle(self, *args, **options):
        empty(CoreModels.Users)
        empty(CoreModels.levels)
        empty(CoreModels.Books)