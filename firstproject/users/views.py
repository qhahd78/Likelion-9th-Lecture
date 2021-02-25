from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth 

# Create your views here.

def userLogin(request) : 
    if request.method == 'POST' : 
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)

        if user is not None: 
            auth.login(request, user)
            return redirect('welcome')
        else: 
            return redirect('signup')
    else: 
        return render(request, 'login.html')

def userLogout(request): 
    auth.logout(request)
    return redirect('welcome')

def userSignup(request): 
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            user = User.objects.create_user(
                username=request.POST.get('username'), 
                password=request.POST.get('password1'),
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                number=request.POST.get('number')
            )
            auth.login(request, user) 
            return redirect('welcome')
        return redirect('signup')
    else: 
        return render(request, 'signup.html')