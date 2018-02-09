from django.db import models

# Create your models here.
'''
First Name
Last Name
Telephone
Date of Birth
Credit Amount
Profile Image
Memo 500 characters
'''
class Person(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	telephone=models.CharField(max_length=15,null=True)
	dob=models.DateField(blank=True,null=True)
	credit_amount=models.DecimalField(max_digits=15, decimal_places=2)
	memo=models.CharField(max_length=500,null=True)