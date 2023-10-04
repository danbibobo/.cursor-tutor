from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from products.models import Book

# Register your models here.
admin.site.register(Book)

class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        fields = ['name', 'author','author_email','price']
   
