from django.shortcuts import render
from .models import Feature
# Create your views here.


def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our service is very quick'
    feature1.is_true = True

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.details = 'Our service is reliable'
    feature2.is_true = False

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Fast'
    feature3.details = 'Our service is very fast'
    feature3.is_true = False

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Safe'
    feature4.details = 'Our service is very safe'
    feature4.is_true = True

    features = [feature1, feature2, feature3, feature4]
    return render(request, 'index.html',
                  {'features': features})


def counter(request):
    words = request.POST['text']    # get form "words" content (GET --> show in link, POST --> hide (CSRF token needed)
    context = {
        'text': words,
        'length': len(words.split())
    }
    return render(request, 'counter.html', context)
