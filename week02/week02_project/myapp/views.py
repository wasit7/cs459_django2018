from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .forms import PersonForm
from .models import Person, Image

from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {'key': "value" })

class CreatePersonView(CreateView):
	queryset = Person()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/'

class UpdatePersonView(UpdateView):
	queryset = Person.objects.all()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/'

class ListPersonView(ListView):
    model = Person
    template_name='person_list.html'