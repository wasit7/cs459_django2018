from django.db import models

# Create your models here.
class Car(models.Model):
	model=models.CharField(max_length=100)
	detail=models.CharField(max_length=100)
	price=models.DecimalField(max_digits=10, decimal_places=2)

class Customer(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	phone=models.CharField(max_length=20)

class Rent(models.Model):
	car_id=models.ForeignKey('Car',on_delete=models.CASCADE)
	customer_id=models.ForeignKey('Customer',on_delete=models.CASCADE)
	start=models.DateTimeField(null=True)
	stop=models.DateTimeField(null=True)