from django.db import models

# Create your models here.
class Car(models.Model):
	name = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	photo = models.ImageField(upload_to='cars')