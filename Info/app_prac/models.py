from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)   # this will create this field as pk insted of creating default one primary key = True

