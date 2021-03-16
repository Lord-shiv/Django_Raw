from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):  # The Category table name that inherits models.Model
    name = models.CharField(max_length=100)  # Like a varchar

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    author = models.CharField(max_length=50, default="User", blank=True)
    content = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.author  # name to be shown when called
