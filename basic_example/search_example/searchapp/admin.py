from django.contrib import admin

from searchapp.models import Book, Booktype

# Register your models here.
admin.site.register(Booktype)
admin.site.register(Book)