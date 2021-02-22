from django.db import models

# Create your models here.

class Pofol(models.Model) : 
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self) : 
        return self.title