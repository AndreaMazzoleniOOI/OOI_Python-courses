from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
# Create your views here.


def index(request):
    features = Feature.objects.all()    # this will read all the object of type Feature from db
    return render(request, 'index.html',
                  {'features': features})


def counter(request):
    words = request.POST['text']    # get form "words" content (GET --> show in link, POST --> hide (CSRF token needed)
    context = {
        'text': words,
        'length': len(words.split())
    }
    return render(request, 'counter.html', context)


def register(request):
    if request.method != 'POST':
        return render(request, 'register.html')
    print(request.POST)

    for field in request.POST:
        print(field)
        if not request.POST[field]:
            print(field)
            messages.info(request, 'Please fill up all the fields!')
            return redirect('register')

    user = request.POST['username']
    email = request.POST['email']
    psw = request.POST['password']
    psw2 = request.POST['password2']

    if User.objects.filter(username=user).exists():
        messages.info(request, 'Username is already in use')
        return redirect('register')
    if psw != psw2:
        messages.info(request, 'Password does not match')
        return redirect('register')
    if User.objects.filter(email=email).exists():
        messages.info(request, 'Email is already in use')
        return redirect('register')

    # Create user in db (USER field)
    user = User.objects.create_user(username=user, email=email, password=psw)
    user.save()
    return redirect('login')
