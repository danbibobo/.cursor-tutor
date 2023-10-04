from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField('Book name', max_length=100)
    author = models.CharField('Author', max_length=100, blank = True)
    author_email = models.EmailField('Author email', max_length=75, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name