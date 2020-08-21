from django.urls import path

from . import views

urlpatterns = [
    path("wiki", views.index, name="index"),
    path("wiki/search", views.search, name="search"),
    path("wiki/new", views.new, name="new"),
    path("wiki/edit", views.edit, name="edit"),
    path("wiki/random", views.random, name="random"),
    path("wiki/<str:title>", views.view_entry, name="view_entry"),
    
]
