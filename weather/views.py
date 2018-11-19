from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests

# Create your views here.
def index(request):
	url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=5aab0bb9f8ec015d11bf96d2fe20f217'
	if(request.method=='POST'):
		form=CityForm(request.POST)
		form.save()

	form=CityForm()

	weather_data=[]
	cities=City.objects.all()
	for city in cities:
	    city_weather=requests.get(url.format(city)).json()
	    weather={
	    'city':city,
	    'temperature':city_weather['main']['temp'],
	    'description':city_weather['weather'][0]['description']
	    }
	    weather_data.append(weather)
	context={'weather_data': weather_data,'form':form}
	return render(request,'index.html',context)

