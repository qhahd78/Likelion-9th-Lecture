from django.contrib import admin
from django.urls import path, include
from .views import *

# 패스 컨버터를 통해 id 를 받아온다. 

urlpatterns = [
    path('', portfolio, name="portfolio"),
    path('pofol_create/', pofol_create, name="pofol_create"),
    path('model_create/', model_create, name="model_create"),
    path('pofol_detail/<str:id>', pofol_detail, name="pofol_detail"),
    path('pofol_edit/<str:id>', pofol_edit, name="pofol_edit"),
    path('model_edit/<str:id>', model_edit, name="model_edit"),
    path('pofol_del/<str:id>', pofol_del, name="pofol_del"),
]
