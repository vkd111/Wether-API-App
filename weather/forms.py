from django.forms import ModelForm
from django.forms import TextInput
from .models import City
 
class CityForm(ModelForm):
	class Meta:
		model=City
		fields=['name']
		widgets={
		'name':TextInput(attrs={'class':'input','placeholder':'City Name'}),
		}