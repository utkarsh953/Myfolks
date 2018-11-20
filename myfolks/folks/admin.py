from django.contrib import admin

# Register your models here.
from folks.models import(
	Location,
	Category,
	SubCategory,
	Profile
	)



class ProfileAdmin(admin.ModelAdmin):
	list_display = ('name','designation','location')
	list_filter = ('designation','location')
	search_fields = ('name',)


admin.site.register(Profile,ProfileAdmin)	
admin.site.register([Location,Category,SubCategory])
	