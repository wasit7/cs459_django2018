from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	Address=models.CharField(max_length=100)
	postcode=models.CharField(max_length=10)
	telephone=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	def __unicode__(self):
		return "id: %s, %s %s"%(self.id, self.first_name, self.last_name)

class Car(models.Model):
	maker=models.CharField(max_length=10)
	model=models.CharField(max_length=10)
	price=models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
	model=models.CharField(max_length=10)
	year=models.DateTimeField( null=True, blank=True )
	def __unicode__(self):
		return "id: %s, %s %s"%(self.id, self.maker, self.model)

class Rent(models.Model):
	rent_date=models.DateTimeField( default=timezone.now )
	return_date=models.DateTimeField( default=timezone.now )
	cost=models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
	car = models.ForeignKey("Car", on_delete=models.SET_NULL, blank=True,null=True)
	customer = models.ForeignKey("Customer", on_delete=models.SET_NULL, blank=True,null=True)
	def __unicode__(self):
		return "id: %s"%(self.id)
