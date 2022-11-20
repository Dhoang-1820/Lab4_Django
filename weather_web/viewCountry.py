...
def index(request):
    ...
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    return render(request, 'weather/index.html') #returns the index.html template

...
def index(request):
    ...
    context = {'weather' : weather}

    return render(request, 'weather/index.html', context) #returns the index.html template