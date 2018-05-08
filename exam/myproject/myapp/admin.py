from django.contrib import admin

from myapp.models import Room, Member, Rent

class RoomAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Room._meta.fields]
admin.site.register(Room, RoomAdmin)

class MemberAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Member._meta.fields]
admin.site.register(Member, MemberAdmin)

class RentAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Rent._meta.fields]
admin.site.register(Rent, RentAdmin)