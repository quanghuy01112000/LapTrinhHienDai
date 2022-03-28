# posts/views.py

from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CreatePostForm

from .models import Post


class ListPostView(ListView):
    model = Post

    def get(self, request, *args, **kwargs):
        template_name = 'posts/list-posts.html'  # sẽ được tạo ở phần dưới
        obj = {
            "messages": "",
            'posts': Post.objects.all()
        }
        return render(request, template_name, obj)

class CreatePostView(SuccessMessageMixin, CreateView):
    template_name = 'posts/create-post.html'
    form_class = CreatePostForm
    success_message = 'Crate Post successfully!'


class UpdatePostView(SuccessMessageMixin, UpdateView):
    template_name = 'posts/edit-post.html'
    model = Post
    fields = ['name', 'content', ]
    success_message = 'Update Post successfully!'

    def get_success_url(self):
        return reverse('posts:list-posts', kwargs={})


def delete_post(request, pk):
    post = Post.objects.filter(id=pk)
    post.delete()
    context = {
        "messages": "Delete Post successfully",
        'posts': Post.objects.all()
    }
    return render(request, 'posts/list-posts.html', context)
