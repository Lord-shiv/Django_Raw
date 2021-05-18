from django.contrib import admin
from . models import Book, Category, Cupboard, Product
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Cupboard)
class ProductAdmin(admin.ModelAdmin):
    pass

