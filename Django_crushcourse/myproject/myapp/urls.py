"""Custom file with url routing"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    # main page
]