from django.shortcuts import render
from .models import Blog

def index(request):
    return render(request,"index.html")

def home(request):
    blogs = Blog.objects
    return render(request,"home.html",{'blogs':blogs})