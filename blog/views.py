from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from .models import Post

def index(request):
    return render(request, "pages/home.html")


def category(request, slug):
    id = Category.objects.get(slug = slug).id
    posts = Post.objects.filter(category_id = id)
    return render(request, "pages/category.html", 
                    {"slug": slug,
                    'posts': posts})


def contact(request):
    return render(request, "pages/contact.html")


# Create your views here.
