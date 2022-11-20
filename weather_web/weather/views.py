import requests
from django.shortcuts import render


# Create your views here.
def index(request):
    url = 'https://lab4-8bee4-default-rtdb.firebaseio.com/test.json'

    city_weather = requests.get(url).json()


    # weather = {
    #     'city': city,
    #     'temperature': city_weather['main']['temp'],
    #     'description': city_weather['weather'][0]['description'],
    #     'icon': city_weather['weather'][0]['icon']
    # }
    weather = {
        'temperature': city_weather['temp'],
    }
    context = {'weather': weather}
    print('weather', weather['temperature'])

    return render(request, 'index.html', context)  # returns the index.html template
