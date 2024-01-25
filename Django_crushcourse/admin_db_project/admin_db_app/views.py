from django.shortcuts import render
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
