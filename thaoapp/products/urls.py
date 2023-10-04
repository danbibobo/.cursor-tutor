from django.urls import path
from . import views
app_name = "products"
urlpatterns = [
    path('', views.DISPLAYDATA),
    path('form1/', views.newBook, name = 'newBook'),
    path('getNewBook/', views.getNewBook, name = "getNewBook"),
    path('insert/', views.insertFile, name = "uploadFile"),
    path('import/', views.import_data, name = "import_data"),
]