from django.contrib import admin

# Register your models here.
from django.contrib import admin 
from . import models
from django.contrib.auth.admin import UserAdmin

@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin): 

    ''' User admin Custon '''

    fieldsets = (
        (None, {"fields": ("username","password", "name", "number", "email")},),
    )

    list_display = (
        "username",
        "name", 
        "email",
        "number",
    )