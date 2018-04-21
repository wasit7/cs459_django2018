# From previous week
## First Run Server
```sh
cd cs459_django2018
mkdir week01
django-admin startproject project01
cd project01 
python manage.py runserver 
git add -A
git commit -m "first run server"
```

## Add Superuser
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

go to (localhost:8000/admin)[localhost:8000/admin]

# For this week
## Install python packages
```python
pip install -r requirement.txt
```

## create app
```sh
python manage.py startapp myapp
```

## install app /myproject/setting.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'crispy_forms',
    'django_extensions',
]
```

## setup media storage and crispy form
```python
CRISPY_TEMPLATE_PACK = 'bootstrap3'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

## edit model.py
```python
from __future__ import unicode_literals
from django.db import models

class Person(models.Model):
	name=models.CharField(max_length=100)
	dob=models.DateField(blank=True,null=True)
	def __unicode__(self):
		return u"%s"%(self.name)

class Image(models.Model):
	image=models.ImageField(upload_to='images')
	description=models.CharField(max_length=100,blank=True,null=True)
```

## view.py
This file work with /myapp/templates/*
```python
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
```
## forms.py
```python
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
#from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets
import datetime
from .models import Person

class PersonForm(ModelForm):
	class Meta:
		model =  Person
		exclude=[]

		widgets = {
			'dob': forms.DateInput(
				attrs={
				'type': 'date', 
				'value': datetime.datetime.now().strftime("%Y-%m-%d")
				}, format="%Y-%m-%d"
			),
		}
		
	def __init__(self, *args, **kwargs):
		super(PersonForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))
```
## admin.py
```python
from django.contrib import admin
from myapp.models import Person, Image

class PersonAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Person._meta.fields]

admin.site.register(Person,PersonAdmin)

class ImageAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Image._meta.fields]

admin.site.register(Image,ImageAdmin)
```

## migrate and run
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
