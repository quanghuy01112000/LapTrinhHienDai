from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("detail/<str:slug>", views.detail, name="detail"),
    path("<str:slug>", views.category, name="category"),
]
