from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Todo(models.Model):
    user = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
