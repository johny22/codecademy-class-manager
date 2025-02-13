from django.db import models
from django.contrib.auth.models import User


class Achievement(models.Model):
    name = models.CharField("Nome da conquista", max_length=400)

class Person(User):
    fullname = models.CharField("Nome completo", max_length=250)
    age = models.IntegerField("Idade")

class Student(Person):
    pass

class Teacher(Person):
    pass

class CodecademyProfile(models.Model):
    badges = models.ManyToManyField(Achievement)
    owner = models.OneToOneField(Person, on_delete=models.PROTECT)
