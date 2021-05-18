from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Max


class Student(User):
    score = models.IntegerField()

    def __repr__(self):
        return str(self.score) + self.username


class Player(models.Model):
    username = models.CharField(max_length=100)
    age = models.IntegerField()
    favorite = models.CharField(max_length=225)

    def __str__(self):
        return self.username


# User.objects.annotate(
#     max_score=Max('finishedexam__score')
# ).aggregate(
#     avg_score=Avg('max_score')
# )['avg_score']


class Animal(models.Model):
    legs = models.IntegerField()

    class Meta:
        db_table = 'Pets'
        verbose_name = 'creature'