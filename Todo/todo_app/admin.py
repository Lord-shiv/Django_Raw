from django.contrib import admin
from .models import TodoItem, Category

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(Category)