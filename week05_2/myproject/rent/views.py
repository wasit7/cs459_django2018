from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Car

# Create your views here.
def home(request):
	print(HttpResponse('Hello World'))
	return HttpResponse('Hello World')

class CarListView(ListView):
    model = Car
    template_name='list.html'