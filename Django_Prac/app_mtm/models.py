from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE WIN LOSE')
    name = models.CharField(max_length=60)
    medal = models.CharField(
        blank=False, choices=MedalType.choices, max_length=10)
    # If I'm changing blank to True after adding some data is it safe to do that?


# * * * *
# part-A *
# * * * *
class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline


# * * * *
# part-B *
# * * * *
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey('app_mtm.Person', on_delete=models.CASCADE)
    group = models.ForeignKey('app_mtm.Group', on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


# * * * *
# part-C *
# * * * *
class APerson(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class MyPerson(Person):
    class Meta:
        proxy = True

    def do_something(self):
        pass


# * * * *
# part-D *
# * * * *
class CUser(User):
    new_name = models.CharField(max_length=90)
    score = models.IntegerField()

    def __str__(self):
        return self.new_name
