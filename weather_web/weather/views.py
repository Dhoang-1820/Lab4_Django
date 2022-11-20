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


def indexCountry(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d53ae461b2cd691622e8cc940bbdd05b'

    city = 'Ho Chi Minh'

    city_weather = requests.get(url.format(city)).json()

    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    context = {'weather': weather}
    print('weather', weather)

    return render(request, 'indexCountry.html', context)  # returns the index.html template
