from django.db import models
from core.models import levels, Books, Users
from people.models import Teachers, Students
from django.core.validators import MinValueValidator, MaxValueValidator


# status
class STATUS_PAY(models.TextChoices):
    PAYED = 'PAYED'
    UNPAYED = 'UNPAYED'


# the model of terms
class Terms(models.Model):
    class TERM_TYPES(models.TextChoices):
        ORDINARY = 'ORDINARY'
        SPEAKING = 'SPEAKING'

    title = models.CharField(max_length=50, null=False, blank=False)
    level = models.ForeignKey(
        levels, null=False, blank=False, on_delete=models.SET_NULL)
    student_book = models.ForeignKey(
        Books, on_delete=models.SET_NULL, null=False, blank=False)
    work_book = models.ForeignKey(
        Books, on_delete=models.SET_NULL, null=False, blank=False)
    story_book = models.ForeignKey(
        Books, on_delete=models.SET_NULL, null=False, blank=False)
    teacher = models.ForeignKey(
        Teachers, on_delete=models.SET_NULL, null=False, blank=False)
    tution = models.IntegerField(
        validators=[
            MinValueValidator(1)
        ],
        null=False, blank=False
    )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    type = models.CharField(
        choices=TERM_TYPES, default=TERM_TYPES.ORDINARY, null=False, blank=False)
    user = models.ForeignKey(
        Users, on_delete=models.SET_NULL, null=False, blank=True)

    class Meta:
        db_table = 'Terms'

    def __str__(self):
        return self.title


# the model of register
class Registers(models.Model):

    student = models.ForeignKey(
        Students, on_delete=models.SET_NULL, null=False, blank=False)
    term = models.ForeignKey(
        Terms, null=False, blank=False, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=STATUS_PAY, null=False, blank=False)
    user = models.ForeignKey(
        Users, null=False, blank=False, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'Registers'

    def __str__(self):
        return f"{self.user} > {self.term}"


# the models of grades
class Grades(models.Model):
    student = models.ForeignKey(
        Students, null=False, blank=True, on_delete=models.SET_NULL)
    term = models.ForeignKey(
        Terms, on_delete=models.SET_NULL, null=False, blank=False)
    class_grade = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(10)
    ], null=False, blank=False)
    workbook_grade = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(20)
    ], null=False, blank=False)
    Storybook_grade = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(10)
    ], null=False, blank=False)
    Videoclip_grade = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(10)
    ], null=False, blank=False)
    Film_grade = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(10)
    ], null=False, blank=False)
    Exam_grade = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(40)
    ], null=False, blank=False)


# the model of book sales
class BookSales(models.Model):
    student = models.ForeignKey(
        Students, null=False, blank=False, on_delete=models.SET_NULL)
    book = models.ForeignKey(Books, null=False, blank=False)
    date = models.DateField(auto_now_add=True)
    number = models.IntegerField(
        validators=[MinValueValidator(1)], null=False, blank=False)
    user = models.ForeignKey(
        Users, null=False, blank=False, on_delete=models.SET_NULL)
    status = models.CharField(choices=STATUS_PAY, null=False, blank=False)

    class Meta:
        db_table = 'BookSales'

    def __str__(self):
        return f"{self.student} -> {self.user}"
