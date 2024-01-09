from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def counter(request):
    words = request.POST['text']    # get form "words" content (GET --> show in link, POST --> hide (CSRF token needed)
    context = {
        'text': words,
        'length': len(words.split())
    }
    return render(request, 'counter.html', context)
