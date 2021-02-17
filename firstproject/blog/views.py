from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def blog(reqeust) : 
    blogs = Blog.objects.all()
    return render (reqeust, 'blog.html', {'blogs' : blogs})

def detail(reqeust, id) :
    blog = get_object_or_404(Blog, pk = id)
    return render(reqeust, 'detail.html', {'blog': blog})