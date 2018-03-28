from django.db import models

class Car(models.Model):
	model=models.CharField(max_length=100)
	detail=models.CharField(max_length=100)
	price=models.DecimalField(max_digits=10, decimal_places=2)
	def __str__(self):
		return "id: %s, model: %s, price: %s"%(self.id, self.model, self.price)

class Customer(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	phone=models.CharField(max_length=20)
	def __str__(self):
		return "id: {}, {}".format(self.id, self.first_name)

class Rent(models.Model):
	car=models.ForeignKey('Car',on_delete=models.CASCADE)
	customer=models.ForeignKey('Customer',on_delete=models.CASCADE)
	start=models.DateTimeField(null=True)
	stop=models.DateTimeField(null=True)