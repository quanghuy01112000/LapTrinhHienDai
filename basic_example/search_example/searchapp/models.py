from pyexpat import model
from django.db import models
from django.urls import reverse

# Create your models here.
class Booktype(models.Model):
    btype = models.CharField(max_length=100, unique=True)
    class Meta:
        ordering=('btype',)

class Book(models.Model):
    book_name = models.CharField(max_length=150)
    author_name = models.CharField(max_length=150)
    type = models.ForeignKey(Booktype, on_delete=models.CASCADE)
    price = models.FloatField()
    publication = models.CharField(max_length=150)

    class Meta:
        ordering = ('book_name',)
    def __str__(self):
        return self.book_name
    def get_url(self):
        return reverse('book_detail', args=[self.id])