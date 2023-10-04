from django.shortcuts import render
from django.http import HttpResponse
from .forms import Book_Form
from .models import Book
from .admin import BookResource
from tablib import Dataset

def DISPLAYDATA(request):
    data = Book.objects.all()
    return render(request, 'index.html', {'data': data})

def newBook(request):
    nb = Book_Form
    return render(request, 'upload.html', {'nb' : nb})

def getNewBook(request):
    if request.method == 'POST':
        nb = Book_Form(request.POST)
        if nb.is_valid():
            nb.save()
            data = Book.objects.all()
            return render(request, 'index.html', {'data': data})
    else:
        return HttpResponse('fail')

def insertFile(request):
    return render(request, 'import.html')

def import_data(request):
    if request.method == 'POST': 
        resource = BookResource()
        dataset = Dataset()
        newBook = request.FILES['myfile']
        imported_data = dataset.load(newBook.read(), format = 'xlsx')

        for data in imported_data:
            value = Book(
                data[0],
                data[1],
                data[2],
                data[3],
            )
            value.save()
        data = Book.objects.all()
        return render(request, 'index.html', {'data': data})
        result = resource.import_data(dataset, dry_run=False)  # Set dry_run to True for a dry run

        #     if result.has_errors():
        #         # Handle errors
        #         errors = result.rows_with_errors()
        #         return render(request, 'import.html', {'form': form, 'errors': errors})
        #     else:
        #         # Successful import
        
    else:
        return render(request, 'import.html', {})
        





