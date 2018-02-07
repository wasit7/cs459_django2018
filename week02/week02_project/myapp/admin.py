from django.contrib import admin
from myapp.models import Person, Image

class PersonAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Person._meta.fields]

admin.site.register(Person,PersonAdmin)

class ImageAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Image._meta.fields]

admin.site.register(Image,ImageAdmin)