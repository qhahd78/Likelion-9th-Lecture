from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
# Create your views here.

def blog(request) : 
    blogs = Blog.objects.all()
    return render (request, 'blog.html', {'blogs' : blogs})

def detail(request, id) :
    # get_object_or_404 는 2가지 인자를 갖고 온다. 
    # 1. 어떤 클래스에서 객체를 가져올지, 
    # 2. 클래스에서 몇 번째 객체를 선택할지. (pk 값을 이용해 detail 페이지를 불러온다. )
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog': blog})

def new(request) : 
    return render(request, 'new.html')

def create(request) : 
    new_blog = Blog()

    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()

    new_blog.save()

    return redirect('detail', new_blog.id)