from django.contrib import admin
from django.urls import path, include
from .views import *

# 패스 컨버터를 통해 id 를 받아온다. 

urlpatterns = [
    path('', portfolio, name="portfolio"),
    path('create/', create, name="create"),
    path('model_create/', model_create, name="model_create"),
]
