from math import ceil
from re import T
from django.shortcuts import render
from django.http import HttpResponse
from pandas import Categorical
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Category, Post

categories = Category.objects.all()

def index(request):
    slideposts = Post.objects.order_by('-id')[:2]
    recentreviews = Post.objects.order_by('-id')[:4]
    # categories = Category.objects.all()
    congngheposts = Post.objects.filter(category_id = 2).order_by("-id")[:7]
    thethaoposts = Post.objects.filter(category_id = 3).order_by("-id")[:6]
    xecoposts = Post.objects.filter(category_id=4).order_by("-id")[:4]
    dulichposts = Post.objects.filter(category_id=5).order_by("-id")[:4]
    giaitriposts = Post.objects.filter(category_id=6).order_by("-id")[:4]
    bottomposts = Post.objects.order_by('-id')[:4]
    return render(request, "pages/home.html", {
        "slideposts": slideposts,
        "recentreviews": recentreviews,
        "congngheposts": congngheposts,
        "thethaoposts": thethaoposts,
        "bottomposts": bottomposts,
        "xecoposts": xecoposts,
        "dulichposts": dulichposts,
        "giaitriposts": giaitriposts,
    })


def category(request, slug):
    category = Category.objects.get(slug=slug)
    posts_list = Post.objects.filter(category_id=category).order_by("-id")
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
    # categories = Category.objects.all()
    latestposts = Post.objects.order_by('-id')[:4]
    return render(request, "pages/blog-single.html", {"post": post, "latestposts": latestposts})

def search(request):
    posts = Post.objects.all()
    posts_search = []
    text = request.GET.get("text")
    for post in posts:
        if text in post.name:
            posts_search.append(post)
    paginator = Paginator(posts_search, 6)

    pageNumber = request.GET.get('page')
    try:
        posts_paginator = paginator.page(pageNumber)
    except PageNotAnInteger:
        posts_paginator = paginator.page(1)
    except EmptyPage:
        posts_paginator = paginator.page(paginator.num_pages)
    
    return render(request, "pages/search.html", {"posts_paginator": posts_paginator})

def categories(request):
    categories = Category.objects.all()
    return {"categories": categories}


# Create your views here.
