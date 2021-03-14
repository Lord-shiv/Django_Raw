from django.db import models
from django.utils import timezone
# Create your models here.


class Category(models.Model):  # The Category table name that inherits models.Model
    name = models.CharField(max_length=100)  # Like a varchar

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    Sr_no = models.AutoField(primary_key=True)
    author = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    created = models.DateField(
        default=timezone.now().strftime("%Y-%m-%d"))  # a date
    due_date = models.DateField(
        default=timezone.now().strftime("%Y-%m-%d"))  # a date
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=13)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title  # name to be shown when called
