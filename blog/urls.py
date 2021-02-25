from django.contrib import admin
from django.urls import path
from .views import *

# 패스 컨버터를 통해 id 를 받아온다. 

urlpatterns = [
    path ('', blog, name="blog"),
    path('<str:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete")
]