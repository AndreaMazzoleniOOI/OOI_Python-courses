from django.urls import path
from . import views

urlpatterns = (
    path('', views.home, name='home'),
    path('<str:room_name>/', views.room, name='room'),
    path('check_room', views.check_room, name='check_room'),
)