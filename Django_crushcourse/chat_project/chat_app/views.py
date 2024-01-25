from django.shortcuts import render, redirect
from .models import Room, Message


def home(request):
    return render(request, 'home.html')


def room(request, room_name):
    print(request.GET)
    post = {
        'username': request.GET["username"],
        'room_name': request.GET["room_name"]
    }
    return render(request, 'room.html', post)


def check_room(request):
    if request.method != 'POST':
        return redirect('home')

    room_name = request.POST["room_name"]
    username = request.POST["username"]

    # Create room if it does not exist
    if not Room.objects.filter(name=room_name).exists():
        new_room = Room.objects.create(name=room_name)
        new_room.save()
    post = {'username': username, 'room_name': room_name}
    return redirect(f"/{room_name}/?username={username}", post)
