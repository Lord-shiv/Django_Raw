from django.db import models

# * * * * * * * * * * * * * * * * * *
# Create your models here.          *
# three types of base classes       *
# ~ Abstract model                  *
# ~ Multi-table model inheritance   *
# ~ proxy models                    *
# * * * * * * * * * * * * * * * * * *


class BaseItem(models.Model):
    ''' output : baseItem was not created in datatable '''
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:  # here we defining abstract class
        abstract = True
        ordering = ['title']

    def __str__(self):
        return self.title


class ItemA(BaseItem):
    ''' created '''
    content = models.TextField()

    class Meta(BaseItem.Meta):
        ordering = ['-created']


class ItemB(BaseItem):
    ''' created '''
    file = models.FileField(upload_to='files')


class ItemC(BaseItem):
    ''' created '''
    file = models.FileField(upload_to='images')


class ItemD(BaseItem):
    ''' created '''
    slug = models.SlugField(max_length=255, unique=True)


# * * * * * * * * * * * * * * * * *
# * Multi-table model inheritance *
# * * * * * * * * * * * * * * * * *
class Books(models.Model):
    ''' created '''
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


class ISBN(Books):
    ''' created '''
    books_ptr = models.OneToOneField(
        Books, on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
    )
    ISBN = models.TextField()


# * * * * * * * * * * * *
# * proxy models        *
# * * * * * * * * * * * *
class NewManager(models.Manager):
    ''' NOT created maybe because of emptyness it has :( '''
    pass


class BookContent(models.Model):
    ''' created '''
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


class BookOrders(BookContent):
    ''' this will not be created in database don't know why figure it out u lazy'''
    objects = NewManager()

    class Meta:
        proxy = True  # because of this maybe
        ordering = ['created']

    def created_on(self):
        return timezone.now() - self.created
