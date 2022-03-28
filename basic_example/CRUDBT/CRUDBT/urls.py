# myproject/urls.py

from django.urls import re_path, include
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^posts/', include(('posts.urls', 'posts'), namespace='posts')),
]