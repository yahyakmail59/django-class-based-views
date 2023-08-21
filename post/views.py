from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
# Create your views here.

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post


class PostDelete(DeleteView):
    model = Post

class PostUpdate(UpdateView):
    model = Post