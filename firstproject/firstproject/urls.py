"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from firstapp import views as first
from wordcount import views as wc
from blog import home

# 패스 컨버터를 통해 id 를 받아온다. 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first.welcome, name="welcome"),
    path('hello/', first.hello, name="hello"),
    path('wc/', wc.home, name="wc"),
    path('wc/result', wc.result, name="result"),
    path('blog/', include('blog.urls'))
]
