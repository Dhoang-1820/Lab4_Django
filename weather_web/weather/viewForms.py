...
from .forms import CityForm

def index(request):
    ...
    form = CityForm()

    weather_data = []
    ...
    context = {'weather_data' : weather_data, 'form' : form}

    ...
    def index(request):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=YOUR_APP_KEY'

        cities = City.objects.all()  # return all the cities in the database

        if request.method == 'POST':  # only true if form is submitted
            form = CityForm(request.POST)  # add actual request data to form for processing
            form.save()  # will validate and save if validate

        form = CityForm()
        ...