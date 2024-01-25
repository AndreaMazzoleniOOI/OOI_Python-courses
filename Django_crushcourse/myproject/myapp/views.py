from django.shortcuts import render


# Create your views here.

def index(request):
    """This will be executed by an url routing. This will render the template """
    context={
        'name': 'John',
        'age': 24,
        'nationality': 'British',
    }
    return render(request, 'index.html', context)    # this will render the template index.html
