from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Pofol
# Create your views here.

# 포폴 홈 화면 
def portfolio(request) : 
    pofols = Pofol.objects.all()
    return render(request, 'portfolio.html', {'pofols' : pofols})

# CRUD - C 
def pofol_create(request) : 
    return render(request, 'pofol_create.html')

def model_create(request) : 
    new_Pofol = Pofol()
    new_Pofol.title = request.POST['title']
    new_Pofol.body = request.POST['body']
    new_Pofol.pub_date = timezone.now()
    # 실행할 코드 
    try: 
        new_Pofol.image=request.FILES['image']
        # 예외 발생시 코드 
    except: 
        pass
    new_Pofol.save()

    return redirect('portfolio')

# CRUD - R 
def pofol_detail(request, id) : 
    pofol = get_object_or_404(Pofol, pk = id)
    return render (request, 'pofol_detail.html', {'pofol' : pofol})

# CRUD - U

def pofol_edit(request, id): 
    edit_pofol = Pofol.objects.get(id = id)
    return render (request, 'pofol_edit.html', {'pofol' : edit_pofol})

def model_edit(request, id): 
    update_pofol = Pofol.objects.get(id = id)
    update_pofol.title = request.POST['title']
    update_pofol.body = request.POST['body']
    update_pofol.pub_date = timezone.now()
    try: 
        update_Pofol.image=request.FILES['image']
        # 예외 발생시 코드 
    except: 
        pass

    update_pofol.save()

    return redirect('pofol_detail', update_pofol.id)

# CRUD - D 

def pofol_del(request, id) : 
    del_pofol = Pofol.objects.get(id=id)
    del_pofol.delete()
    return redirect('portfolio')