from django.shortcuts import render, redirect
from django.contrib import messages
import json
import urllib.request
from urllib.error import HTTPError
from http.client import InvalidURL

# Create your views here.
API_KEY = 'ebc66ffc778631e78ced96c3fe8cde5b'

def index(request):
    if request.method != 'POST':
        return render(request, 'index.html')
    city = request.POST['city']
    if not city:
        return render(request, 'index.html')

    # API call
    try:
        res = urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}").read()
    except (HTTPError, InvalidURL):
        messages.info(request, f'Invalid city: {city}')
        return redirect('/')

    json_data = json.loads(res)
    data = {'city': city,
            'country_code': str(json_data['sys']['country']),
            'coordinates': f"N {json_data['coord']['lat']}° E {json_data['coord']['lon']}°",
            'temperature': str(round(json_data['main']['temp'] - 273.15, 2)),
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
            }
    return render(request, 'index.html', {'posts': data})
