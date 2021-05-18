from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# from polymorphic.models import PolymorphicModel


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': ('book', 'cupboard',)})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['object_id']

class Base(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created',)


class Book(Base):
    publisher = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    m2m = models.ManyToManyField(
        Product,
        related_name = 'book',
        related_query_name = 'book',
    )


class Cupboard(Base):
    shelves = models.IntegerField()
    author = models.CharField(max_length=255)
