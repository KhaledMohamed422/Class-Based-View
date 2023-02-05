from django.shortcuts import render
from .models import Post
from django.views.generic import ListView , DetailView , DeleteView
# Create your views here.

# Class Based View 
# https://ccbv.co.uk/


class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post


# class PostDelete(DeleteView):
    # pass


# class PostList():
#     pass
