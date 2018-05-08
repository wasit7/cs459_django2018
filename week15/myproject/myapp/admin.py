from django.contrib import admin
from myapp.models import Car, Rent, Customer
# Register your models here.
admin.site.register(Car)
admin.site.register(Rent)
admin.site.register(Customer)