from django.shortcuts import render
# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Person
from .forms import PersonForm


class CreatePersonView(CreateView):
	queryset = Person()
	template_name='create.html'
	form_class = PersonForm
	success_url = '/admin'

class ListPersonView(ListView):
    model = Person
    template_name='list.html'