"""Register here your models to the admin page
This will also link the class Feature in your code to the DB"""
from django.contrib import admin
from .models import Feature

# Register your models here.
admin.site.register(Feature)
