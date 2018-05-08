from django import forms
from django.forms import ModelForm
from myapp.models import Car, Rent
class CarForm(ModelForm):
	class Meta:
		model = Car
		fields = '__all__'

class RentForm(ModelForm):
	start = forms.DateTimeField(widget=forms.DateInput(attrs={'class':'myclass', 'data-uk-datepicker':"{format:'YYYY-MM-DD'}"}))
	stop = forms.DateTimeField(widget=forms.DateInput(attrs={'class':'myclass', 'data-uk-datepicker':"{format:'YYYY-MM-DD'}"}))

	# start = forms.DateTimeField(widget=forms.DateInput(attrs={'class':'myclass', 'type': 'date'}))
	# stop = forms.DateTimeField(widget=forms.DateInput(attrs={'class':'myclass', 'type': 'date'}))
	class Meta:
		model = Rent
		fields=['car','start','stop']
