from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser) : 

    ''' User Model '''

    name = models.CharField(max_length=10)
    number = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    def __str__(self) : 
        return self.name