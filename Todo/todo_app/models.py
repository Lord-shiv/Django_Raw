from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Title")

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    name = models.CharField(max_length=50, default="User", blank=True)
    content = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="Soon")

    def __str__(self):
        return self.name  # name to be shown when called
