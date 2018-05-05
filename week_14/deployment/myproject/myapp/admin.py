from django.contrib import admin

# Register your models here.
from myapp.models import Car

class CarAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Car._meta.fields]
admin.site.register(Car,CarAdmin)