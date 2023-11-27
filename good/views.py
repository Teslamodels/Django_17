from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.

class Port(ListView):
    model = Post
    template_name = 'home.html'

class Port2(DetailView):
    model = Post
    template_name = 'detail.html'