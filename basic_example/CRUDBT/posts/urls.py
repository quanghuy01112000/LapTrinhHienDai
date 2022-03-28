# posts/urls.py
# from django.contrib import admin
# from django.urls import path
from django.urls import re_path
from django.contrib import admin

from posts import views
from posts.views import (
  ListPostView,
  CreatePostView,
  UpdatePostView,
)

urlpatterns = [
    re_path(r'^list-posts/$', ListPostView.as_view(), name='list-posts'),
    re_path(r'^create-post/$', CreatePostView.as_view(), name='create-post'),
    re_path(r'^update-post/(?P<pk>[-\w]+)$', UpdatePostView.as_view(), name='update-post'),
    re_path(r'^delete-post/(?P<pk>[-\w]+)$', views.delete_post, name='delete-post'),
]