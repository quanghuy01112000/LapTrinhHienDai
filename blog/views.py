from re import T
from django.shortcuts import render
from django.http import HttpResponse
from pandas import Categorical
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Category, Post


def index(request):
    slideposts = Post.objects.order_by('id')[:2]
    recentreviews = Post.objects.order_by('id')[:4]
    categories = Category.objects.all()
    congngheposts = Post.objects.filter(category_id = 2)[:7]
    thethaoposts = Post.objects.filter(category_id = 3)[:6]
    xecoposts = Post.objects.filter(category_id=4)[:4]
    dulichposts = Post.objects.filter(category_id=5)[:4]
    giaitriposts = Post.objects.filter(category_id=6)[:4]
    bottomposts = Post.objects.order_by('id')[:4]
    return render(request, "pages/home.html", {
        "slideposts": slideposts,
        "recentreviews": recentreviews,
        "categories": categories,
        "congngheposts": congngheposts,
        "thethaoposts": thethaoposts,
        "bottomposts": bottomposts,
        "xecoposts": xecoposts,
        "dulichposts": dulichposts,
        "giaitriposts": giaitriposts,
    })


def category(request, slug):
    category = Category.objects.get(slug=slug)
    posts_list = Post.objects.filter(category_id=category)
    paginator = Paginator(posts_list, 6)

    pageNumber = request.GET.get('page')
    try:
        posts = paginator.page(pageNumber)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "pages/category.html", {"slug": slug, "posts": posts})


def contact(request):
    return render(request, "pages/contact.html")

def detail(request, slug):
    post = Post.objects.get(slug=slug)
    categories = Category.objects.all()
    latestposts = Post.objects.order_by('id')[:4]
    return render(request, "pages/blog-single.html", {"post": post, "categories": categories, "latestposts": latestposts})


# Create your views here.
