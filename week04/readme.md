# basic model-admin
# model.py
define a structure of application database
```python
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Car(models.Model):
	model=models.CharField(max_length=20)
	detail=models.CharField(max_length=100)
	price=models.DecimalField(max_digits=10,decimal_places=2)

class Rent(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	car=models.ForeignKey(Car, on_delete=models.CASCADE)
	start=models.DateTimeField()
	stop=models.DateTimeField()
	fee=models.DecimalField(max_digits=10,decimal_places=2)
  ```
  
# admin.py
database management tool
```python
from django.contrib import admin
from rent.models import Rent, Car

class RentAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Rent._meta.fields]
admin.site.register(Rent,RentAdmin)

class CarAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Car._meta.fields]
admin.site.register(Car,CarAdmin)
```
