from django.db import models
from django.utils import timezone

class Room(models.Model):
	number = models.CharField(max_length=255)
	hour_price = models.DecimalField(max_digits=10, decimal_places=2)

class Member(models.Model):
	name = models.CharField(max_length=255)
	mobile = models.CharField(max_length=20)

class Rent(models.Model):
	room = models.ForeignKey(Room, on_delete=models.SET_NULL, blank=True,null=True)
	member = models.ForeignKey(Member, on_delete=models.SET_NULL, blank=True,null=True)
	start = models.DateTimeField( default=timezone.now )
	stop = models.DateTimeField( default=timezone.now )
	cost = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)