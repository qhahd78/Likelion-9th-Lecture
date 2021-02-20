from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
# Create your views here.
# view 에서 매개변수(id)를 받고 싶을 때는 url 에 패스컨버트를 꼭 써줘야한다. 

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

# 정보 받으면 create 함수를 통해 새로운 블로그 객체를 만들고 이를 저장함. 
# 디테일 페이지로 리다이렉트 시킨다. 
def create(request) : 
    new_blog = Blog()

    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()

    new_blog.save()

    return redirect('detail', new_blog.id)

def edit(request, id) : 
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog': edit_blog})

def update(request, id) : 
    update_blog = Blog.objects.get(id = id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()

    return redirect("detail", update_blog.id)

def delete(request, id): 
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect("blog")