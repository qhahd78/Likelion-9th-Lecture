from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Pofol
# Create your views here.

def portfolio(request) : 
    pofols = Pofol.objects.all()
    return render(request, 'portfolio.html', {'pofols' : pofols})

def create(request) : 
    return render(request, 'create.html')

def model_create(request) : 
    new_Pofol = Pofol()
    new_Pofol.title = request.POST['title']
    new_Pofol.body = request.POST['body']
    new_Pofol.pub_date = timezone.now()
    new_Pofol.save()

    return redirect('portfolio')